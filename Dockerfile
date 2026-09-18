FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install flask google-genai
CMD ["python", "app.py"]