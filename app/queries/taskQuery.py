from flask import jsonify, request, Blueprint
from app.queries.mysqlconnect import execute_query

"""
    In this script I create a task query, that utilizies the execute_query 
    - that class makes a connection to the mysql database 
    - this query script write queries to the mysqldatbase and returns data
    Quires:
        1- Insert Into
        2- Update
        3- Delete
        4- Select, Select with conditions
"""
bp = Blueprint('task', __name__)

## Get all the tasks
@bp.route('/all', methods=['GET'])
def get_tasks():
    """
        Returns:
            the task attributes for all tasks
    """
    try:
        query = "SELECT * FROM task"
        tasks_rows = execute_query(query, fetch_all=True)
        response = jsonify(tasks_rows)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
        return jsonify({"message": "Internal Server Error"}), 500

## Get the data of task by ID
@bp.route('/<int:task_id>', methods=['GET'])
def get_task_by_id(task_id):
    """
        Args: 
            takes a specific task ID 
        Returns:
            the task attributes with specific ID
    """
    try:
        query = "SELECT * FROM task WHERE TaskID = %s"
        task_row = execute_query(query, (task_id), fetch_all=True)
        response = jsonify(task_row)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
        return jsonify({"message": "Internal Server Error"}), 500

### Add Task data
@bp.route('/add', methods=['POST'])
def add_task():
    """
        Args:
            No args, takes the data from JSON request
        Return:
            Response either eror or message
    """
    try:
        """ Get the data from json request """
        data = request.json
        task_id = data['TaskID']
        project_id = data['ProjectID']
        title = data['Title']
        description = data['Description']
        status = data['Status']
        assigned_to = data['AssignedTo']

        query = "INSERT INTO task (TaskID, ProjectID, Title, Description, Status, AssignedTo) VALUES (%s, %s, %s, %s, %s, %s)"
        execute_query(query, (task_id, project_id, title, description, status, assigned_to))
        
        """ If inserted succesfuly return a message"""
        response = jsonify({'message': 'Task information inserted successfully'})
        response.status_code = 200
        return response
    except Exception as e:
        """ Hadnle exceptions by printing the errors and put them in the response """
        print(e)
        response = jsonify({'error': 'An error occurred while inserting task information'})
        response.status_code = 500
        return response

# Delete task by ID
@bp.route('/delete/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """
        Args:
            Taks a task ID to be deleted
        Return:
            response, etheir message or error
    """
    try:
        query = " DELETE FROM task WHERE TaskID = %s"
        execute_query(query, (task_id))

        """ Return respose message if successfuly deletd """
        response = jsonify({'message': 'Task deleted successfully'})
        response.status_code = 200
        return response
    except Exception as e:
        """ Hadnle exceptions by printing the errors and put them in the response """
        print(e)
        response = jsonify({'error': 'An error occurred while deleting task'})
        response.status_code = 500
        return response

## update the task 
@bp.route('/update/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """
        Args:
            None takes teh data from Json request
        Returns:
            Response is the message or the error
    """
    try:
        data = request.json
        project_id = data['ProjectID']
        title = data['Title']
        description = data['Description']
        status = data['Status']
        assigned_to = data['AssignedTo']

        query = "UPDATE task SET ProjectID=%s, Title=%s, Description=%s, Status=%s, AssignedTo=%s WHERE TaskID=%s"
        execute_query(query, (project_id, title, description, status, assigned_to, task_id))

        response = jsonify({'message': 'Task information updated successfully'})
        response.status_code = 200
        return response
    except Exception as e:
        """ Hadnle exceptions by printing the errors and put them in the response """
        print(e)
        response = jsonify({'error': 'An error occurred while updating task information'})
        response.status_code = 500
        return response

# fetch the done tasks for specifc fproject
@bp.route('/done/<int:project_id>', methods=['GET'])
def get_done_tasks_in_project(project_id):
    """
        Args:
            Takes a specifc project ID 
        Returns: 
            All the tasks that are done for that project
            or an error response
    """
    try:
        query = "SELECT * FROM task WHERE Status=%s AND ProjectID=%s"
        done_rows = execute_query(query,("done", project_id), fetch_all=True)

        response = jsonify({"tasks": done_rows})
        response.status_code = 200
        return response
    except Exception as e:
        """ Hadnle exceptions by printing the errors and put them in the response """
        print(e)
        response = jsonify({'error': 'An error occurred while fetching task list'})
        response.status_code = 500
        return response

# fetch the inprogress tasks for specifc fproject
@bp.route('/inprogress/<int:project_id>', methods=['GET'])
def get_inprogress_tasks_in_project(project_id):
    """
        Args:
            Takes a specifc project ID 
        Returns: 
            All the tasks that are in progress for that project
            or an error response
    """
    try:
        query = "SELECT * FROM task WHERE Status=%s AND ProjectID=%s"
        inprogress_rows = execute_query(query,("inprogress", project_id), fetch_all=True)

        response = jsonify({"tasks": inprogress_rows})
        response.status_code = 200
        return response
    except Exception as e:
        """ Hadnle exceptions by printing the errors and put them in the response """
        print(e)
        response = jsonify({'error': 'An error occurred while fetching task list'})
        response.status_code = 500
        return response
    
# fetch the todo tasks for specifc fproject
@bp.route('/todo/<int:project_id>', methods=['GET'])
def get_todo_tasks_in_project(project_id):
    """
        Args:
            Takes a specifc project ID 
        Returns: 
            All the tasks that are to do yet for that project
            or an error response
    """
    try:
        query = "SELECT * FROM task WHERE Status=%s OR ProjectID=%s"
        todo_rows = execute_query(query,("todo", project_id), fetch_all=True)

        response = jsonify({"tasks": todo_rows})
        response.status_code = 200
        return response
    except Exception as e:
        """ Hadnle exceptions by printing the errors and put them in the response """
        print(e)
        response = jsonify({'error': 'An error occurred while fetching task list'})
        response.status_code = 500
        return response
