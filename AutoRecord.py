# -*- coding: utf-8 -*-
from tkinter import *

import os
from time import sleep
import threading


def CMD(command):
    os.system(command)


def start(name):
    print('start recording')
    command = 'adb shell getevent | grep  -e " 0035 " -e " 0036 " > ' + name + '.txt'
    threading.Thread(target=CMD, args=[command]).start()


def stop():
    os.popen('adb shell "killall getevent"')
    print('stop recording')


def getKeyEvent(name):
    list = []
    with open(name + '.txt', 'r') as all:
        for line in all.readlines():
            if '0035' in line:
                x = int(line.strip().split(' ')[-1], 16)
            elif '0036' in line:
                y = int(line.strip().split(' ')[-1], 16)
                list.append(str(x) + ' ' + str(y))
            else:
                continue
    return list


def tap(tap):
    print('tap ' + tap)
    os.system('adb shell "input tap ' + tap + '"')


def startTest(name, times=1, count=1):
    keys = getKeyEvent(name)
    for i in range(int(count)):
        for key in keys:
            tap(key)
            sleep(int(times))
    print('测试完成')


def stoptest():
    exit(0)


class MainWindow:
    def __init__(self):
        self.frame = Tk()

        self.frame.title('UI脚本录制工具')
        self.frame.geometry('300x200')

        self.label_name1 = Label(self.frame, text="输入文件名:", padx=20)
        self.label_name1.grid(row=0, column=0)
        self.text_name1 = Text(self.frame, height="1", width=15)
        self.text_name1.grid(row=0, column=1)
        self.start_record = Button(self.frame, relief=RAISED, fg="blue", bd=7, text="Start Record", width=10,
                                   command=lambda: start(self.text_name1.get('0.0', 'end').strip()))
        self.stop_record = Button(self.frame, relief=RAISED, fg="blue", bd=7, text="Stop Record", width=10,
                                  command=stop)

        self.start_record.grid(row=1, column=0)
        self.stop_record.grid(row=1, column=1)

        self.label_name2 = Label(self.frame, text="运行文件名:")
        self.label_times = Label(self.frame, text="间隔时间:")
        self.label_count = Label(self.frame, text="循环次数:")
        self.label_log = Label(self.frame, text="log日志文件名:")

        self.label_name2.grid(row=4, column=0)
        self.label_times.grid(row=5, column=0)
        self.label_count.grid(row=6, column=0)
        self.label_log.grid(row=7, column=0)

        self.text_name2 = Text(self.frame, height="1", width=15)
        self.text_times = Text(self.frame, height="1", width=15)
        self.text_count = Text(self.frame, height="1", width=15)
        self.text_log = Text(self.frame, height="1", width=15)

        self.text_name2.grid(row=4, column=1)
        self.text_times.grid(row=5, column=1)
        self.text_count.grid(row=6, column=1)
        self.text_log.grid(row=7, column=1)
        print(self.text_name1.get('0.0', 'end').strip())
        self.start_test = Button(self.frame, relief=RAISED, fg="blue", bd=7, text="start test", width=10,
                                 command=lambda: startTest(self.text_name2.get('0.0', 'end').strip(),
                                                           self.text_times.get('0.0', 'end').strip(),
                                                           self.text_count.get('0.0', 'end').strip()))
        self.stop_test = Button(self.frame, relief=RAISED, fg="blue", bd=7, text="stop test", width=10,
                                command=stoptest)

        self.start_test.grid(row=8, column=0)
        self.stop_test.grid(row=8, column=1)

        self.frame.mainloop()


frame = MainWindow()
