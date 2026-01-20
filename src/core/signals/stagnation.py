"""Stagnation detection signal processor"""

from typing import Dict, Any
from datetime import datetime
from src.utils.time_utils import TimeUtils


class StagnationDetector:
    """Detects deal stagnation based on stage duration"""
    
    # Stage-specific thresholds (in days)
    STAGE_THRESHOLDS = {
        "lead": 7,
        "qualified": 14,
        "proposition": 21,
        "negotiation": 14,
        "closed_won": 999,  # No stagnation for closed deals
        "closed_lost": 999,
    }
    
    # Default threshold for unknown stages
    DEFAULT_THRESHOLD = 14
    
    def detect(
        self,
        stage: str,
        created_at: datetime,
        current_time: datetime
    ) -> Dict[str, Any]:
        """
        Detect stagnation based on stage duration
        
        Args:
            stage: Current deal stage
            created_at: Deal creation timestamp (or stage entry time)
            current_time: Current evaluation timestamp
            
        Returns:
            {
                "detected": bool,
                "daysInCurrentStage": float
            }
        """
        # Calculate days in current stage
        days_in_stage = TimeUtils.days_in_stage(created_at, current_time)
        
        # Get threshold for this stage (case-insensitive)
        stage_lower = stage.lower().replace(" ", "_")
        threshold = self.STAGE_THRESHOLDS.get(stage_lower, self.DEFAULT_THRESHOLD)
        
        # Detect stagnation
        detected = days_in_stage > threshold
        
        return {
            "detected": detected,
            "daysInCurrentStage": days_in_stage
        }
