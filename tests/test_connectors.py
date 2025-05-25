import pytest
from unittest.mock import AsyncMock, MagicMock, patch
import os
from connectors.chatgpt_connector import ChatGPTConnector  # Import the class

@pytest.fixture
def mock_openai_api_key():
    """Mock OpenAI API key for testing."""
    return "sk-test-openai-key"

@pytest.fixture
def mock_google_api_key():
    """Mock Google API key for testing."""
    return "test-google-key"

@pytest.fixture(autouse=True)
def mock_env_vars():
    """Mock environment variables for testing."""
    with patch.dict(os.environ, {
        "OPENAI_API_KEY": "sk-test-openai-key",
        "GOOGLE_API_KEY": "test-google-key"
    }):
        yield

def test_chatgpt_connector_initialization(mock_openai_api_key):
    """Test ChatGPT connector initialization."""
    connector = ChatGPTConnector(api_key=mock_openai_api_key)
    assert connector.api_key == mock_openai_api_key

def test_gemini_connector_initialization(mock_google_api_key):
    """Test Gemini connector initialization."""
    from llm_connectors import GeminiConnector
    connector = GeminiConnector(api_key=mock_google_api_key)
    assert connector.api_key == mock_google_api_key

@pytest.mark.asyncio
async def test_chatgpt_chat_method():
    """Test ChatGPT chat method with mock response."""
    mock_response = {"message": "Expected response"}
    
    with patch.object(ChatGPTConnector, 'chat', AsyncMock(return_value=mock_response)):
        connector = ChatGPTConnector(api_key="test_key")
        prompt = "Hello, how are you?"
        response = await connector.chat(prompt)
        
        assert isinstance(response, dict)
        assert "message" in response
        assert response["message"] == "Expected response"

@pytest.mark.asyncio
async def test_gemini_chat_method(mock_google_api_key):
    """Test Gemini chat method with mock response."""
    mock_response = AsyncMock()
    mock_response.text = "Hi there!"
    
    mock_chat = AsyncMock()
    mock_chat.send_message_async = AsyncMock(return_value=mock_response)
    
    mock_model = AsyncMock()
    mock_model.start_chat_async = AsyncMock(return_value=mock_chat)  # Fixed method name

    with patch('google.generativeai.GenerativeModel.from_api_key', return