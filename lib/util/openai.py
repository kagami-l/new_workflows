import os
from typing import Optional

from openai import OpenAI, Stream
from openai.types.chat import ChatCompletionChunk


def create_chat_completion_chunks(
    client: Optional[OpenAI] = None, **kwargs
) -> Stream[ChatCompletionChunk]:
    """
    Create streaming responses.
    """
    _client = client or OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY", None),
        base_url=os.environ.get("OPENAI_API_BASE", None),
    )

    # Force to use streaming
    kwargs["stream"] = True

    return _client.chat.completions.create(**kwargs)