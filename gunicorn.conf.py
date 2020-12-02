import os
from dotenv import load_dotenv

load_dotenv('.env', override=True)

bind = "0.0.0.0:5000"
accesslog = "gunicorn_access.log"
errorlog = "gunicorn_error.log"
daemon = True
 