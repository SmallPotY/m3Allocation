# -*- coding:utf-8 -*-
from flask import Blueprint, request
from flask import jsonify
from web.controllers.api.helper import checkScanningHas
from web.httpCode import APIException
from web.httpCode.code import Success
from web.validators.scanning import InScanning

api = Blueprint("api", __name__)


@api.route("/initData")
def initData():
    return jsonify({"status": 1, "msg": "ok"})


@api.route("/inScanning", methods=['POST'])
def inScanning():
    form = InScanning().validate_for_forms()
    print(form.to_dict())

    return jsonify({"status": 1, "msg": "ok"})


@api.route("/checkScanning")
def checkScanning():
    form = request.args.to_dict()

    if form.get("location_id"):
        response = checkScanningHas("location_id", form.get("location_id"))
    elif form.get("order_id"):
        response = checkScanningHas("order_id", form.get("order_id"))
    else:
        return APIException("参数异常")

    return response
