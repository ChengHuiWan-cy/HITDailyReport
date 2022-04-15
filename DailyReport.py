from random import random, uniform
from selenium import webdriver
import time
import smtplib
from selenium.webdriver.common.keys import Keys
from pathlib import Path
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.header import Header

stu_number = ['1234567890']  # 学号
stu_password = ['password']  # 密码
stu_name = 'name'  # 附件加上同学名字首写字母前缀，用以区分。不必须
sender = '12345678@qq.com'
receiver = '12345678@qq.com'
password_email = 'pgbffekxejqwebjc'
# 输入webdriver放置的路径
driver_url = r"A:\\MyEdgeDriver\\msedgedriver.exe"
driver = webdriver.Edge(executable_path=driver_url)
# 访问网址
url_login = "https://ids.hit.edu.cn/authserver/login?service=https%3A%2F%2Fxg.hit.edu.cn%2Fzhxy-xgzs%2Fcommon%2FcasLogin%3Fparams%3DL3hnX21vYmlsZS94c0hvbWU%3D"
driver.get(url_login)
# 最大化窗口
# driver.maximize_window()

# 学号定位
username = driver.find_element_by_xpath('//*[@id="username"]')
# username = driver.find_element('//*[@id="username"]')
# 输入学号
time.sleep(uniform(1, 2))
for i in range(len(stu_number)):
    username.send_keys(stu_number[i])
    time.sleep(uniform(1, 2))
print('**************************************************')
# 点击记住密码
driver.find_element_by_xpath('//*[@id="rememberMe"]').click()
# driver.find_element('//*[@id="rememberMe"]').click()
# 密码定位
password = driver.find_element_by_xpath('//*[@id="password"]')
# password = driver.find_element('//*[@id="password"]')
# 输入密码
for i in range(len(stu_password)):
    password.send_keys(stu_password[i])
    time.sleep(uniform(1, 2))
print('**************************************************')
password.send_keys(Keys.ENTER)  # 密码输入完毕，键入enter表示确认
time.sleep(1)
# 点击每日上报
dailyReport = driver.find_element_by_partial_link_text('每日上报').click()
time.sleep(1)
# 点击获取地理位置
driver.find_element_by_id('dtjwd').click()
time.sleep(3)
# 我已仔细阅读并同意
driver.find_element_by_xpath('//*[@id="mrsb"]/div[63]/label').click()
driver.find_element_by_xpath('//*[@id="mrsb"]/div[64]/label').click()
driver.find_element_by_xpath('//*[@id="mrsb"]/div[65]/label').click()
time.sleep(1)
# 点击提交
driver.find_element_by_xpath('//*[@id="tj_btn"]/span[1]').click()
# 截图存放在当前py文件所处位置下的image文件夹下面
fileName = u'.\\image'
# 获取当前时间
current_time = time.strftime(stu_name + "-20%y-%m-%d-%H-%M-%S",
                             time.localtime(time.time()))
# 截图名称
picture_location = fileName + '\\' + current_time + '.png'
# 如果image文件夹存在不做处理，否则新建image文件夹
if Path(fileName).is_dir():
    pass
else:
    Path(fileName).mkdir()
# 浏览器截图拍照，并且保存为事先设置好的png
driver.save_screenshot(picture_location)
time.sleep(2)
# 关闭浏览器
driver.quit()

# 邮件服务器
# mixed -- 混合型 alternative--文本混合 related--多媒体元素
message = MIMEMultipart('related')
# 邮件头信息
message['From'] = Header(sender)
message['To'] = Header(receiver)
message['Subject'] = Header('今日每日上报截图', 'utf-8')
# 开启发信服务，这里使用的是加密传输
# 正文-图片 通过html格式来放图片，可通过cid 编号实现上传多个图片
email_body = '''
<p>今日疫情已经上报，无需回复</p>
<p>\n\t上报截图如下：\n</p>
<p><img src='cid:image1'></p>
'''
message.attach(MIMEText(email_body, 'html', 'utf-8'))
# 获取图片
file = open(picture_location, 'rb')
img = MIMEImage(file.read())
file.close()
img.add_header('Content-ID', '<image1>')
# 添加图片
message.attach(img)

# 选择用qq SMTP/IMTP发送
smtp_server = 'smtp.qq.com'
server = smtplib.SMTP_SSL(smtp_server)
# 465为SMTP端口号（绝大多数）
server.connect(smtp_server, 465)
# 用验证码登录qq邮箱
server.login(sender, password_email)
# 发送邮件
server.sendmail(sender, receiver, message.as_string())
# 关闭服务器
server.quit()
