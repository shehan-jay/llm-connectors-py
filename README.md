# LLM Connectors

A Python library providing connectors for popular AI platforms including ChatGPT, Copilot, Gemini, and DeepSeek.

## Installation

```bash
pip install llm-connectors
```

## Development

### Setup

1. Clone the repository
2. Install development dependencies:
```bash
pip install -e ".[dev]"
```

### Testing

```bash
pytest
```

### Publishing to PyPI

1. Copy `.pypirc.template` to `.pypirc`
2. Get your API token from PyPI (https://pypi.org/manage/account/token/)
3. Build the package:
```bash
python -m build
```
4. Upload to PyPI:
```bash
twine upload dist/*
```

Note: Never commit your `.pypirc` file as it contains sensitive authentication information.

## Usage

### ChatGPT

```python
from llm_connectors import ChatGPTConnector

# Initialize the connector
chatgpt = ChatGPTConnector(api_key="your-openai-api-key")

# Chat example
messages = [
    {"role": "user", "content": "Hello, how are you?"}
]
response = await chatgpt.chat(messages)
print(response["content"])

# Text generation example
text = await chatgpt.generate_text("Write a poem about AI")
print(text)

# Get embeddings
embeddings = await chatgpt.get_embeddings("Hello, world!")
print(embeddings)
```

### Gemini

```python
from llm_connectors import GeminiConnector

# Initialize the connector
gemini = GeminiConnector(api_key="your-google-api-key")

# Chat example
messages = [
    {"role": "user", "content": "Hello, how are you?"}
]
response = await gemini.chat(messages)
print(response["content"])

# Text generation example
text = await gemini.generate_text("Write a poem about AI")
print(text)

# Get embeddings
embeddings = await gemini.get_embeddings("Hello, world!")
print(embeddings)
```

### Copilot and DeepSeek

Note: These connectors are currently placeholders and will be implemented when their respective APIs become available.

## Features

- Unified interface for multiple AI platforms
- Async support for better performance
- Consistent API across different providers
- Support for chat, text generation, and embeddings
- Type hints for better IDE support

## Requirements

- Python 3.8+
- OpenAI API key (for ChatGPT)
- Google API key (for Gemini)
- Microsoft API key (for Copilot, when available)
- DeepSeek API key (when available)

## License

MIT License
