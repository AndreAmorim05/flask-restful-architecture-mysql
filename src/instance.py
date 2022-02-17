from flask import Flask
from src.models import db
from src.ext.api import api
from src.ext.login import login_manager
from src.routes.error_handler import errors

# loads the routes file (recommended not remove this)
import src.routes

# instantiate a Flask object and apply configurations on it 
# available configs ['config.DevConfig' or 'config.ProdConfig']
app = Flask(__name__)
app.config.from_object('config.DevConfig')

# register all blueprints
app.register_blueprint(errors)

# init all extensions
db.init_app(app)
api.init_app(app)
login_manager.init_app(app)