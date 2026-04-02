from app.llm_gateway.router import LLMRouter
from app.rag.pipeline import RAGPipeline


class ChatService:
    """Orchestrates the chat flow: query -> RAG retrieval -> LLM generation -> response."""

    def __init__(self):
        self.rag_pipeline = RAGPipeline()
        self.llm_router = LLMRouter()

    async def answer(self, question: str, conversation_id: str | None = None) -> dict:
        # Step 1: Retrieve relevant context
        contexts = await self.rag_pipeline.retrieve(question)

        # Step 2: Generate answer using LLM
        answer = await self.llm_router.generate(
            question=question,
            contexts=contexts,
        )

        return {
            "answer": answer,
            "sources": [ctx.source for ctx in contexts],
            "conversation_id": conversation_id or "new-session",
        }
