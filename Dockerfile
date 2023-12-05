# build the ommage
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt requirements.txt
# install all the requirements
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "PythonMicroService.wsgi"]