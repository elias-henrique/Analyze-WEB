#!/usr/bin/env python3
"""
CRM Web Scanner - Interface de linha de comando

Script principal de varredura para aplicações web (como CRMs).
"""

import argparse
import logging
import sys

from lib.config import (DEFAULT_OUTPUT_FILE, DEFAULT_PERFORMANCE_REQUESTS,
                        DEFAULT_TARGET, DEFAULT_TIMEOUT)
from lib.scanner import CRMScanner
from lib.utils import configure_logging, save_json


def parse_args(argv=None):
    """Parse argumentos da linha de comando."""
    parser = argparse.ArgumentParser(
        description="Scanner simples para aplicações web/CRM."
    )
    parser.add_argument(
        "target",
        nargs="?",
        default=DEFAULT_TARGET,
        help=f"URL base do alvo (default: {DEFAULT_TARGET})",
    )
    parser.add_argument(
        "-o",
        "--output",
        default=DEFAULT_OUTPUT_FILE,
        help=f"Arquivo de saída JSON (default: {DEFAULT_OUTPUT_FILE})",
    )
    parser.add_argument(
        "-t",
        "--timeout",
        type=int,
        default=DEFAULT_TIMEOUT,
        help=f"Timeout padrão em segundos (default: {DEFAULT_TIMEOUT})",
    )
    parser.add_argument(
        "-n",
        "--requests",
        type=int,
        default=DEFAULT_PERFORMANCE_REQUESTS,
        help=f"Número de requisições para teste de performance "
        f"(default: {DEFAULT_PERFORMANCE_REQUESTS})",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Ativa modo verboso (debug).",
    )
    return parser.parse_args(argv)


def main(argv=None):
    """Função principal."""
    args = parse_args(argv)
    configure_logging(args.verbose)

    logger = logging.getLogger("crm_scanner")

    target = args.target
    if not target.startswith(("http://", "https://")):
        target = "https://" + target

    scanner = CRMScanner(
        base_url=target,
        timeout=args.timeout,
        performance_requests=args.requests,
    )

    scanner.run()

    # Salva resultados
    save_json(scanner.results.to_dict(), args.output)

    logger.info(
        "Para visualizar os resultados detalhados, abra o arquivo: %s",
        args.output,
    )

    return 0


if __name__ == "__main__":
    sys.exit(main())
