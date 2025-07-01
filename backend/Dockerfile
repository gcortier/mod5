FROM python:3.11-slim
WORKDIR /app
COPY main.py ./
COPY modules ./modules
COPY tests ./tests
RUN pip install fastapi uvicorn loguru pydantic pytest
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
