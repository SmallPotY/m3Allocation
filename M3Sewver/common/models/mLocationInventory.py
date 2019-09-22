# -*- coding:utf-8 -*-
from common.models import Base, db


class LocationInventoryModel(Base):
    """-config-
        undefined
    """
    __tablename__ = 'LOCATION_INVENTORY'

    id = db.Column(db.Integer, primary_key=True, nullable=False, comment="id")
    location_id = db.Column(db.String(32), comment="货位表")
    order_number = db.Column(db.String(128), comment="订单号")
    number = db.Column(db.Integer, comment="件数")
    state = db.Column(db.String(32), comment="状态")