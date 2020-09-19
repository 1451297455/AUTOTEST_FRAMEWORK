import time

import UITest
from UIconfig import info
from UIconfig.Base import Base


def assertTrue(result, value, caseValuation, screenName):
    info.errorInfo = ""
    if result is None:
        info.errorInfo = "方法结果为None。"
        Base.screenshot(screenName)
        return False
    result = str(result)
    if caseValuation != "":
        info.parameter[caseValuation.split('para_')[1]] = result
    if result.startswith('para_'):
        key = result.split('_')[1]
        result = info.parameter[key]
    if str(value) == "":
        if result == "True":
            return True
        elif result == "False":
            info.errorInfo = "方法结果为：" + str(result)
            Base.screenshot(screenName)
            return False
        else:
            info.errorInfo = "方法结果为：" + str(result) + "，校验值为空。"
            Base.screenshot(screenName)
            return False
    else:
        if str(value).startswith('para_'):
            key = str(value).split('_')[1]
            value = info.parameter[key]
        if result == value:
            return True
        else:
            Base.screenshot(screenName)
            info.errorInfo = "结果不一致。方法结果为：" + str(result) + "，校验值为" + str(value)
            return False


def assertFalse(result, value, caseValuation, screenName):
    info.errorInfo = ""
    if result is None:
        info.errorInfo = "方法结果为None。"
        Base.screenshot(screenName)
        return False
    if caseValuation != "":
        info.parameter[caseValuation.split('para_')[1]] = str(result)
    if str(result).startswith('para_'):
        key = str(result).split('_')[1]
        result = info.parameter[key]
    if value == "":
        if result == "False":
            Base.screenshot(screenName)
            return True
        elif result == "True":
            info.errorInfo = "方法结果为：" + str(result)
            Base.screenshot(screenName)
            return False
        else:
            info.errorInfo = "方法结果为：" + str(result) + "，校验值为空。"
            Base.screenshot(screenName)
            return False
    else:
        if str(value).startswith('para_'):
            key = str(value).split('_')[1]
            value = info.parameter[key]
            print(value)
        if result == value:
            Base.screenshot(screenName)
            info.errorInfo = "结果一致。方法结果为：" + str(result) + "，校验值为" + value
            return False
        else:
            return True


def sleep(second):
    try:
        time.sleep(int(second))
        return True
    except:
        info.errorInfo = 'sleep error。'
        return False


def compareFalse(parameter, checkvalue, caseValuation, screenName):
    info.errorInfo = ""
    if parameter is None or parameter == "":
        info.errorInfo = "传参错误，请确认参数！"
        return False
    if str(parameter).startswith('para_'):
        key = str(parameter).split('_')[1]
        parameter = info.parameter[key]
    if str(checkvalue).startswith('para_'):
        key = str(checkvalue).split('_')[1]
        checkvalue = info.parameter[key]
    return assertFalse(parameter, checkvalue, caseValuation, screenName)


def compareTrue(parameter, checkvalue, caseValuation, screenName):
    info.errorInfo = ""
    if parameter is None:
        info.errorInfo = "传参错误，请确认参数！"
        return False
    if str(parameter).startswith('para_'):
        key = str(parameter).split('_')[1]
        parameter = info.parameter[key]
    if str(checkvalue).startswith('para_'):
        key = str(checkvalue).split('_')[1]
        checkvalue = info.parameter[key]
    return assertTrue(parameter, checkvalue, caseValuation, screenName)


def getText(caseClass, caseMethod, caseParam, caseCheck, caseValuation, screenName):
    info.errorInfo = ""
    base = Base()
    if caseClass == "id":
        element = base.find_element_by_id(caseMethod)
    elif caseClass == "description":
        element = base.find_element_by_description(caseMethod)
    elif caseClass == "text":
        element = base.find_element_by_text(caseMethod)
    elif caseClass == "xpath":
        element = base.find_element_by_xpath(caseMethod)
    elif caseClass == "class":
        element = base.find_element_by_xpath(caseMethod)
    else:
        try:
            result = UITest.getResult(caseClass, caseMethod, caseParam)
        except:
            info.errorInfo = "方法执行异常。"
            Base.screenshot(screenName)
            result = False
        if caseValuation != '' and caseValuation.startswith('para_'):
            info.parameter[caseValuation.split('_')[1]] = result
        if caseCheck != "":
            return assertTrue(result, caseCheck, caseValuation, screenName)
        return True
    if element is not None:
        value = base.get_text(element)
        if caseValuation != '' and caseValuation.startswith('para_'):
            info.parameter[caseValuation.split('_')[1]] = value
        if caseCheck != "":
            return assertTrue(value, caseCheck, caseValuation, screenName)
        return True
    else:
        info.errorInfo = "element 不存在！"
        return assertTrue(False, True, caseValuation, screenName)


