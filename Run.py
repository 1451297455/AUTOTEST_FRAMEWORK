import time
import unittest
import sys
import HTMLTestRunnerCN
from page.BasePage import BasePage as Base
from page.publicMethod import publicMethod as PM

from config import exlsTool, info, assertUntil


class AVN_Test(unittest.TestCase, Base):

    def setUp(self) -> None:
        Base.set_driver(avn_device)

    def demo(self, caseId, caseDescription, caseClass, caseMethod, caseParam, caseAssert, caseCheck, caseValuation):
        '''
               具体case
               :return:
               '''
        global element
        exlsUtil = exlsTool.exlsTool()
        print(
            "caseID:" + caseId + ",  caseDescription:" + caseDescription + ",  caseClass:" + caseClass + ",  caseMethod:" + caseMethod + ",   caseAssert:" + caseAssert + ",   caseCheckValue:" + caseCheck)
        print("param:" + str(caseParam))
        info.errorMessage = ""
        if caseAssert == "skip" or caseId == "":
            return "pass"
        if caseAssert == "assertTrue":
            try:
                result = exlsUtil.getResult(caseClass, caseMethod, caseParam)
            except:
                info.errorMessage = "方法执行异常。"
                result = False
            if caseValuation != '' and caseValuation.startswith('para_'):
                info.para[caseValuation.split('_')[1]] = result
            if caseCheck == "":
                assertUntil.assertTrue(result, caseCheck, caseId)
                self.assertEqual(result, True, info.errorMessage)
            else:
                assertUntil.assertTrue(result, caseCheck, caseId)
                self.assertEqual(result, caseCheck, info.errorMessage)
        elif caseAssert == "assertFalse":
            try:
                result = exlsUtil.getResult(caseClass, caseMethod, caseParam)
            except:
                info.errorMessage = "方法执行异常。"
                result = False
            if caseValuation != '' and caseValuation.startswith('para_'):
                info.para[caseValuation.split('_')[1]] = result
            if caseCheck == "":
                self.assertEqual(result, False, info.errorMessage)
            else:
                self.assertNotEqual(result, caseCheck, info.errorMessage)
        elif caseAssert == "sleep":
            second = caseParam[0]
            assertUntil.sleep(second)

        elif caseAssert == "inputText":
            if caseClass == "id":
                element = Base.find_element_by_id(self, caseMethod)
            elif caseClass == "description":
                element = Base.find_element_by_description(self, caseMethod)
            elif caseClass == "text":
                element = Base.find_element_by_text(self, caseMethod)
            elif caseClass == "xpath":
                element = Base.find_element_by_Xpath(self, caseMethod)
            elif caseClass == "class":
                element = Base.find_element_by_ClassName(self, caseMethod)
            else:
                info.errorMessage = "参数错误"
                return self.assertTrue(False, info.errorMessage)
            if element is not None:
                return Base.input_text(self, element, caseParam[0])
            else:
                info.errorMessage = "element 不存在！"
                return self.assertTrue(False, info.errorMessage)

        elif caseAssert == "getText":
            if caseClass == "id":
                element = Base.find_element_by_id(self, caseMethod)
            elif caseClass == "description":
                element = Base.find_element_by_description(self, caseMethod)
            elif caseClass == "text":
                element = Base.find_element_by_text(self, caseMethod)
            elif caseClass == "xpath":
                element = Base.find_element_by_Xpath(self, caseMethod)
            elif caseClass == "class":
                element = Base.find_element_by_ClassName(self, caseMethod)
            else:
                try:
                    result = exlsUtil.getResult(caseClass, caseMethod, caseParam)
                except:
                    info.errorMessage = "方法执行异常。"
                    result = False
                if caseValuation != '' and caseValuation.startswith('para_'):
                    info.para[caseValuation.split('_')[1]] = result
                return self.assertTrue(result == caseCheck, info.errorMessage)
            if element is not None:
                value = Base.get_text(self, element)
                if caseValuation != '' and caseValuation.startswith('para_'):
                    info.para[caseValuation.split('_')[1]] = value
                return self.assertEqual(value, caseCheck, "获取值：" + value + ",校验值：" + caseCheck)
            else:
                info.errorMessage = "element 不存在！"
                if caseValuation != '' and caseValuation.startswith('para_'):
                    info.para[caseValuation.split('_')[1]] = info.errorMessage
                return self.assertTrue(False, info.errorMessage)

        elif caseAssert == "swipeElement":
            if caseClass == "id":
                element = Base.find_element_by_id(self, caseMethod)
            elif caseClass == "description":
                element = Base.find_element_by_description(self, caseMethod)
            elif caseClass == "text":
                element = Base.find_element_by_text(self, caseMethod)
            elif caseClass == "xpath":
                element = Base.find_element_by_Xpath(self, caseMethod)
            elif caseClass == "class":
                element = Base.find_element_by_ClassName(self, caseMethod)
            if element is not None:
                try:
                    step = int(caseParam[1])
                except:
                    step = 20
                if caseParam[0] == "down":
                    return element.swipe('down', steps=step)
                elif caseParam[0] == "up":
                    return element.swipe('up', steps=step)
                elif caseParam[0] == "left":
                    return element.swipe('left', steps=step)
                elif caseParam[0] == "right":
                    return element.swipe('right', steps=step)
                else:
                    info.errorMessage = "参数错误！"
                    return self.assertTrue(False, info.errorMessage)
            else:
                try:
                    step = int(caseParam[1])
                except:
                    step = 20
                if caseParam[0] == "down":
                    return PM.swipe_down(self, step)
                elif caseParam[0] == "up":
                    return PM.swipe_up(self, step)
                elif caseParam[0] == "left":
                    return PM.swipe_left(self, step)
                elif caseParam[0] == "right":
                    return PM.swipe_right(self, step)
                else:
                    info.errorMessage = "参数错误！"
                    return self.assertTrue(False, info.errorMessage)

        elif caseAssert == "clickElement":
            if caseClass == "id":
                element = Base.find_element_by_id(self, caseMethod)
            elif caseClass == "description":
                element = Base.find_element_by_description(self, caseMethod)
            elif caseClass == "text":
                element = Base.find_element_by_text(self, caseMethod)
            elif caseClass == "xpath":
                element = Base.find_element_by_Xpath(self, caseMethod)
            elif caseClass == "class":
                element = Base.find_element_by_ClassName(self, caseMethod)
            if element is not None:
                return element.click()
            else:
                info.errorMessage = "element 不存在！"
                return self.assertTrue(False, info.errorMessage)
        elif caseAssert == "compare":
            if caseParam[0].startswith('para_'):
                param = info.para[caseParam[0].split("_")[1]]
            else:
                param = caseParam[0]
            if caseCheck.startswith('para_'):
                checkValue = info.para[caseCheck.split("_")[1]]
            else:
                checkValue = caseCheck
            return self.assertEqual(param, checkValue, info.errorMessage)
        else:
            info.errorMessage = "Assert 传入错误！"

    @staticmethod
    def demo_func(caseId, caseDescription, caseClass, caseMethod, caseParam, caseAssert, caseCheck, caseValuation):
        def Func(self):
            self.demo(caseId, caseDescription, caseClass, caseMethod, caseParam, caseAssert, caseCheck, caseValuation)

        return Func


