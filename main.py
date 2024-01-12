import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request
import studentQuery

if __name__ == "__main__":
    app.debug = True
    app.run()