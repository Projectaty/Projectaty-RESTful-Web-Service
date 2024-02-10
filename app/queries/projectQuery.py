from flask import jsonify, request, Blueprint
from app.queries.mysqlconnect import execute_query

bp = Blueprint("project", __name__)

## Get all the projects
@bp.route('/all', methods=['GET'])
def get_projects():
    try:
        query = "SELECT * FROM project"
        project_row = execute_query(query, fetch_all=True)

        if project_row:
            response = jsonify(project_row)
            response.status_code = 200
            return response
        else:
            return jsonify({"message": "No project found"}), 404
    except Exception as e:
        print(e)
        return jsonify({"message": "Internal Server Error"}), 500

@bp.route('/<int:ProjectID>', methods=['GET'])
def get_project_by_id(ProjectID):
    try:
        query = "SELECT * FROM project WHERE ProjectID = %s"
        project_row = execute_query(query, (ProjectID))

        if project_row:
            response = jsonify(project_row)
            response.status_code = 200
            return response
        else:
            return jsonify({"message": "Project not found"}), 404
    except Exception as e:
        print(e)
        return jsonify({"message": "Internal Server Error"}), 500

### Add project data
@bp.route('/add', methods=['POST'])
def add_project():
    """
        Args:
            No args, takes the data from JSON request
        Return:
            Response either eror or message
    """
    try:
        """ Get the data from json request """
        data = request.json

        ProjectID = data['ProjectID']
        Title = data['Title']
        Description = data['Description']
        Deadline = data['Deadline']
        PrivacySetting = data['PrivacySetting']
        
        query = "INSERT INTO project (ProjectID, Title, Description, Deadline,PrivacySetting ) VALUES (%s, %s, %s, %s, %s)"
        execute_query(query,  (ProjectID,Title, Description, Deadline,PrivacySetting))
        
        """ If inserted succesfuly return a message"""
        response = jsonify({'message': 'Project information inserted successfully'})
        response.status_code = 200
        return response
    except Exception as e:
        """ Hadnle exceptions by printing the errors and put them in the response """
        print(e)
        response = jsonify({'error': 'An error occurred while inserting task information'})
        response.status_code = 500
        return response

# Delete project by ID
@bp.route('/delete/<int:ProjectID>', methods=['DELETE'])
def delete_project(ProjectID):
    """
        Args:
            Taks a task ID to be deleted
        Return:
            response, etheir message or error
    """
    try:
        query = "DELETE FROM project WHERE ProjectID = %s"
        execute_query(query, (ProjectID))

        """ Return respose message if successfuly deletd """
        response = jsonify({'message': 'ProjectID deleted successfully'})
        response.status_code = 200
        return response
    except Exception as e:
        """ Hadnle exceptions by printing the errors and put them in the response """
        print(e)
        response = jsonify({'error': 'An error occurred while deleting ProjectID'})
        response.status_code = 500
        return response

 ## update the project 
@bp.route('/update/<int:ProjectID>', methods=['PUT'])
def update_project(ProjectID):
    """
        Args:
            None takes teh data from Json request
        Returns:
            Response is the message or the error
    """
    try:
        data = request.json
        Title = data['Title']
        Description = data['Description']
        Deadline = data['Deadline']
        PrivacySetting = data['PrivacySetting']

        query = "UPDATE project SET Title=%s, Description=%s, Deadline=%s, PrivacySetting=%s WHERE ProjectID=%s"
        execute_query(query, (ProjectID, Title, Description, Deadline, PrivacySetting))

        response = jsonify({'message': 'project information updated successfully'})
        response.status_code = 200
        return response
    except Exception as e:
        """ Hadnle exceptions by printing the errors and put them in the response """
        print(e)
        response = jsonify({'error': 'An error occurred while updating project information'})
        response.status_code = 500
        return response