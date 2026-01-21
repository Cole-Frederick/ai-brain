"""Extract entities (dates, budgets, decision-makers) from messages"""

from typing import List, Dict, Any


class EntityExtractor:
    """Extracts structured entities from conversation text"""
    
    def extract_dates(self, text: str) -> List[str]:
        """Extract date mentions from text"""
        # TODO: Implement date extraction
        pass
    
    def extract_budget(self, text: str) -> Dict[str, Any]:
        """Extract budget/value mentions from text"""
        # TODO: Implement budget extraction
        pass
    
    def extract_decision_makers(self, text: str) -> List[str]:
        """Extract decision-maker names from text"""
        # TODO: Implement decision-maker extraction
        pass
