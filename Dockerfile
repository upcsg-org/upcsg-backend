# Dockerfile
FROM python:3.12.0

# Install netcat (netcat-openbsd version)
RUN apt-get update && apt-get install -y netcat-openbsd

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project files
COPY . /app/