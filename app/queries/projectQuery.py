from flask import jsonify, request, Blueprint
from app.queries.mysqlconnect import execute_query

bp = Blueprint("project", __name__)

@bp.route('/all')
def getProjects():
    try:
        query = "SELECT * FROM project"
        project_rows = execute_query(query, fetch_all=True)

        response = jsonify(project_rows)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
        response = jsonify({'error': 'An error occurred while fetching project information'})
        response.status_code = 500
        return response

@bp.route('/add', methods=['POST'])
def addProject():
    try:
        data = request.json
        Title = data['Title']
        Description = data['Description']
        Deadline = data['Deadline']
        PrivacySetting = data['PrivacySetting']
        CreatorID = data['CreatorID']
        
        query = "INSERT INTO project (Title, Description, Deadline, PrivacySetting , CreatorID) VALUES (%s, %s, %s, %s)"
        execute_query(query,  (Title, Description, Deadline, PrivacySetting, CreatorID), commit=True)

        response = jsonify({'message': 'Project information inserted successfully!'})
        response.status_code = 200
        return response
        
    except Exception as e:
        print(e)
        response = jsonify({'error': 'An error occurred while inserting Project information'})
        response.status_code = 500
        return response
    
@bp.route('/delete/<int:ProjectID>', methods=['DELETE'])
def deleteProject(ProjectID):
    try:
        query = "DELETE FROM project WHERE ProjectID = %s"
        execute_query(query, (ProjectID,), commit=True)

        response = jsonify({'message': 'Project deleted successfully!'})
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
        response = jsonify({'error': 'An error occurred while deleting Project!'})
        response.status_code = 500
        return response

@bp.route('/update', methods=['PUT'])
def updateProject():
    try:
        
        data = request.json
        Title = data['Title']
        Description = data['Description']
        Deadline = data['Deadline']
        PrivacySetting = data['PrivacySetting']
        CreatorID = data['CreatorID']
        
        query = "UPDATE project SET Title=%s, Description=%s, Deadline=%s, PrivacySetting=%s, CreatorID=%s WHERE ProjectId=%s"
        execute_query(query,  (Title, Description, Deadline, PrivacySetting,CreatorID), commit=True)

        response = jsonify({'message': 'project information updated successfully!'})
        response.status_code = 200
        return response
    except Exception as e:

        print(e)
        response = jsonify({'error': 'An error occurred while updating project information!'})
        response.status_code = 500
        return response