# -*- coding:utf-8 -*-
from common.models import Base, db


class AccessRecordModel(Base):
    """-config-
        undefined
    """
    __tablename__ = 'ACCESS_RECORD'

    record_id = db.Column(db.Integer, primary_key=True, nullable=False, comment="id")
    location_id = db.Column(db.String(32), comment="货位号")
    order_number = db.Column(db.String(32), comment="客户订单号")
    type = db.Column(db.String(32), comment="类型")
    number = db.Column(db.String(32), comment="数量")
    time_stamp = db.Column(db.Integer, comment="时间")
    user = db.Column(db.String(32), comment="用户")