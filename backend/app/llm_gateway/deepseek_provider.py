from openai import AsyncOpenAI

from app.config import settings
from app.llm_gateway.base import LLMProvider


class DeepSeekProvider(LLMProvider):
    """DeepSeek LLM provider (OpenAI-compatible API)."""

    def __init__(self):
        self.client = AsyncOpenAI(
            api_key=settings.deepseek_api_key,
            base_url="https://api.deepseek.com",
        )
        self.model = "deepseek-chat"

    async def generate(self, prompt: str, system_prompt: str = "") -> str:
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})

        response = await self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            max_tokens=2048,
        )
        return response.choices[0].message.content or ""

    async def health_check(self) -> bool:
        try:
            await self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": "ping"}],
                max_tokens=10,
            )
            return True
        except Exception:
            return False
