from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
# 配置邮件：服务器／端口／传输层安全协议／邮箱名／密码
app.config.update(
    DEBUG=True,
    MAIL_SERVER='smtp.qq.com',
    MAIL_PROT=465,
    MAIL_USE_TLS=True,
    # MAIL_USE_SSL=False,
    MAIL_USERNAME='wsj0051@qq.com',
    MAIL_PASSWORD='qq授权码',
)

mail = Mail(app)


@app.route('/')
def index():
    with mail.connect() as conn:
        subject = "test subject"
        message = "test message"
        # sender 发送方，recipients 接收方列表
        msg = Message(subject=subject, body=message, sender='wsj0051@qq.com',
                      recipients=['wsj0051@163.com'])
        # 发送邮件
        conn.send(msg)
        print("Mail sent")
    return "Sent　Succeed"


if __name__ == "__main__":
    app.run()
