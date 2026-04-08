FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV API_BASE_URL=https://api.groq.com/openai/v1
ENV MODEL_NAME=llama-3.1-8b-instant

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
