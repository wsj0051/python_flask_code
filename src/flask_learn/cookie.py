# coding:utf-8
from flask import Flask, make_response, request

app = Flask(__name__)


@app.route("/set_cookie")
def set_cookie():
    resp = make_response("success")
    resp.set_cookie("itcast", "python")
    # 设置有效期，单位秒
    resp.set_cookie("itcast1", "java", max_age=3600)
    resp.headers["Set-Cookie"] = "itcast3=python3; Expires=Sat, 30 Oct 2021 09:37:57 GMT; Max-Age=3600; Path=/"
    return resp


@app.route("/get_cookie")
def get_cookie():
    c = request.cookies.get("itcast3")
    resp = make_response("itcast3:%s" % c)

    return resp


@app.route("/delete_cookie")
def delete_cookie():
    resp = make_response("del success")
    resp.delete_cookie("itcast1")
    return resp


if __name__ == "__main__":
    app.run(debug=True)
