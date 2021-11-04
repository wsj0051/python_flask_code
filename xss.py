# coding:utf-8
from flask import Flask, request, url_for, render_template

# from flask_script import Manager

app = Flask(__name__)


# manager = Manager(app)


@app.route("/xss", methods=["GET", "POST"])
def xss():
    text = ""
    if request.method == "POST":
        text = request.form.get("text")
    return render_template("xss.html", text=text)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)
