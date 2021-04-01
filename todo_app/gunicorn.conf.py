bind = "0.0.0.0:$port"
accesslog = "gunicorn_access.log"
errorlog = "gunicorn_error.log"
daemon = False
workers = 2