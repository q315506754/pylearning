import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'marketing@zhishish.com'
# sender = 'from@runoob.com'
receivers = ['jiangli@zhishish.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message = MIMEText('邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header("from测试", 'utf-8')   # 发送者
message['To'] =  Header("to测试", 'utf-8')        # 接收者

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')


try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect('smtp.exmail.qq.com', 25)    # 25 为 SMTP 端口号
    # smtpObj.login('315506754@qq.com','Jl19905237151')
    smtpObj.login('marketing@zhishish.com','Jin123')
    smtpObj.sendmail(sender, receivers, message.as_string())
    print ("邮件发送成功")
except smtplib.SMTPException as e:
    # e.with_traceback()
    print( "Error: 无法发送邮件 %s" % e)
    # print(b'\xc7\xeb\xca\xb9\xd3\xc3\xca\xda\xc8\xa8\xc2\xeb\xb5\xc7\xc2\xbc\xa1\xa3\xcf\xea\xc7\xe9\xc7\xeb\xbf\xb4'.decode("utf-8"))