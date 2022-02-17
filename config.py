import os

# Grabs the folder  where the script runs.
BASEDIR = root_path = os.path.abspath(os.path.dirname(__file__))
# Enable development mode
DEVELOPMENT = True
# Enable debug mode
DEBUG = True
# Sets a secret key
SECRET_KEY = os.urandom(32)
# Connect to the MySQL database
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{0}:{1}@{2}/{3}".format(
    os.environ['DB_USER'],
    os.environ['DB_PASS'],
    os.environ['DB_HOST'],
    os.environ['DB_NAME']
    )
# Turn off the Flask-SQLAlchemy event system and warning
SQLALCHEMY_TRACK_MODIFICATIONS = False