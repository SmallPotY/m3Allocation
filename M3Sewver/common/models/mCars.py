# -*- coding:utf-8 -*-
from common.models import Base, db


class CarsModel(Base):
    """-config-
        车辆表
    """
    __tablename__ = 'CARS'

    cars_id = db.Column(db.Integer, primary_key=True, nullable=False, comment="id")
    registration_number = db.Column(db.String(32), comment="车牌号")
    car_model = db.Column(db.String(32), comment="车型")
    car_height = db.Column(db.Float, comment="车高")
    car_Length = db.Column(db.Float, comment="车长")
    car_width = db.Column(db.Float, comment="车宽")
    hold_weight = db.Column(db.Float, comment="载重")
    hold_volume = db.Column(db.Float, comment="载量")
    default_drivers_id = db.Column(db.String(32), comment="默认司机")
    state = db.Column(db.String(32), comment="状态")