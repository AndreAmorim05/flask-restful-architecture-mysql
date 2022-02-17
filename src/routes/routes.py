from src.ext.api import api as API
from src.controllers import *


API.add_resource(Home, '/', endpoint='home')