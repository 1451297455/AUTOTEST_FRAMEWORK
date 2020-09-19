import datetime
import os
import threading

import sys, time
import xlrd
from UIconfig import assertUntil
from UIconfig import info, adbTool
from UIconfig.htmlReport import Template_mixin
from UIconfig.Base import Base
import adbutils as adb

import UIconfig.logger as loggers


def init(caseFile):
    suitList = {}
    testSuit = caseFile.sheet_by_name("suit")
    row = testSuit.nrows
    for i in range(1, row):
        key = testSuit.cell_value(i, 0)
        value = testSuit.cell_value(i, 1)
        suitList[key] = value
    return suitList


def getCaseCell(sheetName, row, col):
    if sheetName not in allSheet:
        return "sheetName not exist"
    testCase = caseFile.sheet_by_name(sheetName)
    rowCount = testCase.nrows
    if row >= rowCount:
        return "error"
    else:
        return testCase.cell_value(row, col)


def getCaseId(sheetName, row):
    if sheetName not in allSheet:
        return "sheetName not exist"
    testCase = caseFile.sheet_by_name(sheetName)
    rowCount = testCase.nrows
    if row >= rowCount:
        return "error"
    else:
        return str(testCase.cell_value(row, 0))


def getCaseDescription(sheetName, row):
    if sheetName not in allSheet:
        return "sheetName not exist"
    testCase = caseFile.sheet_by_name(sheetName)
    rowCount = testCase.nrows
    if row >= rowCount:
        return "error"
    else:
        return str(testCase.cell_value(row, 2))


def getClass(sheetName, row):
    if sheetName not in allSheet:
        return "sheetName not exist"
    testCase = caseFile.sheet_by_name(sheetName)
    rowCount = testCase.nrows
    if row >= rowCount:
        return "error"
    elif str(testCase.cell_value(row, 3)).__contains__("::"):
        return str.split(testCase.cell_value(row, 3), "::", 2)[0]
    else:
        try:
            return str.split(testCase.cell_value(row, 3), "/", 2)[0]
        except:
            return "empty"


def getMethod(sheetName, row):
    if sheetName not in allSheet:
        return "sheetName not exist"
    testCase = caseFile.sheet_by_name(sheetName)
    rowCount = testCase.nrows
    if row >= rowCount:
        return "error"
    elif str(testCase.cell_value(row, 3)).__contains__("::"):
        return str.split(testCase.cell_value(row, 3), "::", 2)[1]
    else:
        try:
            return str.split(testCase.cell_value(row, 3), "/", 2)[1]
        except:
            return "empty"


def getParam(sheetName, row):
    if sheetName not in allSheet:
        return "sheetName not exist"
    testCase = caseFile.sheet_by_name(sheetName)
    rowCount = testCase.nrows
    if row >= rowCount:
        para = []
    else:
        para = str.split(testCase.cell_value(row, 4), "/", 9)
    return para[0: -1]


def getAssert(sheetName, row):
    if sheetName not in allSheet:
        return "sheetName not exist"
    testCase = caseFile.sheet_by_name(sheetName)
    rowCount = testCase.nrows
    if row >= rowCount:
        return "error"
    else:
        return str(testCase.cell_value(row, 5))


def getCheckValue(sheetName, row):
    if sheetName not in allSheet:
        return "sheetName not exist"
    testCase = caseFile.sheet_by_name(sheetName)
    rowCount = testCase.nrows
    if row >= rowCount:
        return "error"
    else:
        return str(testCase.cell_value(row, 6))


def getValuation(sheetName, row):
    if sheetName not in allSheet:
        return "sheetName not exist"
    testCase = caseFile.sheet_by_name(sheetName)
    rowCount = testCase.nrows
    if row >= rowCount:
        return "error"
    else:
        return str(testCase.cell_value(row, 7))


