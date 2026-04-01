# API Specification

Backend auto-generates OpenAPI documentation at `http://localhost:8000/docs` (Swagger UI).

## Base URL

```
Development: http://localhost:8000/api
Production:  https://your-domain.com/api
```

## Authentication

All endpoints except `/health` and `/api/auth/login` require a Bearer token.

```
Authorization: Bearer <access_token>
```

## Chat API

### POST /api/chat

Send a question to the knowledge base.

**Request:**
```json
{
  "message": "供应商准入的注册资本要求是多少？",
  "conversation_id": "optional-session-id"
}
```

**Response (200):**
```json
{
  "answer": "根据供应商准入标准，注册资本不低于人民币500万元。",
  "sources": ["supplier-admission-standards.md"],
  "conversation_id": "session-abc123"
}
```

## Documents API

### GET /api/docs

List all knowledge base documents.

### POST /api/docs/upload

Upload a document (multipart/form-data).

| Field | Type | Required |
|-------|------|----------|
| file | File | Yes |
| category | string | No (default: "general") |

### DELETE /api/docs/{doc_id}

Remove a document from the knowledge base.

## Evaluation API

### GET /api/eval/metrics

Get the latest RAG evaluation metrics.

**Response:**
```json
{
  "faithfulness": 0.87,
  "answer_relevancy": 0.82,
  "context_precision": 0.79,
  "context_recall": 0.85
}
```

### POST /api/eval/trigger

Trigger a new evaluation run. Returns immediately with a run ID.
