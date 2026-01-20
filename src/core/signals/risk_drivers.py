"""Risk drivers and aggregations prioritization"""

from typing import List, Dict, Any
from enum import Enum


class RiskTypeEnum(Enum):
    """Types of risk drivers"""
    SILENCE = "silence"
    MISSED_COMMITMENTS = "missed_commitments"
    STAGNATION = "stagnation"
    MISSING_DATA = "missing_data"
    INACTIVITY = "inactivity"


class RiskSeverityEnum(Enum):
    """Severity levels for risk drivers"""
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class RiskDriverAggregator:
    """Aggregates and prioritizes risk drivers"""
    
    def aggregate(
        self,
        risk_drivers: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """
        Aggregate and prioritize risk drivers
        
        Args:
            risk_drivers: List of detected risk drivers
            
        Returns:
            Prioritized list of risk drivers
        """   
