from flask import Flask
from flask_cors import CORS
import userQuery
import projectQuery
import taskQuery
import teamQuery
from flaskext.mysql import MySQL

mysql = MySQL()

def create_app(user='root', password='', db='projectatydb', host='127.0.0.1'):
    """
    Import queries and add the blueprints to the app
    Return:
        initialized app
    """
    app = Flask(__name__)
    CORS(app)
    app.config['MYSQL_DATABASE_USER'] =  user
    app.config['MYSQL_DATABASE_PASSWORD'] = password
    app.config['MYSQL_DATABASE_DB'] = db
    app.config['MYSQL_DATABASE_HOST'] = host
    mysql.init_app(app)
    app.register_blueprint(projectQuery.bp, url_prefix='/project')
    app.register_blueprint(taskQuery.bp, url_prefix='/task')
    app.register_blueprint(teamQuery.bp, url_prefix='/team')
    app.register_blueprint(userQuery.bp, url_prefix='/user')
    return app

if __name__ == "__main__":
    app = create_app()
    app.run()