from flask import Flask
from views import views
from flask_cors import CORS

def create_app() -> Flask:
    try:
        app = Flask(__name__)
        CORS(app, origihs=["http://localhost:3001"])
        app.config['SECRET_KEY'] = 'SACRED_KEY'
        app.register_blueprint(views, url_prefix='/')
        return app
    except Exception as e:
        print(e)
