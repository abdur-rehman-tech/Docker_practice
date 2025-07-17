FROM python:3.11-slim

WORKDIR /app

COPY requirement.txt requirement.txt
RUN pip install --no-cache-dir -r requirement.txt
EXPOSE 8080
CMD ["python","python.py"]
