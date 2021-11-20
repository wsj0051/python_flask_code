# coding:utf-8
import unittest
from author_book import Author, db, app


class DatabaseTest(unittest.TestCase):
    def setUp(self):
        app.testing = True
        app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:123456@127.0.0.1:3306/flask_test"
        db.create_all()

    def test_add_author(self):
        author = Author(name="zhang", email="test@163.com", mobile="13333333333")
        db.session.add(author)
        db.session.commit()
        import time
        time.sleep(10)
        res = Author.query.filter_by(name="zhang").first()
        self.assertIsNotNone(res)

    def tearDown(self) -> None:
        """所有测试执行玩之后执行"""
        db.session.remove()
        db.drop_all()
