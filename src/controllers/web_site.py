from flask import render_template, make_response, request, redirect, flash, url_for, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from flask_restful import Resource, reqparse
from src.models.models import *

__all__ = ['Home', ]

class Home(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('home.html'), 200, headers)
    
    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass