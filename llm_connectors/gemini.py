from typing import Any, Dict, List, Optional
import google.generativeai as genai
from google.generativeai.types import GenerateContentResponse
from .base import BaseConnector

class GeminiConnector(BaseConnector):
    """Connector for Google's Gemini API."""
    
    def __init__(self, api_key: str, **kwargs: Any) -> None:
        """Initialize the Gemini connector.
        
        Args:
            api_key (str): Google API key
            **kwargs: Additional Gemini configuration
        """
        super().__init__(api_key, **kwargs)
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(
            model_name=kwargs.get("model", "gemini-pro"),
            **kwargs
        )
    
    async def chat(
        self,
        messages: List[Dict[str, str]],
        temperature: float = 0.7,
        max_tokens: Optional[int] = None,
        **kwargs: Any
    ) -> Dict[str, Any]:
        """Send a chat request to Gemini.
        
        Args:
            messages: A list of message dictionaries with 'role' and 'content' keys.
            temperature: The temperature for the generation
            max_tokens: The maximum number of tokens to generate
            **kwargs: Additional generation configuration
            
        Returns:
            A dictionary containing the response from Gemini.
        """
        chat = self.model.start_chat(history=[])
        response = await chat.send_message(
            messages[-1]["content"],
            generation_config=genai.types.GenerationConfig(
                temperature=temperature,
                max_output_tokens=max_tokens,
                **kwargs
            )
        )
        return {
            "content": response.text,
            "candidates": [{"content": response.text}]
        }
    
    async def generate_text(
        self,
        prompt: str,
        temperature: float = 0.7,
        max_tokens: Optional[int] = None,
        **kwargs: Any
    ) -> str:
        """Generate text using Gemini.
        
        Args:
            prompt: The text prompt to generate from.
            temperature: The temperature for the generation
            max_tokens: The maximum number of tokens to generate
            **kwargs: Additional generation configuration
            
        Returns:
            The generated text.
        """
        response = await self.model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                temperature=temperature,
                max_output_tokens=max_tokens,
                **kwargs
            )
        )
        return str(response.text)
    
    async def get_embeddings(
        self,
        text: str,
        **kwargs: Any
    ) -> List[float]:
        """Get embeddings for the input text using Gemini's embedding model.
        
        Args:
            text: The text to get embeddings for.
            **kwargs: Additional embedding configuration
            
        Returns:
            A list of floats representing the embeddings.
        """
        # Gemini API does not currently support embeddings
        raise NotImplementedError("Embeddings are not yet available for Gemini.") 