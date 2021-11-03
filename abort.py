# coding:utf-8

from flask import Flask, request, abort, Response

app = Flask(__name__)


@app.route("/login", methods=["POST"])
def login():
    name = request.form.get("name")
    pwd = request.form.get("pwd")
    if name != "admin" or pwd != "admin":
        # 使用abort函数可以立即种植视图函数的执行
        # 并可以返回给前端特定的信息
        # 1.传递状态码，必须是标准的http状态码
        # abort(404)
        # 2.传递响应体信息
        resp = Response("login failed")
        abort(resp)
    return "login success"


# 定义错误处理方法
@app.errorhandler(404)
def handle_404_error(error):
    """自定义处理错误方法"""
    # 这个函数的返回值回事前端用户看到的最终结果
    return "出现了404错误， 错误信息：%s" % error


if __name__ == "__main__":
    app.run(debug=True)
