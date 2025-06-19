# Use an official Python image
FROM python:3.13.4

# Set working directory
WORKDIR /app

# Copy files
COPY app.py /app/
COPY requirements.txt /app/
# Install dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expose the port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]