from flask import jsonify, request, Blueprint
from app.queries.mysqlconnect import execute_query

bp = Blueprint('user', __name__)

@bp.route('/add', methods=['POST'])
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

@bp.route('/delete/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    try:
        # Delete related team membership records first
        delete_membership_query = "DELETE FROM teammembership WHERE MemberID = %s"
        execute_query(delete_membership_query, (student_id,))

        # Delete related tasks records
        delete_tasks_query = "DELETE FROM task WHERE ProjectID IN (SELECT ProjectID FROM project WHERE CreatorID = %s)"
        execute_query(delete_tasks_query, (student_id,))

        # Delete related collaboration records
        delete_collaborations_query = "DELETE FROM collaboration WHERE ProjectID IN (SELECT ProjectID FROM project WHERE CreatorID = %s)"
        execute_query(delete_collaborations_query, (student_id,))

        # Delete related projects records
        delete_projects_query = "DELETE FROM project WHERE CreatorID = %s"
        execute_query(delete_projects_query, (student_id,))

        # Finally, delete the student record
        delete_student_query = "DELETE FROM student WHERE StudentID = %s"
        execute_query(delete_student_query, (student_id,))

        response = jsonify({'message': 'Student account deleted successfully'})
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
        response = jsonify({'error': 'An error occurred while deleting student account'})
        response.status_code = 500
        return response

@bp.route('/update/<int:student_id>', methods=['PUT'])
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

@bp.route('/all')
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

@bp.route('/<int:id>', methods=['GET'])
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
    

@bp.route('/login/<string:name>/<string:password>', methods=['GET'])
def get_student_by_name_and_password(name, password):
    try:
        query = "SELECT * FROM student WHERE username = %s AND password = %s"
        student_row = execute_query(query, (name, password), fetch_all=True)

        if student_row:
            response = jsonify({"message":"login"})
            response.status_code = 200
            return response
        else:
            return jsonify({"message":"noLogin"}), 404
    except Exception as e:
        print(e)
        return jsonify({"message": "Internal Server Error"}), 500