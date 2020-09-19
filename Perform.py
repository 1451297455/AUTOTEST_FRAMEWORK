#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 需要安装pychartdir模块，http://blog.csdn.net/gb112211/article/details/43272049
import csv
import threading
import adbutils as adb
from pychartdir import *


class CPU:
    def __init__(self):
        self.path = "./Report/performance/"
        if not os.path.exists(self.path):
            os.makedirs(self.path)
        self.devices = adb.AdbClient().device_list()[0]

    def get_CPU(self, package):
        times = time.strftime("%Y%m%d%H%M%S", time.localtime())
        fileName = self.path + package.split('.')[-1] + "_topInfo_" + times + '.csv'
        f = open(fileName, 'a+', encoding='utf-8')
        csv_writer = csv.writer(f)
        csv_writer.writerow(["Time", "PID", "%CPU", "%MEM", "COMMAND"])
        while True:
            info = self.devices.shell('top -n 1 -o PID -o %CPU -o %MEM -o ARGS -s 2 | grep ' + package + ' ')
            infos = info.split('\r\n')
            if len(infos) > 1:
                for i in infos:
                    if 'grep' in i or 'sh' in i:
                        pass
                    else:
                        print(i.split())
                        csv_writer.writerow(
                            [time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime()), i.split()[0], i.split()[1],
                             i.split()[2], i.split()[3]])
                        f.flush()

    # 获取cpu、mem占用
    def top(self):
        times = time.strftime("%Y%m%d%H%M%S", time.localtime())
        fileName = self.path + "system_topInfo_" + times + '.csv'
        f = open(fileName, 'a+', encoding='utf-8')
        csv_writer = csv.writer(f)
        csv_writer.writerow(["Time", "TotalCpu", "UserCPU", "NiceCPU", "SysCPU", "TotalMem", "UsedMem", "FreeMem"])
        while True:
            top_info = self.devices.shell("top -n 1 -o PID -o %CPU -o %MEM -o ARGS -s 2 | grep -e Mem -e %cpu")
            top_mem_info = str(top_info).split("\r\n")[0]
            top_cpu_info = str(top_info).split("\r\n")[1]
            print(top_mem_info.split())
            print(top_cpu_info.split())
            TotalCpu = top_cpu_info.split()[0].replace("%cpu", "")
            UserCPU = top_cpu_info.split()[1].replace("%user", "")
            NiceCPU = top_cpu_info.split()[2].replace("%nice", "")
            SysCPU = top_cpu_info.split()[3].replace("%sys", "")
            TotalMem = top_mem_info.split()[1].replace("k", "")
            UsedMem = top_mem_info.split()[3].replace("k", "")
            FreeMem = top_mem_info.split()[5].replace("k", "")
            print('*************************')
            csv_writer.writerow(
                [time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime()), TotalCpu, UserCPU, NiceCPU, SysCPU, TotalMem,
                 UsedMem, FreeMem])
            f.flush()


if __name__ == "__main__":
    try:
        long = sys.argv[1]
    except:
        long = 100
    try:
        package = sys.argv[2]
    except:
        package = 'all'
    print("Starting get top information...")
    times = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())
    cpu = CPU()
    if not cpu.devices == "" and package != "all":
        threading.Thread(target=cpu.top).start()
        threading.Thread(target=cpu.get_CPU, args=[package, ]).start()
        time.sleep(int(long))
        os._exit(0)
    elif not cpu.devices == "" and package == "all":
        threading.Thread(target=cpu.top).start()
        time.sleep(int(long))
        os._exit(0)
    else:
        print('设备未连接。。。。。')
        os._exit(0)
