import pymysql
from app import create_app
from config import mysql
from flask import jsonify
from flask import flash, request
import studentQuery

if __name__ == "__main__":
    app = create_app()
    app.run()