def __generateTestCases():
    print("__generateTestCases")
    runList = []
    exlsUtil = exlsTool.exlsTool()
    allSheet = exlsUtil.allSheet
    allSuit = exlsUtil.suitList
    for suitKey in allSuit.keys():
        if str(allSuit[suitKey]).lower() == "yes" and suitKey in allSheet:
            runList.append(suitKey)
    for runSheet in runList:
        print("start test model : " + str(runSheet))
        nrow = exlsUtil.caseFile.sheet_by_name(runSheet).nrows
        for i in range(1, nrow):
            caseId = exlsUtil.getCaseId(runSheet, i)
            if caseId.startswith("#") or caseId == "":
                continue
            caseAssert = exlsUtil.getAssert(runSheet, i)
            if caseAssert == "skip":
                continue
            caseDescription = exlsUtil.getCaseDescription(runSheet, i)
            caseClass = exlsUtil.getClass(runSheet, i)
            caseMethod = exlsUtil.getMethod(runSheet, i)
            caseParam = exlsUtil.getParam(runSheet, i)
            caseCheck = exlsUtil.getCheckValue(runSheet, i)
            caseValuation = exlsUtil.getValuation(runSheet, i)
            setattr(AVN_Test, 'test_%s_%s' % (runSheet, caseId),
                    AVN_Test.demo_func(caseId, caseDescription, caseClass, caseMethod, caseParam, caseAssert,
                                       caseCheck, caseValuation))
            # 通过setattr自动为TestCase类添加成员方法，方法以“test_func_”开头


if __name__ == "__main__":
    try:
        print("start")
        # avn_device = sys.argv[1]
        avn_device = "0a01600e82899a74"
        # avn_device = "0908700e8289588f"
    except:
        print("please make sure the device!")
        sys.exit(0)
    try:
        phone_device = sys.argv[2]
    except:
        pass

    __generateTestCases()
    test = unittest.TestLoader().loadTestsFromTestCase(AVN_Test)
    load = unittest.TestSuite(test)
    now = time.strftime("%Y%m%d_%H_%M_%S", time.localtime())
    report_path = './Report/report_' + now + '.html'
    print('report_path : ' + report_path)
    fp = open(report_path, "wb")
    runner = HTMLTestRunnerCN.HTMLTestReportCN(stream=fp, title="测试报告", tester='Tester', project='D90')
    runner.run(load)
    fp.close()
