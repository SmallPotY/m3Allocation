# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import jsonify
from web.controllers.api.helper import *
from web.validators.scanning import InScanning

api = Blueprint("api", __name__)


@api.route("/initData")
def initData():
    initialization()
    return jsonify({"status": 1, "msg": "ok"})


@api.route("/inScanning")
def inScanning():
    form = InScanning().validate_for_forms()
    print(form.to_dict())

    return jsonify({"status": 1, "msg": "ok"})
