"""
Configurações padrão do scanner
"""

# Configurações de timeout e performance
DEFAULT_TARGET = "http://127.0.0.1:8000/"
DEFAULT_TIMEOUT = 10
DEFAULT_PERFORMANCE_REQUESTS = 10
DEFAULT_OUTPUT_FILE = "scan_results.json"

# User-Agent padrão
DEFAULT_USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/122.0 Safari/537.36"
)

# Headers de segurança para verificar
SECURITY_HEADERS = [
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-XSS-Protection",
    "Referrer-Policy",
    "Permissions-Policy",
]
