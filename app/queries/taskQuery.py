from flask import jsonify
from flask import request
from flask import Blueprint
from app.queries.mysqlconnect import execute_query

bp = Blueprint('task', __name__)