# -*- coding: utf-8 -*-
# D90 首页
from UIconfig.Base import Base
from page.PublicMethod import PublicMethod as pm
import time
import os
import UIconfig.logger as loggers

logger = loggers.Logger()
os.path.abspath('.')


class india_D90_homePage(Base):

    def clickNav(self):
        """
        点击导航图片
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'homePage_resourceId', 'Navigation_Layout')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickWeather(self):
        """
        点击进入天气
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'homePage_resourceId', 'Weather_Layout')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickAC(self):
        """
        点击进入AC
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'homePage_resourceId', 'AC')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickACAirPlus(self):
        """
        点击进入ACAirPlus
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'homePage_resourceId', 'ACAirPlus')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickMusic(self):
        """
        点击进入MUSIC
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'homePage_resourceId', 'Music_Layout')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def getMusicSource(self):
        """
        获取当前音乐来源（USB Music、BT Music、Gaana）
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'homePage_resourceId', 'CurrentMusicSource')
        element = pm().find_element_by_id(id=id)
        return element.get_text()

    def clickMusicPreButton(self):
        """
        点击首页music上一曲按键(已附加判断是否歌曲名称变化)
        :return: True点击成功，False点击失败
        """
        xpath = pm().readConfigByModuleAndKey('india_D90', 'homePage_resourceId', 'Next')
        element = pm().find_element_by_xpath(xpath=xpath)
        id = pm().readConfigByModuleAndKey('india_D90', 'homePage_resourceId', 'MusicTitle')
        songNameelement = pm().find_element_by_id(id=id)
        songNameBeforeChange = songNameelement.get_text()
        pm().click_by_element(element=element)
        time.sleep(3)
        songNameAfterChange = songNameelement.get_text()
        if songNameBeforeChange == songNameAfterChange:
            return False
        else:
            return True

    def clickMusicPlayButton(self):
        """
        点击MUSIC播放按键
        :return: True点击成功，False点击失败
        """
        xpath = pm().readConfigByModuleAndKey('india_D90', 'homePage_resourceId', 'Play')
        element = pm().find_element_by_xpath(xpath=xpath)
        return pm().click_by_element(element=element)

    def clickMusicNextButton(self):
        """
        点击进入MUSIC下一曲按键(已附加判断是否歌曲名称变化)
        :return: True点击成功，False点击失败
        """
        xpath = pm().readConfigByModuleAndKey('india_D90', 'homePage_resourceId', 'Pre')
        element = pm().find_element_by_xpath(xpath=xpath)
        id = pm().readConfigByModuleAndKey('india_D90', 'homePage_resourceId', 'MusicTitle')
        songNameelement = pm().find_element_by_id(id=id)
        songNameBeforeChange = songNameelement.get_text()
        pm().click_by_element(element=element)
        time.sleep(3)
        songNameAfterChange = songNameelement.get_text()
        if songNameBeforeChange == songNameAfterChange:
            return False
        else:
            return True

    def clickRadio(self):
        """
        点击进入Radio
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'homePage_resourceId', 'Radio_Layout')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def getRadioChannle(self):
        """
        获取首页调频（用于切换频道时附加校验调频是否变化）
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'homePage_resourceId', 'Radio_Channle')
        element = pm().find_element_by_id(id=id)
        return element.get_text()

    def clickRadioPreButton(self):
        """
        点击Radio上一首按钮(已附加判断是否调频名称变化)
        :return: True点击成功，False点击失败
        """
        radioTxtId = pm().readConfigByModuleAndKey('india_D90', 'homePage_resourceId', 'Radio_Txt')
        element = pm().find_element_by_id(id=radioTxtId)
        radioPreId = pm().readConfigByModuleAndKey('india_D90', 'homePage_resourceId', 'Pre')
        playButtonElement = element.sibling(resourceId=radioPreId)
        radioChannleBeforeChange = self.getRadioChannle()
        pm().click_by_element(element=playButtonElement)
        time.sleep(3)
        radioChannleAfterChange = self.getRadioChannle()
        if radioChannleAfterChange == radioChannleBeforeChange:
            return False
        else:
            return True

    def clickRadioNextButton(self):
        """
        点击Radio下一首按钮(已附加判断是否调频名称变化)
        :return: True点击成功，False点击失败
        """
        radioTxtId = pm().readConfigByModuleAndKey('india_D90', 'homePage_resourceId', 'Radio_Txt')
        element = pm().find_element_by_id(id=radioTxtId)
        radioNextId = pm().readConfigByModuleAndKey('india_D90', 'homePage_resourceId', 'Next')
        playButtonElement = element.sibling(resourceId=radioNextId)
        radioChannleBeforeChange = self.getRadioChannle()
        pm().click_by_element(element=playButtonElement)
        time.sleep(3)
        radioChannleAfterChange = self.getRadioChannle()
        if radioChannleAfterChange == radioChannleBeforeChange:
            return False
        else:
            return True

    def clickRadioPlayButton(self):
        """
        点击Radio播放
        :return: True点击成功，False点击失败
        """
        radioTxtId = pm().readConfigByModuleAndKey('india_D90', 'homePage_resourceId', 'Radio_Txt')
        radioPlayId = pm().readConfigByModuleAndKey('india_D90', 'homePage_resourceId', 'Play')
        element = pm().find_element_by_id(id=radioTxtId)
        playButtonElement = element.sibling(resourceId=radioPlayId)
        return pm().click_by_element(element=playButtonElement)

    def clickSaicAccount(self):
        """
        点击进入个人中心
        :return: True点击成功，False点击失败
        """
        Xpath = pm().readConfigByModuleAndKey('india_D90', 'homePage_resourceId', 'SaicAccountXpath')
        element = pm().find_element_by_xpath(xpath=Xpath)
        return pm().click_by_element(element)

    def clickBTPhoneXpath(self):
        """
        点击进入蓝牙电话页面
        :return: True点击成功，False点击失败
        """
        Xpath = pm().readConfigByModuleAndKey('india_D90', 'homePage_resourceId', 'BTPhoneXpath')
        element = pm().find_element_by_xpath(xpath=Xpath)
        return pm().click_by_element(element)

    def clickCarPlay(self):
        """
        点击进入Carplay
        :return: True点击成功，False点击失败
        """
        Xpath = pm().readConfigByModuleAndKey('india_D90', 'homePage_resourceId', 'CarPlayXpath')
        element = pm().find_element_by_xpath(xpath=Xpath)
        return pm().click_by_element(element)

    def clickAndroidAuto(self):
        """
        点击进入AndroidAuto
        :return: True点击成功，False点击失败
        """
        Xpath = pm().readConfigByModuleAndKey('india_D90', 'homePage_resourceId', 'AndroidAutoXpath')
        element = pm().find_element_by_xpath(xpath=Xpath)
        return pm().click_by_element(element)

    def clickGanna(self):
        """
        点击进入Ganna
        :return: True点击成功，False点击失败
        """
        Xpath = pm().readConfigByModuleAndKey('india_D90', 'homePage_resourceId', 'GannaXpath')
        element = pm().find_element_by_xpath(xpath=Xpath)
        return pm().click_by_element(element)

    def clickMore(self):
        """
        点击进入More页面
        :return: True点击成功，False点击失败
        """
        Xpath = pm().readConfigByModuleAndKey('india_D90', 'homePage_resourceId', 'MoreXpath')
        element = pm().find_element_by_xpath(xpath=Xpath)
        return pm().click_by_element(element)

    def clickHomeButton(self):
        """
        点击Dock栏中Home键
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'homePage_resourceId', 'DockBarHomeKey')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickDockBarMusic(self):
        """
        点击Dock栏中的MUSIC
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'homePage_resourceId', 'DockBarMusic')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickDockBarVR(self):
        """
        点击Dock栏中的VR
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'homePage_resourceId', 'DockBarVR')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickDockBarLockScreen(self):
        """
        点击Dock栏中锁屏
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'homePage_resourceId', 'DockBarLockScreen')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickDockBarVehicleSetting(self):
        """
        点击Dock栏中车控
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'homePage_resourceId', 'DockBarVehicleSetting')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickScreenHardKeyHomeButton(self):
        """
        点击屏幕硬按键Home键
        :return: True点击成功，False点击失败
        """
        keyEvent = pm().readConfigByModuleAndKey('india_D90', 'HardKeyEvent', 'ScreenHomeKey')
        os.system(keyEvent)
        return True

    def clickScreenHardKeyVolumeUp(self):
        """
        点击屏幕硬按键音量加键
        :return: True点击成功，False点击失败
        """
        keyEvent = pm().readConfigByModuleAndKey('india_D90', 'HardKeyEvent', 'ScreenVolumeUp')
        os.system(keyEvent)
        return True

    def clickScreenHardKeyVolumeDown(self):
        """
        点击屏幕硬按键音量减键
        :return: True点击成功，False点击失败
        """
        keyEvent = pm().readConfigByModuleAndKey('india_D90', 'HardKeyEvent', 'ScreenVolumeDown')
        os.system(keyEvent)
        return True

    def clickWheelHardKeyVolumeUp(self):
        """
        点击方控硬按键音量加键
        :return: True点击成功，False点击失败
        """
        keyEvent = pm().readConfigByModuleAndKey('india_D90', 'HardKeyEvent', 'SteeringWheelVolumeUp')
        os.system(keyEvent)
        return True

    def clickWheelHardKeyVolumeDown(self):
        """
        点击方控硬按键音量减键
        :return: True点击成功，False点击失败
        """
        keyEvent = pm().readConfigByModuleAndKey('india_D90', 'HardKeyEvent', 'SteeringWheelVolumeDown')
        os.system(keyEvent)
        return True

    def clickWheelHardKeyMute(self):
        """
        点击方控硬按键静音
        :return: True点击成功，False点击失败
        """
        keyEvent = pm().readConfigByModuleAndKey('india_D90', 'HardKeyEvent', 'SteeringWheelMute')
        os.system(keyEvent)
        return True

    def clickWheelHardKeyNext(self):
        """
        点击方控硬按键下一首
        :return: True点击成功，False点击失败
        """
        keyEvent = pm().readConfigByModuleAndKey('india_D90', 'HardKeyEvent', 'SteeringWheelMEDIA_NEXT')
        os.system(keyEvent)
        return True

    def clickWheelHardKeyPre(self):
        """
        点击方控硬按键上一首
        :return: True点击成功，False点击失败
        """
        keyEvent = pm().readConfigByModuleAndKey('india_D90', 'HardKeyEvent', 'SteeringWheelMEDIA_PREVIOUS')
        os.system(keyEvent)
        return True

    def clickWheelHardKeyVR(self):
        """
        点击方控硬按键唤起语音
        :return: True点击成功，False点击失败
        """
        keyEvent = pm().readConfigByModuleAndKey('india_D90', 'HardKeyEvent', 'SteeringWheelVR')
        os.system(keyEvent)
        return True

    def clickWheelHardKeyIcall(self):
        """
        点击方控硬按键Icall
        :return: True点击成功，False点击失败
        """
        keyEvent = pm().readConfigByModuleAndKey('india_D90', 'HardKeyEvent', 'SteeringWheelIcall')
        os.system(keyEvent)
        return True

    def clickWheelHardKeySRC(self):
        """
        点击方控硬按键SRC
        :return: True点击成功，False点击失败
        """
        keyEvent = pm().readConfigByModuleAndKey('india_D90', 'HardKeyEvent', 'SteeringWheelSRC')
        os.system(keyEvent)
        return True

    def clickWheelHardKeyPhone(self):
        """
        点击方控硬按键电话
        :return: True点击成功，False点击失败
        """
        keyEvent = pm().readConfigByModuleAndKey('india_D90', 'HardKeyEvent', 'SteeringWheelPhone')
        os.system(keyEvent)
        return True

    def click360AVM(self):
        """
        打开360
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'homePage_resourceId', '360AVM')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def checkClose360ButtonIsExist(self):
        """
        判断360关闭X按键是否存在
        :return: True存在，False不存在
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'homePage_resourceId', 'close360')
        element = pm().find_element_by_id(id=id)
        if element.exists():
            return True
        else:
            return False

    def close360AVN(self):
        """
        关闭360
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'homePage_resourceId', 'close360')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickOk(self):
        """
        点击OK确认（用于Ecall页面OK）
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'homePage_resourceId', 'ok')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def getlockPageTimeElement(self):
        """
        获取锁定页面时间元素
        :return: 时间元素
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'homePage_resourceId', 'lockPageTime')
        return pm().find_element_by_id(id=id)

    def getlockPageDateElement(self):
        """
        获取锁定页面日期元素
        :return: 日期元素
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'homePage_resourceId', 'lockPageTime')

        return pm().find_element_by_id(id=id)

    def checkCurrentPageIsLockPage(self):
        """
        根据锁屏时间和日期判断是否处于锁屏页面
        :return: True 处于锁屏页面，False 不是锁屏页面
        """
        dateElement = self.getlockPageDateElement()
        timeElement = self.getlockPageTimeElement()
        if dateElement and timeElement is not None:
            return True
        else:
            return False

    def checkVolumeBarIsExist(self):
        """
        检查音量条是否存在
        :return: True存在，False不存在
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'homePage_resourceId', 'volumBar')
        element = pm().find_element_by_id(id=id)
        if element.exists():
            return True
        else:
            return False

    def checkVrVuiIsExist(self):
        """
        检查VR对话框是否存在
        :return:  True存在，False不存在
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'homePage_resourceId', 'voiceVui')
        element = pm().find_element_by_id(id=id)
        if element.exists():
            return True
        else:
            return False

    def checkIcallVuiIsExist(self):
        """
        检查Icall对话框是否存在
        :return:  True存在，False不存在
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'homePage_resourceId', 'icallVui')
        element = pm().find_element_by_id(id=id)
        if element.exists():
            return True
        else:
            return False

    def clickACLayout(self):
        """
        点击首页AC卡片进图AC页面
        :return: True, False
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'homePage_resourceId', 'ACLayout')
        element = pm().find_element_by_id(id)
        return pm().click_by_element(element=element)

    def clickACBlowSpeedPlus(self):
        """
        点击首页空调风量加
        :return: True, False
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'homePage_resourceId', 'ACBlowSpeedPlus')
        element = pm().find_element_by_id(id)
        return pm().click_by_element(element=element)

    def clickACBlowSpeedMinus(self):
        """
        点击首页空调风减小
        :return: True, False
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'homePage_resourceId', 'ACBlowSpeedMinus')
        element = pm().find_element_by_id(id)
        return pm().click_by_element(element=element)







    def changeLockPageToHomePage50times(self):
        """
        压力测试（锁屏解锁50次）
        :return: True，False
        """
        k = 0
        self.clickScreenHardKeyHomeButton()
        lockTimeId = pm().readConfigByModuleAndKey('india_D90', 'homePage_resourceId', 'lockPageTime')
        for i in range(50):
            time.sleep(1)
            homeActivity = pm().get_Current_Activity()
            if homeActivity == 'com.saicmotor.launcher.view.MainActivity':
                pass
            else:
                logger.info(str(i) + ' Fail ' + homeActivity)
                k = k + 1
            self.clickDockBarLockScreen()  # 点击锁屏
            time.sleep(1)
            lockTimeElement = pm().find_element_by_id(id=lockTimeId)
            if lockTimeElement.exists():
                pm().click_by_element(element=lockTimeElement)  # 点击解锁
            else:
                logger.info(str(i) + ' Fail 360')
                k = k + 1
        if k == 0:
            return True
        else:
            logger.info('Fail times: ' + str(k))
            return False

    def changeACToNavi100times(self):
        """
        压力测试（首页切换AC切换地图，50次）
        :return: True，False
        """
        k = 0
        for i in range(100):
            self.clickScreenHardKeyHomeButton()
            time.sleep(1)
            homeActivity = pm().get_Current_Activity()
            if homeActivity == 'com.saicmotor.launcher.view.MainActivity':
                pass
            else:
                logger.info(str(i) + ' Fail ' + homeActivity)
                k = k + 1
            self.clickAC()  # 点击AC
            time.sleep(3)
            acActivity = pm().get_Current_Activity()
            if acActivity == 'com.saicmotor.hvac.ui.MainActivity':
                pass
            else:
                logger.info(str(i) + ' Fail ' + acActivity)
                k = k + 1
            self.clickScreenHardKeyHomeButton()
            time.sleep(2)
            homeActivity = pm().get_Current_Activity()
            if homeActivity == 'com.saicmotor.launcher.view.MainActivity':
                pass
            else:
                logger.info(str(i) + ' Fail ' + homeActivity)
                k = k + 1
            self.clickNav()
            time.sleep(3)
            navActivity = pm().get_Current_Activity()
            if navActivity == 'hr.mireo.arthur.common.App':
                pass
            else:
                logger.info(str(i) + ' Fail ' + navActivity)
                k = k + 1
        if k == 0:
            return True
        else:
            logger.info('Fail times: ' + str(k))
            return False

    def changeBTPhoneToAC100times(self):
        """
        压力测试（首页切换蓝牙电话切换空调，100次）
        :return: True，False
        """
        k = 0
        for i in range(100):
            self.clickScreenHardKeyHomeButton()
            time.sleep(1)
            homeActivity = pm().get_Current_Activity()
            if homeActivity == 'com.saicmotor.launcher.view.MainActivity':
                pass
            else:
                logger.info(str(i) + ' Fail ' + homeActivity)
                k = k + 1
            self.clickBTPhoneXpath()  # 点击AC
            time.sleep(2)
            btPhoneActivity = pm().get_Current_Activity()
            if btPhoneActivity == 'com.saicmotor.btphone.ui.activity.BTPhoneMainActivity':
                pass
            else:
                logger.info(str(i) + ' Fail ' + btPhoneActivity)
                k = k + 1
            self.clickScreenHardKeyHomeButton()
            time.sleep(2)
            homeActivity = pm().get_Current_Activity()
            if homeActivity == 'com.saicmotor.launcher.view.MainActivity':
                pass
            else:
                logger.info(str(i) + ' Fail ' + homeActivity)
                k = k + 1
            self.clickAC()
            time.sleep(2)
            acActivity = pm().get_Current_Activity()
            if acActivity == 'com.saicmotor.hvac.ui.MainActivity':
                pass
            else:
                logger.info(str(i) + ' Fail ' + acActivity)
                k = k + 1
        if k == 0:
            return True
        else:
            logger.info('Fail times: ' + str(k))
            return False

    def change360ToWeather100times(self):
        """
        压力测试（首页切换360切换天气，100次）
        :return: True，False
        """
        k = 0
        for i in range(100):
            self.clickScreenHardKeyHomeButton()
            time.sleep(1)
            homeActivity = pm().get_Current_Activity()
            if homeActivity == 'com.saicmotor.launcher.view.MainActivity':
                pass
            else:
                logger.info(str(i) + ' Fail ' + homeActivity)
                k = k + 1
            self.click360AVM()  # 点击360倒车
            time.sleep(2)
            self.close360AVN()  # 关闭360倒车
            homeActivity = pm().get_Current_Activity()
            if homeActivity == 'com.saicmotor.launcher.view.MainActivity':
                pass
            else:
                logger.info(str(i) + ' Fail ' + homeActivity)
                k = k + 1
            self.clickWeather()
            time.sleep(2)
            weatherActivity = pm().get_Current_Activity()
            if weatherActivity == 'com.saicmotor.weathers.activity.MainActivity':
                pass
            else:
                logger.info(str(i) + ' Fail ' + weatherActivity)
                k = k + 1
        if k == 0:
            return True
        else:
            logger.info('Fail times: ' + str(k))
            return False

    def change360ToVehicleSetting100times(self):
        """
        压力测试（首页切换360切换车设，100次）
        :return: True，False
        """
        k = 0
        for i in range(100):
            self.clickScreenHardKeyHomeButton()
            time.sleep(1)
            homeActivity = pm().get_Current_Activity()
            if homeActivity == 'com.saicmotor.launcher.view.MainActivity':
                pass
            else:
                logger.info(str(i) + ' Fail ' + homeActivity)
                k = k + 1
            self.click360AVM()  # 点击360倒车
            time.sleep(2)
            self.close360AVN()  # 关闭360倒车
            homeActivity = pm().get_Current_Activity()
            if homeActivity == 'com.saicmotor.launcher.view.MainActivity':
                pass
            else:
                logger.info(str(i) + ' Fail ' + homeActivity)
                k = k + 1
            self.clickDockBarVehicleSetting()
            time.sleep(2)
            vehicleSettingActivity = pm().get_Current_Activity()
            if vehicleSettingActivity == 'com.saicmotor.vehiclesetting.VehicleSettingActivity':
                pass
            else:
                logger.info(str(i) + ' Fail ' + vehicleSettingActivity)
                k = k + 1
        if k == 0:
            return True
        else:
            logger.info('Fail times: ' + str(k))
            return False

    def changeOpenClose360_100times(self):
        """
        压力测试（首页打开关闭360，100次）
        :return: True，False
        """
        k = 0
        for i in range(100):
            self.clickScreenHardKeyHomeButton()
            time.sleep(1)
            homeActivity = pm().get_Current_Activity()
            if homeActivity == 'com.saicmotor.launcher.view.MainActivity':
                pass
            else:
                logger.info(str(i) + ' Fail ' + homeActivity)
                k = k + 1
            self.click360AVM()  # 点击360倒车
            time.sleep(2)
            self.close360AVN()  # 关闭360倒车
        if k == 0:
            return True
        else:
            logger.info('Fail times: ' + str(k))
            return False

    def change360ToNavi100times(self):
        """
        压力测试（首页切换360切换地图，100次）
        :return: True，False
        """
        k = 0
        for i in range(100):
            self.clickScreenHardKeyHomeButton()
            time.sleep(1)
            homeActivity = pm().get_Current_Activity()
            if homeActivity == 'com.saicmotor.launcher.view.MainActivity':
                pass
            else:
                logger.info(str(i) + ' Fail ' + homeActivity)
                k = k + 1
            self.click360AVM()  # 点击360倒车
            time.sleep(2)
            self.close360AVN()  # 关闭360倒车
            homeActivity = pm().get_Current_Activity()
            if homeActivity == 'com.saicmotor.launcher.view.MainActivity':
                pass
            else:
                logger.info(str(i) + ' Fail ' + homeActivity)
                k = k + 1
            self.clickNav()
            time.sleep(3)
            navActivity = pm().get_Current_Activity()
            if navActivity == 'hr.mireo.arthur.common.App':
                pass
            else:
                logger.info(str(i) + ' Fail ' + navActivity)
                k = k + 1
        if k == 0:
            return True
        else:
            logger.info('Fail times: ' + str(k))
            return False

    def change360ToBTPhone100times(self):
        """
        压力测试（首页切换360切换蓝牙电话，100次）
        :return: True，False
        """
        k = 0
        for i in range(100):
            self.clickScreenHardKeyHomeButton()
            time.sleep(1)
            homeActivity = pm().get_Current_Activity()
            if homeActivity == 'com.saicmotor.launcher.view.MainActivity':
                pass
            else:
                logger.info(str(i) + ' Fail ' + homeActivity)
                k = k + 1
            self.click360AVM()  # 点击360倒车
            time.sleep(2)
            self.close360AVN()  # 关闭360倒车
            homeActivity = pm().get_Current_Activity()
            if homeActivity == 'com.saicmotor.launcher.view.MainActivity':
                pass
            else:
                logger.info(str(i) + ' Fail ' + homeActivity)
                k = k + 1
            self.clickBTPhoneXpath()  # 点击AC
            time.sleep(2)
            btPhoneActivity = pm().get_Current_Activity()
            if btPhoneActivity == 'com.saicmotor.btphone.ui.activity.BTPhoneMainActivity':
                pass
            else:
                logger.info(str(i) + ' Fail ' + btPhoneActivity)
                k = k + 1
        if k == 0:
            return True
        else:
            logger.info('Fail times: ' + str(k))
            return False

    def changeVehicleSettingToNavi100times(self):
        """
        压力测试（首页打开车控切换打开导航，100次）
        :return: True，False
        """
        k = 0
        for i in range(100):
            self.clickScreenHardKeyHomeButton()
            time.sleep(1)
            homeActivity = pm().get_Current_Activity()
            if homeActivity == 'com.saicmotor.launcher.view.MainActivity':
                pass
            else:
                logger.info(str(i) + ' Fail ' + homeActivity)
                k = k + 1
            self.clickDockBarVehicleSetting()  # dock栏中的车设
            vehicleSettingActivity = pm().get_Current_Activity()
            if vehicleSettingActivity == 'com.saicmotor.vehiclesetting.VehicleSettingActivity':
                pass
            else:
                logger.info(str(i) + ' Fail ' + vehicleSettingActivity)
                k = k + 1
            self.clickScreenHardKeyHomeButton()
            time.sleep(2)
            homeActivity = pm().get_Current_Activity()
            if homeActivity == 'com.saicmotor.launcher.view.MainActivity':
                pass
            else:
                logger.info(str(i) + ' Fail ' + homeActivity)
                k = k + 1
            self.clickNav()
            time.sleep(3)
            navActivity = pm().get_Current_Activity()
            if navActivity == 'hr.mireo.arthur.common.App':
                pass
            else:
                logger.info(str(i) + ' Fail ' + navActivity)
                k = k + 1
        if k == 0:
            return True
        else:
            logger.info('Fail times: ' + str(k))
            return False

    def changeVehicleSettingToBtPhone100times(self):
        """
        压力测试（首页打开车控切换打开蓝牙电话，100次）
        :return: True，False
        """
        k = 0
        for i in range(100):
            self.clickScreenHardKeyHomeButton()
            time.sleep(1)
            homeActivity = pm().get_Current_Activity()
            if homeActivity == 'com.saicmotor.launcher.view.MainActivity':
                pass
            else:
                logger.info(str(i) + ' Fail ' + homeActivity)
                k = k + 1
            self.clickDockBarVehicleSetting()  # dock栏中的车设
            vehicleSettingActivity = pm().get_Current_Activity()
            if vehicleSettingActivity == 'com.saicmotor.vehiclesetting.VehicleSettingActivity':
                pass
            else:
                logger.info(str(i) + ' Fail ' + vehicleSettingActivity)
                k = k + 1
            self.clickScreenHardKeyHomeButton()
            time.sleep(2)
            homeActivity = pm().get_Current_Activity()
            if homeActivity == 'com.saicmotor.launcher.view.MainActivity':
                pass
            else:
                logger.info(str(i) + ' Fail ' + homeActivity)
                k = k + 1
            self.clickBTPhoneXpath()
            time.sleep(3)
            btPhoneActivity = pm().get_Current_Activity()
            if btPhoneActivity == 'com.saicmotor.btphone.ui.activity.BTPhoneMainActivity':
                pass
            else:
                logger.info(str(i) + ' Fail ' + btPhoneActivity)
                k = k + 1
        if k == 0:
            return True
        else:
            logger.info('Fail times: ' + str(k))
            return False

    def changeHomePageToMaps(self):
        """
        压力测试（首页打开地图，100次）
        :return: True，False
        """
        k = 0
        for i in range(100):
            self.clickScreenHardKeyHomeButton()
            time.sleep(1)
            homeActivity = pm().get_Current_Activity()
            if homeActivity == 'com.saicmotor.launcher.view.MainActivity':
                pass
            else:
                logger.info(str(i) + ' Fail ' + homeActivity)
                k = k + 1
            self.clickNav()
            time.sleep(3)
            navActivity = pm().get_Current_Activity()
            if navActivity == 'hr.mireo.arthur.common.App':
                pass
            else:
                logger.info(str(i) + ' Fail ' + navActivity)
                k = k + 1
        if k == 0:
            return True
        else:
            logger.info('Fail times: ' + str(k))
            return False
