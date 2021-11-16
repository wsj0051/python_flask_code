# -*-coding:utf-8-*-
import socket
import time
import urllib.request
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import formataddr


def send_email(ip_address):  # 发送邮件
    print("ip地址是：%s" % ip_address)
    if ip_address is not None:
        mail_host = 'smtp.163.com'
        mail_pass = '密钥'
        mail_user = 'wsj0051@163.com'
        mail_port = 25  # 端口号
        receivers = 'wsj0051@qq.com'
        # 邮件内容
        message = MIMEText('当前ip地址是：%s' % ip_address, 'plain', 'utf-8')
        # message['From'] = Header("wsj0051", 'utf-8')  # 发送者
        # message['To'] = Header("test", 'utf-8')  # 接收者
        message['From'] = mail_user  # 发送者
        message['To'] = receivers  # 接受者
        # 设置邮件的主题
        send_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        subject = '邮件测试' + send_time
        message['Subject'] = Header(subject, 'utf-8')  # 邮件标题
        try:
            smtp_obj = smtplib.SMTP()
            smtp_obj.connect(mail_host, mail_port)  # 25 为 SMTP 端口号
            smtp_obj.login(mail_user, mail_pass)
            smtp_obj.sendmail(mail_user, receivers, message.as_string())
            print("邮件发送成功")
        except smtplib.SMTPException as e:
            print(e)
            print("Error: 无法发送邮件")


def check_network():  # 检测网络的连通性
    try_time = 10
    is_connected = False
    while try_time > 0:
        try:
            result = urllib.request.urlopen('https://baidu.com').read()
            print(result)
            print("Network is Ready!")
            is_connected = True
            break
        except Exception as e:
            print(e)
            print("Network is not ready,Sleep 5S...")
            is_connected = False
            try_time -= 1
            time.sleep(5)
    return is_connected


def get_ip(flag):  # 获取当前ip
    ip_address = None
    if flag is True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("1.1.1.1", 80))
            ip_address: object = s.getsockname()[0]
            s.close()
        except Exception as e:
            print(e)
    return ip_address


if __name__ == '__main__':
    send_email(get_ip(check_network()))
