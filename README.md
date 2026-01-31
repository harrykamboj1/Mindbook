# Mindbook Backend API

A powerful FastAPI-based backend for **Mindbook** an intelligent document management and RAG (Retrieval-Augmented Generation) system that enables smart interactions with your documents.

---

## Features

- Authentication — Clerk-based user authentication and authorization
- Project Management — Create, manage, and organize document projects
- Document Processing — Ingest and process multiple document types (PDFs, web pages, etc.)
- AI-Powered Chat — Chat with your documents using advanced RAG techniques
- Intelligent Retrieval — Context-aware document search and retrieval
- Async Processing — Background task processing with Celery and Redis
- Cloud Storage — Cloudflare R2 integration for file storage

---

##  Architecture

```
backend/
├── src/
│   ├── agents/                 # AI Agent implementations
│   │   ├── simple_agent/       # Basic agent for straightforward queries
│   │   └── supervisor_agent/   # Advanced multi-agent supervisor
│   ├── config/                 # Application configuration
│   ├── middleware/             # Custom middleware (logging, auth)
│   ├── models/                 # Data models and schemas
│   ├── rag/                    # RAG system components
│   │   ├── ingestion/          # Document ingestion pipeline
│   │   └── retrieval/          # Document retrieval logic
│   ├── routes/                 # API route handlers
│   │   ├── chatRoutes.py       # Chat endpoints
│   │   ├── projectRoutes.py    # Project management endpoints
│   │   ├── projectFilesRoutes.py # File management endpoints
│   │   └── userRoutes.py       # User endpoints
│   ├── services/               # External service integrations
│   │   ├── celery.py           # Celery task queue
│   │   ├── clerkAuth.py        # Clerk authentication
│   │   ├── cloudflareR2.py     # Cloudflare R2 storage
│   │   ├── llm.py              # LLM configuration
│   │   ├── supabase.py         # Supabase client
│   │   └── webScrapper.py      # Web scraping utilities
│   ├── utils/                  # Utility functions
│   └── server.py               # FastAPI application entry point
├── supabase/                   # Supabase configuration & migrations
├── docker-compose.yml          # Docker services configuration
├── Dockerfile                  # API container definition
├── Makefile                    # Development shortcuts
└── pyproject.toml              # Python dependencies (Poetry)
```

### System Design Diagrams

> Architecture diagrams


#### High-Level Design
<img width="1074" height="461" alt="hld" src="https://github.com/user-attachments/assets/99fe3c04-78b2-4651-9b75-7f805046679a" />

#### RAG Pipeline Architecture
<img width="1278" height="258" alt="Rag_pipeline_architecture" src="https://github.com/user-attachments/assets/db865def-16da-4a0a-aa5b-051d6f9dad96" />

#### RAG Agent Flow
<img width="1072" height="718" alt="rag_agent" src="https://github.com/user-attachments/assets/110bc92c-c005-4f76-b9d3-81e6a5c19d4c" />

#### Retrieval Pipeline
<img width="1188" height="416" alt="retreival_pipeline" src="https://github.com/user-attachments/assets/d1c6b6a3-2f9d-44d2-8a40-c7020350a1bb" />


#### Database Schema
<img width="841" height="752" alt="database_schema" src="https://github.com/user-attachments/assets/7257f96e-c56f-4ef4-bfaa-7962e39d0dbd" />


#### Server Dependency Architecture
<img width="963" height="711" alt="Screenshot 2026-01-29 at 11 51 44 PM" src="https://github.com/user-attachments/assets/2c0cd566-c95e-46cf-8884-711628621490" />




## Quick Start

### Prerequisites

- **Python** 3.10 – 3.13
- **Docker** & **Docker Compose**
- **Poetry** (for dependency management)
- **Supabase CLI** (for local database)

### 1. Clone & Navigate

```bash
cd backend
```

### 2. Environment Setup

Copy the sample environment file and configure your credentials:

```bash
cp .env.sample .env
```

Fill in the required environment variables:

