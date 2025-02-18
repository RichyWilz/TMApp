# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Expose the port the app will run on
EXPOSE 8000

# Run migrations (optional, but recommended)
RUN python manage.py migrate

# Set environment variable to let Django know it's running in production mode
# ENV DJANGO_SETTINGS_MODULE=TMApp.settings.production

# Start the Django development server (for development; use production server in real deployments)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
