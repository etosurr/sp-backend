from flask import Flask
from config import Config
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_login import LoginManager


app = Flask(__name__)
CORS(app)
app.config.from_object(Config)
jwt = JWTManager(app)
login = LoginManager(app)
login.login_view = 'login'

import routes
from database import db




@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'app': app}


if __name__ == '__main__':
    app.run()
