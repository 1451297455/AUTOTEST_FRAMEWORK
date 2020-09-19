# -*- coding: utf-8 -*-
from UIconfig.Base import Base
from page.PublicMethod import PublicMethod as pm
from page.india_D90_homePage import india_D90_homePage as homePage
import os, time
import UIconfig.logger as loggers

logger = loggers.Logger()
os.path.abspath('.')


class india_D90_btPhonePage(Base):

    # 点击进入keypad目录
    def clickKeypad(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'BTPhonePage', 'keypad')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    # 点击进入recents目录
    def clickRecents(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'BTPhonePage', 'recents')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    # 点击进入contacts目录
    def clickContacts(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'BTPhonePage', 'contacts')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    # 点击delete
    def clickDelete(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'BTPhonePage', 'delete')
        element = pm().find_element_by_id(id=id)
        if element is not None:
            return pm().click_by_element(element)
        else:
            return False

    # 长按delete
    def long_clickDelete(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'BTPhonePage', 'delete')
        element = pm().find_element_by_id(id=id)
        if element is not None:
            return pm().long_click_by_element(element)
        else:
            return False

    # 点击one
    def clickOne(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'BTPhonePage', 'one')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    # 点击two
    def clickTwo(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'BTPhonePage', 'two')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    # 点击three
    def clickThree(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'BTPhonePage', 'three')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    # 点击four
    def clickFour(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'BTPhonePage', 'four')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    # 点击five
    def clickFive(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'BTPhonePage', 'five')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    # 点击six
    def clickSix(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'BTPhonePage', 'six')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    # 点击Seven
    def clickSeven(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'BTPhonePage', 'Seven')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    # 点击eight
    def clickEight(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'BTPhonePage', 'eight')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    # 点击nine
    def clickNine(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'BTPhonePage', 'nine')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    # 点击zero
    def clickZero(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'BTPhonePage', 'zero')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    # 点击star
    def clickStar(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'BTPhonePage', 'star')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    # 点击sharp
    def clickSharp(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'BTPhonePage', 'sharp')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    # 点击dial
    def clickDial(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'BTPhonePage', 'dial')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    # 点击star
    def clickStar(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'BTPhonePage', 'star')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    # 点击挂断
    def clickHangUp(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'BTPhonePage', 'hangUp')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    def changeToBTPhonePage50times(self):
        """
        压力测试（首页>蓝牙电话各页面切换，50次）
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
            homePage().clickBTPhoneXpath()  # 点击进入蓝牙电话
            time.sleep(1)
            btPhonePageActivity = pm().get_Current_Activity()
            if btPhonePageActivity == 'com.saicmotor.btphone.ui.activity.BTPhoneMainActivity':
                pass
            else:
                logger.info(str(i) + ' Fail ' + btPhonePageActivity)
                k = k + 1
            self.clickKeypad()
            time.sleep(1)
            self.clickRecents()
            time.sleep(1)
            self.clickContacts()
            time.sleep(1)
        if k == 0:
            return True
        else:
            logger.info('Fail times: ' + str(k))
            return False

    def changeToBTPhonePageDial10086_50times(self):
        """
        压力测试（首页>蓝牙电话各页面切换，50次）
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
            homePage().clickBTPhoneXpath()  # 点击进入蓝牙电话
            time.sleep(1)
            btPhonePageActivity = pm().get_Current_Activity()
            if btPhonePageActivity == 'com.saicmotor.btphone.ui.activity.BTPhoneMainActivity':
                pass
            else:
                logger.info(str(i) + ' Fail ' + btPhonePageActivity)
                k = k + 1
            self.clickKeypad()
            time.sleep(1)
            self.long_clickDelete()
            self.clickOne()
            self.clickZero()
            self.clickZero()
            self.clickEight()
            self.clickSix()
            self.clickDial()
            time.sleep(3)
            self.clickHangUp()
            self.clickContacts()
            time.sleep(1)
        if k == 0:
            return True
        else:
            logger.info('Fail times: ' + str(k))
            return False


btPhonePage = india_D90_btPhonePage()
