# -*- coding:utf-8 -*-
from common.models import Base, db


class DriversModel(Base):
    """-config-
        司机表
    """
    __tablename__ = 'DRIVERS'

    driver_id = db.Column(db.Integer, primary_key=True, nullable=False, comment="id")
    driver_name = db.Column(db.String(32), comment="姓名")
    driver_phone = db.Column(db.String(32), comment="电话")
    driver_idcard = db.Column(db.String(32), comment="证件号")