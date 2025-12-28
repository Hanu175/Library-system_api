from flask import Flask
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from extensions import db

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = SQLALCHEMY_TRACK_MODIFICATIONS

    db.init_app(app)

    from routes.book_routes import book_bp
    app.register_blueprint(book_bp, url_prefix="/api/books/")

    with app.app_context():
        db.create_all()

    return app


def home():
    return "Server is running"


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
    
    
    
