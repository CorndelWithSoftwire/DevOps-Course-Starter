
from flask_login import LoginManager, UserMixin, current_user, login_required, login_user, logout_user
from oauthlib.oauth2 import WebApplicationClient
from flask import redirect
import os
import requests


client_id = os.getenv("GIT_CLIENT_ID")
client_secret = os.getenv("GIT_CLIENT_SECRET")
authorization_base_url = 'https://github.com/login/oauth/authorize'

login_managers = LoginManager()

@login_managers.unauthorized_handler
def unauthenticated():
    client = WebApplicationClient(client_id=client_id) 
    uri = client.prepare_request_uri(authorization_base_url)
    return redirect(uri)

@login_managers.user_loader
def load_user(user_id):
    return None

    