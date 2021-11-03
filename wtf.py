# coding:utf-8
from flask import Flask, render_template, url_for, session, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

app = Flask(__name__)

app.config["SECRET_KEY"] = "dsflsdfslkdf"


class RegisterForm(FlaskForm):
    """自定义的注册表单模型类"""
    #                               名字              验证器
    # DataRequired必填
    user_name = StringField(label=u"用户名", validators=[DataRequired(u"用户名不能为空")])
    password = PasswordField(label=u"密码", validators=[DataRequired(u"密码不能为空")])
    re_password = PasswordField(label=u"确认密码", validators=[DataRequired(u"确认密码不能为空"),
                                                           EqualTo("password", u"两次密码不一致")])
    submit = SubmitField(label=u"提交")


@app.route("/register", methods=["GET", "POST"])
def register():
    # 创建表单对象
    form = RegisterForm()
    if form.validate_on_submit():
        user_name = form.user_name.data
        password = form.password.data
        re_password = form.re_password.data
        print(user_name, password, re_password)
        session["user_name"] = user_name
        return redirect(url_for("index"))
    return render_template("register.html", form=form)


@app.route("/index")
def index():
    user_name = session.get("user_name", "")
    return "hello %s" % user_name


if __name__ == "__main__":
    app.run(debug=True)
