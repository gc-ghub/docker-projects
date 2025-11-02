# ================================
# Stage 1: Build Environment
# ================================
FROM python:3.12-slim AS builder

# Set working directory
WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends gcc

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --user -r requirements.txt

# ================================
# Stage 2: Production Image
# ================================
FROM python:3.12-slim

WORKDIR /app

# Copy only necessary runtime files from builder
COPY --from=builder /root/.local /root/.local
COPY . .

# Update PATH for pip --user installs
ENV PATH=/root/.local/bin:$PATH

# Django environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Expose port 9000
EXPOSE 9000

# Run Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:9000"]

