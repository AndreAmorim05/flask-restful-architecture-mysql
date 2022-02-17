from distutils import errors
import os
from flask import Flask
from src.models import db
from src.ext.api import api
from src.ext.login import login_manager
from src.routes.error_handler import errors

# loads the routes file
import src.routes

static_dir = os.path.abspath('src/static')
template_dir = os.path.abspath('src/templates')
root_path = os.path.dirname(os.path.dirname(__file__))


app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
app.config.from_object('config')



app.register_blueprint(errors)

db.init_app(app)
api.init_app(app)
login_manager.init_app(app)