| Variable | Description |
|----------|-------------|
| `SUPABASE_API_URL` | Local Supabase API URL (e.g., `http://localhost:54321`) |
| `SUPABASE_SECRET_KEY` | Supabase service role key |
| `CLERK_SECRET_KEY` | Clerk authentication secret |
| `AWS_ACCESS_KEY_ID` | Cloudflare R2 Access Key ID |
| `AWS_SECRET_ACCESS_KEY` | Cloudflare R2 Secret Access Key |
| `R2_BUCKET_NAME` | Cloudflare R2 bucket for file storage |
| `REDIS_URL` | Redis connection URL |
| `OPENAI_API_KEY` | OpenAI API key for LLM |
| `TAVILY_API_KEY` | Tavily API for web search |
| `LANGSMITH_API_KEY` | LangSmith for tracing (optional) |

### 3. Start Services

Using the **Makefile** (recommended):

```bash
# Start all services (Supabase, Redis, API, Celery Worker)
make start

# View logs
make logs-api     # API server logs
make logs-worker  # Celery worker logs
make logs-redis   # Redis logs

# Stop all services
make stop

# Clean everything (removes containers, images, volumes)
make clean
```

Or using **Docker Compose** directly:

```bash
docker-compose up -d
```

### 4. Access the API

- **API Server**: [http://localhost:8000](http://localhost:8000)
- **Swagger Docs**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)
- **Health Check**: [http://localhost:8000/health](http://localhost:8000/health)

---

##  API Endpoints

### Health
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/health` | Check API health status |

### User Management
| Method | Endpoint | Description |
|--------|----------|-------------|
| `*` | `/api/user/*` | User-related operations |

### Projects
| Method | Endpoint | Description |
|--------|----------|-------------|
| `*` | `/api/projects/*` | Project CRUD operations |

### Project Files
| Method | Endpoint | Description |
|--------|----------|-------------|
| `*` | `/api/projects/*` | File upload, processing, management |

### Chat
| Method | Endpoint | Description |
|--------|----------|-------------|
| `*` | `/api/chats/*` | AI-powered document chat |

> 📖 For detailed API documentation, visit the Swagger UI at `/docs` after starting the server.

---

##  Development

### Local Development (without Docker)

```bash
# Install dependencies
poetry install

# Start Supabase locally
npx supabase start

# Start Redis (if not using Docker)
redis-server

# Run the development server
uvicorn src.server:app --reload --host 0.0.0.0 --port 8000

# In another terminal, start Celery worker
celery -A src.services.celery:app worker --loglevel=info --pool=threads
```

### Running Tests

```bash
poetry run pytest
```

---

## Docker Services

The `docker-compose.yml` defines three services:

| Service | Container | Port | Description |
|---------|-----------|------|-------------|
| `redis` | redis | 6379 | Message broker for Celery |
| `api` | server | 8000 | FastAPI application |
| `worker` | celery-worker | — | Background task processor |

---

## Key Dependencies

| Package | Purpose |
|---------|---------|
| **FastAPI** | Web framework for building APIs |
| **Uvicorn** | ASGI server |
| **LangChain** | LLM orchestration and RAG |
| **LangChain OpenAI** | OpenAI integration |
| **Celery** | Distributed task queue |
| **Redis** | Message broker & caching |
| **Supabase** | Database and authentication |
| **Unstructured** | Document parsing and processing |
| **Boto3** | Cloudflare R2 integration |
| **Clerk** | User authentication |
| **Structlog** | Structured logging |
| **RAGAS** | RAG evaluation framework |

---

##  Configuration

### Logging

The application uses **structlog** for structured logging. Logs are stored in the `logs/` directory and output to stdout for container environments.

### Database

Supabase is used as the primary database. Migrations are stored in `supabase/migrations/`.

To apply migrations:

```bash
npx supabase db push
```

## 👤 Author

**harrykamboj1** — [singhharnoor116@gmail.com](mailto:singhharnoor116@gmail.com)
