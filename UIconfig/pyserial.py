import re
import serial  # 导入模块
import serial.tools.list_ports
import serial.tools.list_ports


class pyserial():

    def __init__(self):
        self.STRGLO = ""  # 读取的数据
        self.BOOL = True  # 读取标志位

    def GetPortList(self):
        List = []
        port_list = list(serial.tools.list_ports.comports())
        if len(port_list) == 0:
            print('无可用串口')
        else:
            for i in port_list:
                if str(i).lower().__contains__('usb'):
                    List.append(i)
        return List

    # 读数代码本体实现
    def ReadData(self, ser):
        global STRGLO, BOOL
        # 循环接收数据，此为死循环，可用线程实现
        while BOOL:
            if ser.in_waiting:
                STRGLO = ser.read(ser.in_waiting).decode("gbk")
                print(STRGLO)

    # 打开串口
    # 端口，GNU / Linux上的/ dev / ttyUSB0 等 或 Windows上的 COM3 等
    # 波特率，标准值之一：50,75,110,134,150,200,300,600,1200,1800,2400,4800,9600,19200,38400,57600,115200
    # 超时设置,None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
    def DOpenPort(self, portx, bps, timeout):
        ret = False
        try:
            # 打开串口，并得到串口对象
            ser = serial.Serial(portx, bps, timeout=timeout)
            # 判断是否打开成功
            if (ser.is_open):
                ret = True
                # threading.Thread(target=ReadData, args=(ser,)).start()
        except Exception as e:
            ser = None
            print("---异常---：", e)
        return ser, ret

    # 关闭串口
    def DColsePort(self, ser):
        global BOOL
        BOOL = False
        ser.close()

    # 写数据
    def DWritePort(self, ser, text):
        result = ser.write(text.encode())
        while True:
            line = ser.readline()
            print(line)
            try:
                print(line.decode('utf-8'), end='')
            except:
                pass
            if not (re.search(b'OK', line)):
                break
        return line

    # 读数据
    def DReadPort(self):
        global STRGLO
        str = STRGLO
        STRGLO = ""  # 清空当次读取
        return str
