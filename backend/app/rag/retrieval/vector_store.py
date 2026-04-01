from app.rag.pipeline import RetrievedContext


class VectorStore:
    """Interface to the vector database (ChromaDB / Milvus)."""

    async def add(self, chunks: list[str], embeddings: list[list[float]], source: str) -> None:
        """Add embedded chunks to the vector store."""
        # TODO: integrate with ChromaDB
        pass

    async def search(self, query_embedding: list[float], top_k: int = 10) -> list[RetrievedContext]:
        """Search for similar vectors."""
        # TODO: integrate with ChromaDB
        return []
