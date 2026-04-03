import httpx
from anthropic import AsyncAnthropic

from app.config import settings
from app.llm_gateway.base import LLMProvider


class ClaudeProvider(LLMProvider):
    """Anthropic Claude LLM provider — supports custom base_url (e.g. MiniMax)."""

    def __init__(self):
        kwargs: dict = {"api_key": settings.anthropic_api_key}
        if settings.anthropic_base_url:
            kwargs["base_url"] = settings.anthropic_base_url
        # Use a custom httpx client with proxy=None to bypass system/TUN proxies.
        # Required when Clash TUN mode is active and routes domestic CN APIs incorrectly.
        kwargs["http_client"] = httpx.AsyncClient(proxy=None, timeout=60.0)
        self.client = AsyncAnthropic(**kwargs)
        self.model = settings.anthropic_model

    async def generate(self, prompt: str, system_prompt: str = "") -> str:
        message = await self.client.messages.create(
            model=self.model,
            max_tokens=2048,
            system=system_prompt,
            messages=[{"role": "user", "content": prompt}],
        )
        # MiniMax returns multiple content blocks (ThinkingBlock + TextBlock)
        # Extract text from TextBlock
        for block in message.content:
            if hasattr(block, 'text'):
                return block.text
        # Fallback to first block if no TextBlock found
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
