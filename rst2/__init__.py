from flask import Flask
from flask.ext.bootstrap import Bootstrap
from rst2.frontend import frontend as frontend_blueprint

bootstrap = Bootstrap()

def create_app():
    app = Flask(__name__)
    bootstrap.init_app(app)
    app.register_blueprint(frontend_blueprint)

    return app

