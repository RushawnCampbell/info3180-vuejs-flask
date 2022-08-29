from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from .config import Config

app = Flask(__name__, static_folder='../dist/assets')
app.config.from_object(Config)
csrf = CSRFProtect(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'signin'

from flask_migrate import Migrate
migrate =  Migrate(app,db)
from app import views