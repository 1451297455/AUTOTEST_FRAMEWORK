# -*- coding: utf-8 -*-
from UIconfig.Base import Base
from page.PublicMethod import PublicMethod as pm
from page.india_D90_homePage import india_D90_homePage as homePage
import time, os

os.path.abspath('.')


class india_D90_VehicleSettingPage(Base):

    def clickVehicleSettingList(self):
        """
        点击VehicleSetting栏
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'VehicleSettingPage', 'VehicleSettingTitle')
        element = pm().find_element_by_idAndText(id=id, text='VEHICLE SETTING')
        return pm().click_by_element(element)

    def clickDrivingAssistant(self):
        """
        点击Driving Assistant栏
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'VehicleSettingPage', 'VehicleSettingTitle')
        element = pm().find_element_by_idAndText(id=id, text='DRIVING ASSISTANT')
        return pm().click_by_element(element)

    def openVehicleSettingItem(self):
        """
        打开VehicleSetting栏
        :return: True点击成功，False点击失败
        """
        self.swipeDownVehicleSettingList()  # 置顶
        element = pm().find_element_by_text(text='Lamp')  # 判断是否有Lamp选项，如果有则是已经打开VehicleSetting栏
        if element is not None:
            return True
        else:
            return self.clickVehicleSettingList()

    def closeVehicleSettingItem(self):
        """
        关闭VehicleSetting栏
        :return: True点击成功，False点击失败
        """
        self.swipeDownVehicleSettingList()  # 置顶
        element = pm().find_element_by_text(text='Lamp')  # 判断是否有Lamp选项，如果有则是已经打开VehicleSetting栏
        if element is None:
            return True
        else:
            return self.clickVehicleSettingList()

    def openDivingAssistantItem(self):
        """
        打开DivingAssistant栏
        :return: True点击成功，False点击失败
        """
        self.swipeUpVehicleSettingList()  # 置底
        element = pm().find_element_by_text(
            text='Parking Distance Control')  # 判断是否有Parking Distance Control选项，如果有则是已经打开DivingAssistant栏
        if element is not None:
            return True
        else:
            return self.clickVehicleSettingList()

    def closeDivingAssistantItem(self):
        """
        关闭DivingAssistant栏
        :return: True点击成功，False点击失败
        """
        self.swipeUpVehicleSettingList()  # 置底
        element = pm().find_element_by_text(
            text='Parking Distance Control')  # 判断是否有Parking Distance Control选项，如果有则是已经打开DivingAssistant栏
        if element is None:
            return True
        else:
            return self.clickVehicleSettingList()

    def swipeUpVehicleSettingList(self):
        """
        从下至上滑动VehicleSetting列表
        :return: True, False
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'VehicleSettingPage', 'VehicleSettingList')
        element = pm().find_element_by_id(id=id)
        return pm().swipe_up_by_element(element)

    def swipeDownVehicleSettingList(self):
        """
        从上至下滑动VehicleSetting列表
        :return: True, False
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'VehicleSettingPage', 'VehicleSettingList')
        element = pm().find_element_by_id(id=id)
        return pm().swipe_down_by_element(element)

    def clickLampItem(self):
        """
        点击Lamp列
        :return: True,False
        """
        element = pm().find_element_by_text(text='Lamp')
        return pm().click_by_element(element)

    def clickFindMyCarPage(self):
        """
        点击FIND MY CAR列
        :return: True,False
        """
        element = pm().find_element_by_text(text='FIND MY CAR')
        return pm().click_by_element(element)

    def clickFlashingHonking(self):
        """
        点击FlashingHonking按键
        :return: True,False
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'VehicleSettingPage', 'FlashingHonking')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    def clickFlashing(self):
        """
        点击Flashing按键
        :return: True,False
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'VehicleSettingPage', 'Flashing')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    def clickFollowMeHomePage(self):
        """
        点击FOLLOW ME HOME列
        :return: True,False
        """
        element = pm().find_element_by_text(text='FOLLOW ME HOME')
        return pm().click_by_element(element)

    def clickFollowMeHomeOff(self):
        """
        点击FollowMeHome Off按键
        :return: True,False
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'VehicleSettingPage', 'FollowMeHomeOff')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    def clickFollowMeHome30s(self):
        """
        点击FollowMeHome 30s按键
        :return: True,False
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'VehicleSettingPage', 'FollowMeHome30s')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    def clickFollowMeHome60s(self):
        """
        点击FollowMeHome 60s按键
        :return: True,False
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'VehicleSettingPage', 'FollowMeHome60s')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    def clickFollowMeHome90s(self):
        """
        点击FollowMeHome 90s按键
        :return: True,False
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'VehicleSettingPage', 'FollowMeHome90s')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    def clickDrivingAutoMaticLockPage(self):
        """
        点击FOLLOW ME HOME列
        :return: True,False
        """
        element = pm().find_element_by_text(text='DRIVING AUTOMATIC LOCK')
        return pm().click_by_element(element)


































    def clickLockItem(self):
        """
        点击Lock列
        :return: True,False
        """
        element = pm().find_element_by_text(text='Lock')
        return pm().click_by_element(element)

    def clickRearViewMirror_SeatKeyMemoryItem(self):
        """
        点击Rear View Mirror & Seat Key Memory列
        :return: True,False
        """
        self.swipeDownVehicleSettingList()
        Xpath = pm().readConfigByModuleAndKey('india_D90', 'VehicleSettingPage', 'RearViewMirror')
        element = pm().find_element_by_Xpath(Xpath=Xpath)
        return pm().click_by_element(element)

    def clickAmnientLightItem(self):
        """
        点击AmnientLight列
        :return: True, False
        """
        element = pm().find_element_by_text(text='Ambient Light')
        return pm().click_by_element(element)

    def clickTyreItem(self):
        """
        点击Tyre列
        :return: True, False
        """
        element = pm().find_element_by_text(text='Tyre')
        return pm().click_by_element(element)



