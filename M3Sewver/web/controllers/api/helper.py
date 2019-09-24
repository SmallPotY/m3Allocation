# -*- coding:utf-8 -*-
from application import db
from common.models.mLocation import LocationModel
from common.models.mArrivalOrder import ArrivalOrderModel
from web.httpCode.code import Success, NotFound


def initialization():
    for i in range(20):
        _id = "A{0:02d}".format(i)
        l = LocationModel()
        l.area_name = "测试区"
        l.location_id = _id
        l.area_type = "地托"
        db.session.add(l)
        db.session.commit()


def checkScanningHas(check_type, check_item):
    query = None
    check = "货位号" if check_type == "location_id" else "订单号"
    if check_type == "location_id":
        query = LocationModel.query.filter_by(location_id=check_item).first()
    elif check_type == "order_id":
        query = ArrivalOrderModel.query.filter_by(customer_number=check_item).first()

    if query:
        return Success()
    else:
        return NotFound("{check}:{check_item} - 不存在".format(check=check, check_item=check_item))
