# QA Guide

## Environment Setup

### Prerequisites
- Python 3.10+
- Node.js 20+
- Docker Desktop
- Git

### Quick Start

```bash
# Clone the repo
git clone git@github.com:jyhg/organizational-knowledge-repository.git
cd organizational-knowledge-repository

# Backend
cd backend
python -m venv .venv
source .venv/bin/activate
pip install ".[dev]"
cp app/.env.example app/.env  # Edit with your API keys
uvicorn app.main:app --reload

# Frontend (new terminal)
cd frontend
npm install
npm run dev

# Full stack with Docker
cd infra
docker compose -f docker-compose.dev.yml up
```

## Running Tests

### Backend Unit Tests
```bash
cd backend
pytest tests/ -v
```

### API Tests (Evaluation)
```bash
cd evaluation
pytest test_suites/api_tests/ -v
```

### RAG Evaluation (Week 2+)
```bash
cd evaluation
pytest test_suites/rag_eval/ -v
```

### Security Tests (Week 3+)
```bash
cd evaluation
pytest test_suites/security_tests/ -v
```

### Performance Tests
```bash
cd evaluation/test_suites/performance
locust -f locustfile.py --host=http://localhost:8000
```

### Frontend E2E Tests
```bash
cd frontend
npx cypress open    # Interactive mode
npx cypress run     # Headless mode
```

## Evaluation Datasets

- `evaluation/datasets/golden_qa.json` — Standard Q&A pairs for accuracy testing
- `evaluation/datasets/adversarial.json` — Adversarial inputs for security testing

## Weekly Focus

| Week | Test Focus | Key Tools |
|------|-----------|-----------|
| Week 1 | API tests, Prompt regression | Pytest, httpx |
| Week 2 | RAG metrics evaluation | DeepEval, RAGAS |
| Week 3 | E2E tests, Security testing | Cypress, Pytest |
| Week 4 | CI integration, Performance | GitHub Actions, Locust |
