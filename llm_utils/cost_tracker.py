"""Cost tracking utilities."""

from typing import Dict

PRICING = {
    "gpt-4": {"input": 0.03, "output": 0.06},
    "gpt-3.5-turbo": {"input": 0.001, "output": 0.002},
}

class CostTracker:
    def __init__(self, api_key: str = None):
        self.api_key = api_key
        self.total_cost = 0.0
    
    def track(self, model: str, tokens: int, direction: str = "input"):
        if model in PRICING:
            cost = PRICING[model][direction] * (tokens / 1000)
            self.total_cost += cost
            return cost
        return 0.0
    
    def get_total(self) -> float:
        return self.total_cost
