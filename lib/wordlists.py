"""
Wordlists de endpoints e paths comuns
"""

ENDPOINTS_WORDLIST = [
    # === ENDPOINTS POPULARES ===
    # Páginas principais
    "/", "/home", "/index", "/index.html", "/index.php",

    # Autenticação
    "/login", "/signin", "/sign-in", "/auth", "/authenticate",
    "/register", "/signup", "/sign-up", "/logout",
    "/password-reset", "/forgot-password", "/reset-password",

    # Dashboard e painéis
    "/dashboard", "/panel", "/console", "/admin", "/admin/dashboard",
    "/administrator", "/manager", "/user", "/profile",
    "/account", "/settings", "/preferences",

    # CRM específicos
    "/tickets", "/ticket", "/calendar", "/contacts", "/contact",
    "/leads", "/lead", "/customers", "/customer", "/clients", "/client",
    "/opportunities", "/deals", "/pipeline", "/sales",
    "/tasks", "/task", "/activities", "/notes", "/emails",
    "/campaigns", "/marketing",

    # Relatórios e Analytics
    "/reports", "/report", "/analytics", "/statistics",
    "/stats", "/metrics", "/insights", "/charts", "/graphs",

    # Financeiro
    "/finance", "/financial", "/invoices", "/invoice",
    "/billing", "/payments", "/payment", "/transactions", "/transaction",
    "/revenue", "/expenses", "/expense", "/budget", "/accounting",
    "/subscriptions", "/subscription", "/quotes", "/quote",
    "/orders", "/order", "/products", "/product", "/services", "/service",

    # APIs principais
    "/api", "/api/v1", "/api/v2", "/api/v3",
    "/api/health", "/api/status", "/api/ping",
    "/api/dashboard", "/api/tickets", "/api/calendar",
    "/api/contacts", "/api/users", "/api/user",
    "/api/customers", "/api/leads", "/api/finance",
    "/api/financial", "/api/invoices", "/api/billing",
    "/api/payments", "/api/transactions", "/api/revenue",
    "/api/expenses", "/api/reports", "/api/analytics",
    "/api/auth", "/api/login", "/api/register", "/api/logout",

    # GraphQL
    "/graphql", "/api/graphql", "/graphiql", "/playground",

    # Webhooks
    "/webhook", "/webhooks", "/api/webhook",
    "/api/webhooks", "/hooks", "/callback", "/callbacks",

    # Documentação
    "/docs", "/documentation", "/api-docs", "/swagger",
    "/swagger-ui", "/api/docs", "/help", "/support", "/faq",

    # Arquivos estáticos comuns
    "/robots.txt", "/sitemap.xml", "/favicon.ico", "/manifest.json",

    # === ENDPOINTS NÃO POPULARES / SENSÍVEIS ===
    # Arquivos de configuração
    "/.env", "/.env.local", "/.env.production", "/.env.development",
    "/config", "/config.json", "/config.php", "/config.yml", "/config.yaml",
    "/configuration.php", "/settings.php", "/wp-config.php",
    "/.git", "/.git/config", "/.git/HEAD", "/.gitignore",
    "/.svn", "/.hg", "/.DS_Store",

    # Backups e temporários
    "/backup", "/backups", "/backup.sql", "/backup.zip",
    "/dump.sql", "/database.sql", "/db.sql",
    "/temp", "/tmp", "/cache", "/.cache", "/old", "/test", "/tests",
    "/testing", "/dev", "/development",

    # Debug e logs
    "/debug", "/debug.log", "/error.log", "/errors.log", "/access.log",
    "/logs", "/log", "/.log", "/phpinfo.php", "/info.php",
    "/test.php", "/debug.php", "/_debug", "/__debug",
    "/console", "/shell",

    # Admin alternativo
    "/admin.php", "/admin/", "/admin/index.php", "/administrator/",
    "/admin/login", "/admin/login.php", "/admincp", "/modcp",
    "/moderator", "/wp-admin", "/wp-login.php",
    "/phpmyadmin", "/phpMyAdmin", "/pma", "/mysql",
    "/dbadmin", "/adminer.php", "/adminer",

    # APIs internas/privadas
    "/api/internal", "/api/private", "/api/admin",
    "/api/debug", "/api/test", "/api/dev",
    "/internal", "/private", "/_api", "/__api",

    # Uploads e arquivos
    "/upload", "/uploads", "/uploaded", "/files", "/file",
    "/media", "/images", "/img", "/assets", "/public",
    "/static", "/downloads", "/download", "/attachments",

    # Páginas de status
    "/status", "/health", "/healthcheck", "/health-check",
    "/ping", "/version", "/info", "/server-status", "/server-info",

    # Instalação e setup
    "/install", "/install.php", "/setup", "/setup.php",
    "/installer", "/upgrade", "/migration", "/init",

    # Usuários e perfis
    "/users", "/user/1", "/user/admin", "/profiles",
    "/profile/1", "/accounts", "/members", "/member",

    # Exportação e importação
    "/export", "/import", "/api/export", "/api/import",
    "/download/export", "/backup/download",

    # Pesquisa e filtros
    "/search", "/find", "/query", "/filter",

    # Notificações
    "/notifications", "/notification", "/alerts",
    "/messages", "/message", "/inbox",

    # Integrações
    "/integrations", "/integration", "/plugins", "/plugin",
    "/modules", "/module", "/extensions", "/addons",

    # Permissões e roles
    "/permissions", "/roles", "/access", "/groups", "/teams", "/team",

    # Auditoria
    "/audit", "/audit-log", "/activity-log", "/history", "/changelog",

    # Cron e jobs
    "/cron", "/cronjob", "/jobs", "/queue", "/worker", "/scheduler",

    # Socket e realtime
    "/socket.io", "/ws", "/websocket", "/realtime", "/stream",

    # Mobile APIs
    "/api/mobile", "/mobile", "/app", "/api/app",

    # Páginas de erro
    "/404", "/500", "/error", "/error.html",

    # Outros endpoints sensíveis
    "/.well-known", "/.well-known/security.txt", "/security.txt",
    "/crossdomain.xml", "/clientaccesspolicy.xml",
    "/elmah.axd", "/trace.axd", "/web.config", "/.htaccess",
    "/composer.json", "/package.json", "/package-lock.json",
    "/yarn.lock", "/.npmrc", "/Dockerfile",
    "/docker-compose.yml", "/.dockerignore",
    "/Makefile", "/README.md", "/LICENSE",
    "/.editorconfig", "/phpunit.xml", "/.phpunit.result.cache",
]

