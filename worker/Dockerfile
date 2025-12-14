FROM xserrat/facebook-demucs:latest

# Install debug tools, make, and Python dependencies
RUN apt-get update && \
    apt-get install -y iputils-ping netcat redis-tools curl dnsutils make && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy your worker script
COPY worker-server.py .

# Install Python dependencies needed by the worker
RUN pip install --no-cache-dir redis minio requests python-dotenv

# Keep container alive and run the worker
CMD ["python3", "worker-server.py"]
    