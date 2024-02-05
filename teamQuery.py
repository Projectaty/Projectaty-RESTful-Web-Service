from app import app
from flask import jsonify
from flask import request
from config import mysql
import pymysql

class TeamQuery:
    @app.route('/teams')
    def getProjects():
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
