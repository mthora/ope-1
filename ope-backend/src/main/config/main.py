from flask import Flask, request
from flask_restx import Api
from flask_cors import CORS
from src.main.routes import user_namespace, drink_namespace
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_host=1, x_port=1)
CORS(app)


@app.before_request
def log_request():
    app.logger.debug("Request Headers %s", request.headers)
    return None

api = Api(
    title="Talos RMS",
    version='1.0',
    description="Restaurant Management System"
)

api.add_namespace(user_namespace, path='/users')
api.add_namespace(drink_namespace, path='/drinks')