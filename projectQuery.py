from app import app
from flask import jsonify
from flask import request
from config import mysql
import pymysql

class ProjectQuery:
    @app.route('/projects')
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
