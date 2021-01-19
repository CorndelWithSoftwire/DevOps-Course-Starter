from todo_app import app

# do some production specific things to the app
# app.config['DEBUG'] = False
app = app.create_app()
