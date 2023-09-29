from flask import Flask
from .views import views


def create_app():
    app = Flask(__name__, template_folder="website/templates", static_folder="website/static")
    app.config["SECRET_KEY"] = "mysecretkey"

    app.register_blueprint(views)

    return app
