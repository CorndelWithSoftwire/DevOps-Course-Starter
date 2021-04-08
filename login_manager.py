
from flask_login import LoginManager, UserMixin, current_user, login_required, login_user, logout_user
from oauthlib.oauth2 import WebApplicationClient
import os
import requests
from werkzeug.utils import redirect


# flask_login
#login_manager = LoginManager()
#login_manager.init_app(app)

client_id = os.getenv("GIT_CLIENT_ID")
client_secret = os.getenv("GIT_CLIENT_SECRET")
authorization_base_url = 'https://github.com/login/oauth/authorize'

@login_manager.unauthorized_handler
def unauthenticated():
    client = WebApplicationClient(client_id=client_id)
    #client = WebApplicationClient('your_id')
    client.prepare_request_uri('https://example.com')
    #'https://example.com?client_id=your_id&response_type=code'
    
    client.prepare_request_uri(authorization_base_url)
    #'https://example.com?client_id=your_id&response_type=code&redirect_uri=https%3A%2F%2Fa.b%2Fcallback'

    #client.prepare_request_uri('https://example.com', scope=['profile', 'pictures'])
    #'https://example.com?client_id=your_id&response_type=code&scope=profile+pictures'

    #client.prepare_request_uri('https://example.com', foo='bar')
    #'https://example.com?client_id=your_id&response_type=code&foo=bar'
    
    uri = client.prepare_request_uri('https://github.com/login/oauth/authorize')
    #return redirect(uri)
    pass

@login_manager.user_loader
def load_user(user_id):
    return None

    