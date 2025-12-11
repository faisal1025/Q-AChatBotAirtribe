from bot.chat import user_query
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Q&A ChatBot API!"

@app.route('/query', methods=['POST'])
def query():
    data = request.json
    prompt = data.get('prompt', '')
    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    response = user_query(prompt)
    json_response = jsonify({"response": response})
    print(f"json response: \n{json_response.get_json()}")
    return json_response


