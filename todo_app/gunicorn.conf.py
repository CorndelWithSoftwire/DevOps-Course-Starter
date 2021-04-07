import os
bind = "0.0.0.0:" + os.environ.get('PORT')
accesslog = "gunicorn_access.log"
errorlog = "gunicorn_error.log"
daemon = False
workers = 2