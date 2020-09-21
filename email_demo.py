# smtplib 用于邮件的发信动作
import smtplib
from email.mime.text import MIMEText
# email 用于构建邮件内容
from email.header import Header
# 用于构建邮件头
# 发信方的信息：发信邮箱，QQ邮箱授权码）
from_addr = 'ch673@qq.com'
password = 'hfffbf'
# 收信方邮箱
to_addr = ['6329@qq.com','42570@qq.com']
# 发信服务器
smtp_server = 'smtp.qq.com'
name = input('input name')
guan = input('对方的称呼')
# 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
text = '''
hi,{}
我的 {}
'''.format(name,guan)
msg = MIMEText(text,'plain','utf-8')
# 邮件头信息
msg['From'] = Header('老诗')
# msg['To'] = Header('我滴大兄嘚')
msg['To'] = Header(",".join(to_addr))
msg['Subject'] = Header('hi boy')
# 开启发信服务，这里使用的是加密传输
server = smtplib.SMTP_SSL()
server.connect(smtp_server,465)
# 登录发信邮箱
server.login(from_addr, password)
# 发送邮件
server.sendmail(from_addr, to_addr, msg.as_string())
# 关闭服务器
server.quit()