# -*- coding:utf-8 -*-
from common.models.mLocation import LocationModel
from application import db


def initialization():
    for i in range(20):
        _id = "A{0:02d}".format(i)
        l = LocationModel()
        l.area_name = "测试区"
        l.location_id = _id
        l.area_type = "地托"
        db.session.add(l)
        db.session.commit()
