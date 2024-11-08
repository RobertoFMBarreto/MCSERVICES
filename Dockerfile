FROM python:3.13-slim-bookworm
Run apt-get update -y && apt-get install -y python3-pip
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]