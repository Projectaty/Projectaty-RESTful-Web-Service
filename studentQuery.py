from app import app
from flask import jsonify
from flask import request
from config import mysql
import pymysql

class StudentQuery:
   @app.route('/studentsI', methods=['POST'])
   def addStudent():
        try:
            data = request.json
            name = data['name']
            email = data['email']
            profile_pic = data['profile_pic']
            password = data['password']
    
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
         
            cursor.execute("INSERT INTO student (name, email, profile_pic, password) VALUES (%s, %s, %s, %s)",
                           (name, email, profile_pic, password))
            
           
            conn.commit()
            cursor.close()
            conn.close()
            response = jsonify({'message': 'Student information inserted successfully'})
            response.status_code = 200
            return response
        except Exception as e:
            print(e)
            response = jsonify({'error': 'An error occurred while inserting student information'})
            response.status_code = 500
            return response
        
@app.route('/students/<int:student_id>', methods=['DELETE'])
def deleteStudent(student_id):
        try:
           
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("DELETE FROM student WHERE student_id = %s", (student_id,))
            
            conn.commit()
            cursor.close()
            conn.close()
            response = jsonify({'message': 'Student account deleted successfully'})
            response.status_code = 200
            return response
        except Exception as e:
            print(e)
            response = jsonify({'error': 'An error occurred while deleting student account'})
            response.status_code = 500
            return response
        
@app.route('/studentsU', methods=['PUT'])
def updateStudent():
        try:
            
            data = request.json
            student_id = data['student_id']
            name = data['name']
            email = data['email']
            profile_pic = data['profile_pic']
            password = data['password']
            
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            
            cursor.execute("UPDATE student SET name=%s, email=%s, profile_pic=%s, password=%s WHERE student_id=%s",
                           (name, email, profile_pic, password, student_id))
            
            conn.commit()
            cursor.close()
            conn.close()
            
            response = jsonify({'message': 'Student information updated successfully'})
            response.status_code = 200
            return response
        except Exception as e:
            
            print(e)
           
            response = jsonify({'error': 'An error occurred while updating student information'})
            response.status_code = 500
            return response
        
@app.route('/studentsS')
def getStudents():
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("SELECT * FROM student")
            studentsRows = cursor.fetchall()
            respone = jsonify(studentsRows)
            respone.status_code = 200
            return respone
        except Exception as e:
            print(e)
        finally:
            cursor.close() 
            conn.close() 
            