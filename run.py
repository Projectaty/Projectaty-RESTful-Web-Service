from app import create_app

"""
    MAIN
    - Creat App from __init__ => configured, + CROS
    - register blueprints for each query 
    - Run app
"""
app, mysql = create_app()

if __name__ == "__main__":
    from app.queries import userQuery, projectQuery, taskQuery, teamQuery
    app.register_blueprint(projectQuery.bp, url_prefix='/project')
    app.register_blueprint(taskQuery.bp, url_prefix='/task')
    app.register_blueprint(teamQuery.bp, url_prefix='/team')
    app.register_blueprint(userQuery.bp, url_prefix='/user')
    app.run()