from app import app
from flask import jsonify, request, abort,render_template, url_for,json
import flask
import os
import re
import json


@app.route('/crime-charts.html')
def crime_charts():
    return render_template('crime-charts.html')


@app.route('/crime-locator.html')
def crime_locator():
    return render_template('crime-locator.html')




from webscapper import *
@app.route('/',methods=['GET','POST'])
@app.route('/index.html')
def index():
    request_method=request.method
    if request.method=='POST':
        webscrappingfun()
    return render_template('index.html')

    