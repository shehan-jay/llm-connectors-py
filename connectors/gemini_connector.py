class GeminiConnector:
    def __init__(self, api_key: str):
        self.api_key = api_key

    async def chat(self, prompt: str) -> str:
        """Simulate a chat response."""
        # Mocked response for testing purposes
        return "Hi there!"
