from flask import Flask
from flask_cors import CORS, cross_origin
import projectQuery
import taskQuery
import teamQuery
import userQuery

def create_app():
    """
        Import quires and add the blue prints to
        the app 
        Return:
            initialized app
    """
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(projectQuery.bp)
    app.register_blueprint(taskQuery.bp)
    app.register_blueprint(teamQuery.bp)
    app.register_blueprint(userQuery.bp)
    return app