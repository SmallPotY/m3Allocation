# -*- coding:utf-8 -*-
from flask import render_template

from application import app
from web.controllers.api.view import api

app.register_blueprint(api, url_prefix='/api')


# @app.route('/')
# def index():
#     return 'hello'
#     return render_template('index.html')
