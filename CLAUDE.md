# Supply Chain Knowledge Base

## Project Overview
Enterprise AI-powered e-commerce supply chain knowledge base with RAG pipeline.

## Architecture
- **Frontend**: Vue 3 + Vite + TypeScript + Element Plus + Pinia + ECharts
- **Backend**: Python FastAPI + LangChain + ChromaDB
- **LLM Gateway**: Multi-model support (Claude, DeepSeek) with fallback
- **Infra**: Docker Compose + Nginx + GitHub Actions CI/CD

## Directory Structure
- `frontend/` — Vue 3 SPA (chat, docs management, eval dashboard)
- `backend/` — FastAPI application with RAG pipeline
- `knowledge_base/` — Seed documents (procurement, warehouse, fulfillment, QC, supplier)
- `evaluation/` — QA test suites (API tests, RAG eval, security, performance)
- `infra/` — Docker Compose, Nginx, GitHub Actions workflows
- `docs/` — Architecture docs, API spec, QA guide
- `discuss/` — Project discussion and planning documents

## Development
- Frontend dev: `cd frontend && npm run dev`
- Backend dev: `cd backend && uvicorn app.main:app --reload`
- Full stack: `cd infra && docker compose -f docker-compose.dev.yml up`
- Run backend tests: `cd backend && pytest tests/`
- Run evaluations: `cd evaluation && pytest test_suites/`

## Conventions
- Backend uses Python type hints and Pydantic models
- Frontend uses Vue 3 Composition API with `<script setup>`
- All API endpoints prefixed with `/api/`
- Evaluation datasets in JSON format under `evaluation/datasets/`
