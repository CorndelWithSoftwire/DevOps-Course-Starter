import os

LOG_PATH = "/var/log/gunicorn"
port = os.getenv("PORT")
workers = 2
threads = 4
worker_class = "gthread"
bind = f"0.0.0.0:{port}"
error_logfile= f"{LOG_PATH}/gunicorn_error.log"
log_file = f"{LOG_PATH}/gunicorn.log"
