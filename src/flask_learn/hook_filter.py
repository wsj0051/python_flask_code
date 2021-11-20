# coding:utf-8
from flask import Flask, request, url_for, render_template

# from flask_script import Manager

app = Flask(__name__)


# manager = Manager(app)


@app.route("/index")
def index():
    print("index 被执行")
    data = {
        "name": "wsj",
        "age": 18,
        "my_dict": {"city": "beijing"},
        "my_list": [1, 2, 3, 4]
    }
    return render_template("data.html", **data)


@app.before_first_request
def handle_before_first_request():
    print("handle_before_first_request 被執行")


@app.before_request
def handle_before_request():
    print("before_request 被執行")


@app.after_request
def handle_after_request(response):
    """在每次请求之后被执行，前提是试图函数没有异常"""
    print("after_request 被執行")
    return response


@app.teardown_request
def handle_teardown_request(response):
    """在每次请求之后被执行，无论是否出现异常，非debug模式生效"""
    print("handle_teardown_request被执行")
    path = request.path
    print(path)
    return response


@app.template_filter("li2")
def list_step_2(li):
    """自定义过滤器"""
    return li[::2]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)
