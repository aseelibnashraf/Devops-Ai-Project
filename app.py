import os
from flask import Flask, request
from google import genai

app = Flask(__name__)
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

@app.route("/")
def home():
    return {"status": "alive"}

@app.route("/summarize", methods=["POST"])
def summarize():
    text = request.json["text"]
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=f"Summarize in 2 sentences: {text}"
    )
    return {"summary": response.text}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
