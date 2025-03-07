FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the application files to the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r app/requirements.txt

# Expose the Flask application's default port
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=app/main.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the application
CMD ["python", "-m", "flask", "run"]
