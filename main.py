# app.py
from flask import Flask, request, jsonify
from main import load_user_data, gradientBoostingClassifier  # Import functions from main.py

app = Flask(__name__)

# Endpoint for predictions
@app.route('/get/', methods=['GET'])
def respond():
    user_input_text = request.args.get("data", None)
    if user_input_text:
        user_data = load_user_data('data.json')
        predicted_class, predicted_provider = gradientBoostingClassifier(user_data, user_input_text)
        response = {
            "predicted_class": predicted_class,
            "predicted_provider": predicted_provider
        }
    else:
        response = {"error": "No data provided"}

    return jsonify(response)


# Default index endpoint
@app.route('/')
def index():
    return "Welcome to the ---BACKEND---"

if __name__ == '__main__':
    app.run(threaded=True, port=5000)
