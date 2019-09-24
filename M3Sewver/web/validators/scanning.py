# -*- coding:utf-8 -*-
from wtforms.validators import DataRequired

from web.validators import BaseForm
from wtforms import StringField, IntegerField, DateField


class InScanning(BaseForm):
    location_id = StringField(validators=[DataRequired(message='请输入货位号')])
    order_number = StringField(validators=[DataRequired(message='请输入订单号')])


class CheckLocationId(BaseForm):
    """检查货位ID"""
    location_id = StringField(validators=[DataRequired(message='请输入货位号')])


class CheckOrderNumber(BaseForm):
    """检查订单号"""
    order_number = StringField(validators=[DataRequired(message='请输入订单号')])
