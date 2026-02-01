# Stage 1: Builder - Export requirements
FROM python:3.12-slim AS builder

WORKDIR /app

# Install Poetry and export plugin
RUN pip install --no-cache-dir poetry poetry-plugin-export

# Copy dependency files
COPY pyproject.toml poetry.lock* ./

# Export to requirements.txt (without dev dependencies)
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes --without dev


# Stage 2: Final - Minimal runtime image
FROM python:3.12-slim

WORKDIR /app

# Install only essential runtime dependencies
# - poppler-utils: for PDF text extraction with pdfminer
# - libmagic1: for file type detection
# Removed: tesseract-ocr, libgl1, libglib2.0-0 (not needed without unstructured ML)
RUN apt-get update && apt-get install -y --no-install-recommends \
    poppler-utils \
    libmagic1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && rm -rf /root/.cache

# Copy requirements from builder
COPY --from=builder /app/requirements.txt .

# Install Python dependencies with optimizations
RUN pip install --no-cache-dir --compile -r requirements.txt \
    && rm -rf /root/.cache/pip \
    && find /usr/local/lib/python3.12 -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true \
    && find /usr/local/lib/python3.12 -type d -name "tests" -exec rm -rf {} + 2>/dev/null || true \
    && find /usr/local/lib/python3.12 -type d -name "test" -exec rm -rf {} + 2>/dev/null || true \
    && find /usr/local/lib/python3.12 -type f -name "*.pyc" -delete 2>/dev/null || true \
    && find /usr/local/lib/python3.12 -type f -name "*.pyo" -delete 2>/dev/null || true

# Copy application code
COPY . .

# Make start script executable
RUN chmod +x start.sh

# Expose port and run both API + Celery worker
EXPOSE 8000
CMD ["./start.sh"]