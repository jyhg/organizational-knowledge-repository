from dataclasses import dataclass

from app.rag.chunking.splitter import TextSplitter
from app.rag.embedding.embedder import Embedder
from app.rag.rerank.reranker import Reranker
from app.rag.retrieval.vector_store import VectorStore


@dataclass
class RetrievedContext:
    content: str
    source: str
    score: float


class RAGPipeline:
    """End-to-end RAG pipeline: chunk -> embed -> retrieve -> rerank."""

    def __init__(self):
        self.splitter = TextSplitter()
        self.embedder = Embedder()
        self.vector_store = VectorStore()
        self.reranker = Reranker()

    async def ingest(self, text: str, source: str) -> None:
        """Process and store a document into the vector database."""
        chunks = self.splitter.split(text)
        embeddings = await self.embedder.embed(chunks)
        await self.vector_store.add(chunks, embeddings, source)

    async def retrieve(self, query: str, top_k: int = 5) -> list[RetrievedContext]:
        """Retrieve relevant context for a query."""
        query_embedding = await self.embedder.embed_query(query)
        candidates = await self.vector_store.search(query_embedding, top_k=top_k * 2)
        reranked = await self.reranker.rerank(query, candidates, top_k=top_k)
        return reranked
