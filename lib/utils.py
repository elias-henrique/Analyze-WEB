"""
Utilitários compartilhados
"""

import json
import logging
from pathlib import Path
from typing import Any, Dict

logger = logging.getLogger("crm_scanner")


def save_json(data: Dict[str, Any], filename: str) -> bool:
    """Salva dados em formato JSON."""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        logger.info("Dados salvos em: %s", filename)
        return True
    except OSError as exc:
        logger.error("Erro ao salvar em %s: %s", filename, exc)
        return False


def load_json(filename: str) -> Dict[str, Any]:
    """Carrega dados de um arquivo JSON."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError) as exc:
        logger.error("Erro ao carregar %s: %s", filename, exc)
        return {}


def ensure_dir(directory: str) -> None:
    """Garante que um diretório existe."""
    Path(directory).mkdir(parents=True, exist_ok=True)


def configure_logging(verbose: bool = False) -> None:
    """Configura logging global."""
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="[%(levelname)s] %(message)s",
    )
