from flask import jsonify
from flask import request
import pymysql
from flask import Blueprint
from flaskext.mysql import MySQL
from app import mysql

bp = Blueprint('project', __name__)

@bp.route('/all')
def getProjects():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM project")
        projectsRows = cursor.fetchall()
        respone = jsonify(projectsRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()  
