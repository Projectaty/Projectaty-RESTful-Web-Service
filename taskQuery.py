from __init__ import create_app
from flask import jsonify
from flask import request
import pymysql
from flask import Blueprint
from flaskext.mysql import MySQL

mysql = MySQL()

bp = Blueprint('task', __name__)

@bp.route('/all')
def getProjects():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM task")
        tasksRows = cursor.fetchall()
        respone = jsonify(tasksRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()  

# @appi.route('/add')
# def addProject():

# @appi.route('/delete')
# def deleteProject():

# @appi.route('/update')
# def updateProject():
