LOG_PATH = "/var/log/gunicorn"

workers = 2
threads = 4
worker_class = "gthread"
bind = "0.0.0.0:5000"
error_logfile= f"{LOG_PATH}/gunicorn_error.log"
log_file = f"{LOG_PATH}/gunicorn.log"
