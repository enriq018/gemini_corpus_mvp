# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies (e.g., Git, GCC)
RUN apt-get update && apt-get install -y --no-install-recommends \
  git \
  gcc \
  python3-dev \
  build-essential \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Copy only the requirements file into the container
COPY requirements.txt requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# List installed packages for debugging
RUN pip list > packages.txt

# Copy the rest of the application code into the container
COPY . .

# Copy the .env file into the container
COPY .env .env

# Ensure the credentials directory exists and copy the service account key
RUN mkdir -p /app/semantic_retrieval/credentials
COPY semantic_retrieval/credentials/geminiapideveloper-1623bba633a0.json /app/semantic_retrieval/credentials/geminiapideveloper-1623bba633a0.json

# Install gunicorn
RUN pip install --no-cache-dir gunicorn

# Expose the port the app runs on
EXPOSE 8080

# Set environment variables
ENV PORT=8080

# Run the application with gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "2", "server.app:app"]
