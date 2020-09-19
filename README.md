# Introduction 
    ***使用简介***
    
    # 需要运行的脚本名称
     -file", type=str, help='运行的脚本文件名，可选 UITest、Voice、Monkey', default='UITest'
    # 执行语音脚本时传入的参数
     -project : type=str, help='执行的项目名称，D90、AS23、EP21', default='D90' 
     -country : type=str, help='如果运行语音脚本，该参数默认为India，也可传参修改', default='India' 
     -module : type=str, help='执行语音脚本时，需要测试的模块，   '
                                                 '默认测试所有模块。call map   music   others radio vc'
                                                 'nowakeup  complex open_settings System '
                                                 '如果测试部分模块，请输入对应的数字组合。'
                                                 '比如：测试 map，则输入：map', default='all')
    # 执行Pcan脚本时传入的参数
     -pdata : type=str,help='运行Pcan通信脚本时，需要传输的数据文件名，发送的数据都在文件中,该文件应该在Pconfig文件夹下的txt文件，只需传入文件名，不可为空')
     -cycle : type=str, help='是否同时发送can信号', default='true'

    # 执行性能脚本时传入的参数
     -pack : type=str, help='获取指定应用的包名,可以不指定包名，默认获取系统整机性能信息', default="System" 
     -cpu : type=str, help='获取对应应用的CPU占比信息,默认true是获取，false时表示不获取', default="ture" 
     -mem : type=str, help='获取对应应用的内存占比信息,默认true是获取，false时表示不获取', default="ture" 

    #  执行UI自动化脚本传入的参数
     -driver : type=str, help="主测设备驱动号,不可为空"，default="默认使用已连接设备的设备ID"
     -phone : type=str, help='辅助机设备驱动号，可为空，为空时默认不需要辅助机', default='' 
     -case : type=str, help='输入要测试的项目类型，TestCase中会跟据各个项目存放不同的测试case，通过该参数来调用不同的case,默认参数为D90',
                       default="India_D90" 
    # 执行monkey脚本传入的参数
     -whiteFile : type=str, help="执行monkey命令时涉及的白名单文件,非必须" 
     -duration: type=str, help="monkey执行脚本时每次点击间隔时间,单位ms", default="1000" 
     -times : type=str, help="moneky脚本执行总次数，默认1H，3600次", default='3600' 
    
    # 执行性能脚本传入的参数
    -long: type=str, help="执行性能脚本的时长，默认值1000s", default='100'
    -package: type=str, help="需要获取性能信息的包名，默认值为all，即获取系统总体的性能信息", default="all"

# Getting Started
    TODO: Guide users through getting your code up and running on their own system. In this section you can talk about:
    1.	安装python3环境；
    2.      安装pip库；运行'python libConfig/get-pip.py'， get-pip下载地址（https://github.com/yi3/get-pip/archive/master.zip）
    3.	安装项目依赖库requirements.txt；     执行'pip install -r requirements.txt' 安装依赖库


# Build and Test
    TODO: Describe and show how to build your code and run the tests. 
    运行流程：
    1，进入项目工作空间
    2，终端中运行： python Run.py -file 脚本名 -参数名 参数
    eg: python Run.py -file Monkey -whiteFile whitePack -duration 1000  -times 1000


# Install Pcan Driver
    TODO:
    安装流程：
    1，下载驱动后，解压到目录下。 [驱动](https://pan.baidu.com/s/1mm7aSMp7vscGmK5vXtfcyg)  
    2，进入安装包。  
        cd peak-linux-driver-x.x.x
    3，清空
        make clean
    4，构建
        make
    5，最终构建
        sudo make install
    6，重启激活即可   
     
    如果出现"popt.h not found"，那么请执行下面的指令安装libpopt­dev
        sudo apt­get install libpopt­dev