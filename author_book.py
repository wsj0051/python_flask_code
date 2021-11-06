# coding:utf-8
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)


class Config(object):
    """配置参数"""
    # sqlalchemy的配置参数
    SQLALCHEMY_DATABASE_URI = "mysql://root:123456@127.0.0.1:3306/author_book_py"
    # 设置sqlalchemy自动跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = "lldsfjsldfk"


app.config.from_object(Config)

# 创建数据库sqlalchemy工具对象
db = SQLAlchemy(app)
# 创建flask脚本管理工具对象
manager = Manager(app=app)
# 创建数据库迁移工具对象
Migrate(app, db)
# 向Manyr对象中添加数据库操作命令
manager.add_command("db", MigrateCommand)


# ihome -> ih_user 数据库名缩写_表名
# tbl_user tbl_表名
# 创建数据库模型类
class Author(db.Model):
    """作者"""
    __tablename__ = "tbl_authors"
    id = db.Column(db.Integer, primary_key=True)  # 整型的主键会默认自增
    name = db.Column(db.String(32), unique=True)
    books = db.relationship("Book", backref="author")
    email = db.Column(db.String(64))
    mobile = db.Column(db.String(64))

    def __repr__(self):
        """定义之后，可以让对象显示的更直观"""
        return "Author Object: name=%s" % self.name


class Book(db.Model):
    """书籍"""
    __tablename__ = "tbl_books"
    id = db.Column(db.Integer, primary_key=True)  # 整型的主键会默认自增
    name = db.Column(db.String(64), unique=True)
    author_id = db.Column(db.Integer, db.ForeignKey("tbl_authors.id"))

    def __repr__(self):
        """定义之后，可以让对象显示的更直观"""
        return "Book Object: name=%s" % self.name


# 表单模型类
class AuthorBookForm(FlaskForm):
    """作者数据表单模型类"""
    author_name = StringField(label="作者", validators=[DataRequired("作者必填")])
    book_name = StringField(label="书籍", validators=[DataRequired("书籍必填")])
    submit = SubmitField(label="保存")


@app.route("/", methods=["GET", "POST"])
def index():
    form = AuthorBookForm()
    if form.validate_on_submit():
        # 验证成功，保存书籍
        author_name = form.author_name.data
        book_name = form.book_name.data
        author = Author.query.filter_by(name=author_name).first()
        if author:
            book = Book.query.filter_by(name=book_name).first()
            if book:
                print("已存在相同书籍")
            else:
                try:
                    book = Book(name=book_name, author=author)
                    db.session.add(book)
                    db.session.commit()
                except Exception as e:
                    print(e)
                    print("添加书籍失败")
                    db.session.rollback()
        else:
            try:
                author = Author(name=author_name)
                db.session.add(author)
                db.session.commit()
                book = Book(name=book_name, author=author)
                db.session.add(book)
                db.session.commit()
            except Exception as e:
                print(e)
                print("添加作者或书籍失败")
                db.session.rollback()

    # 查询数据库
    authors = Author.query.all()
    return render_template("author_book.html", authors=authors, form=form)


@app.route("/delete_book_post", methods=["POST"])
def delete_book_post():
    # 如果定义前端发送的是json格式
    req_dict = request.get_json()
    book_id = req_dict.get("book_id")
    # 删除书籍
    book = Book.query.get(book_id)
    db.session.delete(book)
    db.session.commit()
    return jsonify(code=0, message="删除成功")


@app.route("/delete_book_get", methods=["GET"])
def delete_book_get():
    book_id = request.args.get("book_id")
    # 删除书籍
    book = Book.query.get(book_id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("index"))


if __name__ == "__main__":
    # 通过manager启动程序
    manager.run()
    # app.run(debug=True)
    # 清除数据库所有数据
    # db.drop_all()
    # # 创建所有表
    # db.create_all()
    # # 创建对象
    # au_san = Author(name="唐家三少")
    # db.session.add(au_san)
    # db.session.commit()
    # # session记录对象任务
    # au_tian = Author(name="天蚕土豆")
    # db.session.add(au_tian)
    # db.session.commit()
    #
    # bk_guang = Book(name="光之子", author_id=au_san.id)
    # bk_bing = Book(name="冰火魔厨", author_id=au_san.id)
    # bk_dou = Book(name="斗罗大陆", author_id=au_san.id)
    # bk_po = Book(name="斗破苍穹", author_id=au_tian.id)
    # bk_yuan = Book(name="元尊", author_id=au_tian.id)
    # # 一次保存多条数据
    # db.session.add_all([bk_guang, bk_bing, bk_dou, bk_po, bk_yuan])
    # db.session.commit()
