# -*- coding:utf-8 -*-
from common.models import Base, db


class ArrivalOrderModel(Base):
    """-config-
        undefined
    """
    __tablename__ = 'ARRIVAL_ORDER'

    id = db.Column(db.Integer, primary_key=True, nullable=False, comment="id")
    predictable_arrival_time = db.Column(db.DateTime, comment="预到达时间")
    delivery_time = db.Column(db.DateTime, comment="提货时间")
    car_number = db.Column(db.String(32), comment="车牌号")
    customer_number = db.Column(db.String(128), comment="客户单号")
    order_number = db.Column(db.String(128), comment="订单号")
    prefecture = db.Column(db.String(32), comment="区域")
    receiving_address = db.Column(db.String(512), comment="收货地址")
    receiving_contact = db.Column(db.String(32), comment="收货联系人")
    receiving_telephone = db.Column(db.String(32), comment="收货联系电话")
    predictable_quantity = db.Column(db.Integer, comment="预知数量")
    predictable_weight = db.Column(db.Float, comment="预知重量")
    predictable_volume = db.Column(db.Float, comment="预知方数")
    remarks = db.Column(db.String(512), comment="备注内容")
    actual_quantity = db.Column(db.Integer, comment="实际数量")
    actual_weight = db.Column(db.Float, comment="实际重量")
    actual_volume = db.Column(db.Float, comment="实际方数")
    actual_arrival_time = db.Column(db.DateTime, comment="实际到达时间")
    complete_time = db.Column(db.DateTime, comment="完结时间")
    state = db.Column(db.String(32), comment="状态")