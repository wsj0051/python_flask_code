# coding:utf-8
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/login", methods=["POST"])
def login():
    user_name = request.form.get("user_name")
    password = request.form.get("password")
    if not all([user_name, password]):
        return jsonify({"code": 0, "message": "invalid params"})
    if user_name == "admin" and password == "admin":
        return jsonify({"code": 1, "message": "login success"})
    else:
        return jsonify({"code": 2, "message": "用户名或密码错误"})


if __name__ == '__main__':
    app.run(debug=True)
