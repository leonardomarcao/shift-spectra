# Use the official Python runtime as the base image
FROM python:3.11.3

# Set labels
LABEL maintainer="chichi13"

# Set the working directory inside the container
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# Copy the entire backend directory to the working directory
COPY . /app

# Install system dependencies
RUN apt-get update -y && apt-get upgrade -y && rm -rf /var/lib/apt/lists/*

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements/dev.txt

# Expose port 8000
EXPOSE 8000