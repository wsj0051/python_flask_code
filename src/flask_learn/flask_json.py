# coding:utf-8
from flask import Flask, jsonify
import json

app = Flask(__name__)


@app.route("/index")
def index():
    # json就是字符串
    data = {
        "name": "python",
        "age": 18
    }
    # json_str = json.dumps(data)  # 将字典转换为json字符串，json.loads(字符串) 将字符串转换为json的字典
    # return json_str, 200, {"Content-Type": "application/json"}
    # jsonify帮助转换为json数据，并设置响应头为Content-Type:application/json
    # return jsonify(data)
    return jsonify(city="bj", country="china")


if __name__ == "__main__":
    app.run(debug=True)
