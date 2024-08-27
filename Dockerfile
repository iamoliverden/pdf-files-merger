# Dockerfile

# Use the official Python image from the Docker Hub
FROM python:3.8.12-slim

# ENV Variable
ENV PDF_FILES_MERGER=/app

# Create the work directory
RUN mkdir -p $PDF_FILES_MERGER

# Upgrade pip
RUN pip install --upgrade pip

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR $PDF_FILES_MERGER

# Install dependencies
COPY requirements.txt .
RUN python -m venv venv
RUN pip install -r requirements.txt

# Copy project
COPY . .

# Copy entry point and ensure it is executable
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Set entry point
ENTRYPOINT ["sh", "/entrypoint.sh"]

# CMD line for Gunicorn
CMD ["gunicorn", "pdf_files_merger.wsgi:application", "--bind", "0.0.0.0:8000"]
