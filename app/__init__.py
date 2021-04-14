
from flask import Flask
from flask_redis import FlaskRedis
from config.conf import Config

def create_app(config_class=Config):
    app = Flask(__name__,
                template_folder='templates',
                static_folder='static',
                static_url_path='/backend-static')
    app.config.from_object(config_class)
    redis_client = FlaskRedis(app)
    return app
