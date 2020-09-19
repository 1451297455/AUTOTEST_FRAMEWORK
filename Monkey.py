import os, sys
import time, threading
import unittest
from shutil import copyfile
import UIconfig.adbTool as tool
from Mconfig import HTMLTestRunnerCN
from Mconfig.configparserHandler import Createxmlfile
from Mconfig.htmlParser import htmlParser
import CreatBug


class monkeyTest(unittest.TestCase):

    def setUp(self) -> None:
        if not adb.checkConnectDevcie():
            self.assertTrue(False)
        self.startTime = time.strftime("%Y%m%d%H%M", time.localtime())
        print(' monkey started at :' + self.startTime)
        adb.screenthread('monkey')

    def analysisLog(self, file, monkeylog):
        print("***********logfile:log/monkey/logcat/" + file + "***********")
        print('')
        module = file.split("_")[0]
        print('***************开始分析Monkey日志******************')
        if not os.path.exists(monkeylog):
            print('monkeylog 文件' + monkeylog + 'monkeylog不存在！ ')
            return False
        text = open(monkeylog, 'r').read()
        if str(text).strip().endswith('Monkey finished'):
            print('            monkey 执行正常！         ')
            print('')
            print('            分析结果如下：         ')
        else:
            print('    Monkey执行异常中断，请重新执行Monkey脚本!           ')
            print('')
        if not os.path.exists('log/monkey/logcat/' + file):
            print('logcat 文件' + file + '不存在！')
            return False
        text = open('log/monkey/logcat/' + file, 'r', errors='ignore')
        flag = 0
        while True:
            line = text.readline().strip()
            if line:
                if ' ANR ' in line and module in line:
                    print("****************ANR*******************")
                    print(line)
                    print(text.readline(), end='')
                    print('')
                    flag = 1
                    continue
                elif 'CRASH' in line and module in line:
                    print("***************CRASH******************")
                    print(line)
                    print(text.readline(), end='')
                    print('')
                    flag = 1
                    continue
                elif 'Fatal' in line and module in line:
                    print("*************Exception****************")
                    print(line)
                    print(text.readline(), end='')
                    print('')
                    flag = 1
                    continue
                else:
                    continue
            else:
                break
        return flag == 0

    def fun(self, package, duration, times):
        adb.startLogcatThread()
        self.CpuThread = threading.Thread(target=adb.get_CPU, args=[package, self.startTime, ])
        self.CpuThread.start()
        monkeylog = self.monkeyTest(package, duration, times, self.startTime)
        caseID = str(package).split('.')[-1]
        adb.stopLogcatThread('monkey', caseID, self.startTime)
        self.assertTrue(self.analysisLog(caseID + '_' + self.startTime + '.txt', monkeylog))

    @staticmethod
    def runTest(package, duration, times, ):
        def Func(self):
            self.fun(package, duration, times, )

        return Func

    def monkeyTest(self, package, duration, times, startTime):
        CMD_MONKEY = 'adb shell " monkey -p ' + package.strip() + " -v -v -v -s 500 --ignore-crashes --ignore-timeouts --ignore-security-exceptions --kill-process-after-error --pct-trackball 0 --pct-nav 0 --pct-syskeys 0  --pct-anyevent 0 --pct-flip 0  --throttle " + duration + " " + times + ' > /sdcard/Monkey.log"'
        CMD_PULL_LOG = 'adb pull /sdcard/Monkey.log  log/monkey/monkeylog/' + startTime + '.log'
        logPath = 'log/monkey/monkeylog/'
        version = adb.getPkgVersion(package.strip())
        print('packageName=' + package.strip() + ' version=' + version)
        if not os.path.exists(logPath):
            os.makedirs(logPath)
        os.system(CMD_MONKEY)
        os.system(CMD_PULL_LOG)
        return logPath + startTime + '.log'

    def tearDown(self):
        adb.stopThread(self.CpuThread.ident)


def setCase(file, duration, times):
    packages = open('Mconfig/' + file + '.txt').readlines()
    syspackages = adb.listPackages()
    for package in packages:
        if '#' in package.strip():
            pass  # 白名单中带#号不处理
        else:
            if package.strip() in syspackages:
                setattr(monkeyTest, 'test_monkey_%s' % (package.strip().split('.')[-1]),
                        monkeyTest.runTest(package.strip(), duration, times))
            else:
                print(package + ' 不存在！')
                continue


if __name__ == '__main__':
    '''
    参数1：  要跑的应用包名
    参数2：  每次点击间隔时长
    参数3：  白名单文件名
    参数4：  运行时长，单位h
    '''
    adb = tool.adbtool()
    if not adb.checkConnectDevcie():
        print("请连接设备驱动。。。。")
        sys.exit(0)
    else:
        adb.callCMD(adb.CMD_ADB_ROOT)
        adb.callCMD(adb.CMD_DEL_ANR_TOM)
        adb.setAndroidDate()
        avnVersion = adb.getAvnVersion()
    try:
        # 白名单文件名
        whiteFile = sys.argv[1]
        if whiteFile == '' or whiteFile == None:
            print('whitePackage 未配置！')
            sys.exit(0)
    except:
        print('whitePackage 配置错误！')
        sys.exit(0)

    try:
        # 每次点击的间隔时间
        duration = sys.argv[2]
    except:
        duration = '1000'
    try:
        # 每个包运行次数
        times = sys.argv[3]
    except:
        times = '1000'

    setCase(whiteFile, duration, times)
    now = time.strftime("%Y%m%d_%H_%M_%S", time.localtime())
    test = unittest.TestLoader().loadTestsFromTestCase(monkeyTest)
    load = unittest.TestSuite(test)
    htmlParsers = htmlParser()
    Createxmlfile = Createxmlfile()
    report_temp_path = './Report/report.html'
    report_path = './Report/report_monkey_' + now + '.html'
    if not os.path.exists('Report'):
        os.makedirs('Report')
    print('report_temp_path : ' + report_temp_path)
    TopThread = threading.Thread(target=adb.top, args=[now, ])
    TopThread.start()
    fp = open(report_temp_path, "wb")
    runner = HTMLTestRunnerCN.HTMLTestReportCN(stream=fp, title="monkey测试报告", tester='Tester', project=whiteFile,
                                               version=avnVersion)
    runner.run(load)
    fp.close()
    adb.stopThread(TopThread.ident)
    copyfile(report_temp_path, report_path)
    adb.pull_ANR()
    filePath = './Report/monkey_' + now + 'xmlReport.ini'
    htmlParsers.traverseHtmlWriteToFile(report_path, filePath)
    Createxmlfile.createxmlfile(filePath)
    Createxmlfile.mywrite()
    Bug = CreatBug.CreateBug()
    Bug.CreateBug(report_path)
    os._exit(0)
