from flask import jsonify
from flask import request
import pymysql
from flask import Blueprint
from app import mysql

bp = Blueprint('team', __name__)

@bp.route('/all')
def getTeams():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM team")
        teamsRows = cursor.fetchall()
        respone = jsonify(teamsRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()  