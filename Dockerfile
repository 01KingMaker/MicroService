    # building image
    FROM python:3.9-slim
    WORKDIR /app
        # Working directory
    COPY requirements.txt requirements.txt
    RUN pip install --no-cache-dir -r requirements.txt
    # Copy requirements file and install dependencies
    # Copy the rest of the project files
    COPY . .
    # Expose the server port
    EXPOSE 8000
    # Command to start the server
    CMD ["gunicorn", "--bind", "0.0.0.0:8000", "PythonMicroService.wsgi"]