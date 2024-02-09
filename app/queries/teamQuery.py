from flask import jsonify, request, Blueprint
from app.queries.mysqlconnect import execute_query

bp = Blueprint('team', __name__)

# Get team data by ID
@bp.route('/all', methods=['GET'])
def get_teams():
    try:
        query = "SELECT * FROM Team"
        teams = execute_query(query)

        if teams:
            response = jsonify(teams)
            response.status_code = 200
            return response
        else:
            return jsonify({"message": "No teams found"}), 404
    except Exception as e:
        print(e)
        return jsonify({"message": "Internal Server Error"}), 500

# Get team data by ID
@bp.route('/<int:team_id>', methods=['GET'])
def get_team_by_id(team_id):
    try:
        query = "SELECT * FROM Team WHERE TeamID = %s"
        team_row = execute_query(query, (team_id), fetch_one=True)

        if team_row:
            response = jsonify(team_row)
            response.status_code = 200
            return response
        else:
            return jsonify({"message": "team not found"}), 404
    except Exception as e:
        print(e)
        return jsonify({"message": "Internal Server Error"}), 500
    
# Add Team data
@bp.route('/add', methods=['POST'])
def add_team():
    try:
        """ Get the data from json request """
        data = request.json
        team_id = data['TeamID']
        team_name = data['TeamName']
        description = data['Description']
        status = data['Status']
        
        query = "INSERT INTO Team (TeamID, TeamName, Description, Status) VALUES (%s, %s, %s, %s)"
        execute_query(query, (team_id, team_name, description, status), commit=True)
        
        """ If inserted succesfuly return a message"""
        response = jsonify({'message': 'Team information inserted successfully'})
        response.status_code = 200
        return response
    except Exception as e:
        """ Hadnle exceptions by printing the errors and put them in the response """
        print(e)
        response = jsonify({'error': 'An error occurred while inserting team information'})
        response.status_code = 500
        return response
    
# Delete team by ID
@bp.route('/delete/<int:team_id>', methods=['DELETE'])
def delete_team(team_id):

    try:
        query = "DELETE FROM Team WHERE TeamID = %s"
        execute_query(query, (team_id,), commit=True)

        """ Return respose message if successfuly deletd """
        response = jsonify({'message': 'Team deleted successfully'})
        response.status_code = 200
        return response
    except Exception as e:
        """ Hadnle exceptions by printing the errors and put them in the response """
        print(e)
        response = jsonify({'error': 'An error occurred while deleting team'})
        response.status_code = 500
        return response

# update team data
@bp.route('/update', methods=['PUT'])
def update_team():

    try:
        data = request.json
        team_id = data['TeamID']
        team_name = data['TeamName']
        description = data['Description']
        status = data['Status']

        query = "UPDATE Team SET TeamName=%s, Description=%s, Status=%s WHERE TeamID=%s"
        execute_query(query, (team_id, team_name, description, status), commit=True)

        response = jsonify({'message': 'Team information updated successfully'})
        response.status_code = 200
        return response
    except Exception as e:
        """ Hadnle exceptions by printing the errors and put them in the response """
        print(e)
        response = jsonify({'error': 'An error occurred while updating team information'})
        response.status_code = 500
        return response
    
# add member to the team
@bp.route('/<int:team_id>/member', methods=['POST'])
def add_member():

    try:
        data = request.json
        member_id = data['StudentID']
        team_id = ['TeamID']

        query = "INSERT INTO members (member_id, team_id) VALUES (%s, %s)"
        execute_query(query, (member_id, team_id), commit=True)
        """ If inserted succesfuly return a message"""
        response = jsonify({'message': 'Member inserted successfully'})
        response.status_code = 200
        return response
    except Exception as e:
        """ Hadnle exceptions by printing the errors and put them in the response """
        print(e)
        response = jsonify({'error': 'An error occurred while inserting member'})
        response.status_code = 500
        return response
    
# Get team members
@bp.route('/<int:team_id>/member', methods=['GET'])
def get_members(student_id):

    try:
        query = "SELECT StudentId FROM TeamMEmbership WHERE TeamId=%s"
        members_row = execute_query(query, (student_id), fetch_one=True)
        if members_row:
            response = jsonify(members_row)
            response.status_code = 200
            return response
        else:
            return jsonify({"message": "Members not found"}), 404
    except Exception as e:
        print(e)
        return jsonify({"message": "Internal Server Error"}), 500

# Delete team member by ID
@bp.route('/delete/<int:team_id>', methods=['DELETE'])
def delete_team_member(member_id):

    try:
        query = "DELETE FROM TeamMEmbership WHERE StudentID = %s"
        execute_query(query, (student_id,), commit=True)

        """ Return respose message if successfuly deletd """
        response = jsonify({'message': 'Student deleted successfully'})
        response.status_code = 200
        return response
    except Exception as e:
        """ Hadnle exceptions by printing the errors and put them in the response """
        print(e)
        response = jsonify({'error': 'An error occurred while deleting student'})
        response.status_code = 500
        return response

# add project to the team
@bp.route('/<int:team_id>/project', methods=['POST'])
def add_project():

    try:
        data = request.json
        project_id = data['ProjectID']
        team_id = ['TeamID']

        query = "INSERT INTO Collabration (project_id, team_id) VALUES (%s,%s)"
        execute_query(query, (project_id, team_id), commit=True)
        """ If inserted succesfuly return a message"""
        response = jsonify({'message': 'Project inserted successfully'})
        response.status_code = 200
        return response
    except Exception as e:
        """ Hadnle exceptions by printing the errors and put them in the response """
        print(e)
        response = jsonify({'error': 'An error occurred while inserting project'})
        response.status_code = 500
        return response
    
# Get team projects
@bp.route('/<int:team_id>/project', methods=['GET'])
def get_project(project_id):

    try:
        query = "SELECT PROJECTID FROM Collaboration WHERE TeamID=%s"
        projects_row = execute_query(query, (project_id), fetch_one=True)
        if projects_row:
            response = jsonify(projects_row)
            response.status_code = 200
            return response
        else:
            return jsonify({"message": "Projects not found"}), 404
    except Exception as e:
        print(e)
        return jsonify({"message": "Internal Server Error"}), 500

# Delete team project by ID
@bp.route('/delete/<int:team_id>', methods=['DELETE'])
def delete_team_project(project_id):

    try:
        query = "DELETE FROM Collabraion WHERE ProjectID = %s"
        execute_query(query, (project_id,), commit=True)

        """ Return respose message if successfuly deletd """
        response = jsonify({'message': 'Project deleted successfully'})
        response.status_code = 200
        return response
    except Exception as e:
        """ Hadnle exceptions by printing the errors and put them in the response """
        print(e)
        response = jsonify({'error': 'An error occurred while deleting project'})
        response.status_code = 500
