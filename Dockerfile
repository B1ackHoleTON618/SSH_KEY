FROM python:3
WORKDIR /app
COPY Triangle.py /app/Triangle.py
CMD ["python", "/app/Triangle.py"]