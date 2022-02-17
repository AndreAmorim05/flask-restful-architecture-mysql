import os


# Grabs the folder  where the script runs.
BASEDIR = root_path = os.path.abspath(os.path.dirname(__file__))

class Config:
    """Base config"""
    SECRET_KEY = os.urandom(32) # Sets a secret key
    TEMPLATES_FOLDER = 'src/templates' # Sets templates folder dir
    STATIC_FOLDER = 'src/static' # Sets static folder dir
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{0}:{1}@{2}/{3}".format(
        os.environ['DB_USER'],
        os.environ['DB_PASS'],
        os.environ['DB_HOST'],
        os.environ['DB_NAME']
        ) # Connect to the MySQL database
    SQLALCHEMY_TRACK_MODIFICATIONS = False # Turn off the Flask-SQLAlchemy event system and warning

class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False

class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True