import os
import logging
import time
from flask import Flask, request
from google import genai

app = Flask(__name__)
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route("/")
def home():
    return {"status": "alive"}

@app.route("/healthz")
def healthz():
    return {"status": "healthy"}

@app.route("/summarize", methods=["POST"])
def summarize():
    start = time.time()
    text = request.json["text"]
    logger.info(f"Received summarize request, text length: {len(text)} chars")

    response = client.models.generate_content(
        model="gemini-3.6-flash",
         contents=f"Summarize in 2 sentences: {text}"
    )


    duration = round(time.time() - start, 2)
    logger.info(f"Request completed in {duration}s")

    return {"summary": response.text}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
