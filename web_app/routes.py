from web_app import app

import json, plotly
from flask import render_template
#from flask import render_template, request, Response, jsonify
from scripts.data import return_figures

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

