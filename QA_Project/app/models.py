from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Question(db.Model):
    """
    This class defines the 'Question' model, which represents a table
    in the database with columns for question text and answer text.
    """
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String(200), nullable=False)
    answer_text = db.Column(db.String(200), nullable=False)


def init_app(app):
    """
    Initialize the application with the database setup.

    This function sets up the database with the provided Flask app
    and creates all tables defined in the models.

    :param app: The Flask application instance.
    """
    db.init_app(app)
    with app.app_context():
        db.create_all()
