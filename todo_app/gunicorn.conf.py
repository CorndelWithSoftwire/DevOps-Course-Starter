import os
bind = "0.0.0.0:" + os.environ.get('PORT', '5000')
accesslog = "gunicorn_access.log"
errorlog = "gunicorn_error.log"
daemon = False
workers = 2