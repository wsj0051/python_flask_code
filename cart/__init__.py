# coding:utf-8
from flask import Blueprint

# 创建了一个蓝图
app_cart = Blueprint("app_cart", __name__, template_folder="templates")

# 在init执行的时候，把视图加载尽量
from .view import get_cart
