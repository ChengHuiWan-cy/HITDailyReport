# HITDailyReport 2.0
**哈工大每日上报+出校申请**  

## Version: 1.0
通过edge浏览器自动上报，并且将上报成功截图发送给自己的qq邮箱   

## Version: 2.0
### 更新内容
- 增加了出校申请功能
- 修复了一些卡住的bug
- 增加了一个日志记录文件,每日成功上报之后再次进入程序会提示并退出，可以选择是否出校申请，可以选择是否邮件提醒
- 完善配置说明，并且加入到readme文件中
- 删除了配置说明.pdf和.vscoede

# 配置说明
## 1.下载第三方库
	pip install selenium==4.0.0
这里需要注意的是，selenium的版本过高会影响程序运行
## 2.下载edge驱动文件:
注意查看edge版本（如果你使用的是edge beta或者dev，请仍然使用原版edge），下载对应版本的驱动器：
![1](./readmeAssets/1.png)
https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
这里选择edgediver x64版本

下载之后解压在任何位置皆可，记住解压之后的路径，后面要用

## 3.开启qq邮箱设置：

如果不想要发送邮件（发邮件主要为了告诉你已经成功每日上报，往往是把改任务设成了定时任务的时使用），可以跳过这一步

![2](./readmeAssets/2.png)

然后下拉

（如果这里默认是已开启，就关了重开一次）
![3](./readmeAssets/3.png)

按照要求发送短信，记住（复制一下）这个授权码

![4](./readmeAssets/4.png)

## 4.文件配置：
### 修改DaliyReport.py的14-21行

更改自己学工平台的学号和密码，以及qq邮箱

其中stu_name是提交成功截图命名的一部分，可随意更改。

password_email是qq邮箱开通SMTP之后的授权码（不是邮箱密码），driver_url是下载的驱动器的路径

```python
#需要修改
stu_number = ['1234567890']  # 学号
stu_password = ['password']  # 密码
stu_name = 'name'  # 你的姓名的拼音，仅用来命名截图，可以不改，这里不要用中文
sender = '12345678@qq.com' # 你的邮箱
receiver = '12345678@qq.com' # 你的邮箱
password_email = 'pgbffekxejqwebjc' #授权码
# 输入下载的edgedriver放置的路径，建议使用双斜杠
driver_url = r"A:\\MyEdgeDriver\\msedgedriver.exe"
Reason='吃饭' #出校申请的理由
```


### 修改dateRecorder.txt
```
2022-06-29
需要出校申请
需要发送邮件
```
其中第一行可以不改动，这里一般是由程序自动填写的它最后一次成功的每日上报的日期

如果该日期为今天程序会提示今日已上报并退出
如果需要重新上报可以改成昨天的日期

第二行填写“需要出校申请”/"不需要出校申请"

第三行填写“需要发送邮件”/"不需要发送邮件"

## 5. 每日自动上报、申请
### 1.打包
如果你的电脑对.py文件的默认打开方式是运行，那么可以不需要打包（一般都是打包比较好）

如果不是，可以使用pyinstaller工具

```
pip install pyinstaller
pyinstaller -F ./DailyReport.py
```
默认生成在从dist文件夹中，拖出来到和DailyReport.py同一个文件夹即可

![5](./readmeAssets/5.png)
### 2.自动运行
#### 这里可以设置开机自启动
将DailyReport.exe生成快捷方式

放入开机自启动的文件夹中即可

一般的路径为：C:\Users\【用户名】\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
#### 也可以定一个计划任务让它每天定时启动
具体可以百度“win10怎么设置定时任务”

# 关于疫苗记录

每日上报中昨天刚刚加入了疫苗记录，这里没有写自动填写功能。

第一次需要大家手动每日上报的时候填写一下，后面应当会保持不变。