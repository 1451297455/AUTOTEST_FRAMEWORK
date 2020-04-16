# -*- coding: utf-8 -*-
# D90 首页
from page.BasePage import BasePage
from page.publicMethod import publicMethod as pm
from config import india_D90_propertiseConfig
from config import india_D90_hardKeyPropertiseConfig
import time


class india_D90_homePage(BasePage):

    # 点击导航图片
    def clickNav(self):
        element = pm.find_element_by_id(self, id=india_D90_propertiseConfig.homePageConfig.get('Navigation'))
        print("Click Navigation")
        return pm.click_by_element(self, element=element)

    # 点击进入天气
    def clickWeather(self):
        element = pm.find_element_by_id(self, id=india_D90_propertiseConfig.homePageConfig.get('Weather'))
        print("Click Weather")
        return pm.click_by_element(self, element=element)

    # 点击home键（建议使用publicMethod中的home键方法）
    def clickDockBarHome(self):
        element = pm.find_element_by_id(self, id=india_D90_propertiseConfig.homePageConfig.get('DockBarHomeKey'))
        print("Click homePage")
        return pm.click_by_element(self, element=element)

    # 点击进入MUSIC
    def clickMusic(self):
        element = pm.find_element_by_id(self, id=india_D90_propertiseConfig.homePageConfig.get('Music'))
        print("Click MUSIC")
        return pm.click_by_element(self, element=element)

    # 点击Dock栏中的MUSIC
    def clickDockBarMusic(self):
        element = pm.find_element_by_id(self, id=india_D90_propertiseConfig.homePageConfig.get('DockBarHomeKey'))
        print("Click Dock Bar MUSIC")
        return pm.click_by_element(self, element=element)

    # 点击导航图标进入地图
    def clickNavi(self):
        element = pm.find_element_by_id(self, id=india_D90_propertiseConfig.homePageConfig.get('Navigation'))
        print("Click NavIcon")
        return pm.click_by_element(self, element=element)

    # 点击Dock栏中的地图导航
    def clickDockBarMap(self):
        element = pm.find_element_by_id(self, id=india_D90_propertiseConfig.homePageConfig.get('DockBarNavi'))
        print("Click Dock Bar Navi")
        return pm.click_by_element(self, element=element)

    # 点击Dock栏中的VR
    def clickDockBarVR(self):
        element = pm.find_element_by_id(self, id=india_D90_propertiseConfig.homePageConfig.get('DockBarVR'))
        print("Click Dock Bar VR")
        return pm.click_by_element(self, element=element)

    # 点击Dock栏中锁屏
    def clickDockBarLockScreen(self):
        element = pm.find_element_by_id(self, id=india_D90_propertiseConfig.homePageConfig.get('DockBarLockScreen'))
        print("Click Dock Bar Lock Screen")
        return pm.click_by_element(self, element=element)

    # 点击Dock栏中车控
    def clickDockBarVehicleSetting(self):
        element = pm.find_element_by_id(self, id=india_D90_propertiseConfig.homePageConfig.get('DockBarVehicleSetting'))
        print("Click Dock Bar VehicleSetting")
        return pm.click_by_element(self, element=element)

    # 点击屏幕Home键
    def clickScreenHomeKey(self):
        pm.pressButtenByKeyevent(self, 'ScreenHomeKey')  # 使用屏幕Home键返回首页
        element = pm.find_element_by_id(self,
                                        id=india_D90_hardKeyPropertiseConfig.homePageConfig.get(
                                            'Navigation'))
        return pm.click_by_element(self, element=element)  # 检测到地图模块控件说明已返回首页

    # 点击屏幕外侧音量+
    def clickScreenVolumeUp(self):
        pm.pressButtenByKeyevent(self, 'ScreenVolumeUp')  # 使用屏幕Home键返回首页
        element = pm.find_element_by_id(self,
                                        id=india_D90_hardKeyPropertiseConfig.homePageConfig.get(
                                            'VolumnBar'))
        return pm.click_by_element(self, element=element)  # 检测到地图模块控件说明已返回首页

    # 点击屏幕外侧音量-
    def clickScreenVolumeDown(self):
        pm.pressButtenByKeyevent(self, 'ScreenVolumeDown')  # 使用屏幕Home键返回首页
        element = pm.find_element_by_id(self,
                                        id=india_D90_hardKeyPropertiseConfig.homePageConfig.get(
                                            'VolumnBar'))
        return pm.click_by_element(self, element=element)  # 检测到地图模块控件说明已返回首页

    # 方控音量+
    def clickSteeringWheelVolumeUp(self):
        pm.pressButtenByKeyevent(self, 'SteeringWheelVolumeUp')  # 使用屏幕Home键返回首页
        element = pm.find_element_by_id(self,
                                        id=india_D90_hardKeyPropertiseConfig.homePageConfig.get(
                                            'VolumnBar'))
        return pm.click_by_element(self, element=element)  # 检测到地图模块控件说明已返回首页

    # 方控音量-
    def clickSteeringWheelVolumeDown(self):
        pm.pressButtenByKeyevent(self, 'SteeringWheelVolumeDown')  # 使用屏幕Home键返回首页
        element = pm.find_element_by_id(self,
                                        id=india_D90_hardKeyPropertiseConfig.homePageConfig.get(
                                            'VolumnBar'))
        return pm.click_by_element(self, element=element)  # 检测到地图模块控件说明已返回首页

    # 方控音量-
    def clickSteeringWheelVolumeUp(self):
        pm.pressButtenByKeyevent(self, 'clickSteeringWheelVolumeUp')  # 使用屏幕Home键返回首页
        element = pm.find_element_by_id(self,
                                            id=india_D90_hardKeyPropertiseConfig.homePageConfig.get(
                                                'VolumnBar'))
        return pm.click_by_element(self, element=element)  # 检测到地图模块控件说明已返回首页


    ##########################################################
    ###########################分割线#########################
    ##########################################################
    ##########################################################



if __name__ == '__main__':
    # homePage.clickHome()
    pass
