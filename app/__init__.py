from flask import Flask
from app.controllers.main_controller import main_bp
from app.extensions import db
from app.models.expense import Expense

def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "dev-secret-key"

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///expense_tracker.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(main_bp)

    return app