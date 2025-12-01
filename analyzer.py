#!/usr/bin/env python3
"""
Security Analyzer - Análise de vulnerabilidades

Script de análise de segurança para aplicações web.
"""

import argparse
import sys

from exploits.analyzer import SecurityAnalyzer
from lib.utils import configure_logging
from utils.reporter import ReportGenerator


def parse_args(argv=None):
    """Parse argumentos da linha de comando."""
    parser = argparse.ArgumentParser(
        description="Analisador de vulnerabilidades de segurança."
    )
    parser.add_argument(
        "target",
        help="URL base do alvo",
    )
    parser.add_argument(
        "-o",
        "--output",
        default="vulnerability_report",
        help="Prefixo para arquivos de saída (default: vulnerability_report)",
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

    target = args.target
    if not target.startswith(("http://", "https://")):
        target = "https://" + target

    # Executa análise
    analyzer = SecurityAnalyzer(target)
    results = analyzer.run_analysis()

    # Gera relatórios
    reporter = ReportGenerator(results)
    files = reporter.generate_all(args.output)

    print("\n📁 Relatórios gerados:")
    for format_type, filename in files.items():
        print(f"  • {filename} ({format_type.upper()})")

    return 0


if __name__ == "__main__":
    sys.exit(main())
