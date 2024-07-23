from flask import Flask, request, jsonify
from app.config import Config
import openai


def create_app():
    """
    Create and configure the Flask application.

    This function initializes the Flask application, loads the configuration,
    and sets the OpenAI API key. It also defines the route for the /ask endpoint.

    :return:
        Flask app instance.
    """
    app = Flask(__name__)
    app.config.from_object(Config)

    # Set your OpenAI API key from the configuration
    openai.api_key = app.config['OPENAI_API_KEY']

    @app.route('/ask', methods=['POST'])
    def ask():
        """
        Handle POST requests to the /ask endpoint.

        This function receives a JSON payload with a question, generates a response
        using the OpenAI API, and returns the question and answer as a JSON response.

        :return:
            JSON response containing the question and the generated answer.
        """
        data = request.get_json()
        question = data['question']

        # Generate a response using the new OpenAI API
        response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "user",
                        "content": question,
                    },
                ],
            )
        print(response.choices[0].message.content)
        answer = response.choices[0].message.content.strip()

        return jsonify({'question': question, 'answer': answer})

    return app
