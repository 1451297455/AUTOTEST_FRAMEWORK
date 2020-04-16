# -*- coding: utf-8 -*-
from page.BasePage import BasePage
from page.publicMethod import publicMethod as pm
import time
from config import india_D90_propertiseConfig as conf


class userManual(BasePage):

    # 点击User Manual，滑动查找
    def clickUserManual(self):
        pm.stopApp(conf.userManualPage.get('packageName'))
        pm.openApp(conf.userManualPage.get('packageName'))
        time.sleep(2)
        for i in range(5):
            elist = pm.find_element_by_id(self, id=conf.userManualPage.get('menuList'))
            Manual = pm.find_element_by_text(self, text=conf.userManualPage.get('titleText'))
            if Manual:
                return pm.click_by_element(self, Manual)
            time.sleep(1)
            pm.swipe_up_by_element(self, elist)
        return False

    # 检查页面标题是否正确
    def checkPage(self, text):
        title = pm.find_element_by_Xpath(self,
                                         Xpath=conf.userManualPage.get('titleXpath'))
        return pm.get_text_by_element(self, title) == text

    # 点击用户手册类型，text参数表示：子项内容文本
    def clickItem(self, text):
        elist = pm.find_element_by_id(self, id=conf.userManualPage.get('menuContentList'))
        if elist:
            pm.swipe_forwardto_description(self, text)
        element = pm.find_element_by_text(self, text=text)
        if element:
            return pm.click_by_element(self, element)
        return False

    # 等待用户手册文本展示完成
    def loadPdf(self):
        load = pm.find_element_by_id(self, id=conf.userManualPage.get('pageInfo'))
        if load.exists(timeout=60):
            return True
        return False

    # 点击页面返回按钮
    def pressBack(self):
        backTitle = pm.find_element_by_id(self, id=conf.userManualPage.get('backButton'))
        return pm.click_by_element(self, backTitle)

    # 获取页面页码
    def getPageNum(self, page):
        pageNum = pm.find_element_by_id(self, id=conf.userManualPage.get('pageInfo'))
        text = pm.get_text_by_element(self, pageNum)
        return text == page + " / 92"

    # 滑动PDF页面， up/down：表示向上/向下滑， times：表示滑动几次
    def swipPdf(self, up, times):
        times = int(times)
        pdfView = pm.find_element_by_id(self, id=conf.userManualPage.get('pdfView'))
        if pdfView.exists():
            if str.lower(up) == 'up':
                for i in range(0, times):
                    if pm.swipe_up_by_element(self, pdfView):
                        continue
                    else:
                        return False
                return True
            elif str.lower(up) == 'down':
                for i in range(0, times):
                    if pm.swipe_down_by_element(self, pdfView):
                        continue
                    else:
                        return False
                return True
            else:
                return False
        return False