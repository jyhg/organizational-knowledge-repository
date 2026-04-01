from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class ChatRequest(BaseModel):
    message: str
    conversation_id: str | None = None


class ChatResponse(BaseModel):
    answer: str
    sources: list[str]
    conversation_id: str


@router.post("", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Handle knowledge base Q&A requests via RAG pipeline."""
    # TODO: integrate RAG pipeline
    return ChatResponse(
        answer="[RAG pipeline not yet connected]",
        sources=[],
        conversation_id=request.conversation_id or "new-session",
    )
