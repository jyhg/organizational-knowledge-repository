from app.rag.models import RetrievedContext


class Reranker:
    """Rerank retrieved contexts for better relevance."""

    async def rerank(self, query: str, candidates: list[RetrievedContext], top_k: int = 5) -> list[RetrievedContext]:
        """Rerank candidates by relevance to the query."""
        # TODO: integrate with cross-encoder or LLM-based reranker
        return candidates[:top_k]
