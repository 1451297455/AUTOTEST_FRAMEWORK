import os, sys
from argparse import ArgumentParser
from UIconfig import adbTool as tool
import logging

logger = logging.getLogger("UITest.htmlParser")
logger.setLevel(level=logging.INFO)
formatter = logging.Formatter('%(asctime)s %(name)s-%(levelname)s: %(message)s')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(formatter)
logger.addHandler(console)
''''''


def healthCheck():
    adb = tool.adbtool()
    if not adb.checkConnectDevcie():
        print("请连接设备驱动。。。。")
        sys.exit(0)
    else:
        devicelits = adb.devices()
        imfo = os.popen('adb root').read().strip()
        if imfo.__contains__('as root') or imfo.__contains__('already'):
            pass
        else:
            print('已连设备' + devicelits[0].serial + ',root权限不足！')
            sys.exit(0)
    return devicelits


if __name__ == '__main__':
    parse = ArgumentParser(usage='使用简介')

    # 需要运行的脚本名称
    parse.add_argument("-file", type=str, help='运行的脚本文件名，默认Run文件', default='UITest')

    # 执行语音脚本时传入的参数
    parse.add_argument("-project", type=str, help='执行的项目名称，D90、AS23、EP21', default='D90')
    parse.add_argument("-country", type=str, help='如果运行语音脚本，该参数默认为India，也可传参修改', default='India')
    parse.add_argument("-module", type=str, help='执行语音脚本时，需要测试的模块,'
                                                 '默认测试所有模块。call map   music   others radio vc'
                                                 'nowakeup  complex open_settings System '
                                                 '如果测试部分模块，请输入对应的数字组合。'
                                                 '比如：测试 map，则输入：map', default='all')
    # 执行Pcan脚本时传入的参数
    parse.add_argument("-pdata", type=str,
                       help='运行Pcan通信脚本时，需要传输的数据文件名，发送的数据都在文件中,该文件应该在Pconfig文件夹下的txt文件，只需传入文件名，不可为空')
    parse.add_argument("-cycle", type=str, help='是否同时发送can信号', default='true')

    # 执行性能脚本时传入的参数
    parse.add_argument("-pack", type=str, help='获取指定应用的包名,可以不指定包名，默认获取系统整机性能信息', default="System")
    parse.add_argument("-cpu", type=str, help='获取对应应用的CPU占比信息,默认true是获取，false时表示不获取', default="ture")
    parse.add_argument("-mem", type=str, help='获取对应应用的内存占比信息,默认true是获取，false时表示不获取', default="ture")

    #  执行UI自动化脚本传入的参数
    parse.add_argument("-driver", type=str, help="主测设备驱动号,不可为空", default='devices')
    parse.add_argument("-phone", type=str, help='辅助机设备驱动号，可为空，为空时默认不需要辅助机', default='')
    parse.add_argument("-case", type=str, help='输入要测试的项目类型，TestCase中会跟据各个项目存放不同的测试case，通过该参数来调用不同的case,默认参数为D90',
                       default="India_D90")
    # 执行monkey脚本传入的参数
    parse.add_argument("-whiteFile", type=str, help="执行monkey命令时涉及的白名单文件,非必须")
    parse.add_argument("-duration", type=str, help="monkey执行脚本时每次点击间隔时间,单位ms", default="1000")
    parse.add_argument("-times", type=str, help="moneky脚本执行总次数，默认1H，3600次", default='3600')

    # 执行性能脚本传入的参数
    parse.add_argument("-long", type=str, help="执行性能脚本的时长，默认值1000s", default='100')
    parse.add_argument("-package", type=str, help="需要获取性能信息的包名，默认值为all，即获取系统总体的性能信息", default="all")

    args = parse.parse_args()
    devices = healthCheck()

    if args.file == 'UITest':
        # Driver = args.driver
        # Phone = args.phone
        case = args.case
        if len(devices) == 0:
            print('请连接测试设备。')
            sys.exit(0)
        else:
            Driver = devices[0].serial
        os.system('python UITest.py ' + case)
    elif args.file == 'Voice':
        project = args.project
        country = args.country
        module = args.module
        os.system('python Voice.py ' + project + ' ' + country + ' ' + module)
    elif args.file == 'Pcan':
        data = args.pdata
        cycle = args.cycle
        if data is None:
            print('信号文件不可为空！')
            sys.exit(0)
        os.system('python Pcan.py ' + data + ' ' + cycle)
    elif args.file == 'Monkey':
        WhiteFile = args.whiteFile
        Duration = args.duration
        Times = args.times
        os.system('python Monkey.py ' + WhiteFile + " " + Duration + " " + Times)
    elif args.file == 'Perform':
        long = args.long
        packag = args.package
        os.system('python Perform.py ' + long + " " + packag)
    else:
        print('args [-file] is wrong!')
