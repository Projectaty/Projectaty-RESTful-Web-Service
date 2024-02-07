from flask import jsonify
from flask import request
from flask import Blueprint
from app.queries.mysqlconnect import execute_query

bp = Blueprint('/user', __name__)

@bp.route('/students', methods=['POST'])
def add_student():
    try:
        data = request.json
        name = data['name']
        email = data['email']
        profile_pic = data['profile_pic']
        password = data['password']

        query = "INSERT INTO student (name, email, profile_pic, password) VALUES (%s, %s, %s, %s)"
        execute_query(query, (name, email, profile_pic, password))

        response = jsonify({'message': 'Student information inserted successfully'})
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
        response = jsonify({'error': 'An error occurred while inserting student information'})
        response.status_code = 500
        return response

@bp.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    try:
        query = "DELETE FROM student WHERE student_id = %s"
        execute_query(query, (student_id,))

        response = jsonify({'message': 'Student account deleted successfully'})
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
        response = jsonify({'error': 'An error occurred while deleting student account'})
        response.status_code = 500
        return response

@bp.route('/students', methods=['PUT'])
def update_student():
    try:
        data = request.json
        student_id = data['student_id']
        name = data['name']
        email = data['email']
        profile_pic = data['profile_pic']
        password = data['password']

        query = "UPDATE student SET name=%s, email=%s, profile_pic=%s, password=%s WHERE student_id=%s"
        execute_query(query, (name, email, profile_pic, password, student_id))

        response = jsonify({'message': 'Student information updated successfully'})
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
        response = jsonify({'error': 'An error occurred while updating student information'})
        response.status_code = 500
        return response

@bp.route('/students', methods=['GET'])
def get_students():
    try:
        query = "SELECT * FROM student"
        students_rows = execute_query(query, fetch_all=True)

        response = jsonify(students_rows)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
        response = jsonify({'error': 'An error occurred while fetching student information'})
        response.status_code = 500
        return response