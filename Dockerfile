# ---------- Build stage ----------
FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt


# ---------- Runtime stage ----------
FROM python:3.11-slim

WORKDIR /app

# Create non-root user for security
RUN useradd -m appuser

# Copy installed dependencies from builder
COPY --from=builder /root/.local /home/appuser/.local

# Copy application code
COPY app/ ./app/

ENV PATH=/home/appuser/.local/bin:$PATH
ENV APP_VERSION=1.0.0
ENV PYTHONUNBUFFERED=1

# Run as non-root
USER appuser

EXPOSE 5000

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/health')" || exit 1

CMD ["python", "-m", "flask", "--app", "app.main", "run", "--host=0.0.0.0", "--port=5000"]