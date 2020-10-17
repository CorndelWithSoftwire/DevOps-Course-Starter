from flask import Flask, render_template, request, redirect, url_for
import config as cf
from model import Item, ViewModel
from trello_app import trello_bp
import session_items as session
import requests
import json


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    #app.config.from_object('app_config.Config')
    
    app.register_blueprint(trello_bp)
        
    return app
