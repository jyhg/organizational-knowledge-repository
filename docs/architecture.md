# Architecture Overview

## System Architecture

```
User (Browser) → Nginx → Frontend (Vue 3) → Backend API (FastAPI)
                                                    ↓
                                              RAG Pipeline
                                          ┌─────────────────┐
                                          │ Document Parsing │
                                          │ Chunking         │
                                          │ Embedding        │
                                          │ Vector Retrieval │
                                          │ Reranking        │
                                          │ LLM Generation   │
                                          └─────────────────┘
                                                    ↓
                                          LLM Gateway (Multi-model)
                                          ┌──────┬──────────┐
                                          │Claude│ DeepSeek │
                                          └──────┴──────────┘
```

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Vue 3, Vite, TypeScript, Element Plus, Pinia, ECharts |
| Backend | Python, FastAPI, LangChain, SQLAlchemy |
| Vector DB | ChromaDB (dev) / Milvus (prod) |
| Cache | Redis |
| LLM | Claude, DeepSeek (via unified gateway) |
| Testing | Pytest, DeepEval, RAGAS, Cypress, Locust |
| Infra | Docker Compose, Nginx, GitHub Actions |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| POST | /api/chat | Knowledge base Q&A |
| GET | /api/docs | List documents |
| POST | /api/docs/upload | Upload document |
| DELETE | /api/docs/{id} | Delete document |
| POST | /api/auth/login | User login |
| GET | /api/auth/me | Current user info |
| GET | /api/eval/metrics | Latest eval metrics |
| GET | /api/eval/runs | Eval run history |
| POST | /api/eval/trigger | Trigger eval run |
| GET | /health | Health check |
