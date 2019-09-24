# -*- coding:utf-8 -*-
from common.models import Base, db


class LocationModel(Base):
    """-config-
        货位表
    """
    __tablename__ = 'LOCATION'

    id = db.Column(db.Integer, primary_key=True, nullable=False, comment="id")
    revision = db.Column(db.Integer, nullable=False, default=0, server_default="0", comment="乐观锁")
    location_id = db.Column(db.String(32), nullable=False, default="", server_default="", comment="货位号")
    area_name = db.Column(db.String(32), nullable=False, default="", server_default="", comment="区域名")
    area_type = db.Column(db.String(32), nullable=False, default="", server_default="", comment="区域类型")
    location_describe = db.Column(db.String(512), nullable=False, default="", server_default="", comment="描述")