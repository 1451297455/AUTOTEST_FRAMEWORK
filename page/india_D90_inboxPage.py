# -*- coding: utf-8 -*-
from UIconfig.Base import Base
from page.PublicMethod import PublicMethod as pm
from page.india_D90_homePage import india_D90_homePage as homePage
from page.india_D90_morePage import morePage
import time, os
import UIconfig.logger as loggers

logger = loggers.Logger()
os.path.abspath('.')


class india_D90_inboxPage(Base):

    def checkInboxLoadingIconIsExist(self):
        """
        检查inbox是否处于loading状态
        :return: True, False
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'InboxPage', 'loadingIcon')
        element = pm().find_element_by_id(id=id)
        if element is not None:
            return True
        else:
            return False

    def clickTravelPlan(self):
        """
        点击进入TravelPlan目录
        :return: True点击成功，False点击失败
        """
        element = pm()._find_element_by_text(text='TRAVEL PLAN')
        pm().click_by_element(element)
        while True:
            if self.checkInboxLoadingIconIsExist():
                time.sleep(3)
            else:
                break
        return pm().click_by_element(element)  # 此处再次点击一下是为了确保已经在该页面。
        # PS：我就奇怪了。都是saic1.0的系统，有些项目可以通过捕捉当前栏目下相应高亮控件来确保已经切换到该页面。
        # 然而D90就没有这么做，问了开发人员，他们说都是一个框架的开发的人员不同。所以呈现方式不一样...传说中的百家争鸣吧。

    def clickPOI(self):
        """
        点击进入poi目录
        :return:True点击成功，False点击失败
        """
        element = pm().find_element_by_text(text='POI')
        while True:
            if self.checkInboxLoadingIconIsExist():
                time.sleep(3)
            else:
                break
        return pm().click_by_element(element)  # 此处再次点击一下是为了确保已经在该页面。
        # PS：我就奇怪了。都是saic1.0的系统，有些项目可以通过捕捉当前栏目下相应高亮控件来确保已经切换到该页面。
        # 然而D90就没有这么做，问了开发人员，他们说都是一个框架的开发的人员不同。所以呈现方式不一样...传说中的百家争鸣吧。

    def clickMessage(self):
        """
        点击进入Message目录
        :return:True点击成功，False点击失败
        """
        element = pm()._find_element_by_text(text='MESSAGE')
        while True:
            if self.checkInboxLoadingIconIsExist():
                time.sleep(3)
            else:
                break
        return pm().click_by_element(element)  # 此处再次点击一下是为了确保已经在该页面。
        # PS：我就奇怪了。都是saic1.0的系统，有些项目可以通过捕捉当前栏目下相应高亮控件来确保已经切换到该页面。
        # 然而D90就没有这么做，问了开发人员，他们说都是一个框架的开发的人员不同。所以呈现方式不一样...传说中的百家争鸣吧。

    def changeToInboxPage50times(self):
        """
        压力测试（首页>more页面点击Inbox，点击Travel Plan、POI、Message，50次）
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
            morePage.clickInbox()
            inboxPageActivity = pm().get_Current_Activity()
            if inboxPageActivity == 'com.saicmotor.saicinbox.module.inbox.InboxActivity':
                pass
            else:
                logger.info(str(i) + ' Fail ' + inboxPageActivity)
                k = k + 1
            self.clickTravelPlan()
            time.sleep(3)
            self.clickPOI()
            time.sleep(3)
            self.clickMessage()
            time.sleep(3)
        if k == 0:
            return True
        else:
            logger.info('Fail times: ' + str(k))
            return False


inboxPage = india_D90_inboxPage()
