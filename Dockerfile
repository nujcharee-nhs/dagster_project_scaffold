# Use official uv image
FROM ghcr.io/astral-sh/uv:0.7.12 AS uv

# Use an official Python base image
FROM python:3.12-slim

# Set environment variables
ENV DAGSTER_HOME=/opt/dagster_home \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Create dagster home directory
RUN mkdir -p $DAGSTER_HOME

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN --mount=from=uv,source=/uv,target=/bin/uv \
    --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv export --frozen --no-emit-workspace --no-dev --no-editable -o requirements.txt && \
    uv pip install -r requirements.txt --target /app/

# Copy quickstart project
COPY quickstart/ /app/quickstart/

# Expose Dagster web server port
EXPOSE 3000

# Default command to run Dagster web server
CMD ["dagster", "dev", "-f", "quickstart/assets/s3.py"]
