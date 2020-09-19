import sys
import threading
import time

from Pconfig.PCANBasic import *


class Pcan():

    def __init__(self):
        self.m_objPCANBasic = PCANBasic()
        self.initDriver()

    def readDate(self, file):
        data = open('Pconfig/' + file + '.txt')
        datas = data.readlines()
        if '\n' in datas:
            datas.remove('\n')
        elif 'ID:Data:Times:Duration(ms)\n' in datas:
            datas.remove('ID:Data:Times:Duration(ms)\n')
        return datas

    def initDriver(self):
        result = self.m_objPCANBasic.Initialize(c_ubyte(81), c_ushort(28), c_ubyte(1), 256, 3)
        if result != PCAN_ERROR_OK:
            print("Init Pcan Drive Error")
            # sys.exit(0)
        else:
            return result

    def uninitDriver(self):
        code = self.m_objPCANBasic.Uninitialize(c_ubyte(81))
        return code

    def sendMessag(self, id, data, times, duration):
        ONCANMsg = TPCANMsg()
        ONCANMsg.ID = int(id, 16)
        ONCANMsg.LEN = len(data)
        ONCANMsg.MSGTYPE = c_ubyte(0)
        duration = float(int(duration) / 1000)
        if times == '\n' or times == '' or times == " ":
            times = '999999999999999999999999999999'
        for i in range(len(data)):
            ONCANMsg.DATA[i] = int(data[i], 16)
        for i in range(int(times)):
            result = self.m_objPCANBasic.Write(c_ubyte(81), ONCANMsg)
            time.sleep(duration)
            if result == PCAN_ERROR_OK:
                print(str(data) + " send successful!")
            # else:
            #     print(str(data) + " send Error!")

    def write(self, canfile, cycle):
        """
        can信号发送
        :param canfile:   写好can信号的文件名，该文件应该在Pconfig目录下
        :param cycle:     是否同时发送这些信号  true：同时发， false：按顺序发送
        :return:    无返回值
        """
        can = Pcan()
        data = can.readDate(canfile)
        for i in range(0, len(data)):
            if data[i].startswith('sleep') and cycle.lower() == 'false':
                time.sleep(int(data[i].split(":")[1]))
            elif data[i].startswith('sleep') and cycle.lower() == 'true':
                continue
            else:
                canData = data[i].strip('\n').split(":")
                id = canData[0]
                datas = canData[1].split(',')
                duration = float(int(canData[3]) / 1000)
                try:
                    times = canData[2]
                except:
                    times = ''
                if cycle.lower() == 'true':
                    t = threading.Thread(target=can.sendMessag, args=(id, datas, times.strip(), duration,))
                    t.start()
                else:
                    can.sendMessag(id, datas, times.strip(), duration)
        if cycle.lower() == 'false':
            can.uninitDriver()


if __name__ == "__main__":
    file = sys.argv[1]
    cycle = sys.argv[2]
    Pcan().write(file, cycle)
