# -*- coding: utf-8 -*-
from UIconfig.Base import Base
from page.PublicMethod import PublicMethod as pm
from page.india_D90_homePage import india_D90_homePage as homePage
import time, os
import UIconfig.logger as loggers

logger = loggers.Logger()
os.path.abspath('.')


class india_D90_morePage(Base):

    def clickFolder(self):
        """
        点击进入Folder目录
        :return: True点击成功，False点击失败
        """
        text = pm().readConfigByModuleAndKey('india_D90', 'morePage', 'FOLDER')
        element = pm().find_element_by_text(text=text)
        return pm().click_by_element(element)

    def clickICall(self):
        """
        点击进入I-CALL目录
        :return:True点击成功，False点击失败
        """
        text = pm().readConfigByModuleAndKey('india_D90', 'morePage', 'ICALL')
        element = pm().find_element_by_text(text=text)
        return pm().click_by_element(element)

    def clickInbox(self):
        """
        点击进入INBOX目录
        :return:True点击成功，False点击失败
        """
        text = pm().readConfigByModuleAndKey('india_D90', 'morePage', 'INBOX')
        element = pm().find_element_by_text(text=text)
        return pm().click_by_element(element)

    def clickSetting(self):
        """
        点击进入SETTING目录
        :return:True点击成功，False点击失败
        """
        text = pm().readConfigByModuleAndKey('india_D90', 'morePage', 'SETTING')
        element = pm().find_element_by_text(text=text)
        return pm().click_by_element(element)

    def clickOK(self):
        """
        点击OK按键
        :return: True，False
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'homePage_resourceId', 'ok')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    def changeToICall50times(self):
        """
        压力测试（首页>more页面拨打Icall，50次）
        :return: True，False
        """
        k = 0
        for i in range(50):
            homePage().clickScreenHardKeyHomeButton()  # 点击Home硬按键
            time.sleep(1)
            homeActivity = pm().get_Current_Activity()
            if homeActivity == 'com.saicmotor.launcher.view.MainActivity':
                pass
            else:
                logger.info(str(i) + ' Fail ' + homeActivity)
                k = k + 1
            homePage().clickMore()  # 点击dock栏More按键页面
            time.sleep(1)
            morePageActivity = pm().get_Current_Activity()
            if morePageActivity == 'com.saicmotor.launcher.view.MoreActivity':
                pass
            else:
                logger.info(str(i) + ' Fail ' + morePageActivity)
                k = k + 1
            self.clickICall()  # 进入点击Icall
            time.sleep(1)
            self.clickOK()  # 点击OK
            time.sleep(1)
        if k == 0:
            return True
        else:
            logger.info('Fail times: ' + str(k))
            return False


morePage = india_D90_morePage()
