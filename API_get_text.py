from flask import Flask, request, jsonify, render_template
import json
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Load API key and model from environment
API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")

openai.api_key = API_KEY

# Function to call OpenAI API
def get_openai_response(user_input, temperature=0.7, max_tokens=300):
    try:
        response = openai.ChatCompletion.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": "You are an eLearning assistant. Based on the user's input, generate a JSON response containing two parts: 1) a 'tags' array containing relevant topic tags and 2) a 'path' string which outlines a structured learning path. The 'tags' array should include topics separated by commas, and the 'path' string should provide a step-by-step plan for learning."
                },
                {"role": "user", "content": user_input}
            ],
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.choices[0].message['content']

    except openai.error.OpenAIError as e:
        print("OpenAI Error:", str(e))
        return None

# Route for homepage
@app.route("/")
def index():
    return render_template("index.html")

# Route for generating content
@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    user_input = data.get("prompt")

    response_text = get_openai_response(user_input)
    tags = []
    path = ""

    if response_text:
        try:
            # Parse the response as a structured JSON format
            response_data = json.loads(response_text)
            tags = response_data.get("tags", [])
            path = response_data.get("path", "")
        except Exception as e:
            print("Parse Error:", str(e))
            path = response_text

    return jsonify({"tags": tags, "path": path})

# Run app
if __name__ == "__main__":
    print("App running. Access via http://127.0.0.1:5000/")
    app.run(debug=os.getenv("FLASK_DEBUG") == "1")