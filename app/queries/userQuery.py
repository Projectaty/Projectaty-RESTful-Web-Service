from flask import jsonify, request, Blueprint
from app.queries.mysqlconnect import execute_query

bp = Blueprint('user', __name__)

@bp.route('/studentsI', methods=['POST'])
def add_student():
    try:
        data = request.json
        student_id = data['StudentID']
        name = data['username']
        email = data['email']
        profile_pic = data['profile_pic']
        password = data['password']

        query = "INSERT INTO student (StudentID, username, password, email, profile_pic) VALUES (%s, %s, %s, %s, %s)"
        execute_query(query, (student_id, name, password, email, profile_pic))

        response = jsonify({'message': 'Student information inserted successfully'})
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
        response = jsonify({'error': 'An error occurred while inserting student information'})
        response.status_code = 500
        return response

@bp.route('/studentsD/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    try:
        query = "DELETE FROM student WHERE StudentID = %s"
        execute_query(query, (student_id,))

        response = jsonify({'message': 'Student account deleted successfully'})
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
        response = jsonify({'error': 'An error occurred while deleting student account'})
        response.status_code = 500
        return response

@bp.route('/studentsU/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    try:
        data = request.json

        name = data['username']
        email = data['email']
        profile_pic = data['profile_pic']
        password = data['password']

        query = "UPDATE student SET username=%s, password=%s, email=%s, profile_pic=%s WHERE StudentID=%s"
        execute_query(query, (name, password, email, profile_pic, student_id))

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

@bp.route('/studentsS/<int:id>', methods=['GET'])
def get_student_by_id(id):
    try:
        query = "SELECT * FROM student WHERE StudentID = %s"
        student_row = execute_query(query, (id,), fetch_all=True)

        if student_row:
            response = jsonify(student_row)
            response.status_code = 200
            return response
        else:
            return jsonify({"message": "Student not found"}), 404
    except Exception as e:
        print(e)
        return jsonify({"message": "Internal Server Error"}), 500
    

@bp.route('/studentsS/<string:name>/<string:password>', methods=['GET'])
def get_student_by_name_and_password(name, password):
    try:
        query = "SELECT * FROM student WHERE username = %s AND password = %s"
        student_row = execute_query(query, (name, password), fetch_all=True)

        if student_row:
            response = jsonify(student_row)
            response.status_code = 200
            return response
        else:
            return jsonify({"message": "Student not found"}), 404
    except Exception as e:
        print(e)
        return jsonify({"message": "Internal Server Error"}), 500