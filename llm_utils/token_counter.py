"""Token counting utilities."""

class TokenCounter:
    def __init__(self, model: str = "gpt-4"):
        self.model = model
        # Approximate tokens per character
        self.ratio = 0.25 if "gpt-4" in model else 0.3
    
    def count(self, text: str) -> int:
        return int(len(text) * self.ratio)
