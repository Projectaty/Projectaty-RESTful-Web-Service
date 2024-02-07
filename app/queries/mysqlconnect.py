from run import mysql
import pymysql

def get_db_connection():
    """
        Returns mysql connection
    """
    return mysql.connect()

def close_db_connection(conn, cursor):
    """
        Args:
            Conn: Mysql DB connection
            Cursor
        Cleans and close connection
    """
    cursor.close()
    conn.close()

def execute_query(query, params=None, fetch_all=False):
    """
        Args:
            Takes a query, and parameters 
            Fetch all is for SELECT queries
        Returns:
            Result: either none or fetched data

    """
    conn = get_db_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

        conn.commit()

        if fetch_all:
            result = cursor.fetchall()
        else:
            result = None
        return result
    except Exception as e:
        print(e)
        raise
    finally:
        close_db_connection(conn, cursor)