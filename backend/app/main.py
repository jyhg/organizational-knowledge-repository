from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import auth, chat, docs
from app.api import eval as eval_api
from app.config import settings

app = FastAPI(
    title="供应链知识库 API",
    description="Enterprise AI-powered supply chain knowledge base",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat.router, prefix="/api/chat", tags=["Chat"])
app.include_router(docs.router, prefix="/api/docs", tags=["Documents"])
app.include_router(auth.router, prefix="/api/auth", tags=["Auth"])
app.include_router(eval_api.router, prefix="/api/eval", tags=["Evaluation"])


@app.get("/health")
async def health_check():
    return {"status": "ok"}
