# Stage 1: Build & dependency isolation
FROM python:3.12-slim-bookworm AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir --prefix=/install -r requirements.txt

# Stage 2: Minimal hardened runtime
FROM python:3.12-slim-bookworm

WORKDIR /app

# Import clean dependencies from builder
COPY --from=builder /install /usr/local

# Remove outdated Debian packages flagged by Trivy
RUN rm -rf /usr/lib/python3/dist-packages/*

# Run as non-root user
RUN adduser --system --uid 1001 --no-create-home appuser

COPY --chown=appuser:appuser . .

USER appuser

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]