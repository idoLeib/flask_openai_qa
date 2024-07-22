from flask import Flask, request, jsonify
from app.config import Config


def create_app():
    app = Flask(__name__)

    @app.route('/ask', methods=['POST'])
    def ask():
        data = request.get_json()
        question = data['question']
        return jsonify({'question': question, 'answer': 'This is a placeholder answer'})

    return app
