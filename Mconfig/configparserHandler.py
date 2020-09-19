# -*- coding: utf-8 -*-
# https://www.cnblogs.com/sea-stream/p/11861039.html
from configparser import ConfigParser
import os
import logging
import configparser
from xml.etree import ElementTree as ET
from xml.dom import minidom


# 创建管理对象
logger = logging.getLogger("UITest.configparserHandler")


class configparserHandler():
    def __init__(self, configFilePath):
        self.cf = ConfigParser()
        try:
            if configFilePath is None:
                raise FileNotFoundError("Can't found config file!")
            else:
                self.configFilePath = configFilePath
                self.cf.read(self.configFilePath, encoding="utf-8")
        except Exception as e:
            raise e

    # 添加索引[index]
    def add_section(self, section):
        self.cf.add_section(section)

    # 根据索引添加内容信息（key，value）
    def set_section(self, section, option, value):
        self.cf.set(section, option, value)

    # 保存写入内容
    def save(self):
        logger.info('11111' + self.configFilePath)
        fp = open(self.configFilePath, 'w',
                  encoding='utf-8')  # with open(self.configFilePath,"w+") as f:self.cf.write(f)
        self.cf.write(fp)
        fp.close()

class Createxmlfile():
    def __init__(self):
        self.root = None

    def createxmlfile(self, iniPath):
        conf = configparser.ConfigParser()  # 调用读取配置模块中的类
        conf.read(iniPath, encoding='utf-8')
        secList = conf.sections()  # 遍历Xml文件的根节点
        suitname = {}  # 定义一个空的集合用于存放suit数据
        totalcase = conf.get(secList[0], "totalnum")
        totalpass = conf.get(secList[0], "passnum")
        totalfail = conf.get(secList[0], "failnum")
        totalerror = conf.get(secList[0], "errornum")
        starttime = conf.get(secList[0], "starttime")
        totaltime = conf.get(secList[0], "totaltime")
        casetime = (int(conf.get(secList[0], "sec")))/int(totalcase)
        #model_name = conf.get(secList[0], "modelname")
        p = str(conf.get(secList[1], "suit")).split("_")

        for i in range(1, len(secList)):
            suit = conf.get(secList[i], "suit")  # 调用get方法，然后获取配置的数据
            # print(suit)
            status = conf.get(secList[i], "status")
            # print(status)
            testCase = conf.get(secList[i], "testCase")
            # print(testCase)
            classnam = suit + '.' + testCase
            message = conf.get(secList[i], "message")
            #model_name = suit.split("_")[-1]
            suitsumnub = ''
            #prjname = model_name + suitsumnub + ' Model TestReport'
            prjname = suitsumnub + ' Model TestReport'
            countsuitex = 0

            if not self.root:
                self.root = ET.Element('testsuites',
                                       {'tests': str(totalcase), 'pass': str(totalpass), 'failure': str(totalfail),
                                        'error': str(totalerror),
                                        'time': str(totaltime), 'timestamp': str(starttime),
                                        'name': prjname})  # 创建根节点

            if suit not in suitname.keys():
                # print(status)
                son = ET.SubElement(self.root, 'testsuite',
                                    {'name': suit, 'tests': str(''), 'pass': '0', 'fail': '0',
                                     'error': '0', 'time': str(casetime)})  # 创建子节点
                suitname[suit] = son
            else:
                son = suitname[suit]
            if 'passCase' in status:
                son.set('pass', str(int(son.get("pass")) + 1))
                countsuitex = countsuitex + 1
                sub = ET.SubElement(son, 'testcase',
                                    {'name': str(testCase), 'status': str(status), 'time': str(casetime),
                                     'classname': str(classnam)})
                pass
            elif 'errorCase' in status:
                son.set('error', str(int(son.get("error")) + 1))
                sub = ET.SubElement(son, 'testcase',
                                    {'name': str(testCase), 'status': str(status), 'time': str(casetime),
                                     'classname': str(classnam)})
                ub1 = ET.SubElement(sub, 'failure',
                                    {'message': str(message), 'type': 'ErrorType'}).text = 'errormessage'
            else:
                son.set('fail', str(int(son.get("fail")) + 1))

                sub = ET.SubElement(son, 'testcase',
                                    {'name': str(testCase), 'status': str(status), 'time': str(casetime),
                                     'classname': str(classnam)})
                ub1 = ET.SubElement(sub, 'failure',
                                    {'message': str(message), 'type': 'ErrorType'}).text = 'errormessage'
            casu = int(son.get("pass")) + int(son.get("error")) + int(son.get("fail"))#计算每个测试套件执行case数
            suittime=casetime*int(casu)#计算每个测试套件执行时间

            # 判断执行testsuite的总数定义测试报告标题
            keys = list(suitname.keys())
            # print(keys)
            if len(keys) == 1:
                suitsumnub = keys[0]
            else:
                suitsumnub = "Multi"

            # 更新根节点中name（测试报告标题）属性
            #prjname = model_name + ' ' + suitsumnub + ' Model TestReport'
            prjname = suitsumnub + ' Model TestReport'
            # print(prjname)
            self.root.set('name', str(prjname))
            son.set('tests', str(casu))#更新测试套件case执行总数
            son.set('time', str(suittime))#更新测试套件执行时间
            # print(suittime)
            # print(self.root)

        return self.root



    def mywrite(self):
        # print(self.root)
        rough_str = ET.tostring(self.root, 'utf-8')
        reparsed = minidom.parseString(rough_str)
        new_str = reparsed.toprettyxml(indent='\t')
        f = open('./Report/AVNTestReport.xml', 'w', encoding='utf-8')
        f.write(new_str)
        f.close()
'''
av = Createxmlfile()
av.createxmlfile()
av.mywrite('AVNTestReport.xml')
'''