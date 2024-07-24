from flask import Flask, request, jsonify
from app.config import Config
from app.models import db, Question, init_app as init_db
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
    init_db(app)
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
        #get answer
        answer = response.choices[0].message.content.strip()

        #save question and answer in DB
        db_question = Question(question_text=question, answer_text=answer)
        db.session.add(db_question)
        db.session.commit()

        return jsonify({'question': question, 'answer': answer})

    return app
