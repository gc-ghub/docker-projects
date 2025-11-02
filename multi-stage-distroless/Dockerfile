# ================================
# Stage 1: Builder
# ================================
FROM python:3.12-slim AS builder

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends gcc

COPY requirements.txt .

# ✅ install globally, not as --user
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

# ================================
# Stage 2: Distroless runtime
# ================================
FROM gcr.io/distroless/python3-debian12

WORKDIR /app

# Copy site-packages and binaries from builder
COPY --from=builder /usr/local /usr/local
COPY --from=builder /app /app

# Expose port
EXPOSE 8080

# Start Gunicorn
CMD ["/usr/local/bin/gunicorn", "--bind", "0.0.0.0:8080", "stark_industries.wsgi:application"]

