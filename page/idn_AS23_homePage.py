# -*- coding: utf-8 -*-
# 印尼AS23 首页方法
from UIconfig.Base import Base
from page.PublicMethod import PublicMethod as pm
import time
import UIconfig.logger as loggers

logger = loggers.Logger()


class idn_AS23_homePage(Base):

    # 检查AS23P 首页右侧recycles栏中的泰语是否正确
    def checkHomePageRecyclerView(self):
        # logger.info('--checkHomePageRecyclerView--')
        i = 0
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'homePage_resourceId', 'RecycleView')
        value = pm().readConfigItemsByModule('thailand_AS23P', 'homePage_recyclerView_txt')
        elist = pm().find_element_by_id(id=id)
        flag = True
        if elist:
            for i in value:
                # logger.info(i)
                # logger.info(i[1])
                pm().swipe_to_beginning()
                time.sleep(1)
                pm().swipe_forwardto_description(i[1])
                element = pm().find_element_by_text(i[1])
                if element.exists():
                    continue
                else:
                    # 元素不存在，flag置为false
                    # logger.info(i[1] + ' is not exist ')
                    flag = False
            return flag
        else:
            # logger.info('homepage is not exist')
            return False

    # 点击Dock栏中Home键
    def clickHomeButton(self):
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'homePage_resourceId', 'HomeButton')
        # logger.info(id)
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    # 点击车机首页Radio按键进入Radio页面
    def clickRadio(self):
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'homePage_recyclerView_txt', 'Radio')
        # logger.info('Radio Name ' + name)
        element = pm().find_element_by_text(name)
        if not element.exists:
            pm().swipe_to_beginning()
            time.sleep(1)
            pm().swipe_forwardto_description(name)
            newElement = pm().find_element_by_text(name)
            if newElement.exists:
                return pm().click_by_element(element=newElement)
            else:
                return False
        else:
            return pm().click_by_element(element=element)

    # 点击车机首页BTPhone按键进入BTPshone页面
    def clickBTPhone(self):
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'homePage_recyclerView_txt', 'BTPHONE')
        # logger.info('BTPHONE Name ' + name)
        element = pm().find_element_by_text(name)
        if not element.exists:
            pm().swipe_to_beginning()
            time.sleep(1)
            pm().swipe_forwardto_description(name)
            newElement = pm().find_element_by_text(name)
            if newElement.exists:
                return pm().click_by_element(element=newElement)
            else:
                return False
        else:
            return pm().click_by_element(element=element)

    # 点击车机首页lifeStyle按键进入lifeStyle页面
    def clickLifeStyle(self):
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'homePage_recyclerView_txt', 'lifestyle')
        # logger.info('LifeStyle Name ' + name)
        element = pm().find_element_by_text(name)
        if not element.exists:
            pm().swipe_to_beginning()
            time.sleep(1)
            pm().swipe_forwardto_description(name)
            newElement = pm().find_element_by_text(name)
            if newElement.exists:
                return pm().click_by_element(element=newElement)
            else:
                return False
        else:
            return pm().click_by_element(element=element)

    # 点击进入CallCentre页面
    def clickCallCentre(self):
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'homePage_recyclerView_txt', 'CALLCENTRE')
        # logger.info('LifeStyle Name ' + name)
        element = pm().find_element_by_text(name)
        if not element.exists:
            pm().swipe_to_beginning()
            time.sleep(1)
            pm().swipe_forwardto_description(name)
            newElement = pm().find_element_by_text(name)
            if newElement.exists:
                return pm().click_by_element(element=newElement)
            else:
                return False
        else:
            return pm().click_by_element(element=element)

    # 点击进入CarPhone页面
    def clickCarPhone(self):
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'homePage_recyclerView_txt', 'Carphone')
        # logger.info('CarPhone Name ' + name)
        element = pm().find_element_by_text(name)
        if not element.exists:
            pm().swipe_to_beginning()
            time.sleep(1)
            pm().swipe_forwardto_description(name)
            newElement = pm().find_element_by_text(name)
            if newElement.exists:
                return pm().click_by_element(element=newElement)
            else:
                return False
        else:
            return pm().click_by_element(element=element)

    # 点击进入Inbox页面
    def clickInbox(self):
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'homePage_recyclerView_txt', 'Inbox')
        # logger.info('CarPhone Name ' + name)
        element = pm().find_element_by_text(name)
        if not element.exists:
            pm().swipe_to_beginning()
            time.sleep(1)
            pm().swipe_forwardto_description(name)
            newElement = pm().find_element_by_text(name)
            if newElement.exists:
                return pm().click_by_element(element=newElement)
            else:
                return False
        else:
            return pm().click_by_element(element=element)

    # 点击进入Folder页面
    def clickFolder(self):
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'homePage_recyclerView_txt', 'Folder')
        # logger.info('CarPhone Name ' + name)
        element = pm().find_element_by_text(name)
        if not element.exists:
            pm().swipe_to_beginning()
            time.sleep(1)
            pm().swipe_forwardto_description(name)
            newElement = pm().find_element_by_text(name)
            if newElement.exists:
                return pm().click_by_element(element=newElement)
            else:
                return False
        else:
            return pm().click_by_element(element=element)

    # 点击进入PassionService页面
    def clickPassionService(self):
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'homePage_recyclerView_txt', 'PassionService')
        # logger.info('PassionService ' + name)
        element = pm().find_element_by_text(name)
        if not element.exists:
            pm().swipe_to_beginning()
            time.sleep(1)
            pm().swipe_forwardto_description(name)
            newElement = pm().find_element_by_text(name)
            if newElement.exists:
                return pm().click_by_element(element=newElement)
            else:
                return False
        else:
            return pm().click_by_element(element=element)

    # 点击进入Battery页面
    def clickBatteryCard(self):
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'Battery_resourceId', 'Battery')
        # logger.info('BatteryCard ' + id)
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    # 点击进入AC页面
    def clickACCard(self):
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'AC_resourceId', 'AC')
        # logger.info('ACCard ' + id)
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    # 点击首页Setting页面
    def clickSetting(self):
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'homePage_recyclerView_txt', 'Setting')
        # logger.info('Setting ' + name)
        element = pm().find_element_by_text(name)
        if not element.exists:
            pm().swipe_to_beginning()
            time.sleep(1)
            pm().swipe_forwardto_description(name)
            newElement = pm().find_element_by_text(name)
            if newElement.exists:
                return pm().click_by_element(element=newElement)
            else:
                return False
        else:
            return pm().click_by_element(element=element)

    # 点击首页VehicleSetting页面
    def clickVehicleSetting(self):
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'homePage_recyclerView_txt', 'VehicleSetting')
        # logger.info('VehicleSetting ' + name)
        element = pm().find_element_by_text(name)
        if not element.exists:
            pm().swipe_to_beginning()
            time.sleep(1)
            pm().swipe_forwardto_description(name)
            newElement = pm().find_element_by_text(name)
            if newElement.exists:
                return pm().click_by_element(element=newElement)
            else:
                return False
        else:
            return pm().click_by_element(element=element)

    # 点击进入个人中心
    def clickAccount(self):
        recycleViewid = pm().readConfigByModuleAndKey('thailand_AS23P', 'homePage_resourceId', 'RecycleView')
        elist = pm().find_element_by_id(id=recycleViewid)
        pm().swipe_down_by_element(elist)  # 滑动首页list列表至最上方
        time.sleep(2)
        Xpath = pm().readConfigByModuleAndKey('thailand_AS23P', 'homePage_resourceId', 'Account')
        element = pm().find_element_by_xpath(xpath=Xpath)  # 通过Xpath定位
        # logger.info('111')
        return pm().click_by_element(element)

    # 点击泰国AS23P 主页Music Layout进入音乐页面
    def clickMusicByLayout(self):
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'homePage_resourceId', 'Music_layout')
        element = pm().find_element_by_text(name)
        return pm().click_by_element(element=element)

    # 点击泰国AS23P 主页右侧导航栏中的多媒体图标进入音乐页面
    def clickMusicByNavi(self):
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'homePage_resourceId', 'Music_Navi_txt')
        element = pm().find_element_by_text(name)
        return pm().click_by_element(element=element)

    # 点击首页多媒体卡片下一首按键
    def clickNextSongButton(self):
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'homePage_resourceId', 'nextSongButton')
        element = pm().find_element_by_text(name)
        return pm().click_by_element(element=element)

    # 点击首页多媒体卡片上一首按键
    def clickPrevSongButton(self):
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'homePage_resourceId', 'prevSongButton')
        element = pm().find_element_by_text(name)
        return pm().click_by_element(element=element)

    # 点击首页多媒体卡片播放/暂停按键
    def clickPlayButton(self):
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'homePage_resourceId', 'playButton')
        element = pm().find_element_by_text(name)
        return pm().click_by_element(element=element)


if __name__ == '__main__':
    pass
