from typing import Any, Dict, List, Optional, cast
import openai
from openai.types.chat import ChatCompletion, ChatCompletionMessage
from openai.types.create_embedding_response import CreateEmbeddingResponse

from .base import BaseConnector

class ChatGPTConnector(BaseConnector):
    """Connector for OpenAI's ChatGPT API."""

    def __init__(self, api_key: str, **kwargs: Any) -> None:
        """Initialize the ChatGPT connector.

        Args:
            api_key (str): OpenAI API key
            **kwargs: Additional OpenAI client configuration
        """
        super().__init__(api_key, **kwargs)
        self.client = openai.OpenAI(api_key=api_key, **kwargs)

    async def chat(
        self,
        messages: List[Dict[str, str]],
        temperature: float = 0.7,
        max_tokens: Optional[int] = None,
        **kwargs: Any
    ) -> Dict[str, Any]:
        """Send a chat request to ChatGPT."""
        response = self.client.chat.completions.create(
            model=kwargs.get("model", "gpt-3.5-turbo"),
            messages=cast(Any, messages),
            temperature=temperature,
            max_tokens=max_tokens,
            **kwargs
        )
        if hasattr(response, "model_dump"):
            return cast(Dict[str, Any], response.model_dump())
        return {
            "content": response.choices[0].message.content,
            "choices": [{"message": {"content": response.choices[0].message.content}}]
        }

    async def generate_text(
        self,
        prompt: str,
        temperature: float = 0.7,
        max_tokens: Optional[int] = None,
        **kwargs: Any
    ) -> str:
        """Generate text using ChatGPT."""
        response = self.client.chat.completions.create(
            model=kwargs.get("model", "gpt-3.5-turbo"),
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens,
            **kwargs
        )
        return str(response.choices[0].message.content)

    async def get_embeddings(
        self,
        text: str,
        **kwargs: Any
    ) -> List[float]:
        """Get embeddings for the input text using OpenAI's embedding model."""
        response = self.client.embeddings.create(
            model=kwargs.get("model", "text-embedding-ada-002"),
            input=text,
            **kwargs
        )
        return cast(List[float], response.data[0].embedding) 