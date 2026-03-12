# Project Dan Maje Backend

Production-ready FastAPI backend starter for **Project Dan Maje** by **Astrovia Systems**.

## Included
- FastAPI API server
- Gunicorn production server
- JWT auth
- PostgreSQL-ready SQLAlchemy models
- Render deployment config
- Health route and Swagger docs

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

## Run in production style

```bash
gunicorn -k uvicorn.workers.UvicornWorker app.main:app --bind 0.0.0.0:10000
```

## Render settings
- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn -k uvicorn.workers.UvicornWorker app.main:app --bind 0.0.0.0:$PORT`

## Endpoints
- `/health`
- `/docs`
- `/api/auth/register`
- `/api/auth/login`
- `/api/wallet/balance`
- `/api/services/airtime`
- `/api/services/data`
- `/api/transactions`
