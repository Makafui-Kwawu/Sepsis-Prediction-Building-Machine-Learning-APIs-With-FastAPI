# Use the official Python image from the Docker Hub
FROM python:3.10.11

# Copy the requirements.txt file into the tmp directory
COPY requirements.txt /tmp/requirements.txt

# Upgrade pip and install requirements.txt
RUN python -m pip install --no-cache-dir --upgrade pip && \
    python -m pip install --no-cache-dir --upgrade --timeout 3000000 -r /tmp/requirements.txt

# Copy the entire project
COPY . /app

# Set up the working directory
WORKDIR /app

# Expose the port
EXPOSE 8501

# Run the application
CMD ["streamlit", "run", "main.py", "--server.port", "8501"]
