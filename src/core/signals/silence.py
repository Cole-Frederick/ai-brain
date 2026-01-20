"""Silence detection signal processor"""

from typing import Dict, Any, Optional
from datetime import datetime
from enum import Enum
from src.utils.time_utils import TimeUtils


class SilenceType(Enum):
    """Types of silence detection"""
    EXPECTED = "expected"
    UNEXPECTED = "unexpected"
    GRACE_PERIOD = "grace_period"
    UNKNOWN = "unknown"


class SilenceDetector:
    """Detects and classifies silence in deal conversations"""
    
    def detect(
        self,
        last_activity_at: Optional[datetime],
        expected_response_window: Optional[Dict[str, Any]],
        current_time: datetime
    ) -> Dict[str, Any]:
        """
        Detect silence and classify type
        
        Args:
            last_activity_at: Timestamp of last activity
            expected_response_window: Expected response window from persisted state
            current_time: Current evaluation timestamp
            
        Returns:
            {
                "detected": bool,
                "type": SilenceType,
                "daysSinceLastActivity": float
            }
        """
        # Calculate days since last activity
        days_since = TimeUtils.days_since(last_activity_at, current_time)
        
        # No activity data - no silence detected
        if last_activity_at is None:
            return {
                "detected": False,
                "type": SilenceType.UNKNOWN.value,
                "daysSinceLastActivity": 0
            }
        
        # No expected response window - check basic threshold
        if expected_response_window is None:
            # More than 3 days = unexpected silence
            if days_since > 3:
                return {
                    "detected": True,
                    "type": SilenceType.UNEXPECTED.value,
                    "daysSinceLastActivity": days_since
                }
            else:
                return {
                    "detected": False,
                    "type": SilenceType.EXPECTED.value,
                    "daysSinceLastActivity": days_since
                }
        
        # Have expected response window
        expected_by = expected_response_window.get("expectedBy")
        grace_period_hours = expected_response_window.get("gracePeriodHours", 24)
        
        if expected_by is None:
            # Fallback to basic threshold
            if days_since > 3:
                return {
                    "detected": True,
                    "type": SilenceType.UNEXPECTED.value,
                    "daysSinceLastActivity": days_since
                }
            else:
                return {
                    "detected": False,
                    "type": SilenceType.EXPECTED.value,
                    "daysSinceLastActivity": days_since
                }
        
        # Check if within expected window
        if current_time <= expected_by:
            return {
                "detected": False,
                "type": SilenceType.EXPECTED.value,
                "daysSinceLastActivity": days_since
            }
        
        # Past expected time - check grace period
        if TimeUtils.is_within_grace_period(expected_by, grace_period_hours, current_time):
            return {
                "detected": True,
                "type": SilenceType.GRACE_PERIOD.value,
                "daysSinceLastActivity": days_since
            }
        
        # Past grace period - unexpected silence
        return {
            "detected": True,
            "type": SilenceType.UNEXPECTED.value,
            "daysSinceLastActivity": days_since
        }
