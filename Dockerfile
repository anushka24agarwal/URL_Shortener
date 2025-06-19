# Use official Python base image
FROM python:3.11

# Set working directory
WORKDIR /app

# Copy files
COPY ./app /app/app
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port and run server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]