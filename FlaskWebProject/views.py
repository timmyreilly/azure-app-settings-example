"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, Response 
from FlaskWebProject import app
import os

token = os.getenv('BING_MAP_TOKEN')

if token == None:
    print 'here'
    from tokens import *  
    token = BING_API_KEY


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    """ And shows part of your token!""" 
    return render_template(
        'index.html',
        title='Home Page',
        info=token[1:6],
        year=datetime.now().year,
    )

@app.route('/map')
def bingtrial():
    data = [
        {
            "list_a": [37.767111,-122.445811],
            "list_b": [37.792111, -122.403611],
            "color": [200, 200, 0, 100]
        }
    ]
    return render_template(
        'map.html',
        data=data,
        key=token)