# Use the official Python image from the Docker Hub
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the prometheus_client package
RUN pip install prometheus_client

# Run hello_world.py when the container launches
CMD ["python", "hello_world.py"]
