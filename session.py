# coding:utf-8
from flask import Flask, session

app = Flask(__name__)
# flask的session需要用到的密钥字符串
app.config["SECRET_KEY"] = "waralaf"


@app.route("/login")
def login():
    session["name"] = "python"
    session["mobile"] = "18233333333"
    return "login success"


@app.route("/index")
def index():
    name = session.get("name")
    return "hello %s" % name


if __name__ == "__main__":
    app.run(debug=True)
