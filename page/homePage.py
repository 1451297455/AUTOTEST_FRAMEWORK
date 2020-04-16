# -*- coding: utf-8 -*-
from page.BasePage import BasePage
from page.publicMethod import publicMethod as pm
from config import india_D90_propertiseConfig
import time


class homePage(BasePage):

    # 点击导航图片
    def clickNav(self):
        '''
        click home page Navi button
        :return:
        '''
        element = pm.find_element_by_id(self, id="com.archermind.saic.launcher:id/iv_navi_image")
        print("Click Nav")
        return pm.click_by_element(self, element=element)

    # 点击进入天气
    def clickWeather(self):
        '''
        click homePage Weather button
        :return:
        '''
        element = pm.find_element_by_id(self, id="com.archermind.saic.launcher:id/iv_weather_big")
        print("Click Weather")
        return pm.click_by_element(self, element=element)

    # 点击进入电量管理
    def clickEV_BATTERY(self):
        '''
        click homePage Weather button
        :return:
        '''
        element = pm._find_element_by_text(self, text="EV BATTERY")
        print("Click EV BATTERY")
        return pm.click_by_element(self, element=element)

    # 点击进入MUSIC
    def clickVehicle(self):
        element = pm._find_element_by_text(self, text="MUSIC")
        print("Click MUSIC")
        return pm.click_by_element(self, element=element)

    # 点击进入MG iSMART
    def clickMG(self):
        print('start find ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        element = pm._find_element_by_text(self, "MG iSMART")
        print("Click MG iSMART")
        print('end find ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

        return pm.click_by_element(self, element=element)

    # 点击进入MG Radio
    def clickRadio(self):
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        element = pm._find_element_by_text(self, "Radio")
        print("Click Radio")
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        return pm.click_by_element(self, element=element)

    # 点击进入BT Phone
    def clickBT_Phone(self):
        element = pm._find_element_by_text(self, "BT Phone")
        print("Click BT Phone")
        return pm.click_by_element(self, element=element)

    # 点击进入Gaana
    def clickBT_Phone(self):
        element = pm._find_element_by_text(self, "Gaana")
        print("Click Gaana")
        return pm.click_by_element(self, element=element)

    # 点击进入Setting
    def clickSetting(self):
        element = pm._find_element_by_text(self, "Setting")
        print("Click Setting")
        return pm.click_by_element(self, element=element)

    # 点击进入I-Call
    def clickICall(self):
        element = pm._find_element_by_text(self, text="I-Call")
        print("Click I-Call")
        return pm.click_by_element(self, element=element)

    # 点击进入VehicleSetting
    def clickVehicle(self):
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        element = pm._find_element_by_text(self, text="Vehicle Setting")
        print("Click Vehicle_setting")
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        return pm.click_by_element(self, element=element)

    # 点击进入Folder
    def clickFolder(self):
        element = pm._find_element_by_text(self, text="Folder")
        print("Click Folder")
        return pm.click_by_element(self, element=element)

    # 滑动点击进入Inbox
    def clickInbox(self):
        # 再此休眠1秒确保该指令之前的动作完成
        time.sleep(1)
        # 获取主页右侧RecyclerView并上拉
        BasePage._find_element_by_ClassName(self, className="android.support.v7.widget.RecyclerView").swipe('up',
                                                                                                            steps=6)
        print("swipe test")
        element = pm._find_element_by_text(self, text="Inbox")
        print("swipe Inbox")
        return pm.click_by_element(self, element=element)

    # ***滑动点击进入用户中心(Xpath定位)***
    def clickSaicAccount(self):
        elements = []
        # 再此休眠1秒确保该指令之前的动作完成
        time.sleep(1)
        elements = BasePage.find_element_by_Xpath(self,
                                                  Xpath='//*[@resource-id="com.archermind.saic.launcher:id/rv_menu_list"]/android.view.ViewGroup[1]')
        return pm.click_by_element(self, element=elements)

    # 点击右侧导航Icon图标进入地图
    def clickNavIcon(self):
        element = pm.find_element_by_id(self, id="com.archermind.saic.launcher:id/iv_navi_map")
        print("Click NavIcon")
        return pm.click_by_element(self, element=element)

    # 点击右侧音乐Icon图标进入地图
    def clickMusicIcon(self):
        element = pm.find_element_by_id(self, id="com.archermind.saic.launcher:id/iv_navi_media")
        print("Click MusicIcon")
        return pm.click_by_element(self, element=element)

    # 点击右侧车控Icon图标进入地图
    def clickVehicleSettingIcon(self):
        element = pm.find_element_by_id(self, id="com.archermind.saic.launcher:id/iv_navi_car")
        print("Click Vehicle Setting")
        return pm.click_by_element(self, element=element)

    # 点击右侧锁屏Icon图标进入地图
    def clickLock(self):
        element = pm.find_element_by_id(self, id="com.archermind.saic.launcher:id/iv_navi_lock")
        print("Click Lock")
        return pm.click_by_element(self, element=element)

    # 点击home键（建议使用publicMethod中的home键方法）
    def clickHome(self):
        element = BasePage.find_element_by_id(self, id="com.archermind.saic.launcher:id/iv_home")
        print("Click homepage")
        return pm.click_by_element(self, element=element)

    # 点击右侧VR Icon图标进入地图
    def clickVR(self):
        element = BasePage.find_element_by_id(self, id="com.archermind.saic.launcher:id/iv_vr")
        print("Click VR")
        return pm.click_by_element(self, element=element)

    def clickMusicIcon(self):
        '''
        click homePage music Icon
        :return:
        '''
        element = pm.find_element_by_id(self, id="launcher.n4.launcher82:id/img_music_default")
        return pm.click_by_element(self, element=element)

    def clickMusicPause(self):
        '''
        click homePage music pause Button
        :return:
        '''
        element = pm.find_element_by_id(self, id="launcher.n4.launcher82:id/ll_music_control_bg")
        return pm.click_by_element(self, element=element)

    def clickMusicNextSong(self):
        '''
        click homePage next song button
        :return:
        '''
        element = pm.find_element_by_id(self, id="launcher.n4.launcher82:id/btn_music_next")
        return pm.click_by_element(self, element=element)

    def clickMusicpreviousSong(self):
        '''
        click homePage previous song button
        :return:
        '''
        element = pm.find_element_by_id(self, id="launcher.n4.launcher82:id/btn_music_previous")
        return pm.click_by_element(self, element=element)

    def clickNaviCard(self):
        '''
        click homePage navi_card
        :return:
        '''
        element = pm.find_element_by_id(self, id="launcher.n4.launcher82:id/rl_navi_card")
        return pm.click_by_element(self, element=element)

    def clickUserCard(self):
        '''
        click homePage UserCard
        :return:
        '''
        element = pm.find_element_by_id(self, id="launcher.n4.launcher82:id/rl_user_card")
        return pm.click_by_element(self, element=element)

    def clickUserIcon(self):
        '''
        click homePage UserIcon
        :return:
        '''
        element = pm.find_element_by_id(self, id="launcher.n4.launcher82:id/cv_image")
        return pm.click_by_element(self, element=element)

    def getText(self):
        element = pm.find_element_by_id(self, "com.saic.roewe.iov:id/btn_login")
        value = element.get_text()
        return value

    def clickSearch(self):
        return pm.click_by_element(self, pm.find_element_by_id(self, 'com.saicmotor.weathers:id/tvRefreshWeather'))

    def inputPlace(self, place):
        element = pm.find_element_by_id(self, 'com.saicmotor.weathers:id/et_search')
        return element.send_keys(place)

    def getWeatherLocation(self):
        location = pm.find_element_by_id(self, id=india_D90_propertiseConfig.homePageConfig.get('WeatherCityName'))
        return pm.get_text_by_element(self, location)


if __name__ == '__main__':
    # homePage.clickHome()
    pass
