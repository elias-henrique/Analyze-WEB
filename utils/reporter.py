"""
Gerador de relatórios em múltiplos formatos
"""

import json
from datetime import datetime
from typing import Any, Dict


class ReportGenerator:
    """Gera relatórios de scan e vulnerabilidades."""

    def __init__(self, data: Dict[str, Any]):
        self.data = data

    def generate_json(self, output_file: str = 'report.json') -> str:
        """Gera relatório JSON."""
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, indent=2, ensure_ascii=False)
        return output_file

    def generate_html(self, output_file: str = 'report.html') -> str:
        """Gera relatório HTML."""
        vulnerabilities = self.data.get('vulnerabilities', [])

        severity_colors = {
            'High': '#dc3545',
            'Medium': '#fd7e14',
            'Low': '#ffc107',
            'Informational': '#17a2b8'
        }

        vuln_html = ""
        for vuln in vulnerabilities:
            severity = vuln.get('severity', 'Low')
            color = severity_colors.get(severity, '#6c757d')

            vuln_html += f"""
            <div class="vulnerability" style="border-left: 4px solid {color};">
                <h3>{vuln.get('title', 'N/A')}
                    <span class="severity" style="background: {color};">{severity}</span>
                </h3>
                <p><strong>Tipo:</strong> {vuln.get('type', 'N/A')}</p>
                <p><strong>Descrição:</strong> {vuln.get('description', 'N/A')}</p>
                <p><strong>Impacto:</strong> {vuln.get('impact', 'N/A')}</p>
                <p><strong>Recomendação:</strong> {vuln.get('recommendation', 'N/A')}</p>
            </div>
            """

        html_content = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Relatório de Segurança</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: #f5f5f5;
            padding: 20px;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            padding: 30px;
        }}
        h1 {{
            color: #333;
            border-bottom: 3px solid #007bff;
            padding-bottom: 15px;
            margin-bottom: 30px;
        }}
        .info {{
            background: #e7f3ff;
            padding: 15px;
            border-radius: 5px;
            margin-bottom: 30px;
        }}
        .vulnerability {{
            background: #fff;
            border: 1px solid #ddd;
            border-radius: 5px;
            padding: 20px;
            margin-bottom: 20px;
        }}
        .vulnerability h3 {{
            color: #333;
            margin-bottom: 15px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        .severity {{
            color: white;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: bold;
        }}
        .vulnerability p {{
            margin: 10px 0;
            line-height: 1.6;
        }}
        .vulnerability strong {{
            color: #555;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Relatório de Análise de Segurança</h1>

        <div class="info">
            <p><strong>Target:</strong> {self.data.get('target', 'N/A')}</p>
            <p><strong>Data:</strong> {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}</p>
            <p><strong>Total de Achados:</strong> {len(vulnerabilities)}</p>
        </div>

        <h2>Vulnerabilidades Encontradas</h2>
        {vuln_html if vuln_html else '<p>Nenhuma vulnerabilidade encontrada.</p>'}

        <div style="margin-top: 40px; padding: 20px; background: #f8f9fa; border-radius: 5px;">
            <h3>⚠️ Aviso Legal</h3>
            <p>Este relatório foi gerado apenas para fins educacionais e de teste de segurança autorizado.
            Não utilize estas informações para atividades maliciosas.</p>
        </div>
    </div>
</body>
</html>"""

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)

        return output_file

    def generate_markdown(self, output_file: str = 'report.md') -> str:
        """Gera relatório Markdown."""
        vulnerabilities = self.data.get('vulnerabilities', [])

        md_content = f"""# Relatório de Segurança

**Target:** {self.data.get('target', 'N/A')}
**Data:** {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}
**Total de Vulnerabilidades:** {len(vulnerabilities)}

---

## Vulnerabilidades Encontradas

"""

        for vuln in vulnerabilities:
            md_content += f"""
### {vuln.get('title', 'N/A')}

- **Severidade:** {vuln.get('severity', 'N/A')}
- **Tipo:** {vuln.get('type', 'N/A')}
- **Descrição:** {vuln.get('description', 'N/A')}
- **Impacto:** {vuln.get('impact', 'N/A')}
- **Recomendação:** {vuln.get('recommendation', 'N/A')}

---
"""

        md_content += """
## ⚠️ Aviso Legal

Este relatório foi gerado apenas para fins educacionais e de teste de segurança autorizado.
Não utilize estas informações para atividades maliciosas.
"""

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(md_content)

        return output_file

    def generate_all(self, prefix: str = 'report') -> Dict[str, str]:
        """Gera todos os formatos de relatório."""
        return {
            'json': self.generate_json(f'{prefix}.json'),
            'html': self.generate_html(f'{prefix}.html'),
            'markdown': self.generate_markdown(f'{prefix}.md'),
        }
