import flask.app
from flask import Flask
from views import views
from views import views
from flask cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000","http://localhost:3001"])

def create_app()-> flask.app.Flask:
    try:
        app = Flask(__name__)
        app.config['SECRET_KEY'] = 'SACRED_KEY'
        app.register_blueprint(views,url_prefix='/')
        return app
    except Exception as e:
        print(e)
