# AVN_AUTOTEST_FRAMEWORK 
	1，安装atx
	pip3 install atx
	
	2，安装uiautomator2
	pip3 install --pre --upgrade uiautomator2
	
	3，初始化操作
	python3 -m uiautomator2 init
	
	4,启动捕捉工具
	python3 -m weditor


## 简单介绍

	python-uiautomator2是一个自动化测试开源工具，仅支持Android平台的原生应用测试。
	
## 支持平台及语言
	
	python-uiautomator2封装了谷歌自带的uiautomator2测试框架，提供便利的python接口。他允许测试人员直接在PC上编写Python的测试代码，操作手机应用，	完成自动化，大大提高了自动化代码编写的效率。
	
## 工作原理
	
	python-uiautomator2主要分为两个部分，python客户端，移动设备
	python端: 运行脚本，并向移动设备发送HTTP请求
	移动设备：移动设备上运行了封装了uiautomator2的HTTP服务，解析收到的请求，并转化成uiautomator2的代码。
	
##  整个过程
	
	在移动设备上安装atx-agent(守护进程), 随后atx-agent启动uiautomator2服务(默认7912端口)进行监听
	在PC上编写测试脚本并执行（相当于发送HTTP请求到移动设备的server端）
	移动设备通过WIFI或USB接收到PC上发来的HTTP请求，执行制定的操作
	
##  安装工具
	Python2或者Python3均可。(也可以尝试使用Android上Python客户端：QPython)


# 环境搭建
## 安装adb
	如命令行可以执行adb devices，则跳过此步骤
	从谷歌官网下载Android Platform Tools https://developer.android.com/studio/releases/platform-tools.html，解压，并加包含adb.exe的目录加入到系统的PATH中。
	
## 安装python-uiautomator2

	pip install --pre -U uiautomator2
	
## 设备安装atx-agent
	
	首先设备连接到PC，并能够adb devices发现该设备。
	从github下载atx-agent文件，并推送到手机。在手机上安装包名为`com.github.uiautomator`的apk
	$ python3 -m uiautomator2 init
	$ success
	最后提示success，代表atx-agent初始化成功。
	
## 应用及操作

	调用uiautomator2的过程
	配置手机设备参数，设置具体操作的是哪一台手机
	抓取手机上应用的控件，制定对应的控件来进行操作
	对抓取到的控件进行操作，比如点击、填写参数等。

## 配置手机设备参数

	python-uiautomator2连接手机的方式有两种，一种是通过WIFI，另外一种是通过USB。两种方法各有优缺点。
	WIFI最便利的地方要数可以不用连接数据线，USB则可以用在PC和手机网络不在一个网段用不了的情况。
		使用WIFI连接
	手机获取到手机的IP，并确保电脑可以PING通手机。手机的IP可以在设置-WIFI设置里面获取到。
	比如手机的IP是192.168.0.100，连接设备的代码为
	import uiautomator2 as u2
	d = u2.connect('192.168.0.100')
		使用USB连接
	手机的序列号可以通过adb devices获取到，假设序列号是123456f，连接代码为
	import uiautomator2 as u2
	d = u2.connect_usb('123456f')
		抓取手机上应用的控件
	虽然很想用Android SDK内置工具uiautomatorviewer.bat，但是运行uiautomator2的时候，uiautomatorviewer.bat运行不起来，两者之间冲突太严重。
	于是参考着uiautomatorviewer的界面，我又写了一个weditor，调用python-uiautomator2的两个接口screenshot和dump_hierarchy这样就不会有冲突问题了
	注：weditor依然处于开发期，功能可能会跟文中描述的有所不同
	安装方法: pip install --pre weditor
		使用方法: 
	首先运行python -m weditor，之后浏览器会自动打开一个网页 http://atx.open.netease.com （注：这个网址仅提供一个前端，而python -mweditor这个命令则本地开放了HTTP的接口，前端去跟本地的服务去通信）输入框中可以写设备的IP或者设备的Serial（序列号），跟上面提到的配置手机设备参数用法一致。之后点击Connect，如果一切正常就会出现一个绿色的叶子。页面刷新时，点击蓝色的Reload按钮重新刷新。

## 定位方式
	
	ResourceId定位: d(resourceId="com.smartisanos.clock:id/text_stopwatch").click()
	Text定位 d(text="秒表").click()
	Description定位 d(description="..").click()
	ClassName定位 d(className="android.widget.TextView").click()
	xpath定位并不支持，一开始打算做支持的，但是发现不用也能搞定。就是代码写的长一点而已。

## 操作控件
	click
	d(text="Settings").click()

	long click
	d(text="Settings").long_click()

	等待元素的出现
	d(text="Settings").wait(timeout=10.0)
	九宫格解锁：以前文章写过 https://testerhome.com/topics/11034
	中文字符的输入
	如果可以定位到元素，直接通过set_text就可以输入中文
	d(text="Settings").set_text("你好")
	如果定位不到元素需要使用send_keys方法，以及切换输入法
	d.set_fastinput_ime(True)
	d.send_keys("你好 Hello")
	d.set_fastinput_ime(False) # 输入法用完关掉
	截图：d.screenshot("home.jpg")
	获取图层信息：xml = d.dump_hierarchy()

## 滑动
	垂直滚动到页面顶部/横向滚动到最左侧
	d(scrollable=True).scroll.toBeginning()
	d(scrollable=True).scroll.horiz.toBeginning()
	垂直滚动到页面最底部/横向滚动到最右侧
	d(scrollable=True).scroll.toEnd()
	d(scrollable=True).scroll.horiz.toEnd()
	垂直向后滚动到指定位置/横向向右滚动到指定位置
	d(scrollable=True).scroll.to(description="指定位置")
	d(scrollable=True).scroll.horiz.to(description="指定位置")
	垂直向前滚动（横向同理）
	d(scrollable=True).scroll.forward()
	垂直向前滚动到指定位置（横向同理）
	d(scrollable=True).scroll.forward.to(description="指定位置")




## HTMLTestRunner修改成Python3版本
	
	修改前：HTMLTestRunner下载地址：http://tungwaiyip.info/software/HTMLTestRunner.html
			BSTestRunner     下载地址：https://github.com/easonhan007/HTMLTestRunner

	修改后：HTMLTestRunner下载地址：https://pan.baidu.com/s/1W6e_Bqg9dZTkVOWUP93XkA
			BSTestRunner     下载地址：https://pan.baidu.com/s/1nuJLWYdbq5ur8qoOSUq-8A
	修改方法：
	第94行，将import StringIO修改成import io
	第539行，将self.outputBuffer = StringIO.StringIO()修改成self.outputBuffer = io.StringIO()
	第642行，将if not rmap.has_key(cls):修改成if not cls in rmap:
	第766行，将uo = o.decode('latin-1')修改成uo = e
	第775行，将ue = e.decode('latin-1')修改成ue = e
	第631行，将print >> sys.stderr, '\nTime Elapsed: %s' % (self.stopTime-self.startTime)修改成print(sys.stderr, '\nTime Elapsed: %s' % (self.stopTime-self.startTime))





