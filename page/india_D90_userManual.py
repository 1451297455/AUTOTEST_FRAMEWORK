# -*- coding: utf-8 -*-
from UIconfig.Base import Base
from page.PublicMethod import PublicMethod as pm
import time
import os
import UIconfig.logger as loggers

logger = loggers.Logger()
os.path.abspath('.')


class india_D90_userManual(Base):

    # 点击User Manual，滑动查找
    def clickUserManual(self):
        packageName = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'packageName')
        pm().stopApp(packageName)
        pm().openApp(packageName)
        time.sleep(2)
        for i in range(5):
            id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'menuList')
            elist = pm().find_element_by_id(id=id)
            text = pm().readConfigByModuleAndKey('india_D90', 'userManualPage', 'titleText')
            Manual = pm().find_element_by_text(text=text)
            if Manual:
                return pm().click_by_element(Manual)
            time.sleep(1)
            pm().swipe_up_by_element(elist)
        return False

    # 检查页面标题是否正确
    def checkPage(self, text):
        Xpath = pm().readConfigByModuleAndKey('india_D90', 'userManualPage', 'titleXpath')
        title = pm().find_element_by_xpath(xpath=Xpath)
        return pm().get_text_by_element(title) == text

    # 点击用户手册类型，text参数表示：子项内容文本
    def clickItem(self, text):
        id = pm().readConfigByModuleAndKey('india_D90', 'userManualPage', 'menuContentList')
        elist = pm().find_element_by_id(id=id)
        if elist:
            pm().swipe_forwardto_description(text)
        element = pm().find_element_by_text(text=text)
        if element:
            return pm().click_by_element(element)
        return False

    # 等待用户手册文本展示完成
    def loadPdf(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'userManualPage', 'pageInfo')
        for i in range(2):
            load = pm().find_element_by_id(id=id)
            if load is None:
                continue
            else:
                return True
        return False

    # 点击页面返回按钮
    def pressBack(self):
        id = id = pm().readConfigByModuleAndKey('india_D90', 'userManualPage', 'backButton')
        backTitle = pm().find_element_by_id(id=id)
        return pm().click_by_element(backTitle)

    # 获取页面页码
    def getPageNum(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'userManualPage', 'pageInfo')
        pageNum = pm().find_element_by_id(id=id)
        if pageNum is None:
            return False
        text = pm().get_text_by_element(pageNum)
        return text.split(' / ')[0]

        # 滑动PDF页面， up/down：表示向上/向下滑， times：表示滑动几次

    def swipPdf(self, up, times):
        times = int(times)
        id = pm().readConfigByModuleAndKey('india_D90', 'userManualPage', 'pdfView')
        pdfView = pm().find_element_by_id(id=id)
        if pdfView is not None and pdfView.exists():
            if str.lower(up) == 'up':
                for i in range(0, times):
                    if pm().swipe_up_by_element(pdfView):
                        continue
                    else:
                        return False
                return True
            elif str.lower(up) == 'down':
                for i in range(0, times):
                    if pm().swipe_down_by_element(pdfView):
                        continue
                    else:
                        return False
                return True
            else:
                return False
        return False
