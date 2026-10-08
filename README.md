# Production RAG Knowledge Assistant

Production-style Retrieval-Augmented Generation platform using Python 3.12, FastAPI, PostgreSQL + pgvector, Redis, JWT, Docker and GitHub Actions.

## Architecture
Client -> FastAPI -> PostgreSQL/pgvector -> retrieval -> LLM -> answer + citations
                         \-> Redis

## RAG pipeline
Document -> normalize -> chunk -> embedding -> pgvector -> similarity search -> top-K context -> LLM -> grounded answer + citations

## Features
- JWT registration/login and bcrypt password hashing
- Document ingestion and chunking
- Vector embeddings and pgvector similarity search
- RAG chat endpoint with citations
- Conversation persistence
- Redis-ready infrastructure
- Prometheus metrics
- Docker Compose
- GitHub Actions: Ruff, MyPy, Pytest, Docker build, pip-audit
- Provider-independent AI boundary; default mock provider needs no API key

## Run
```bash
cp .env.example .env
docker compose up --build
```
Windows:
```powershell
copy .env.example .env
docker compose up --build
```
Open http://localhost:8000/docs

## Main APIs
POST /api/v1/auth/register
POST /api/v1/auth/login
POST /api/v1/documents
POST /api/v1/chat
GET /api/v1/health
GET /metrics

## Example
Register/login, click Authorize in Swagger, create a document, then:
```json
{"question":"What does this document say?","top_k":5}
```

## Real LLM
Set AI_PROVIDER and provider credentials in `.env`. The adapter boundary is in `app/ai/providers.py`.

## Production roadmap
Add Alembic, Celery/Dramatiq, Kafka, S3, PDF/OCR extraction, hybrid BM25 + vector search, reranking, pgvector indexes, multi-tenancy, RBAC, rate limiting, OpenTelemetry, Prometheus/Grafana, Kubernetes, Helm, Terraform, secret manager and RAG evaluation.

## GitHub description
Production RAG Knowledge Assistant using Python, FastAPI, PostgreSQL, pgvector, Redis, JWT, Docker and GitHub Actions.

Topics: python fastapi rag generative-ai llm embeddings pgvector postgresql redis docker github-actions jwt ai
