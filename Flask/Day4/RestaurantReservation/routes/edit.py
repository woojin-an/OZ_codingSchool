from flask import jsonify, request
from flask.views import MethodView
from flask_smorest import Blueprint
from flask.views import MethodView
from models import Reservation
from db import db

reserve_edit_blp = Blueprint('Reservations Edit',
                             'reservations Edit',
                             description='Edits on reservations',
                             url_prefix='/')