def ifFalse(caseClass, caseMethod, caseParam, caseCheck, caseValuation, screenName):
    info.errorInfo = ""
    if caseClass == "":
        result = info.parameter[caseParam[0].split('para_')[1]]
    else:
        try:
            result = UITest.getResult(caseClass, caseMethod, caseParam)
        except:
            info.errorInfo = "方法执行异常。"
            Base.screenshot(screenName)
            info.flag = True
            result = False
    if caseValuation != '' and caseValuation.startswith('para_'):
        info.parameter[caseValuation.split('_')[1]] = result
    if caseCheck != "":
        result = assertTrue(result, caseCheck, caseValuation, screenName)
    info.flag = False if str(result).lower() == 'true' else True


def ifTure(caseClass, caseMethod, caseParam, caseCheck, caseValuation, screenName):
    info.errorInfo = ""
    if caseClass == "":
        result = info.parameter[caseParam[0].split('para_')[1]]
    else:
        try:
            result = UITest.getResult(caseClass, caseMethod, caseParam)
        except:
            info.errorInfo = "方法执行异常。"
            Base.screenshot(screenName)
            info.flag = False
            result = False
    if caseValuation != '' and caseValuation.startswith('para_'):
        info.parameter[caseValuation.split('_')[1]] = result
    if caseCheck != "":
        result = assertTrue(result, caseCheck, caseValuation, screenName)
    info.flag = True if str(result).lower() == 'true' else False


def endIf():
    info.flag = True


def clickElement(caseClass, caseMethod, caseValuation, screenName):
    info.errorInfo = ""
    base = Base()
    if caseClass == "id":
        element = base.find_element_by_id(caseMethod)
    elif caseClass == "description":
        element = base.find_element_by_description(caseMethod)
    elif caseClass == "text":
        element = base.find_element_by_text(caseMethod)
    elif caseClass == "xpath":
        element = base.find_element_by_xpath(caseMethod)
    elif caseClass == "class":
        element = base.find_element_by_xpath(caseMethod)
    else:
        info.errorInfo = '参数错误。'
        if caseValuation != "":
            info.parameter[caseValuation.split('para_')[1]] = 'False'
        return False
    if base.click_element(element):
        if caseValuation != "":
            info.parameter[caseValuation.split('para_')[1]] = 'True'
        return True
    else:
        Base.screenshot(screenName)
        info.errorInfo = '元素点击失败。'
        if caseValuation != "":
            info.parameter[caseValuation.split('para_')[1]] = 'False'
        return False


def inputText(caseClass, caseMethod, caseParam, caseValuation, screenName):
    caseParams = []
    base = Base()
    for i in range(len(caseParam)):
        if str(caseParam[i]).startswith('para_'):
            caseParams.append(info.parameter[str(caseParam[i]).split('para_')[1]])
        else:
            caseParams.append(caseParam[i])
    if caseClass == "id":
        element = base.find_element_by_id(caseMethod)
    elif caseClass == "description":
        element = base.find_element_by_description(caseMethod)
    elif caseClass == "text":
        element = base.find_element_by_text(caseMethod)
    elif caseClass == "xpath":
        element = base.find_element_by_xpath(caseMethod)
    elif caseClass == "class":
        element = base.find_element_by_class_name(caseMethod)
    else:
        info.errorMessage = "参数错误"
        return assertTrue(False, True, caseValuation, screenName)
    if element is not None:
        return base.input_text(element, caseParams[0])
    else:
        info.errorMessage = "element 不存在！"
        return assertTrue(False, True, caseValuation, screenName)
