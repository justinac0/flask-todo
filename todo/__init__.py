import os
from flask import Flask

from . import models


def create_app(config=None):
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.sqlite3"
    app.config["SECRET_KEY"] = "dev"

    from . import models
    
    models.db.init_app(app)

    with app.app_context():
        models.db.create_all()

    from . import views

    app.register_blueprint(views.todo)

    return app
