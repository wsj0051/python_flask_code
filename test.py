# coding:utf-8

import unittest
from login import app
import json


class LoginTest(unittest.TestCase):
    """构造单元测试案例"""

    def setUp(self):
        self.client = app.test_client()
        # app.testing = True
        app.config["TESTING"] = True

    def test_empty_user_name_password(self):
        """测试用户名密码不完整的情况"""
        # 创建进行web请求的客户端，使用flask提供的
        # 利用client发送请求
        ret = self.client.post("/login", data={"password": "admin"})
        # ret是视图返回的响应对象
        resp = ret.data
        # login返回的是json
        resp = json.loads(resp)
        # 断言测试
        self.assertIn("code", resp)
        self.assertEqual(resp["code"], 0)
        ret = self.client.post("/login", data={"user_name": "admin"})
        # ret是视图返回的响应对象
        resp = ret.data
        # login返回的是json
        resp = json.loads(resp)
        # 断言测试
        self.assertIn("code", resp)
        self.assertEqual(resp["code"], 0)

    def test_wrong_user_name_password(self):
        ret = self.client.post("/login", data={"user_name": "addmin", "password": "admin"})
        resp = json.loads(ret.data)
        self.assertIn("code", resp)
        self.assertEqual(resp["code"], 2)


if __name__ == '__main__':
    unittest.main()
