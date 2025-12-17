# Lightweight Python image
FROM python:3.12-slim

# Workdir
WORKDIR /app

# Copy dependency list first (better caching)
COPY requirements.txt .

# Install Python dependencies (use python -m pip to avoid PATH issues)
RUN python -m pip install --upgrade pip \
    && python -m pip install -r requirements.txt

# Copy application code
COPY . .

# Expose app port
EXPOSE 8000

# Start FastAPI via uvicorn (module:object)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port","8000"]