def getResult(className, MethodName, Param):
    if className == "" or MethodName == "":
        return False
    try:
        package = __import__("page", fromlist=[className])
        pyName = getattr(package, className)
        '''
        如果模块导入成功，该模块下的所有py文件会作为模块的属性，因此使用getattr(模块，文件名)获取即可
                文件名不需要加.py后缀
        '''
    except Exception as e:
        logger.info(str(e))
        info.errorInfo = str(e)
        return False

    '''
    如果模块导入成功，该模块下的所有py文件会作为模块的属性，因此使用getattr(模块，文件名)获取即可
            文件名不需要加.py后缀
    '''
    try:
        # 根据子类名称从fileName.py中获取该类
        NameClass = getattr(pyName, className)
        # 实例化对象
        classa = NameClass()
        # 调用返回方法函数
        runMethod = getattr(classa, MethodName)
    except Exception as e:
        info.errorInfo = str(e)
        logger.info("errorinfo:" + str(e))
        return False
    argCount = runMethod.__code__.co_argcount
    ParamCount = len(Param)
    ##self is also a parameter no need to input
    if argCount - 1 == ParamCount:
        try:
            res = runMethod(*Param)
            return res
        except Exception as e:
            info.errorInfo = str(e)
            logger.info("errorinfo:" + str(e))
            return False
    else:
        return False


