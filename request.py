# coding:utf-8

from flask import Flask, request

app = Flask(__name__)


# 127.0.0.1:5000/index?city=beijing
@app.route("/index", methods=["GET", "POST"])
def index():
    # request包含了前端发送过来的所有请求数据
    # request.form可以直接提取请求体中的表单格式数据
    # form和data是用来提取请求体数据
    # 通过get只能拿到多个同名参数的第一个
    name = request.form.get("name")
    age = request.form.get("age")
    city = request.args.get("city")
    name_list = request.form.getlist("name")
    print("request data %s") % request.data
    print(name)
    if request.method == "GET":
        pass
    else:

        pass
    return "hello name=%s, age=%s, city=%s, name_list=%s" % (name, age, city, name_list)


@app.route("/upload", methods=["POST"])
def upload():
    """接收前端传送过来的文件"""
    file_obj = request.files.get("pic")
    if file_obj is None:
        # 表示没有发送文件
        return "未上传文件"
    # 将文件保存到本地
    # 1.创建一个文件
    # file = open("./demo.png", "wb")
    # # 2.向文件中写内容
    # data = file_obj.read()
    # file.write(data)
    # file.close()
    # 直接使用上传的文件保存
    # file_obj.save("./demo1.png")
    with open("./1.png", "wb") as f:
        f.write(file_obj.read())

    return "上传成功"


if __name__ == '__main__':
    app.run(debug=True)
