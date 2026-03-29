"""
config/llm_config.py
--------------------
LLM backend configuration helpers.

Supports:
  - OpenAI          (default)
  - Azure OpenAI
  - Ollama          (local, experimental)

Set the backend via the LLM_BACKEND environment variable:
  LLM_BACKEND=openai      → uses OPENAI_API_KEY + LLM_MODEL
  LLM_BACKEND=azure       → uses AZURE_OPENAI_* variables
  LLM_BACKEND=ollama      → uses OLLAMA_BASE_URL + LLM_MODEL
"""

import os
from autogen_ext.models.openai import OpenAIChatCompletionClient


def get_model_client() -> OpenAIChatCompletionClient:
    """Return an appropriate OpenAIChatCompletionClient based on env vars."""
    backend = os.getenv("LLM_BACKEND", "openai").lower()

    if backend == "azure":
        return OpenAIChatCompletionClient(
            model=os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-4o"),
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            base_url=os.getenv("AZURE_OPENAI_ENDPOINT"),
            api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2024-08-01-preview"),
        )

    if backend == "ollama":
        return OpenAIChatCompletionClient(
            model=os.getenv("LLM_MODEL", "llama3"),
            base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434/v1"),
            api_key="ollama",          # Ollama doesn't require a real key
        )

    # Default: OpenAI
    return OpenAIChatCompletionClient(
        model=os.getenv("LLM_MODEL", "gpt-4o"),
    )
