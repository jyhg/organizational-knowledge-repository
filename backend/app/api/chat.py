from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.chat_service import ChatService

router = APIRouter()
_chat_service = ChatService()


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
    try:
        result = await _chat_service.answer(
            question=request.message,
            conversation_id=request.conversation_id,
        )
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"LLM 服务暂时不可用: {e}") from e
    return ChatResponse(
        answer=result["answer"],
        sources=result["sources"],
        conversation_id=result["conversation_id"],
    )