# Endpoints admin específicos para descoberta
ADMIN_ENDPOINTS = [
    "/admin", "/admin/", "/admin/login", "/admin/dashboard",
    "/administrator", "/admin-panel", "/admin_area", "/adminpanel",
    "/control-panel", "/cp", "/admin/cp", "/admin/index",
    "/admin/admin", "/admin-console", "/backend", "/backend/admin",
    "/staff", "/superuser", "/management", "/manage", "/admin/settings",
    "/api/admin", "/api/v1/admin", "/api/users/admin", "/api/auth/admin",
    "/graphql", "/api/graphql",
    "/admin_login", "/admin_panel",
    "/_next/admin", "/api/admin/auth",
]

# Padrões de SQL Injection
SQLI_PAYLOADS = [
    "admin' OR '1'='1",
    "admin'--",
    "admin' #",
    "admin'/*",
    "' or 1=1--",
    "' or '1'='1'--",
    "admin' or '1'='1'/*",
]

# Credenciais padrão para teste
DEFAULT_CREDENTIALS = [
    {"username": "admin", "password": "admin"},
    {"username": "admin", "password": "Admin123"},
    {"username": "admin", "password": "password"},
    {"username": "administrator", "password": "administrator"},
    {"username": "admin", "password": "123456"},
    {"email": "admin@example.com", "password": "admin"},
]
