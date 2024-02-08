from app import app
from flask import jsonify
from flask import request
from config import mysql
import pymysql
from flask import Blueprint

bp = Blueprint("project", __name__)

@app.route('/all')
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



@app.route('/ProjectId', methods=['POST'])
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
    
@app.route('/project/<int:ProjectID>', methods=['DELETE'])
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

@app.route('/projectUpdate', methods=['PUT'])
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


@bp.route('/project/<int:id>', methods=['GET'])
def getProjectById(id):
    try:
        query = "SELECT * FROM project WHERE id = %s"
        project_row = execute_query(query, (id,), fetch_one=True)

        if project_row:
            response = jsonify(project_row)
            response.status_code = 200
            return response
        else:
            return jsonify({"message": "project not found"}), 404
    except Exception as e:
        print(e)
        return jsonify({"message": "Internal Server Error"}), 500
