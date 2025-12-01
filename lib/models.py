"""
Modelos de dados para resultados de scan
"""

from dataclasses import asdict, dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class AvailabilityResult:
    """Resultado do teste de disponibilidade"""
    status: str
    status_code: int
    response_time: float
    headers: Dict[str, str]


@dataclass
class EndpointResult:
    """Resultado da análise de um endpoint"""
    endpoint: str
    status_code: int
    content_type: str
    size: int


@dataclass
class ScanResults:
    """Resultados completos do scan"""
    timestamp: str
    target: str
    availability: Optional[AvailabilityResult] = None
    endpoints: List[EndpointResult] = field(default_factory=list)
    security_headers: Dict[str, Optional[str]] = field(default_factory=dict)
    ssl: Dict[str, Any] = field(default_factory=dict)
    performance: Dict[str, Any] = field(default_factory=dict)
    technologies: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        """Converte dataclasses em um dicionário pronto para JSON."""
        return {
            "timestamp": self.timestamp,
            "target": self.target,
            "tests": {
                "availability": asdict(self.availability) if self.availability else None,
                "endpoints": [asdict(e) for e in self.endpoints],
                "security_headers": self.security_headers,
                "ssl": self.ssl,
                "performance": self.performance,
                "technologies": self.technologies,
            },
        }
