# -*- coding: utf-8 -*-
# australia AS23 首页方法
from UIconfig.Base import Base
from page.PublicMethod import PublicMethod as pm
import time
import UIconfig.logger as loggers

logger = loggers.Logger()


class australia_AS23_homePage(Base):

    def clickVRButton(self):
        """
        点击右侧Dock栏中VR Button进入VR页面
        :return: True,False
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'homePage_resourceId', 'VRButton')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickMapButton(self):
        """
        点击右侧Dock栏中MapButton进入Map页面
        :return: True,False
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'homePage_resourceId', 'MapButton')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickMediaButton(self):
        """
        点击右侧Dock栏中MediaButton进入Media页面
        :return: True,False
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'homePage_resourceId', 'MediaButton')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickACButton(self):
        """
        点击右侧Dock栏中AC Button进入AC页面
        :return: True,False
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'homePage_resourceId', 'ACButton')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickLockButton(self):
        """
        点击右侧Dock栏中Lock Button进入Lock页面
        :return: True,False
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'homePage_resourceId', 'LockButton')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickHomeButton(self):
        """
        点击右侧Dock栏中Dock栏中Home键
        :return: True,False
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'homePage_resourceId', 'HomeButton')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickRecycleViewByItemName(self, itemName):
        """
        点击车机首页右侧滑动列表进入模块
        :param itemName: ：Radio、BTphone、Setting、More等
        :return: True,False
        """
        item = pm().readConfigByModuleAndKey('australia_AS23', 'homePage_recyclerView_txt', itemName)
        recycleViewResourceId = pm().readConfigByModuleAndKey('australia_AS23', 'homePage_resourceId', 'RecycleView')
        recycleViewElement = pm().find_element_by_id(id=recycleViewResourceId)
        pm().swipe_to_beginning_by_id(id=recycleViewResourceId)
        for i in range(2):
            newElement = pm().find_element_by_Xpath(
                Xpath="//*[@text='" + itemName + "' or @text='" + item + "']")  # 通过Xpath正则兼容泰语字符
            if not newElement.exists:
                pm().swipe_up_by_element(element=recycleViewElement)
            else:
                return pm().click_by_element(element=newElement)
        return False

    def clickAccount(self):
        """
        点击进入个人中心
        :return: True,False
        """
        recycleViewid = pm().readConfigByModuleAndKey('australia_AS23', 'homePage_resourceId', 'RecycleView')
        elist = pm().find_element_by_id(id=recycleViewid)
        pm().swipe_down_by_element(elist)  # 滑动首页list列表至最上方
        time.sleep(2)
        Xpath = pm().readConfigByModuleAndKey('australia_AS23', 'homePage_resourceId', 'Account')
        element = pm().find_element_by_Xpath(Xpath=Xpath)  # 通过Xpath定位
        return pm().click_by_element(element)

    def clickMusicByLayout(self):
        """
        点击主页Music Layout进入音乐页面
        :return: True,False
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'homePage_resourceId', 'Music_layout')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickWeatherByLayout(self):
        """
        点击主页Weather Layout进入音乐页面
        :return: True,False
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'homePage_resourceId', 'Weather_layout')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickACByLayout(self):
        """
        点击主页AC Layout进入音乐页面
        :return: True,False
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'homePage_resourceId', 'AC_layout')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickMapByLayout(self):
        """
        点击主页Map Layout进入音乐页面
        :return: True,False
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'homePage_resourceId', 'Map_layout')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickNextSongButton(self):
        """
        点击首页多媒体卡片下一首按键
        :return: True,False
        """
        name = pm().readConfigByModuleAndKey('australia_AS23', 'homePage_resourceId', 'nextSongButton')
        element = pm().find_element_by_text(name)
        return pm().click_by_element(element=element)

    def clickPrevSongButton(self):
        """
        点击首页多媒体卡片上一首按键
        :return: True,False
        """
        name = pm().readConfigByModuleAndKey('australia_AS23', 'homePage_resourceId', 'prevSongButton')
        element = pm().find_element_by_text(name)
        return pm().click_by_element(element=element)

    def clickPlayButton(self):
        """
        点击首页多媒体卡片播放/暂停按键
        :return:  True,False
        """
        name = pm().readConfigByModuleAndKey('australia_AS23', 'homePage_resourceId', 'playButton')
        element = pm().find_element_by_text(name)
        return pm().click_by_element(element=element)


if __name__ == '__main__':
    pass