if __name__ == '__main__':
    startTime = datetime.datetime.now()
    logger = loggers.Logger()
    try:
        case = sys.argv[1]
    except:
        case = 'India_D90'
    caseFile = xlrd.open_workbook("./TestCase/" + case + "Case.xlsx")
    allSheet = caseFile.sheet_names()
    allSuit = init(caseFile)
    runList = []
    caseList = []
    adbtools = adbTool.adbtool()
    try:
        device = adb.AdbClient().device_list()[0]
        adbtools.callCMD(adbtools.CMD_ADB_ROOT)
        adbtools.setAndroidDate()
        AvnVersion = adbtools.getAvnVersion()
        Base().set_driver(add=device.serial)
    except Exception as e:
        logger.info('设备驱动未连接。')
        logger.info(str(e))
        AvnVersion = ""
        exit(0)

    logger.info("startTime : " + str(startTime))
    # 启动性能获取线程
    TopThread = threading.Thread(target=adbtools.top,
                                 args=[str(startTime).replace(" ", "_").replace(':', "_").split('.')[0], 'ui'])
    TopThread.start()
    for suitKey in allSuit.keys():
        if str(allSuit[suitKey]).lower() == "yes" and suitKey in allSheet:
            runList.append(suitKey)
    for runSheet in runList:
        logger.info("***************************")
        nrow = caseFile.sheet_by_name(runSheet).nrows
        for i in range(1, nrow):
            info.errorInfo = ''
            info.pic = ''
            caseDetail = {}
            caseId = getCaseId(runSheet, i)
            if caseId.startswith("#") or caseId == "":
                continue
            caseAssert = getAssert(runSheet, i)
            if caseAssert == "skip":
                continue
            caseDescription = getCaseDescription(runSheet, i)
            caseClass = getClass(runSheet, i)
            caseMethod = getMethod(runSheet, i)
            caseParam = getParam(runSheet, i)
            caseCheck = getCheckValue(runSheet, i)
            caseValuation = getValuation(runSheet, i)
            screenName = runSheet + "_" + caseId
            logger.info("module:" + runSheet)
            logger.info("caseID:" + caseId + ",  caseDescription:" + caseDescription)
            logger.info("caseClass:" + caseClass + ",  caseMethod:" + caseMethod)
            logger.info("caseAssert:" + caseAssert + ",   caseCheckValue:" + caseCheck)
            logger.info('caseParam:')
            logger.info(caseParam)
            for para in caseParam:
                if para.startswith('para_'):
                    logger.info(info.parameter[para.split('para_')[1]])
                else:
                    logger.info(para)
            # 启动logcat线程
            logcatTH = adbtools.startLogcatThread()
            if caseAssert == 'assertTrue':
                if not info.flag:
                    logger.info('case skip')
                    logger.info("***************************")
                    continue
                methodResult = getResult(caseClass, caseMethod, caseParam)
                caseResult = assertUntil.assertTrue(str(methodResult), caseCheck, caseValuation, screenName)
                logger.info("methodResult:" + str(methodResult) + ",caseResult:" + str(caseResult))
            elif caseAssert == 'assertFalse':
                if not info.flag:
                    logger.info('case skip')
                    logger.info("***************************")
                    continue
                methodResult = getResult(caseClass, caseMethod, caseParam)
                caseResult = assertUntil.assertFalse(str(methodResult), caseCheck, caseValuation, screenName)
                logger.info("methodResult:" + str(methodResult) + ",caseResult:" + str(caseResult))
            elif caseAssert == 'sleep':
                if not info.flag:
                    logger.info('case skip')
                    logger.info("***************************")
                    continue
                caseResult = assertUntil.sleep(caseParam[0])
                logger.info("caseResult:" + str(caseResult))
            elif caseAssert == 'compareFalse':
                if not info.flag:
                    logger.info('case skip')
                    logger.info("***************************")
                    continue
                caseResult = assertUntil.compareFalse(caseParam[0], caseCheck, caseValuation, screenName)
                logger.info("caseResult:" + str(caseResult))
            elif caseAssert == 'compareTrue':
                if not info.flag:
                    logger.info('case skip')
                    logger.info("***************************")
                    continue
                caseResult = assertUntil.compareTrue(caseParam[0], caseCheck, caseValuation, screenName)
                logger.info("caseResult:" + str(caseResult))
            elif caseAssert == 'getText':
                if not info.flag:
                    logger.info('case skip')
                    logger.info("***************************")
                    continue
                caseResult = assertUntil.getText(caseClass, caseMethod, caseParam, caseCheck, caseValuation, screenName)
            elif caseAssert == 'clickElement':
                caseResult = assertUntil.clickElement(caseClass, caseMethod, caseValuation, screenName)
            elif caseAssert == 'ifTrue':
                logger.info(info.flag)
                caseResult = assertUntil.ifTure(caseClass, caseMethod, caseParam, caseCheck, caseValuation, screenName)
                logger.info("***************************")
                continue
            elif caseAssert == 'ifFalse':
                caseResult = assertUntil.ifFalse(caseClass, caseMethod, caseParam, caseCheck, caseValuation, screenName)
                logger.info("***************************")
                continue
            elif caseAssert == 'inputText':
                if not info.flag:
                    logger.info('case skip')
                    logger.info("***************************")
                    continue
                caseResult = assertUntil.inputText(caseClass, caseMethod, caseParam, caseValuation, screenName)
            elif caseAssert == 'endIf':
                caseResult = assertUntil.endIf()
                continue
            else:
                info.errorInfo = '断言值不正确'
                logger.info(info.errorInfo)
                caseResult = False
                logger.info("***************************")
                continue
            # 停止logcat线程
            adbtools.stopLogcatThread("UI", screenName, str(time.strftime("%Y%m%d%H%M%S")))
            caseDetail['module'] = runSheet
            caseDetail['caseID'] = caseId
            caseDetail[
                'description'] = "{0}<br/>{1} : {2}<br/>{3}<br/>{4}".format(caseDescription,
                                                                            caseClass, caseMethod,
                                                                            caseParam, caseCheck)
            caseDetail['assert'] = caseAssert
            caseDetail['detail'] = info.errorInfo
            caseDetail['result'] = str(caseResult)
            caseDetail['pic'] = info.pic
            caseList.append(caseDetail)
            logger.info("***************************")
    adbtools.stopThread(TopThread.ident)
    logger.info("测试完成。")
    htmlTest = Template_mixin(title=case + "车机自动化测试报告", project=case, tester='tester',
                              startTime=startTime, version=AvnVersion)
    htmlTest.writeHtml(caseList)
