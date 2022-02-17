from src.models import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from src.ext.login import login_manager

@login_manager.user_loader
def get_user(user_id):
    return User.query.filter_by(id=user_id).first()

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(84), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    permission = db.Column(db.Integer, nullable=False)

    def __init__(self, name, email, password, permission):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)
        self.permission = permission
    
    def verify_password(self, pwd):
        return check_password_hash(self.password, pwd)
