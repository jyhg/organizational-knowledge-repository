from app.config import settings
from app.llm_gateway.base import LLMProvider
from app.llm_gateway.claude_provider import ClaudeProvider
from app.llm_gateway.deepseek_provider import DeepSeekProvider


class LLMRouter:
    """Routes LLM requests to the configured provider with fallback support."""

    PROVIDERS: dict[str, type[LLMProvider]] = {
        "claude": ClaudeProvider,
        "deepseek": DeepSeekProvider,
    }

    def __init__(self):
        self.primary = self._create_provider(settings.default_llm_provider)
        self.fallback_order = [
            name for name in self.PROVIDERS if name != settings.default_llm_provider
        ]

    def _create_provider(self, name: str) -> LLMProvider:
        provider_cls = self.PROVIDERS.get(name)
        if not provider_cls:
            raise ValueError(f"Unknown LLM provider: {name}")
        return provider_cls()

    async def generate(self, question: str, contexts: list, system_prompt: str = "") -> str:
        """Generate response using primary provider, falling back on failure."""
        context_text = "\n\n".join(str(ctx) for ctx in contexts)
        prompt = f"上下文:\n{context_text}\n\n问题: {question}"

        try:
            return await self.primary.generate(prompt, system_prompt)
        except Exception:
            for fallback_name in self.fallback_order:
                try:
                    fallback = self._create_provider(fallback_name)
                    return await fallback.generate(prompt, system_prompt)
                except Exception:
                    continue
            raise RuntimeError("All LLM providers failed")
