# -*- coding: utf-8 -*-
# https://blog.csdn.net/xlynx/article/details/101551010
# https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#id19
from bs4 import BeautifulSoup
import re
import Mconfig.configparserHandler as config




class htmlParser():

    # 读取Html文件返回BeautifulSoup对象
    def readHtml(self, htmlPath):
        with open(htmlPath, 'r', encoding='utf-8') as htmlfile:
            htmlhandle = htmlfile.read()
            soup = BeautifulSoup(htmlhandle, 'lxml')
        return soup

    # 传入BeautifulSoup对象，返回Body段(bs4.element.Tag类型)
    def getHtmlBody(self, soup):
        return soup.body

    # 传入某tag节点，根据tag名称查找并返回Set类型的所有子类(bs4.element.ResultSet类型)
    def find_allNodeByTagName(self, tag, tagName):
        return tag.find_all(tagName)

    # 传入beautifulSoup对象和id，查找第一个明细
    def find_NodeByIdName(self, soup, id):
        return soup.find(id=id)

    # 传入beautifulSoup对象和id，查找第一个明细
    def find_NodeByClassName(self, soup, className):
        return soup.find(class_=className)

    # 传入beautifulSoup对象和id，查找所有明细
    def find_AllNodeByClassName(self, soup, className):
        return soup.find_all(class_=className)

    # 传入某tag节点，查找Id内容
    def getTagIdMessage(self, tag):
        return tag.attrs['id']

    # 传入某tag节点，查找Class内容
    def getTagClassMessage(self, tag):
        return tag.attrs['class']

    # 获取模块名称
    def getSuitName(self, contents):
        list = contents.replace('test_', '').split('_')
        suitName = list[0] + '_' + list[1]
        return suitName

    # 移除报文中换行和空格
    def replaceMessage(self, contents):
        try:
            contents = contents.replace(' ', '').replace('\n', '')
        except Exception as e:
            #logging.info(e)
            return ''
        return contents

    # 时间类型时分秒转换成秒
    def str2sec(self, strTime):
        h, m, s = strTime.strip().split(':') #.split()函数将其通过':'分隔开，.strip()函数用来除去空格
        return int(h)*3600 + int(m)*60 + int(s) #int()函数转换成整数运算

    # 传入html，遍历Body节点下所有子节点
    def traverseHtmlWriteToFile(self, htmlPath, filePath):
        #logger.info(filePath)
        configparserHandlers = config.configparserHandler(filePath) # 实例化ini文件操作类
        soup = self.readHtml(htmlPath) # 获取html文件中beautifulSoup对象
        body = self.getHtmlBody(soup)  # 获取body层
        nodes = self.find_allNodeByTagName(body, 'tr')  # 获取所有以tr命名的tag节点
        startIndex = 2  # 测试用例节点起始下标
        endIndex = len(nodes) - 1  # 测试用例节点末尾下标
        #print(body)
        passNode = self.find_NodeByClassName(soup, 'btn btn-success') # 成功数节点
        failNode = self.find_NodeByClassName(soup, 'btn btn-danger') # 失败数节点
        errorNode = self.find_NodeByClassName(soup, 'btn btn-warning') # 错误case数节点
        totalNode = self.find_NodeByClassName(soup, 'btn btn-info') # 所有case数节点
        passNum = re.findall(r"\d+\.?\d*", passNode.text)  # 成功数
        failNum = re.findall(r"\d+\.?\d*", failNode.text)  # 失败数
        errorNum = re.findall(r"\d+\.?\d*", errorNode.text)  # 错误case数
        totalNum = re.findall(r"\d+\.?\d*", totalNode.text)  # 所有case数
        #bodyHead=self.find_allNodeByTagName(body, 'div') # 获取body节点下第一个tag是div的节点内容
        #pNode = self.find_allNodeByTagName(bodyHead, 'attribute')
        heading = self.find_AllNodeByClassName(soup, 'attribute')  # 获取class为attribute的tag节点
        startTime = heading[3].text.replace('开始时间 : ', '')
        totalTime = heading[4].text.replace('合计耗时 : ', '')
        strTime = totalTime.split('.')[0].replace(' ', '')
        sec = self.str2sec(strTime)
        configparserHandlers.add_section('summary')  # 添加[index]索引
        configparserHandlers.set_section('summary', 'passNum', str(passNum[0]))
        configparserHandlers.set_section('summary', 'failNum', str(failNum[0]))
        configparserHandlers.set_section('summary', 'errorNum', str(errorNum[0]))
        configparserHandlers.set_section('summary', 'totalNum', str(totalNum[0]))
        configparserHandlers.set_section('summary', 'startTime', str(startTime))
        configparserHandlers.set_section('summary', 'totalTime', str(totalTime))
        configparserHandlers.set_section('summary', 'sec', str(sec))
        configparserHandlers.save()
        while startIndex < endIndex:
            #logger.info(str(startIndex) + '+'+ str(startIndex + 1))
            tag = nodes[startIndex:startIndex + 1]
            id = self.getTagIdMessage(tag[0])  # case ID
            className = self.getTagClassMessage(tag[0])  # class Name
            node = tag[0].find('td')  # case执行结果节点
            status = node['class'][0]  # case执行结果 passCase
            testCase = node.contents[0].text  # 执行模块&模块名&case编号 test_AS23P_Translate_03
            suitName = self.getSuitName(testCase)  # 模块名称AS23P_Translate
            message = self.replaceMessage(tag[0].find('pre').text)  # case执行日志
            #logger.info(message)
            configparserHandlers.add_section(id)  # 添加[index]索引
            configparserHandlers.set_section(id, 'suit', str(suitName))
            configparserHandlers.set_section(id, 'testCase', str(testCase))
            configparserHandlers.set_section(id, 'status', str(status))
            configparserHandlers.set_section(id, 'message', str(message))
            configparserHandlers.save()
            startIndex += 1
            if startIndex == endIndex:
                #logger.info('over')
                break
            else:
                pass
        return filePath

if __name__ == '__main__':
    '''just for test'''
    htmlParser = htmlParser()
    htmlPath = '../Report/report_20200706_09_19_32.html'
    filePath = '../UIconfig/'+'report_20200630_14_08_41_'+'xmlReport.ini'
    #logger.info(htmlParser.traverseHtmlWriteToFile(htmlPath, filePath))
    # print(htmlParser.getSuitName('test_D90_UserManual_09'))
    #configparserHandlers = config.configparserHandler('./UIconfig/xmlReport.ini')
    #configparserHandlers.__init__()
    #configparserHandlers.add_section('test')
    #configparserHandlers.save()

    '''
    totalIndex = len(soup.body.find_all('tr'))
    startIndex = 2
    endIndex = totalIndex -1
    #print(type(soup.body)) # 只读取下标2至倒数第2个
    tag = soup.body.find_all('tr')[2:3][0]
    #print(tag.attrs['class'])
    #print(type(tag.find_all('td')[0].contents[0]['class']))
    print(tag.find('pre').text.replace(' ', '').replace('\n', ''))



    
    [startIndex:startIndex+1]
    print(soup.title)
    tag = soup.find(id='show_detail_line')  # 获取html中第一个搜索到的指定id的列
    tag1 = soup.find(class_="btn btn-success").text  # 获取html中第一个搜索到的指定class的列
    print(tag)
    totalCount = re.sub("\D", "", tag1)  # 提取数字部分
    print(totalCount)
'''
