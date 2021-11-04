# coding:utf-8
from flask import Flask, current_app, redirect, url_for
from werkzeug.routing import BaseConverter

app = Flask(__name__)


# class Config(object):
#     DEBUG = True
#     TEST = "Test"
#
#
# app.config.from_object(Config)


# 转换器http://127.0.0.1:5050/goods/123
# @app.route("/goods/<int:goods_id>")
@app.route("/goods/<goods_id>")
def goods_detail(goods_id):
    return "goods detail page %s" % goods_id


class MobileConverter(BaseConverter):
    def __init__(self, url_map):
        super(MobileConverter, self).__init__(url_map)
        self.regex = r'1[34578]\d{9}'


# 定义自己的转换器
class RegexConverter(BaseConverter):
    def __init__(self, url_map, regex):
        # 调用父类的初始化方法
        super(RegexConverter, self).__init__(url_map)
        # 将正则表达式的参数保存到对象的属性中，flask会使用这个属性来进行路由的正则匹配
        self.regex = regex

    def to_python(self, value):
        print("to_python被调用")
        return value

    def to_url(self, value):
        """使用url_for的时候被调用"""
        print("to_url被调用")
        return value


# 将自定义的转换器添加到Flask的应用中
app.url_map.converters["re"] = RegexConverter
app.url_map.converters["mobile"] = MobileConverter


@app.route("/send/<re(r'1[34578]\\d{9}'):mobile>")
def send_sms(mobile):
    return "send sms to %s" % mobile


@app.route("/index")
def index():
    url = url_for("send_sms", mobile="18912345678")
    return redirect(url)


@app.route("/send2/<mobile:mobile_num>")
def send_mobile(mobile_num):
    return "send mobile %s" % mobile_num


@app.route("/call/<re(r'[0][1-9]{2,3}-[0-9]{5,10}'):tel>")
def call_tel(tel):
    return "call tel %s" % tel


# 通过methods限定访问方式
@app.route("/post_only", methods=["GET", "POST"])
def post_only():
    return "post only page"


@app.route("/hello", methods=["POST"])
def hello():
    return "hello 1"


@app.route("/hello", methods=["GET"])
def hello2():
    return "hello 2"


@app.route("/hi1")
@app.route("/hi2")
def hi():
    return "hi page"


@app.route("/login")
def login():
    # 使用url_for函数，通过视图函数的名字找到对应的url路径
    url = url_for("index")
    return redirect(url)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # 通过url_map可以查看整个flask中的路由信息
    print(app.url_map)
    app.run(host="0.0.0.0", port=5050, debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
