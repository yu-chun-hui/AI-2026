import os
from pathlib import Path

from dotenv import load_dotenv
from autogen_ext.models.openai import OpenAIChatCompletionClient



def _setup_deepseek_model_client():
    """设置模型客户端"""
    model_config = {"model": "deepseek-v4-pro", "api_key": "sk-xxxxxxxxxxxxxxx", "model_info": {
        "vision": False,
        "function_calling": True,
        "json_output": True,
        "family": "unknown",
        "multiple_system_messages": True,
        "structured_output": True
    }, "base_url": "https://api.deepseek.com"}

    return OpenAIChatCompletionClient(**model_config)


deepseek_model_client = _setup_deepseek_model_client()

