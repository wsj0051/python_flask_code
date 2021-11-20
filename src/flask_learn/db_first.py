# coding:utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


class Config(object):
    """配置参数"""
    # sqlalchemy的配置参数
    SQLALCHEMY_DATABASE_URI = "mysql://root:123456@127.0.0.1:3306/db_python04"
    # 设置sqlalchemy自动跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True


app.config.from_object(Config)

# 创建数据库sqlalchemy工具对象
db = SQLAlchemy(app)


# ihome -> ih_user 数据库名缩写_表名
# tbl_user tbl_表名
# 创建数据库模型类
class Role(db.Model):
    """用户角色表"""
    __tablename__ = "dp_roles"
    id = db.Column(db.Integer, primary_key=True)  # 整型的主键会默认自增
    name = db.Column(db.String(32), unique=True)
    users = db.relationship("User", backref="role")

    def __repr__(self):
        """定义之后，可以让对象显示的更直观"""
        return "Role Object: name=%s" % self.name


class User(db.Model):
    """用户表"""
    __tablename__ = "dp_users"
    id = db.Column(db.Integer, primary_key=True)  # 整型的主键会默认自增
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey("dp_roles.id"))

    def __repr__(self):
        """定义之后，可以让对象显示的更直观"""
        return "User Object: name=%s" % self.name


# @app.route("/")
# def index():
#     return "hello "


if __name__ == "__main__":
    # 清除数据库所有数据
    db.drop_all()
    # 创建所有表
    db.create_all()
    # 创建对象
    role1 = Role(name="admin")
    db.session.add(role1)
    db.session.commit()
    # session记录对象任务
    role2 = Role(name="stuff")
    db.session.add(role2)
    db.session.commit()

    us1 = User(name="Wang", email="wang@163.com", password="123456", role_id=role1.id)
    us2 = User(name="zhang", email="zhang@163.com", password="234567", role_id=role2.id)
    # 一次保存多条数据
    db.session.add_all([us1, us2])
    db.session.commit()
