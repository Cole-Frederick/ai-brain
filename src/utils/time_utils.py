"""Time-based utility functions"""

from datetime import datetime, timedelta
from typing import Optional


class TimeUtils:
    """Utility functions for time calculations"""
    
    @staticmethod
    def days_since(past_time: Optional[datetime], current_time: datetime) -> float:
        """
        Calculate days since a past timestamp
        
        Args:
            past_time: Past timestamp
            current_time: Current timestamp
            
        Returns:
            Number of days (float)
        """
        if past_time is None:
            return float('inf')
        
        delta = current_time - past_time
        return delta.total_seconds() / 86400  # seconds in a day
    
    @staticmethod
    def is_within_grace_period(
        expected_by: datetime,
        grace_period_hours: float,
        current_time: datetime
    ) -> bool:
        """
        Check if current time is within grace period
        
        Args:
            expected_by: Expected response timestamp
            grace_period_hours: Grace period in hours
            current_time: Current timestamp
            
        Returns:
            True if within grace period
        """
        grace_end = expected_by + timedelta(hours=grace_period_hours)
        return current_time <= grace_end
    
    @staticmethod
    def days_in_stage(created_at: datetime, current_time: datetime) -> float:
        """
        Calculate days in current stage
        
        Args:
            created_at: Stage start timestamp
            current_time: Current timestamp
            
        Returns:
            Number of days (float)
        """
        return TimeUtils.days_since(created_at, current_time)
