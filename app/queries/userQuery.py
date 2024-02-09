from flask import jsonify, request, Blueprint
from app.queries.mysqlconnect import execute_query

bp = Blueprint('user', __name__)

@bp.route('/studentsI', methods=['POST'])
def add_student():
    try:
        data = request.json
        student_id = data['student_id']
        name = data['name']
        email = data['email']
        profile_pic = data['profile_pic']
        password = data['password']

        query = "INSERT INTO student (student_id, name, email, profile_pic, password) VALUES (%s, %s, %s, %s, %s)"
        execute_query(query, (student_id, name, email, profile_pic, password), commit=True)

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
        execute_query(query, (student_id,), commit=True)

        response = jsonify({'message': 'Student account deleted successfully'})
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
        response = jsonify({'error': 'An error occurred while deleting student account'})
        response.status_code = 500
        return response

@bp.route('/studentsU', methods=['PUT'])
def update_student():
    try:
        data = request.json
        student_id = data['student_id']
        name = data['name']
        email = data['email']
        profile_pic = data['profile_pic']
        password = data['password']

        query = "UPDATE student SET name=%s, email=%s, profile_pic=%s, password=%s WHERE student_id=%s"
        execute_query(query, (name, email, profile_pic, password, student_id), commit=True)

        response = jsonify({'message': 'Student information updated successfully'})
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
        response = jsonify({'error': 'An error occurred while updating student information'})
        response.status_code = 500
        return response

@bp.route('/studentsS')
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

@bp.route('/students/<int:id>', methods=['GET'])
def get_student_by_id(id):
    try:
        query = "SELECT * FROM student WHERE id = %s"
        student_row = execute_query(query, (id,), fetch_one=True)

        if student_row:
            response = jsonify(student_row)
            response.status_code = 200
            return response
        else:
            return jsonify({"message": "Student not found"}), 404
    except Exception as e:
        print(e)
        return jsonify({"message": "Internal Server Error"}), 500