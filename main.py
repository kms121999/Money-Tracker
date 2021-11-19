VERSION = "1.0.0"

from flask import render_template, flash, redirect, url_for, request, current_app
from gevent.pywsgi import WSGIServer

from app import app

# Landing Page
@app.route('/', methods=['GET', 'POST'])
@app.route('/home/', methods=['GET', 'POST'])
def home():
  return render_template('home.html')
