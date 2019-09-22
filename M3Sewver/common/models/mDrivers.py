# -*- coding:utf-8 -*-
from common.models import Base, db


class DriversModel(Base):
    """-config-
        undefined
    """
    __tablename__ = 'DRIVERS'

    driver_id = db.Column(db.Integer, primary_key=True, nullable=False, comment="id")
    name = db.Column(db.String(32), comment="姓名")
    phone = db.Column(db.String(32), comment="电话")
    id_card = db.Column(db.String(32), comment="证件号")