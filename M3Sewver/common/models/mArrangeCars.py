# -*- coding:utf-8 -*-
from common.models import Base, db


class ArrangeCarsModel(Base):
    """-config-
        排车表
    """
    __tablename__ = 'ARRANGE_CARS'

    arrange_id = db.Column(db.Integer, primary_key=True, nullable=False, comment="id")
    registration_number = db.Column(db.String(32), comment="车牌号")
    car_model = db.Column(db.String(32), comment="车型")
    car_height = db.Column(db.Float, comment="车高")
    car_length = db.Column(db.Float, comment="车长")
    car_width = db.Column(db.Float, comment="车宽")
    hold_weight = db.Column(db.Float, comment="载重")
    hold_volume = db.Column(db.Float, comment="载量")
    driver_name = db.Column(db.String(32), comment="司机姓名")
    driver_phone = db.Column(db.String(32), comment="司机电话")
    driver_idcard = db.Column(db.String(32), comment="证件号")
    seal_number = db.Column(db.String(32), comment="封条号")
    in_time = db.Column(db.DateTime, comment="到达时间")
    out_time = db.Column(db.DateTime, comment="离开时间")