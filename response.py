# coding:utf-8

from flask import Flask, request, abort, Response, make_response

app = Flask(__name__)


@app.route("/index", methods=["GET"])
def index():
    # 使用元组，返回自定义的响应信息
    # 响应体，状态码，响应头
    # return "index page", 400, [("Itcast", "python"),("city", "beijing")]
    # return "index page", 666, {"itcast":"python", "city":"beijing"}
    # return "index page", "666 itcast status", {"itcast":"python", "city":"beijing"}
    # return "index page", "666 itcast status"
    # 使用make_response来构造响应信息
    resp = make_response("index page 2")
    resp.status = "999 itcast"  # 设置状态码
    resp.headers["city"] = "beijing"  # 设置响应头
    return resp


if __name__ == "__main__":
    app.run(debug=True)
