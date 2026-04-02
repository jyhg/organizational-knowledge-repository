from fastapi import APIRouter, File, UploadFile
from pydantic import BaseModel

router = APIRouter()


class DocumentInfo(BaseModel):
    id: str
    title: str
    category: str
    status: str
    updated_at: str


@router.get("", response_model=list[DocumentInfo])
async def list_documents():
    """List all knowledge base documents."""
    # TODO: query database
    return []


@router.post("/upload")
async def upload_document(file: UploadFile = File(...), category: str = "general"):
    """Upload a document to the knowledge base."""
    # TODO: parse document, chunk, embed, store
    return {"filename": file.filename, "category": category, "status": "pending"}


@router.delete("/{doc_id}")
async def delete_document(doc_id: str):
    """Remove a document from the knowledge base."""
    # TODO: delete from DB and vector store
    return {"id": doc_id, "deleted": True}
