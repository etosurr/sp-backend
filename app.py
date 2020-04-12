from flask import Flask
from config import Config
from flask_cors import CORS
from flask_jwt_extended import JWTManager


app = Flask(__name__)
app.config.from_object(Config)
app.config.from_object(Config)
jwt = JWTManager(app)

import routes

CORS(app)


if __name__ == '__main__':
    app.run()
