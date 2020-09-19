import zipfile

import adbutils as adb

from UIconfig.pyserial import pyserial as pyser
import ctypes
import inspect
import os
import shlex
import subprocess
import threading
import shutil
import time
import csv


class adbtool():

    def __init__(self):
        self.CMD_GET_PROP = 'adb shell getprop '
        self.CMD_CLEAN_LOGCAT = 'adb shell logcat -b all -c'
        self.CMD_LOGCAT = 'adb shell logcat -v time > log/logcat.txt'
        self.CMD_ADB_REMOUNT = 'adb remount'
        self.CMD_ADB_ROOT = 'adb root'
        self.CMD_GET_LOGCAT_THREAD = 'adb shell killall logcat'
        self.CMD_GET_DEVICEID = 'adb shell settings get secure android_id'
        self.CMD_CHECK_WIFI = 'adb shell ip -f inet addr show wlan0'
        self.CMD_CHECK_BT = 'adb shell dumpsys bluetooth_manager'
        self.CMD_GET_SCREEN = 'adb shell screencap -p /sdcard/screencap.png'
        self.CMD_HANG_UP_PHONE = 'adb shell service call phone 3 '
        self.CMD_ALLPACKAGE = "adb shell pm list packages"
        self.CMD_ADB_SCREENCAP = 'adb shell screencap -p /sdcard/crash.png'
        self.CMD_GET_VERSION = 'adb shell pm dump '
        self.CMD_DEL_ANR_TOM = 'adb shell "rm -rf /data/anr/* && rm -rf /data/tombstones/*"'
        self.CMD_PULL_TOM = 'adb pull /data/tombstones '
        self.CMD_PULL_ANR = 'adb pull /data/anr '
        self.host2device = 'start host2device'
        self.device2host = 'start device2host'
        self.enter = '\r'
        self.sudo = 'su root'
        self.path = "./log/monkey/perform/"
        if not os.path.exists(self.path):
            os.makedirs(self.path)
        try:
            self.device = adb.AdbClient().device_list()[0]
        except:
            pass

    def setAndroidDate(self):
        dates = time.strftime("%m%d%H%M%Y.%S", time.localtime())
        try:
            self.callCMD('adb shell date ' + dates)
        except:
            pass

    def pull_ANR(self):
        if not os.path.exists('./log/monkey/logcat/anr'):
            os.makedirs('./log/monkey/logcat/anr')
        try:
            os.system(self.CMD_PULL_ANR + ' ./log/monkey/logcat/anr')
            os.system(self.CMD_PULL_TOM + ' ./log/monkey/logcat/anr')
        except:
            pass
        self.zip_dir_path('./log/monkey/logcat/anr')

    def openAdb(self):
        """
        通过串口打开设备ADB模式，前提设备连接串口
        :return:
        """
        seri = pyser()
        port_list = seri.GetPortList()
        flag = False
        if len(port_list) == 0:
            print('无可用串口')
        else:
            for i in port_list:
                if str(i).lower().__contains__('usb'):
                    perserial = str(i).split(" ")[0]
                    try:
                        ser, ret = seri.DOpenPort(perserial, 115200, timeout=100)
                        if ret:
                            seri.DWritePort(ser, (self.sudo + self.enter))
                            time.sleep(1)
                            seri.DWritePort(ser, (self.host2device + self.enter))
                            time.sleep(1)
                            seri.DWritePort(ser, (self.device2host + self.enter))
                            time.sleep(1)
                            seri.DWritePort(ser, (self.host2device + self.enter))
                            time.sleep(1)
                            seri.DColsePort(ser)
                            flag = True
                    except Exception as e:
                        flag = False
                        print(i + "---串口打开异常---：", e)
                        continue
            return flag

    def devices(self):
        """
        获取已连接设备列表
        :return:
        """
        deviceList = adb.AdbClient().device_list()
        return deviceList

    def callCMD(self, command):
        """
        执行指令
        :param command:
        :return:
        """
        '''执行command命令'''
        return os.popen(command)

    def stopThread(self, tids, exctype=SystemExit):
        """
        根据进程ID，强制关闭进程
        :param tid:
        :param exctype:
        :return:
        """
        """raises the exception, performs cleanup if needed"""
        tid = ctypes.c_long(tids)
        if not inspect.isclass(exctype):
            exctype = type(exctype)
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
        if res == 0:
            print("invalid thread id " + str(tids))
            # raise ValueError("invalid thread id")
        elif res != 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
            raise SystemError("PyThreadState_SetAsyncExc failed")

    def startLogcatThread(self):
        """
        启动logcat进程
        :return:
        """
        try:
            self.callCMD(self.CMD_CLEAN_LOGCAT)
            '''启动线程同步获取log'''
            log = threading.Thread(target=self.callCMD, args=([self.CMD_LOGCAT]))
            log.start()
            return log.ident
        except Exception as e:
            print(str(e))
            print('logcat抓取线程启动失败。')
            pass

    #
    def stopLogcatThread(self, mode, caseId, times):
        """
        通过杀死killall logcat，停止logcat进程
        :param mode:
        :param caseId:
        :param times:
        :return:
        """
        '''停止logcat线程'''
        try:
            os.system(self.CMD_GET_LOGCAT_THREAD)
            logpath = 'log/' + mode + '/logcat/'
            if not os.path.exists(logpath):
                os.makedirs(logpath)
            shutil.move('log/logcat.txt', logpath + caseId + '_' + times + '.txt')
        except Exception as e:
            print(str(e))
            print('logcat 抓取失败。')
            pass

    def checkConnectDevcie(self):
        """
        检查设备是否连接成功
        :return: Bool
        """
        for i in range(4):
            devices = adb.AdbClient().device_list()
            if len(devices) == 0:
                print("设备未连接成功!")
                time.sleep(2)
                continue
            else:
                print("设备连接成功!")
                return True
        return False

    def listPackages(self):
        """
        读取系统的应用包名列表
        :return:
        """
        return self.device.list_packages()

    def getPkgVersion(self, package):
        """
        根具包名获取应用的版本号
        :param package:
        :return:
        """
        return self.device.shell('pm dump ' + package + '| grep versionName').split("=")[1]

    def getAvnVersion(self):
        """
        获取系统版本号
        :return:
        """
        try:
            # 大通项目 版本号标识
            versionInfo = self.device.getprop('ro.build.display.id')
            if versionInfo.startswith('SW') or versionInfo.startswith('DB'):
                return versionInfo
            else:
                # 南京延峰项目 版本标识
                versionInfo = self.device.getprop('ro.build.mt2712.version')
                return versionInfo
        except:
            return ''

    def screenCap(self):
        """
        截屏
        :return:
        """
        os.system(self.CMD_ADB_SCREENCAP)

    def minitorLog(self, model):
        """
        实时监控logcat中的ANR、CRASH、Fatal，并截图
        :param model:
        :return:
        """
        keyword_ANR = 'ANR'
        keyword_CRASH = 'CRASH'
        keyword_Exception = 'Fatal'
        crashScreenPath = 'log/' + model + '/crash/'
        if not os.path.exists(crashScreenPath):
            os.makedirs(crashScreenPath)
        ps = subprocess.Popen('adb shell logcat -v time', stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                              shell=True)
        while True:
            try:
                line = str(ps.stdout.readline().strip())
            except:
                continue
            if line:
                Time = time.strftime("%Y%m%d%H%M", time.localtime())
                if keyword_ANR in line or keyword_CRASH in line or keyword_Exception in line:
                    self.screenCap()
                    os.system('adb pull /sdcard/crash.png ' + crashScreenPath + Time + '.png')
            else:
                break

    def screenthread(self, model):
        """
        启动实时监控线程
        :param model:
        :return:
        """
        threading.Thread(target=self.minitorLog, args=[model, ]).start()

    def get_CPU(self, package, times):
        fileName = self.path + package.split('.')[-1] + "_topInfo_" + times + '.csv'
        f = open(fileName, 'a+', encoding='utf-8')
        csv_writer = csv.writer(f)
        csv_writer.writerow(["Time", "PID", "%CPU", "%MEM", "COMMAND"])
        try:
            while True:
                info = self.device.shell('top -n 1 -o PID -o %CPU -o %MEM -o ARGS -s 2 | grep ' + package + ' ')
                infos = info.split('\r\n')
                if len(infos) > 1:
                    for i in infos:
                        if ('grep' in i) or ('sh' in i):
                            pass
                        else:
                            csv_writer.writerow(
                                [time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime()), i.split()[0], i.split()[1],
                                 i.split()[2], i.split()[3]])
                            f.flush()
        except Exception as e:
            print(e)

    # 获取cpu、mem占用
    def top(self, times, mode='monkey'):
        fileName = "./log/" + mode + "/perform/"
        if not os.path.exists(fileName):
            os.makedirs(fileName)
        f = open(fileName + "system_topInfo_" + times + '.csv', 'a+', encoding='utf-8')
        csv_writer = csv.writer(f)
        csv_writer.writerow(["Time", "TotalCpu", "UserCPU", "NiceCPU", "SysCPU", "TotalMem", "UsedMem", "FreeMem"])
        try:
            while True:
                top_info = self.device.shell("top -n 1 -o PID -o %CPU -o %MEM -o ARGS -s 2 | grep -e Mem -e %cpu")
                top_mem_info = str(top_info).split("\r\n")[0]
                top_cpu_info = str(top_info).split("\r\n")[1]
                TotalCpu = top_cpu_info.split()[0].replace("%cpu", "")
                UserCPU = top_cpu_info.split()[1].replace("%user", "")
                NiceCPU = top_cpu_info.split()[2].replace("%nice", "")
                SysCPU = top_cpu_info.split()[3].replace("%sys", "")
                TotalMem = top_mem_info.split()[1].replace("k", "")
                UsedMem = top_mem_info.split()[3].replace("k", "")
                FreeMem = top_mem_info.split()[5].replace("k", "")
                csv_writer.writerow(
                    [time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime()), TotalCpu, UserCPU, NiceCPU, SysCPU, TotalMem,
                     UsedMem, FreeMem])
                f.flush()
        except Exception as e:
            print(e)

    def zip_file_path(self, files):
        zip_name = files.replace('.txt', '.zip')
        print(zip_name)
        anr = './log/monkey/logcat/anr.zip'
        print(zip_name.split('/')[-1])
        zp = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)
        for file in [files, anr]:
            zp.write(file)
        zp.close()
        time.sleep(3)
        return zip_name

    def zip_dir_path(self, startdir):
        # 压缩后文件夹的名字
        zip_name = startdir + '.zip'
        # 参数一：文件夹名
        z = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)
        for dirpath, dirnames, filenames in os.walk(startdir):
            # 不replace的话，就从根目录开始复制
            fpath = dirpath.replace(startdir, '')
            # 实现当前文件夹以及包含的所有文件的压缩
            fpath = fpath and fpath + os.sep or ''
            for filename in filenames:
                z.write(os.path.join(dirpath, filename), fpath + filename)
                print('压缩成功')
        z.close()
        return zip_name
#
# if __name__ == "__main__":
#     CPU = threading.Thread(target=adbtool().top, args=['123414', 'com.saicmotor.radio'])
#     CPU.start()
#     time.sleep(10)
# print(adbtool().openAdb())
# for i in range(5):
#     id = adbtool().startLogcatThread()
#     time.sleep(20)
#     print(i)
#     adbtool().stopLogcatThread('ui', str(i), 'local')
