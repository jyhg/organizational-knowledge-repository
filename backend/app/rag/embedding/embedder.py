class Embedder:
    """Generate embeddings for text chunks using configured embedding model."""

    async def embed(self, texts: list[str]) -> list[list[float]]:
        """Embed a batch of texts."""
        # TODO: integrate with OpenAI / local embedding model
        return [[0.0] * 768 for _ in texts]

    async def embed_query(self, query: str) -> list[float]:
        """Embed a single query text."""
        # TODO: integrate with embedding model
        return [0.0] * 768
