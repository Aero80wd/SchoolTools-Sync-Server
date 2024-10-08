from flask import Flask
def create_app():
    app = Flask(__name__)
    from .routes import database
    app.register_blueprint(database.bp)
    return app