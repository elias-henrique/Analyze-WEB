"""
Scanner principal de CRM
"""

import logging
import time
from datetime import datetime
from typing import Any, Optional
from urllib.parse import urljoin

import requests
from requests import Response
from requests.exceptions import RequestException

from .config import (DEFAULT_PERFORMANCE_REQUESTS, DEFAULT_TIMEOUT,
                     DEFAULT_USER_AGENT)
from .models import AvailabilityResult, EndpointResult, ScanResults
from .wordlists import ENDPOINTS_WORDLIST

logger = logging.getLogger("crm_scanner")


class CRMScanner:
    """Scanner simples para aplicações web do tipo CRM."""

    def __init__(
        self,
        base_url: str,
        timeout: int = DEFAULT_TIMEOUT,
        performance_requests: int = DEFAULT_PERFORMANCE_REQUESTS,
    ) -> None:
        self.base_url = base_url.rstrip("/") + "/"
        self.timeout = timeout
        self.performance_requests = performance_requests

        self.session = requests.Session()
        self.session.headers.update({"User-Agent": DEFAULT_USER_AGENT})

        self.results = ScanResults(
            timestamp=datetime.now().isoformat(),
            target=self.base_url,
        )

    def _safe_get(
        self,
        url: str,
        timeout: Optional[int] = None,
        **kwargs: Any,
    ) -> Optional[Response]:
        """Wrapper seguro para GET com tratamento básico de erros."""
        _timeout = timeout or self.timeout
        try:
            logger.debug("GET %s", url)
            return self.session.get(url, timeout=_timeout, **kwargs)
        except RequestException as exc:
            logger.warning("Falha na requisição para %s: %s", url, exc)
            return None

    def test_availability(self) -> bool:
        """Testa disponibilidade do site."""
        logger.info("Testando disponibilidade...")

        start = time.perf_counter()
        resp = self._safe_get(self.base_url)
        elapsed = time.perf_counter() - start

        if resp is None:
            self.results.availability = AvailabilityResult(
                status="offline",
                status_code=0,
                response_time=elapsed,
                headers={},
            )
            logger.error("Site offline ou inacessível.")
            return False

        status = "online" if resp.ok else "issues"
        self.results.availability = AvailabilityResult(
            status=status,
            status_code=resp.status_code,
            response_time=round(elapsed, 3),
            headers=dict(resp.headers),
        )

        logger.info(
            "Status: %s | Código HTTP: %d | Tempo: %.3fs",
            status,
            resp.status_code,
            elapsed,
        )
        return resp.ok

    def test_common_endpoints(self) -> None:
        """Testa endpoints comuns e sensíveis."""
        logger.info("Testando endpoints populares e sensíveis...")

        for endpoint in ENDPOINTS_WORDLIST:
            url = urljoin(self.base_url, endpoint.lstrip("/"))
            resp = self._safe_get(url, timeout=5, allow_redirects=False)
            if resp is None:
                continue

            if resp.status_code < 404:
                symbol = "✓" if resp.status_code == 200 else "!"
                logger.info(
                    "[%s] %-40s -> %d",
                    symbol,
                    endpoint,
                    resp.status_code,
                )

                self.results.endpoints.append(
                    EndpointResult(
                        endpoint=endpoint,
                        status_code=resp.status_code,
                        content_type=resp.headers.get(
                            "Content-Type", "unknown"),
                        size=len(resp.content),
                    )
                )

        logger.info("Total de endpoints encontrados: %d",
                    len(self.results.endpoints))

    def test_security_headers(self) -> None:
        """Verifica headers de segurança comuns."""
        logger.info("Analisando headers de segurança...")

        resp = self._safe_get(self.base_url)
        if resp is None:
            self.results.security_headers = {"error": "Falha na requisição"}
            return

        headers = resp.headers
        security_headers = {
            "X-Frame-Options": headers.get("X-Frame-Options"),
            "X-Content-Type-Options": headers.get("X-Content-Type-Options"),
            "Strict-Transport-Security": headers.get("Strict-Transport-Security"),
            "Content-Security-Policy": headers.get("Content-Security-Policy"),
            "X-XSS-Protection": headers.get("X-XSS-Protection"),
            "Referrer-Policy": headers.get("Referrer-Policy"),
            "Permissions-Policy": headers.get("Permissions-Policy"),
        }

        for name, value in security_headers.items():
            symbol = "✓" if value else "✗"
            logger.info(
                "[%s] %-26s -> %s",
                symbol,
                name + ":",
                value if value else "Não presente",
            )

        self.results.security_headers = security_headers

    def test_ssl(self) -> None:
        """Verifica configuração básica de SSL/TLS."""
        logger.info("Testando SSL/TLS...")

        resp = self._safe_get(self.base_url)
        if resp is None:
            self.results.ssl = {"error": "Falha na requisição"}
            return

        ssl_info = {
            "https_enabled": self.base_url.startswith("https"),
            "redirects_to_https": False,
        }

        if self.base_url.startswith("https"):
            http_url = self.base_url.replace("https://", "http://", 1)
            http_resp = self._safe_get(
                http_url, timeout=5, allow_redirects=True)
            if http_resp is not None:
                ssl_info["redirects_to_https"] = http_resp.url.startswith(
                    "https")

        logger.info("HTTPS habilitado: %s", ssl_info["https_enabled"])
        logger.info("Redirect HTTP -> HTTPS: %s",
                    ssl_info["redirects_to_https"])

        self.results.ssl = ssl_info

    def test_performance(self) -> None:
        """Testa performance com múltiplas requisições."""
        logger.info(
            "Testando performance (%d requisições)...",
            self.performance_requests,
        )

        times = []

        for i in range(1, self.performance_requests + 1):
            start = time.perf_counter()
            resp = self._safe_get(self.base_url)
            elapsed = time.perf_counter() - start

            if resp is None:
                logger.warning("Requisição %d falhou.", i)
                continue

            times.append(elapsed)
            logger.info("Requisição %2d -> %.3fs", i, elapsed)

        if not times:
            self.results.performance = {
                "error": "Todas as requisições falharam"}
            return

        self.results.performance = {
            "min": round(min(times), 3),
            "max": round(max(times), 3),
            "avg": round(sum(times) / len(times), 3),
            "total_requests": len(times),
        }

        logger.info(
            "Performance (s) -> min: %.3f | max: %.3f | média: %.3f",
            self.results.performance["min"],
            self.results.performance["max"],
            self.results.performance["avg"],
        )

    def test_technologies(self) -> None:
        """Detecta tecnologias utilizadas com base em headers e conteúdo HTML."""
        logger.info("Detectando tecnologias...")

        resp = self._safe_get(self.base_url)
        if resp is None:
            self.results.technologies = {"error": "Falha na requisição"}
            return

        headers = resp.headers
        content = resp.text[:5000].lower()

        technologies = {
            "server": headers.get("Server", "Unknown"),
            "powered_by": headers.get("X-Powered-By", "Unknown"),
            "detected": [],
        }

        tech_patterns = {
            "Next.js": ["/_next/", "__next_data__"],
            "React": ["react", "reactdom"],
            "Vercel": ["vercel"],
            "WordPress": ["wp-content", "wp-includes"],
            "Vue.js": ["vue.js", "vue"],
            "Angular": ["ng-", "angular"],
        }

        for tech, patterns in tech_patterns.items():
            if any(pattern.lower() in content for pattern in patterns):
                technologies["detected"].append(tech)

        logger.info("Server: %s", technologies["server"])
        logger.info("Powered-by: %s", technologies["powered_by"])
        logger.info(
            "Tecnologias detectadas: %s",
            ", ".join(
                technologies["detected"]) if technologies["detected"] else "Nenhuma específica",
        )

        self.results.technologies = technologies

    def run(self) -> None:
        """Executa todos os testes em sequência."""
        logger.info("=" * 60)
        logger.info("Iniciando varredura em: %s", self.base_url)
        logger.info("=" * 60)

        if not self.test_availability():
            logger.error("Site não está acessível. Abortando demais testes.")
            return

        self.test_security_headers()
        self.test_ssl()
        self.test_common_endpoints()
        self.test_technologies()
        self.test_performance()

        logger.info("=" * 60)
        logger.info("Varredura concluída!")
        logger.info("=" * 60)
