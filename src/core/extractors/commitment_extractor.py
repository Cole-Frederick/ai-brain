"""Extract commitments from raw message text"""

from typing import List, Dict, Any
from datetime import datetime
from enum import Enum


class CommitmentType(Enum):
    """Types of commitments"""
    CLIENT_PROMISE = "client_promise"
    INTERNAL_DEADLINE = "internal_deadline"
    FOLLOW_UP = "follow_up"


class CommitmentExtractor:
    """Extracts commitments and promises from conversation text"""
    
    def extract(
        self,
        messages: List[Dict[str, Any]],
        current_time: datetime
    ) -> List[Dict[str, Any]]:
        """
        Extract commitments from raw message text
        
        Args:
            messages: List of messages with rawText
            current_time: Current evaluation timestamp
            
        Returns:
            List of commitments:
            {
                "extractedAt": datetime,
                "messageId": str,
                "type": CommitmentType,
                "dueDate": datetime,
                "description": str,
                "fulfilled": bool
            }
        """
        # TODO: Implement commitment extraction logic
        # Pattern matching for: "I'll send by...", "Let's meet on...", etc.
        pass
