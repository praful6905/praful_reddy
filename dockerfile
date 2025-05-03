# Use the official Python image from Docker Hub
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy your application code and dependency file
#COPY app.py requirements.txt ./
COPY . .
# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask will run on
EXPOSE 5000

# Set environment variable for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# Run the Flask app
CMD ["flask", "run"]
