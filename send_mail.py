import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import config

# 发送email
def send_mail():
    receive = config.receive
    image = config.project_dir + 'luckball.png'
    
    body = """
    <p>抱抱龙和笑笑龙给您送幸运号码啦！</p>
    <img src="cid:image1"/>   
    """
    msg = MIMEMultipart() 
    msg['Subject'] = 'LuckBall'
    msg.attach(MIMEText(body, 'html', 'utf-8'))
    # 二进制模式读取图片
    with open(image, 'rb') as f:
        msgImage = MIMEImage(f.read())
    # 定义图片ID
    msgImage.add_header('Content-ID', '<image1>')
    msg.attach(msgImage)

    # 连接到SMTP服务器
    smtpObj = smtplib.SMTP(config.smtp,25)
    smtpObj.ehlo()
    smtpObj.starttls()

    # 登录发送邮箱
    smtpObj.login(config.sendusername, config.sendpassword)

    # 发送
    smtpObj.sendmail(config.sendusername, receive, msg.as_string())

    # 从SMTP服务器断开
    smtpObj.quit()