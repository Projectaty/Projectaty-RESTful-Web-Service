from flask import Flask
from flask_cors import CORS
from flaskext.mysql import MySQL

def create_app(user='root', password='', db='projectatydb', host='127.0.0.1'):
    """
    Import queries and regesiter the blueprints to the app
    Return:
        initialized app
    """
    app = Flask(__name__)
    CORS(app)

    app.config['MYSQL_DATABASE_USER'] =  user
    app.config['MYSQL_DATABASE_PASSWORD'] = password
    app.config['MYSQL_DATABASE_DB'] = db
    app.config['MYSQL_DATABASE_HOST'] = host

    mysql = MySQL(app)
    return app, mysql