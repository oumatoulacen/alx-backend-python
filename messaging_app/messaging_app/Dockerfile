# Use a base Python image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container (adjust path)
COPY ../requirements.txt /app/requirements.txt

# Install dependencies from the requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY .. /app

# Expose the port your Django app runs on (default 8000)
EXPOSE 8000

# Set the entry point for the container to run the Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
