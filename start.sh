#!/bin/bash

# Start Celery worker in background
echo "Starting Celery worker..."
celery -A src.services.celery:app worker --loglevel=info --pool=threads &
CELERY_PID=$!

# Give Celery a moment to start
sleep 3

# Start Uvicorn (FastAPI) in foreground
echo "Starting FastAPI server..."
uvicorn src.server:app --host 0.0.0.0 --port ${PORT:-8000}

# If Uvicorn exits, kill Celery
kill $CELERY_PID 2>/dev/null
