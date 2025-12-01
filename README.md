# CRM Scanner & Security Tools

Uma coleção modular de ferramentas para análise de segurança em aplicações web (CRMs).

## 📁 Estrutura do Projeto

```
test/
├── lib/                      # Biblioteca principal de scanning
│   ├── __init__.py
│   ├── config.py            # Configurações padrão
│   ├── models.py            # Modelos de dados
│   ├── scanner.py           # Scanner principal
│   ├── utils.py             # Utilitários do scanner
│   └── wordlists.py         # Listas de endpoints
│
├── exploits/                # Módulos de exploração
│   ├── __init__.py
│   ├── analyzer.py          # Analisador de vulnerabilidades
│   ├── exploit_admin.py     # Exploração de admin
│   └── generator.py         # Gerador de exploits
│
├── utils/                   # Utilitários compartilhados
│   ├── __init__.py
│   └── reporter.py          # Gerador de relatórios
│
├── scanner.py               # CLI: Scanner de endpoints
├── analyzer.py              # CLI: Análise de vulnerabilidades
├── exploit.py               # CLI: Exploração admin
├── requirements.txt         # Dependências Python
└── README.md               # Este arquivo
```

## 🚀 Instalação

```bash
# Clone ou navegue até o diretório
cd test/

# Instale as dependências
pip install -r requirements.txt
```

## 📖 Uso

### 1. Scanner de Endpoints

Realiza varredura completa de endpoints, headers de segurança, SSL, performance e tecnologias.

```bash
# Scan básico
python scanner.py https://exemplo.com

# Com opções
python scanner.py https://exemplo.com -o resultados.json -v

# Opções:
#   -o, --output      Arquivo de saída (default: scan_results.json)
#   -t, --timeout     Timeout em segundos (default: 10)
#   -n, --requests    Número de requisições de performance (default: 10)
#   -v, --verbose     Modo verboso
```

### 2. Analisador de Vulnerabilidades

Analisa vulnerabilidades de segurança e gera relatórios em múltiplos formatos.

```bash
# Análise básica
python analyzer.py https://exemplo.com

# Com opções
python analyzer.py https://exemplo.com -o relatorio -v

# Gera 3 arquivos:
#   - relatorio.json      (dados estruturados)
#   - relatorio.html      (visualização web)
#   - relatorio.md        (markdown)
```

### 3. Exploração Admin

Tenta explorar vulnerabilidades para acessar painéis administrativos.

```bash
# Exploração básica
python exploit.py https://exemplo.com

# Com modo verboso
python exploit.py https://exemplo.com -v

# ⚠️ APENAS PARA FINS EDUCACIONAIS E TESTES AUTORIZADOS
```

## 🔍 Funcionalidades

### Scanner (scanner.py)
- ✅ Teste de disponibilidade
- ✅ Varredura de endpoints (300+ paths)
- ✅ Análise de headers de segurança
- ✅ Teste de SSL/TLS
- ✅ Medição de performance
- ✅ Detecção de tecnologias (React, Next.js, etc)

### Analyzer (analyzer.py)
- ✅ Detecção de Client-Side Routing (SPA)
- ✅ Análise de headers ausentes
- ✅ Teste de Clickjacking
- ✅ Verificação de CORS
- ✅ Detecção de vazamento de informações
- ✅ Relatórios em JSON, HTML e Markdown

### Exploit (exploit.py)
- ✅ Reconhecimento avançado
- ✅ Descoberta de endpoints admin
- ✅ Teste de credenciais padrão
- ✅ SQL Injection básico
- ✅ Análise de código JavaScript
- ✅ Geração de exploits (token manipulation)

## 📦 Módulos

### lib/ - Biblioteca de Scanning
- `config.py` - Configurações e constantes
- `models.py` - Classes de dados (dataclasses)
- `scanner.py` - Lógica principal de scanning
- `wordlists.py` - Listas de endpoints e payloads
- `utils.py` - Funções auxiliares

### exploits/ - Exploração
- `analyzer.py` - Análise de vulnerabilidades
- `exploit_admin.py` - Exploração de admin
- `generator.py` - Geração de PoCs e exploits

### utils/ - Utilitários
- `reporter.py` - Geração de relatórios

## 🎯 Exemplos de Uso

### Scan completo com relatório
```bash
# 1. Execute o scanner
python scanner.py https://test.app -o scan.json -v

# 2. Analise vulnerabilidades
python analyzer.py https://test.app -o vuln

# 3. Visualize os relatórios
# - scan.json (resultados do scan)
# - vuln.json, vuln.html, vuln.md (vulnerabilidades)
```

### Pipeline completo
```bash
# Scan → Análise → Exploração
python scanner.py https://exemplo.com && \
python analyzer.py https://exemplo.com && \
python exploit.py https://exemplo.com
```

## ⚠️ Aviso Legal

**IMPORTANTE:** Estas ferramentas são para fins **EDUCACIONAIS** e **TESTES AUTORIZADOS** apenas.

- ✅ Use apenas em sistemas que você possui ou tem permissão explícita para testar
- ✅ Sempre obtenha autorização por escrito antes de realizar testes
- ❌ Uso não autorizado é ILEGAL e pode resultar em consequências criminais
- ❌ Nunca use contra sistemas de terceiros sem permissão

O autor não se responsabiliza por uso indevido destas ferramentas.

## 📝 Testes

Todos os scripts foram testados com:
- Python 3.8+
- requests 2.31.0
- beautifulsoup4 4.12.0

## 🤝 Contribuindo

Este é um projeto educacional. Sinta-se livre para estudar, modificar e aprender!

## 📄 Licença

Apenas para fins educacionais.

---

**Made for Security Education** 🔒
