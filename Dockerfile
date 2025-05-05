# Use official Python base image
FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Copy all project files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the app port
EXPOSE 8080

# Run the app
CMD ["python", "run.py"]
