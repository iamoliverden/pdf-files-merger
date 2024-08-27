#!/bin/bash

# Wait for the database to be ready
while ! nc -z db 5432; do
  echo "Waiting for the database..."
  sleep 1
done

# Run migrations
python manage.py makemigrations
python manage.py migrate --no-input

# Collect static files
python manage.py collectstatic --no-input

# Run the server
exec "$@"
