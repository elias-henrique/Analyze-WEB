"""
Biblioteca principal do CRM Scanner
"""

from .models import AvailabilityResult, EndpointResult, ScanResults
from .scanner import CRMScanner

__version__ = "1.0.0"
__all__ = ["CRMScanner", "ScanResults", "AvailabilityResult", "EndpointResult"]
