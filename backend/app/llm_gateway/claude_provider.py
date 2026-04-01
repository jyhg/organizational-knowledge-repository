from anthropic import AsyncAnthropic

from app.config import settings
from app.llm_gateway.base import LLMProvider


class ClaudeProvider(LLMProvider):
    """Anthropic Claude LLM provider."""

    def __init__(self):
        self.client = AsyncAnthropic(api_key=settings.anthropic_api_key)
        self.model = "claude-sonnet-4-20250514"

    async def generate(self, prompt: str, system_prompt: str = "") -> str:
        message = await self.client.messages.create(
            model=self.model,
            max_tokens=2048,
            system=system_prompt,
            messages=[{"role": "user", "content": prompt}],
        )
        return message.content[0].text

    async def health_check(self) -> bool:
        try:
            await self.client.messages.create(
                model=self.model,
                max_tokens=10,
                messages=[{"role": "user", "content": "ping"}],
            )
            return True
        except Exception:
            return False
