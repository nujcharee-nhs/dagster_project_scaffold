# Use an official Python base image
FROM python:3.11-slim

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

# Copy quickstart project
COPY quickstart/ /app/

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -e ".[dev]"

# Expose Dagster web server port
EXPOSE 3000

# Default command to run Dagster web server
CMD ["dagster", "dev", "-f", "quickstart_workspace.py"]
