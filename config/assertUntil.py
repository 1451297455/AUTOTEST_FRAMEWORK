from config import info
from page import BasePage
import time


def assertTrue(result, value, screenName):
    if result == None:
        info.errorMessage = "方法结果错误。"
        BasePage.BasePage.screenshot(screenName)
        return False
    result = str(result)
    if value == "":
        if result == "True":
            return True
        elif result == "False":
            BasePage.BasePage.screenshot(screenName)
            return False
        else:
            info.errorMessage = "方法结果为：" + result + "，校验值为空。"
            BasePage.BasePage.screenshot(screenName)
            return False
    else:
        if result == value:
            return True
        else:
            info.errorMessage = "结果不一致。方法结果为：" + result + "，校验值为" + value
            BasePage.BasePage.screenshot(screenName)
            return False


def assertFalse(result, value, screenName):
    if result == None:
        info.errorMessage = "方法结果错误。"
        BasePage.BasePage.screenshot(screenName)
        return False
    if value == "":
        if result == "False":
            return True
        elif result == "True":
            BasePage.BasePage.screenshot(screenName)
            return False
        else:
            info.errorMessage = "方法结果为：" + result + "，校验值为空。"
            BasePage.BasePage.screenshot(screenName)
            return False
    else:
        if result == value:
            BasePage.BasePage.screenshot(screenName)
            info.errorMessage = "结果一致。方法结果为：" + result + "，校验值为" + value
            return False
        else:
            return True


def sleep(second):
    time.sleep(int(second))
    print('sleep ' + str(second))
