# -*- coding: utf-8 -*-
from UIconfig.Base import Base
from page.PublicMethod import PublicMethod as pm
from page.india_D90_homePage import india_D90_homePage as homePage
from page.india_D90_morePage import morePage

import os, time

os.path.abspath('.')


class australia_AS23_settingsPage(Base):

    def clickSystemVersionInformationButton(self):
        """
        点击System页面中版本信息
        :return: True, False
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'Setting_resourceId', 'SystemVersionInfo')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def openSystemVersionPage(self):
        """
        判断System页面是否打开（通过判断CopyRight控件是否存在来检测页面是否打开）
        :return: True, False
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'Setting_resourceId', 'SystemCopyRight')
        element = pm().find_element_by_id(id=id)
        if element is not None:
            return True
        else:
            return self.clickSystemVersionInformationButton()


    def closeSystemVersionPage(self):
        """
        判断System页面是否关闭（通过判断CopyRight控件是否存在来检测页面是否关闭）
        :return: True, False
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'Setting_resourceId', 'SystemCopyRight')
        element = pm().find_element_by_id(id=id)
        if element is not None:
            return self.clickSystemVersionInformationButton()
        else:
            return True

    def clickSystemResetButton(self):
        """
        点击SystemResetButton开关
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'Setting_resourceId', 'systemResetButton')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickVehicleResetButton(self):
        """
        点击VehicleResetButton开关
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'Setting_resourceId', 'vehicleResetButton')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def checkSystemResetText(self):
        """
        检查；System Reset话术
        :return: True话术正确，False话术错误
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'Setting_resourceId', 'resetDialog')
        element = pm().find_element_by_id(id=id)
        if element.get_text() == 'Do you want to reset the system?':
            return True
        else:
            return False

    def checkVehicleResetText(self):
        """
        检查；Vehicle Reset话术
        :return: True话术正确，False话术错误
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'Setting_resourceId', 'resetDialog')
        element = pm().find_element_by_id(id=id)
        if element.get_text() == 'Do you want to reset the vehicle?':
            return True
        else:
            return False

    def clickSound(self):
        """
        滑动查找Setting页面中的Sound栏
        :return: True点击成功，False点击失败
        """
        elementName = pm().readConfigByModuleAndKey('australia_AS23', 'settingsPage_recyclerView_txt',
                                                    'Sound')  # 子页面名称
        listId = pm().readConfigByModuleAndKey('australia_AS23', 'Setting_resourceId', 'menuList')  # 右侧子页面列表
        elist = pm().find_element_by_id(id=listId)
        element = pm().find_element_by_text(elementName)
        if element:
            return pm().click_by_element(element=element)
        else:
            pm().swipe_to_beginning_by_id(id=listId)  # 先将列表划至最上方
            for i in range(2):
                newElement = pm().find_element_by_text(elementName)
                if newElement:
                    return pm().click_by_element(newElement)
                else:
                    pm().swipe_up_by_element(elist)  # 滑动右侧列表
            return False

    def clickToneFieldPage(self):
        """
        点击ToneField页面（附带页面校验checkCurrentPage方法）
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'Setting_resourceId', 'toneFieldPage')
        element = pm().find_element_by_id(id=id)
        pm().click_by_element(element=element)
        return self.checkCurrentPage('toneFieldPageTitle')

    def clickToneEffectPage(self):
        """
        点击ToneEffect页面（附带页面校验checkCurrentPage方法）
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'Setting_resourceId', 'toneEffectPage')
        element = pm().find_element_by_id(id=id)
        pm().click_by_element(element=element)
        return self.checkCurrentPage('toneEffectPageTitle')

    def clickVolumePage(self):
        """
        点击VolumePage页面（附带页面校验checkCurrentPage方法）
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'Setting_resourceId', 'volumePage')
        element = pm().find_element_by_id(id=id)
        pm().click_by_element(element=element)
        return self.checkCurrentPage('volumePageTitle')

    def checkCurrentPage(self, title):
        """
        根据传入页面Title检查当前页面（判断该页面下高亮条是否存在）
        :return: True当前处于该页面，False当前不是该页面
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'Setting_resourceId', title)
        element = pm().find_element_by_id(id=id)
        if element is not None:
            return True
        else:
            return False

    def clickToneFieldResetButton(self):
        """
        点击ToneField页面Reset按键
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'Setting_resourceId', 'toneFieldResetButton')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickClassicMode(self):
        """
        点击Classic模式
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'Setting_resourceId', 'classic')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickPopMode(self):
        """
        点击pop模式
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'Setting_resourceId', 'pop')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickVocalMode(self):
        """
        点击vocal模式
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'Setting_resourceId', 'vocal')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickJazzMode(self):
        """
        点击jazz模式
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'Setting_resourceId', 'jazz')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickRockMode(self):
        """
        点击rock模式
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'Setting_resourceId', 'rock')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickManualMode(self):
        """
        点击manual模式
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'Setting_resourceId', 'manual')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickResetMode(self):
        """
        点击reset模式
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'Setting_resourceId', 'reset')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def checkdToneEffectFrequency(self):
        """
        检查音轨下标数值是否与实际一致80、500、1k、5k、16k
        :return: True文本正确，False文本错误
        """
        text80 = pm().find_element_by_id(
            id=pm().readConfigByModuleAndKey('australia_AS23', 'Setting_resourceId', '80Freq'))
        text500Freq = pm().find_element_by_id(id=pm().readConfigByModuleAndKey('australia_AS23', 'Setting_resourceId',
                                                                               '500Freq'))
        text1kFreq = pm().find_element_by_id(
            id=pm().readConfigByModuleAndKey('australia_AS23', 'Setting_resourceId',
                                             '1kFreq'))
        text5kFreq = pm().find_element_by_id(
            id=pm().readConfigByModuleAndKey('australia_AS23', 'Setting_resourceId',
                                             '5kFreq'))
        text16kFreq = pm().find_element_by_id(id=pm().readConfigByModuleAndKey('australia_AS23', 'Setting_resourceId',
                                                                               '16kFreq'))
        if '80' == text80.get_text() and '500' == text500Freq.get_text() and '1K' == text1kFreq.get_text() and '5K' == text5kFreq.get_text() and '16K' == text16kFreq.get_text():
            return True
        else:
            print()
            return False

    def swip80seek(self):
        """
        滑动声道（预留方法）
        :return: True滑动成功，False滑动失败
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'Setting_resourceId', '80seek')
        element = pm().find_element_by_id(id=id)
        return pm().swipe_down_by_element(element=element)

    def swipeUpVolumePage(self):
        """
        Volume页面上划
        :return: True滑动成功 False滑动失败
        """
        xpath = pm().readConfigByModuleAndKey('australia_AS23', 'Setting_resourceId', 'volumeScrollViewXpath')
        element = pm().find_element_by_Xpath(Xpath=xpath)
        return pm().swipe_up_by_element(element=element)

    def swipeDownVolumePage(self):
        """
        Volume页面下划
        :return: True滑动成功 False滑动失败
        """
        xpath = pm().readConfigByModuleAndKey('australia_AS23', 'Setting_resourceId', 'volumeScrollViewXpath')
        element = pm().find_element_by_Xpath(Xpath=xpath)
        return pm().swipe_down_by_element(element=element)

    def checkLoudnessStatus(self):
        """
        查看Loudness状态
        :return: On 打开，Off 关闭
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'Setting_resourceId', 'loudnessStatus')
        element = pm().find_element_by_id(id=id)
        return element.get_text()

    def openLoudnessMode(self):
        """
        打开Loudness模式（附加状态校验）
        :return: True打开成功,False打开失败
        """
        self.swipeDownVolumePage()
        self.swipeDownVolumePage()  # 上划2次至顶部
        id = pm().readConfigByModuleAndKey('australia_AS23', 'Setting_resourceId', 'loudnessButton')
        element = pm().find_element_by_id(id=id)  # 获取开关元素
        if element is None:  # 如果元素不存在，返回False
            return False
        else:
            statusId = pm().readConfigByModuleAndKey('australia_AS23', 'Setting_resourceId', 'loudnessStatus')
            element = pm().find_element_by_id(id=statusId)  # 获取开关状态
            if element.get_text() == 'On':
                return True
            else:
                elementButton = pm().find_element_by_id(id=id)
                pm().click_by_element(element=elementButton)
                if element.get_text() == 'On':  # 打开成功 返回True
                    return True
                else:
                    return False

    def closeLoudnessMode(self):
        """
        关闭Loudness模式（附加状态校验）
        :return: True关闭成功,False关闭失败
        """
        self.swipeDownVolumePage()
        self.swipeDownVolumePage()  # 上划2次至顶部
        id = pm().readConfigByModuleAndKey('australia_AS23', 'Setting_resourceId', 'loudnessButton')
        element = pm().find_element_by_id(id=id)  # 获取开关元素
        if element is None:  # 如果元素不存在，返回False
            return False
        else:
            statusId = pm().readConfigByModuleAndKey('australia_AS23', 'Setting_resourceId', 'loudnessStatus')
            element = pm().find_element_by_id(id=statusId)  # 获取开关状态
            if element.get_text() == 'Off':
                return True
            else:
                elementButton = pm().find_element_by_id(id=id)
                pm().click_by_element(element=elementButton)
                if element.get_text() == 'Off':  # 关闭成功 返回True
                    return True
                else:
                    return False

    def clickSystemNotificationHigh(self):
        """
        点击SystemNotification High按键
        :return:  True点击成功，False点击失败
        """
        self.swipeDownVolumePage()
        self.swipeDownVolumePage()  # 上划2次至顶部
        id = pm().readConfigByModuleAndKey('australia_AS23', 'Setting_resourceId', 'notificationHigh')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickSystemNotificationLow(self):
        """
        点击SystemNotification Low按键
        :return:  True点击成功，False点击失败
        """
        self.swipeDownVolumePage()
        self.swipeDownVolumePage()  # 上划2次至顶部
        id = pm().readConfigByModuleAndKey('australia_AS23', 'Setting_resourceId', 'notificationLow')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickSystemNotificationOff(self):
        """
        点击SystemNotification Off按键
        :return:  True点击成功，False点击失败
        """
        self.swipeDownVolumePage()
        self.swipeDownVolumePage()  # 上划2次至顶部
        id = pm().readConfigByModuleAndKey('australia_AS23', 'Setting_resourceId', 'notificationOff')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickSystemBeepHigh(self):
        """
        点击SystemBeep High按键
        :return:  True点击成功，False点击失败
        """
        self.swipeDownVolumePage()
        self.swipeDownVolumePage()  # 上划2次至顶部
        id = pm().readConfigByModuleAndKey('australia_AS23', 'Setting_resourceId', 'BeepsHigh')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickSystemBeepLow(self):
        """
        点击SystemBeep Low按键
        :return:  True点击成功，False点击失败
        """
        self.swipeDownVolumePage()
        self.swipeDownVolumePage()  # 上划2次至顶部
        id = pm().readConfigByModuleAndKey('australia_AS23', 'Setting_resourceId', 'BeepsLow')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def findSVCGroup(self):
        """
        定位SVC栏，无返回
        :return: 无
        """
        self.swipeDownVolumePage()
        self.swipeDownVolumePage()  # 上划2次至顶部
        id = pm().readConfigByModuleAndKey('australia_AS23', 'Setting_resourceId', 'svcId')
        element = pm().find_element_by_id(id=id)
        if element is None:
            return self.swipeUpVolumePage()
        else:
            return True

    def clickSVCHigh(self):
        """
        点击SVC High按键
        :return:  True点击成功，False点击失败
        """
        self.findSVCGroup()
        id = pm().readConfigByModuleAndKey('australia_AS23', 'Setting_resourceId', 'svcHigh')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickSVCNormal(self):
        """
        点击SVC Normal按键
        :return:  True点击成功，False点击失败
        """
        self.findSVCGroup()
        id = pm().readConfigByModuleAndKey('australia_AS23', 'Setting_resourceId', 'svcNormal')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickSVCLow(self):
        """
        点击SVC Low按键
        :return:  True点击成功，False点击失败
        """
        self.findSVCGroup()
        id = pm().readConfigByModuleAndKey('australia_AS23', 'Setting_resourceId', 'svcLow')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickSVCOff(self):
        """
        点击SVC Off按键
        :return:  True点击成功，False点击失败
        """
        self.findSVCGroup()
        id = pm().readConfigByModuleAndKey('australia_AS23', 'Setting_resourceId', 'svcOff')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def naviVolumeMax(self):
        """
        导航音量最大（附带最值校验）
        :return: True最值比较正确，False最值比较错误
        """
        self.swipeUpVolumePage()
        self.swipeUpVolumePage()
        id = pm().readConfigByModuleAndKey('australia_AS23', 'Setting_resourceId', 'naviBar')
        element = pm().find_element_by_id(id=id)
        pm().swipe_right_by_element(element=element)
        volumeId = pm().readConfigByModuleAndKey('australia_AS23', 'Setting_resourceId', 'navVolume')
        elementVolume = pm().find_element_by_id(id=volumeId)
        if elementVolume.get_text() == '8':
            return True
        else:
            return False

    def naviVolumeMin(self):
        """
        导航音量最小（附带最值校验）
        :return: True最值比较正确，False最值比较错误
        """
        self.swipeUpVolumePage()
        self.swipeUpVolumePage()
        id = pm().readConfigByModuleAndKey('australia_AS23', 'Setting_resourceId', 'naviBar')
        element = pm().find_element_by_id(id=id)
        pm().swipe_left_by_element(element=element)
        volumeId = pm().readConfigByModuleAndKey('australia_AS23', 'Setting_resourceId', 'navVolume')
        elementVolume = pm().find_element_by_id(id=volumeId)
        if elementVolume.get_text() == '1':
            return True
        else:
            return False

    def mediaVolumeMax(self):
        """
        媒体音量最大（附带最值校验）
        :return: True最值比较正确，False最值比较错误
        """
        self.swipeUpVolumePage()
        self.swipeUpVolumePage()
        id = pm().readConfigByModuleAndKey('australia_AS23', 'Setting_resourceId', 'mediaBar')
        element = pm().find_element_by_id(id=id)
        pm().swipe_right_by_element(element=element)
        volumeId = pm().readConfigByModuleAndKey('australia_AS23', 'Setting_resourceId', 'mediaVolume')
        elementVolume = pm().find_element_by_id(id=volumeId)
        if elementVolume.get_text() == '32':
            return True
        else:
            return False

    def mediaVolumeMin(self):
        """
        媒体音量最小（附带最值校验）
        :return: True最值比较正确，False最值比较错误
        """
        self.swipeUpVolumePage()
        self.swipeUpVolumePage()
        id = pm().readConfigByModuleAndKey('australia_AS23', 'Setting_resourceId', 'mediaBar')
        element = pm().find_element_by_id(id=id)
        pm().swipe_left_by_element(element=element)
        volumeId = pm().readConfigByModuleAndKey('australia_AS23', 'Setting_resourceId', 'mediaVolume')
        elementVolume = pm().find_element_by_id(id=volumeId)
        if elementVolume.get_text() == '0':
            return True
        else:
            return False

    def phoneVolumeMax(self):
        """
        电话音量最大（附带最值校验）
        :return: True最值比较正确，False最值比较错误
        """
        self.swipeUpVolumePage()
        self.swipeUpVolumePage()
        id = pm().readConfigByModuleAndKey('australia_AS23', 'Setting_resourceId', 'phoneBar')
        element = pm().find_element_by_id(id=id)
        pm().swipe_right_by_element(element=element)
        volumeId = pm().readConfigByModuleAndKey('australia_AS23', 'Setting_resourceId', 'phoneVolume')
        elementVolume = pm().find_element_by_id(id=volumeId)
        if elementVolume.get_text() == '32':
            return True
        else:
            return False

    def phoneVolumeMin(self):
        """
        电话音量最小（附带最值校验）
        :return:  True最值比较正确，False最值比较错误
        """
        self.swipeUpVolumePage()
        self.swipeUpVolumePage()
        id = pm().readConfigByModuleAndKey('australia_AS23', 'Setting_resourceId', 'phoneBar')
        element = pm().find_element_by_id(id=id)
        pm().swipe_left_by_element(element=element)
        volumeId = pm().readConfigByModuleAndKey('australia_AS23', 'Setting_resourceId', 'phoneVolume')
        elementVolume = pm().find_element_by_id(id=volumeId)
        if elementVolume.get_text() == '0':
            return True
        else:
            return False

    def mediaStepIncrease(self):
        self.swipeUpVolumePage()
        self.swipeUpVolumePage()
        # D90HomePage = india_D90_homePage()
        volumeId = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'mediaVolume')
        elementVolume = pm().find_element_by_id(id=volumeId)
        mediaVolumeBeforeChange = int(elementVolume.get_text())
        homePage().clickWheelHardKeyVolumeUp()
        time.sleep(4)  # 等待硬按键操作后音量栏消失后再执行元素获取操作
        mediaVolumeAfterChange = int(elementVolume.get_text())
        if mediaVolumeBeforeChange == 32:  # 初始值最大的情况下最值判断
            if mediaVolumeAfterChange == mediaVolumeBeforeChange:
                return True
            else:
                print(mediaVolumeBeforeChange)
                print(mediaVolumeAfterChange)
                return False
        else:  # 初始值不是最大的情况下数值判断
            if mediaVolumeBeforeChange + 1 == mediaVolumeAfterChange:
                return True
            else:
                print(mediaVolumeBeforeChange)
                print(mediaVolumeAfterChange)
                return False

    def mediaStepReduce(self):
        self.swipeUpVolumePage()
        self.swipeUpVolumePage()
        volumeId = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'mediaVolume')
        elementVolume = pm().find_element_by_id(id=volumeId)
        if elementVolume is None:
            return False
        mediaVolumeBeforeChange = int(elementVolume.get_text())
        homePage().clickWheelHardKeyVolumeDown()
        time.sleep(4)  # 等待硬按键操作后音量栏消失后再执行元素获取操作
        mediaVolumeAfterChange = int(elementVolume.get_text())
        if mediaVolumeBeforeChange == 0:  # 初始值最小的情况下最值判断
            if mediaVolumeAfterChange == mediaVolumeBeforeChange:
                return True
            else:
                print(mediaVolumeBeforeChange)
                print(mediaVolumeAfterChange)
                return False
        else:  # 初始值不是最小的情况下数值判断
            if mediaVolumeBeforeChange - 1 == mediaVolumeAfterChange:
                return True
            else:
                print(mediaVolumeBeforeChange)
                print(mediaVolumeAfterChange)
                return False











    def clickBluetooth(self):
        """
        滑动查找Setting页面中的Bluetooth栏
        :return: True点击成功，False点击失败
        """
        elementName = pm().readConfigByModuleAndKey('india_D90', 'settingsPage_recyclerView_txt',
                                                    'Bluetooth')  # 子页面名称
        listId = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'menuList')  # 右侧子页面列表
        elist = pm().find_element_by_id(id=listId)
        element = pm().find_element_by_text(elementName)
        if element:
            return pm().click_by_element(element=element)
        else:
            pm().swipe_to_beginning_by_id(id=listId)  # 先将列表划至最上方
            for i in range(2):
                newElement = pm().find_element_by_text(elementName)
                if newElement:
                    return pm().click_by_element(newElement)
                else:
                    pm().swipe_up_by_element(elist)  # 滑动右侧列表
            return False

    def clickBtButton(self):
        """
        点击蓝牙开关（用于openBTButton，）
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'BluetoothButton')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def getBlueToothStatus(self):
        """
        获取蓝牙状态
        :return: On Off
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'bluetoothStatus')
        element = pm().find_element_by_id(id=id)
        return element.get_text()

    def openBTButton(self):
        """
        打开蓝牙开关，如果未打开则打开蓝牙开关（带点击后状态校验）
        :return: True点击成功，False点击失败
        """
        btStatus = self.getBlueToothStatus()
        if btStatus == 'On':
            return True
        else:
            self.clickBtButton()
            if self.getBlueToothStatus() == 'On':
                return True
            else:
                return False

    def closeBTButton(self):
        """
        关闭蓝牙开关，如果未关闭则关闭蓝牙开关（带点击后状态校验）
        :return: True点击成功，False点击失败
        """
        btStatus = self.getBlueToothStatus()
        if btStatus == 'Off':
            return True
        else:
            self.clickBtButton()
            if self.getBlueToothStatus() == 'Off':
                return True
            else:
                return False

    def swipeBtDevices(self):
        """
        滑动蓝牙驱动连接页面
        :return:  True滑动成功，False滑动失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'contentList')
        element = pm().find_element_by_id(id=id)
        return pm().swipe_up_by_element(element=element)

    def clickNetWorkDevicesByWifiName(self, wifiName):
        """
        查询wifi连接，如果存在则点击，如果未找到则滑动2次查找，2次滑动找不到则判定失败
        :return:  True滑动成功，False滑动失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'contentList')
        element = pm().find_element_by_id(id=id)
        pm().swipe_down_by_element(element=element)  # 先将列表划至最上方
        for i in range(2):
            element = pm().find_element_by_text(text=wifiName)
            if element is not None:
                return pm().click_by_element(element=element)
            else:
                continue
        return False  # 滑动2次未找到判定失败

    def clickOK(self):
        """
        点击OK按键
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'ok')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickReset(self):
        """
        点击Reset按键
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'ok')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickConfirm(self):
        """
        点击Confirm按键
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'Confirm')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickCancel(self):
        """
        点击cancel按键
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'cancel')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickNetwork(self):
        """
        滑动查找Setting页面中的Network栏
        :return: True点击成功，False点击失败
        """
        elementName = pm().readConfigByModuleAndKey('india_D90', 'settingsPage_recyclerView_txt',
                                                    'Network')  # 子页面名称
        listId = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'menuList')  # 右侧子页面列表
        elist = pm().find_element_by_id(id=listId)
        element = pm().find_element_by_text(elementName)
        if element:
            return pm().click_by_element(element=element)
        else:
            pm().swipe_to_beginning_by_id(id=listId)  # 先将列表划至最上方
            for i in range(2):
                newElement = pm().find_element_by_text(elementName)
                if newElement:
                    return pm().click_by_element(newElement)
                else:
                    pm().swipe_up_by_element(elist)  # 滑动右侧列表
            return False

    def clickWifiButton(self):
        """
        点击wifi开关
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'wifiButton')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def checkWifiButtonStatusIsOn(self):
        """
        检测wifi开关状态是否为On
        :return: True On, False Off
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'wifiStatus')
        element = pm().find_element_by_id(id=id)
        if element.get_text() == 'On':
            return True
        else:
            print(element.get_text())
            return False

    def checkWifiButtonStatusIsOn(self):
        """
        检测wifi开关状态是否为On
        :return: True On, False Off
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'wifiStatus')
        element = pm().find_element_by_id(id=id)
        if element.get_text() == 'On':
            return True
        else:
            return False

    def checkWifiButtonStatusIsOff(self):
        """
        检测wifi开关状态是否为Off
        :return: True On, False Off
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'wifiStatus')
        element = pm().find_element_by_id(id=id)
        if element.get_text() == 'Off':
            return True
        else:
            return False

    def openWifiButton(self):
        """
        打开wifi开关(附带wifi开关状态校验)
        :return:  True打开成功，False打开失败
        """
        for i in range(1):
            if self.checkWifiButtonStatusIsOn():
                return True
            else:
                self.clickWifiButton()
                if self.checkWifiButtonStatusIsOn():
                    return True
                else:
                    return False

    def closeWifiButton(self):
        """
        关闭wifi开关(附带wifi开关状态校验)
        :return:  True关闭成功，False关闭失败
        """
        for i in range(1):
            if self.checkWifiButtonStatusIsOff():
                return True
            else:
                self.clickWifiButton()
                if self.checkWifiButtonStatusIsOff():
                    return True
                else:
                    return False

    def chooseANetWorkTextIsExist(self):
        """
        判断是否有choose a network栏（用于判断滑动wifi列表是否已经划至顶）
        :return: True该控件存在，False该控件不存在
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'chooseANetworkTitle')
        element = pm().find_element_by_id(id=id)
        if element is not None:
            return True
        else:
            return False

    def swipeWifiConnectListTobeginning(self):
        """
        向上滑动wifi连接列表置顶
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'contentList')
        pm().swipe_to_beginning_by_id(id=id)

    def swipeWifiConnectListToEnding(self):
        """
        向下滑动wifi连接列表至底部
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'contentList')
        pm().swipe_to_end_by_id(id=id)

    def swipeUpWifiConnectList(self):
        """
        向上滑动wifi连接列表
        :return: True滑动成功，False滑动失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'contentList')
        element = pm().find_element_by_id(id=id)
        return pm().swipe_down_by_element(element=element)

    def swipeDownWifiConnectList(self):
        """
        向下滑动wifi连接列表
        :return: True滑动成功，False滑动失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'contentList')
        element = pm().find_element_by_id(id=id)
        return pm().swipe_up_by_element(element=element)

    def getAllWifiConnectElements(self):
        """
        获取当前页面中wifi列表所有connect项(包含已连接过和未连接过)
        :return: elements 返回element列表
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'contentList')
        element = pm().find_element_by_id(id=id)
        return element.child()

    def getWifiConnectElementsWhichConnected(self):
        """
        获取当前页面中wifi列表中已连接过的所有connect项
        :return: elements 返回element列表
        """
        element = self.getAllWifiConnectElements()
        return element.child(className='android.view.ViewGroup')  # 获取contentList下所有ViewGroup子集

    def getWifiStatusByName(self, wifiName):
        """
        通过wifi名称获取wifi连接状态
        :param wifiName: wifi名称传参
        :return: 返回wifi连接状态Connected、Saved，连接状态不存在返回None，找不到wifi名称返回None
        """
        self.swipeWifiConnectListTobeginning()  # 置顶
        for i in range(5):
            element = pm().find_element_by_text(text=wifiName)
            if element.exists():
                statusText = element.sibling(resourceId='com.saicmotor.settings:id/list_item_status')
                if statusText.exists():
                    return statusText.get_text()
                else:
                    print('status is not exist')
                    return None
            else:
                self.swipeDownWifiConnectList()
        return None

    def checkWifiIncludLockIconByName(self, wifiName):
        """
        通过wifi名称检测是否有锁图标
        :param wifiName: wifi名称传参
        :return: True有所，
        """
        self.swipeWifiConnectListTobeginning()  # 置顶
        for i in range(5):
            element = pm().find_element_by_text(text=wifiName)
            if element is not None:
                lockIcon = element.sibling(resourceId='com.saicmotor.settings:id/list_item_lock')
                if lockIcon.exists():
                    return True
                else:
                    print('Lock icon is Not Exist')
                    return False
            else:
                self.swipeDownWifiConnectList()
        print('WIFI Name is not Exist')
        return False

    def inputWifiPassword(self, text):
        """
        搜索输入框输入密码（输入wifi密码）
        :param text: 输入wifi密码
        :return: True传入成功，False传入失败
        """
        passwordBox = pm().find_element_by_id(id=pm().readConfigByModuleAndKey('india_D90', 'settingsPage',
                                                                               'passwordInput'))
        return pm().inputText(passwordBox, text)

    def getInputWifiPassword(self):
        """
        获取输入框中输入的密码水印（输入wifi密码）
        :return: 返回字符串
        """
        passwordBox = pm().find_element_by_id(id=pm().readConfigByModuleAndKey('india_D90', 'settingsPage',
                                                                               'passwordInput'))
        return passwordBox.get_text()

    def checkKeyboardIsExist(self):
        """
        检查键盘是否已经弹出
        :return:
        """
        element = pm().find_element_by_id(id=pm().readConfigByModuleAndKey('india_D90', 'settingsPage',
                                                                           'keyboard'))
        if element is not None:
            return True
        else:
            return False

    def checkDisconnectDialogIsExist(self):
        """
        判断是否有点开wifi连接提示文本
        :return: True文本存在，False文本不存在
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'disconnectMessage')
        element = pm().find_element_by_id(id=id)
        if element is not None:
            return True
        else:
            return False

    def getDisconnectDialogMessage(self):
        """
        判断是否有点开wifi连接提示文本
        :return: True文本存在，False文本不存在
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'disconnectMessage')
        element = pm().find_element_by_id(id=id)
        if element is not None:
            return element.get_text()
        else:
            return None

    def deleteWifiConnectByName(self, text):
        """
        根据wifi名称左滑删除链接
        :param text: wifi名称
        :return: True 删除成功，False删除失败
        """
        element = pm().find_element_by_text(text=text)
        if element is None:
            return True
        while element.exists():
            pm().swipe_left_by_element(element=element)
            time.sleep(2)
            id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'deleteButton')
            deleteButton = pm().find_element_by_id(id=id)
            pm().click_by_element(element=deleteButton)
            if not element.exists():
                return True
            else:
                continue

    def checkWifiIconIsExistInTitle(self):
        """
        检查车机顶部title栏中是否有已连接图标
        :return: True连接存在，False连接不存在
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'wifiTitleState')
        element = pm().find_element_by_id(id=id)
        if element is not None:
            return True
        else:
            return False

    def checkWifiIconIsNotExistInTitle(self):
        """
        检查车机顶部title栏中是否有已连接图标
        :return: True连接不存在，False连接存在
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'wifiTitleState')
        element = pm().find_element_by_id(id=id)
        if element is None:
            return True
        else:
            return False

    def clickTheme(self):
        """
        滑动查找Setting页面中的Theme栏
        :return: True点击成功，False点击失败
        """
        elementName = pm().readConfigByModuleAndKey('india_D90', 'settingsPage_recyclerView_txt',
                                                    'Theme')  # 子页面名称
        listId = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'menuList')  # 右侧子页面列表
        elist = pm().find_element_by_id(id=listId)
        element = pm().find_element_by_text(elementName)
        if element:
            return pm().click_by_element(element=element)
        else:
            pm().swipe_to_beginning_by_id(id=listId)  # 先将列表划至最上方
            for i in range(2):
                newElement = pm().find_element_by_text(elementName)
                if newElement:
                    return pm().click_by_element(newElement)
                else:
                    pm().swipe_up_by_element(elist)  # 滑动右侧列表
            return False

    def chooseThemeBusinnesGrey(self):
        """
        选择business皮肤（带校验）
        :return: True点击成功，False点击失败
        """
        select1Id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'themeSelect1')
        elementSelect1 = pm().find_element_by_id(id=select1Id)
        pm().click_by_element(element=elementSelect1)
        if elementSelect1 is not None:
            return True
        else:
            id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'theme1')
            elementTheme1 = pm().find_element_by_id(id=id)
            pm().click_by_element(element=elementTheme1)
            elementSelect1 = pm().find_element_by_id(id=select1Id)  # 重新获取element（变量不会自动刷新，必须重新获取）
            if elementSelect1 is not None:
                return True
            else:
                return False

    def chooseThemeMysteriousPurple(self):
        """
        选择Mysterious皮肤（带校验）
        :return: True点击成功，False点击失败
        """
        select1Id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'themeSelect2')
        elementSelect2 = pm().find_element_by_id(id=select1Id)
        if elementSelect2 is not None:
            return True
        else:
            id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'theme2')
            elementTheme2 = pm().find_element_by_id(id=id)
            pm().click_by_element(element=elementTheme2)
            elementSelect2 = pm().find_element_by_id(id=select1Id)  # 重新获取element（变量不会自动刷新，必须重新获取）
            if elementSelect2 is not None:
                return True
            else:
                return False



    def swipTime(self):
        """预留方法（暂不使用）"""
        element = pm().find_element_by_id(id='com.saicmotor.settings:id/day_list')
        return pm().swipe_down_by_element(element=element)

    def clickTime(self):
        """
        滑动查找Setting页面中的Time栏
        :return: True点击成功，False点击失败
        """
        elementName = pm().readConfigByModuleAndKey('india_D90', 'settingsPage_recyclerView_txt', 'Time')  # 子页面名称
        listId = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'menuList')  # 右侧子页面列表
        elist = pm().find_element_by_id(id=listId)
        element = pm().find_element_by_text(elementName)
        if element:
            return pm().click_by_element(element=element)
        else:
            pm().swipe_to_beginning_by_id(id=listId)  # 先将列表划至最上方
            for i in range(2):
                newElement = pm().find_element_by_text(elementName)
                if newElement:
                    return pm().click_by_element(newElement)
                else:
                    return False

    def clickSetTheTime(self):
        """
        点击进入Time页面Set the Time
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'timeFormat')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def click24HTime(self):
        """
        点击选择24小时制（附带校验）
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', '24h')
        element = pm().find_element_by_id(id=id)
        pm().click_by_element(element=element)
        selectId24 = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', '24Select')
        elementSelect24 = pm().find_element_by_id(id=selectId24)
        if elementSelect24 is not None:
            return True
        else:
            return False

    def click12HTime(self):
        """
        点击选择12小时制（附带校验）
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', '12h')
        element = pm().find_element_by_id(id=id)
        pm().click_by_element(element=element)
        selectId12 = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', '12Select')
        elementSelect12 = pm().find_element_by_id(id=selectId12)
        if elementSelect12 is not None:
            return True
        else:
            return False

    def clickBackButton(self):
        """
        点击返回按键
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'settinsgBackButton')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def checkTimeFormatIs12Hour(self):
        """
        检查12小时制话术（用于校验点击选择12小时制后的话术显示）
        :return:  True校验成功，False校验失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'timeFormatText')
        element = pm().find_element_by_id(id=id)
        if element.get_text() == '12 Hour Time':
            return True
        else:
            return False

    def checkTimeFormatIs24Hour(self):
        """
        检查24小时制话术（用于校验点击选择12小时制后的话术显示）
        :return: True校验成功，False校验失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'timeFormatText')
        element = pm().find_element_by_id(id=id)
        if element.get_text() == '24 Hour Time':
            return True
        else:
            return False

    def clickAutoTimeZoneButton(self):
        """
        点击AutoTimeZone按键
        :return:  True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'autoTimeZoneButton')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def getAutoTimeZoneStatus(self):
        """
        查看AutoTimeZone状态
        :return:  On、Off
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'autoTimeZoneStatus')
        element = pm().find_element_by_id(id=id)
        return element.get_text()

    def openAutoTimeZone(self):
        """
        打开时间自动校准（带校验）
        :return:
        """
        if self.getAutoTimeZoneStatus() == 'On':
            pass
        else:
            self.clickAutoTimeZoneButton()
            if self.clickAutoTimeZoneButton() == 'On':
                return True
            else:
                return False

    def closeAutoTimeZone(self):
        """
        打开时间自动校准（带校验）
        :return:
        """
        if self.getAutoTimeZoneStatus() == 'Off':
            pass
        else:
            self.clickAutoTimeZoneButton()
            if self.clickAutoTimeZoneButton() == 'Off':
                return True
            else:
                return False

    def clickDisplay(self):
        """
        滑动查找Setting页面中的Display栏
        :return: True点击成功，False点击失败
        """
        elementName = pm().readConfigByModuleAndKey('india_D90', 'settingsPage_recyclerView_txt',
                                                    'Display')  # 子页面名称
        listId = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'menuList')  # 右侧子页面列表
        elist = pm().find_element_by_id(id=listId)
        element = pm().find_element_by_text(elementName)
        if element:
            return pm().click_by_element(element=element)
        else:
            pm().swipe_to_end_by_id(id=listId)  # 先将列表划至最下方
            for i in range(2):
                newElement = pm().find_element_by_text(elementName)
                if newElement:
                    return pm().click_by_element(newElement)
                else:
                    return False
                pm().swipe_up_by_element(elist)  # 滑动右侧列表

    def clickDisplayDay(self):
        """
        点击Dispaly Day按键
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'day')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickDisplayNight(self):
        """
        点击Dispaly Night按键
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'night')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickDisplayAuto(self):
        """
        点击Dispaly Auto按键
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'auto')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def swipDisplayBrightnessMax(self):
        """
        滑动亮度至最大(附带数值校验)
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'brightNessSeekBar')
        element = pm().find_element_by_id(id=id)
        pm().swipe_right_by_element(element=element)
        disPlayValueId = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'disPlayValue')
        disPlayElement = pm().find_element_by_id(disPlayValueId)
        if disPlayElement.get_text() == '100':
            return True
        else:
            return False

    def swipDisplayBrightnessMin(self):
        """
        滑动亮度至最小(附带数值校验)
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'brightNessSeekBar')
        element = pm().find_element_by_id(id=id)
        pm().swipe_left_by_element(element=element)
        disPlayValueId = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'disPlayValue')
        disPlayElement = pm().find_element_by_id(disPlayValueId)
        if disPlayElement.get_text() == '0':
            return True
        else:
            return False

    def clickUpdate(self):
        """
        滑动查找Setting页面中的Update栏
        :return: True点击成功，False点击失败
        """
        elementName = pm().readConfigByModuleAndKey('india_D90', 'settingsPage_recyclerView_txt',
                                                    'Update')  # 子页面名称
        listId = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'menuList')  # 右侧子页面列表
        elist = pm().find_element_by_id(id=listId)
        element = pm().find_element_by_text(elementName)
        if element:
            return pm().click_by_element(element=element)
        else:
            pm().swipe_to_end_by_id(id=listId)  # 先将列表划至最下方
            for i in range(2):
                newElement = pm().find_element_by_text(elementName)
                if newElement:
                    return pm().click_by_element(newElement)
                else:
                    return False

    def clickUpdateBackButton(self):
        """
        点击Setting模块Update页面左上返回按键
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'updateBackButton')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def checkUpdateMessage(self):
        """
        检查Setting模块Update页面文本信息是否正确
        :return: True文本信息正确，False文本信息错误
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'updateMessageId')
        element = pm().find_element_by_id(id=id)
        text = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'updateMessage')
        if element.get_text() == text:
            return True
        else:
            return False

    def clickUSBStorage(self):
        """
        滑动查找Setting页面中的USBStorage栏
        :return: True点击成功，False点击失败
        """
        elementName = pm().readConfigByModuleAndKey('india_D90', 'settingsPage_recyclerView_txt',
                                                    'USBStorage')  # 子页面名称
        listId = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'menuList')  # 右侧子页面列表
        elist = pm().find_element_by_id(id=listId)
        element = pm().find_element_by_text(elementName)
        if element:
            return pm().click_by_element(element=element)
        else:
            pm().swipe_to_end_by_id(id=listId)  # 先将列表划至最下方
            for i in range(2):
                newElement = pm().find_element_by_text(elementName)
                if newElement:
                    return pm().click_by_element(newElement)
                else:
                    return False

    def clickUserManual(self):
        """
        滑动查找Setting页面中的UserManual栏
        :return: True点击成功，False点击失败
        """
        elementName = pm().readConfigByModuleAndKey('india_D90', 'settingsPage_recyclerView_txt',
                                                    'UserManual')  # 子页面名称
        listId = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'menuList')  # 右侧子页面列表
        elist = pm().find_element_by_id(id=listId)
        element = pm().find_element_by_text(elementName)
        if element:
            return pm().click_by_element(element=element)
        else:
            pm().swipe_to_end_by_id(id=listId)  # 先将列表划至最下方
            for i in range(2):
                newElement = pm().find_element_by_text(elementName)
                if newElement:
                    return pm().click_by_element(newElement)
                else:
                    return False

    def getSumPageNum(self):
        """
        获取用户手册总页码
        :return: 用户手册总页码
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'sumPageNum')
        element = pm().find_element_by_id(id=id)
        sumPage = element.get_text()
        print(sumPage.split('/')[-1])

    def clickVoiceAssistant(self):
        """
        滑动查找Setting页面中的VoiceAssistant栏
        :return: True点击成功，False点击失败
        """
        elementName = pm().readConfigByModuleAndKey('india_D90', 'settingsPage_recyclerView_txt',
                                                    'VoiceAssistant')  # 子页面名称
        listId = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'menuList')  # 右侧子页面列表
        elist = pm().find_element_by_id(id=listId)
        element = pm().find_element_by_text(elementName)
        if element:
            return pm().click_by_element(element=element)
        else:
            pm().swipe_to_end_by_id(id=listId)  # 先将列表划至最下方
            for i in range(2):
                newElement = pm().find_element_by_text(elementName)
                if newElement:
                    return pm().click_by_element(newElement)
                else:
                    return False
                pm().swipe_up_by_element(elist)  # 滑动右侧列表

    def swipeUpVoiceAssistantPage(self):
        """
        划至VoiceAssistant页面顶部
        :return: True滑动成功，False滑动失败
        """
        Xpath = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'voiceAssistantLayout')
        element = pm().find_element_by_Xpath(Xpath=Xpath)
        return pm().swipe_down_by_element(element=element)

    def swipeDownVoiceAssistantPage(self):
        """
        划至VoiceAssistant页面底部
        :return: True滑动成功，False滑动失败
        """
        Xpath = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'voiceAssistantLayout')
        element = pm().find_element_by_Xpath(Xpath=Xpath)
        return pm().swipe_up_by_element(element=element)

    def clickHelloMGButton(self):
        """
        点击HelloMG开关
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'helloMGButton')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def checkHelloMGStatusIsOn(self):
        """
        检查HelloMG状态是否是ON
        :return: True返回状态ON，False返回状态Off
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'helloMGButtonStatus')
        element = pm().find_element_by_id(id=id)
        if element.get_text() == 'On':
            return True
        else:
            return False

    def checkHelloMGStatusIsOff(self):
        """
        检查HelloMG状态是否是OFF
        :return: True返回状态ON，False返回状态Off
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'helloMGButtonStatus')
        element = pm().find_element_by_id(id=id)
        if element.get_text() == 'Off':
            return True
        else:
            return False

    def openHelloMGButton(self):
        """
        打开HelloMG（附带状态校验）
        :return: True 打开成功，False打开失败
        """
        self.swipeUpVoiceAssistantPage()  # 划至顶部
        if self.checkHelloMGStatusIsOn():  # 当前已经打开
            return True
        else:
            self.clickHelloMGButton()  # 点击打开开关
            if self.checkHelloMGStatusIsOn():  # 检测状态
                return True
            else:
                return False

    def closeHelloMGButton(self):
        """
        关闭HelloMG（附带状态校验）
        :return:  True 关闭成功，False关闭失败
        """
        self.swipeUpVoiceAssistantPage()  # 划至顶部
        if self.checkHelloMGStatusIsOff():  # 当前已经关闭
            return True
        else:
            self.clickHelloMGButton()  # 点击打开开关
            if self.checkHelloMGStatusIsOff():  # 检测状态
                return True
            else:
                return False

    def clickWelcomeMessageButton(self):
        """
        点击welcomeMessage开关
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'welcomeMessageButton')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def checkWelcomeMessageButtonStatusIsOn(self):
        """
        检查welcomeMessageButton状态是否是ON
        :return: True返回状态ON，False返回状态Off
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'welcomeMessageButtonStatus')
        element = pm().find_element_by_id(id=id)
        if element.get_text() == 'On':
            return True
        else:
            return False

    def checkWelcomeMessageButtonStatusIsOff(self):
        """
        检查WelcomeMessageButtonStatus状态是否是OFF
        :return: True返回状态ON，False返回状态Off
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'welcomeMessageButtonStatus')
        element = pm().find_element_by_id(id=id)
        if element.get_text() == 'Off':
            return True
        else:
            return False

    def openWelcomeMessageButton(self):
        """
        打开WelcomeMessage（附带状态校验）
        :return: True 打开成功，False打开失败
        """
        self.swipeUpVoiceAssistantPage()  # 划至顶部
        if self.checkHelloMGStatusIsOn():  # 当前已经打开
            return True
        else:
            self.clickWelcomeMessageButton()  # 点击打开开关
            if self.checkWelcomeMessageButtonStatusIsOn():  # 检测状态
                return True
            else:
                return False

    def closeWelcomeMessageButton(self):
        """
        关闭WelcomeMessage（附带状态校验）
        :return:  True 关闭成功，False关闭失败
        """
        self.swipeUpVoiceAssistantPage()  # 划至顶部
        if self.checkHelloMGStatusIsOff():  # 当前已经关闭
            return True
        else:
            self.clickWelcomeMessageButton()  # 点击打开开关
            if self.checkWelcomeMessageButtonStatusIsOff():  # 检测状态
                return True
            else:
                return False

    def clickCustomButton(self):
        """
        点击Custom按键
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'customModeButton')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickRandomButton(self):
        """
        点击Random按键
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'randomModeButton')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def checkCustomInputBoxIsExist(self):
        """
        检查开机欢迎语输入框是否存在
        :return: True存在，False不存在
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'customStrbg')
        element = pm().find_element_by_id(id=id)
        if element is not None:
            return True
        else:
            return False

    def openCustomButton(self):
        """
        打开Custom开机自定义模式
        :return: True打开成功，False打开失败
        """
        if self.checkCustomInputBoxIsExist():
            return True
        else:
            self.clickCustomButton()
            if self.checkCustomInputBoxIsExist():
                return True
            else:
                return False

    def clickGoodByeMessageButton(self):
        """
        点击GoodByeMessageButton开关
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'goodbyeMessageButton')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def checkGoodByeMessageStatusIsOn(self):
        """
        检测GoddByeMessage状态是On
        :return: True检验成功，False检验失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'goodbyeMessageButtonStatus')
        element = pm().find_element_by_id(id=id)
        if element.get_text() == 'On':
            return True
        else:
            return False

    def checkGoodByeMessageStatusIsOff(self):
        """
        检测GoddByeMessage状态是Off
        :return: True检验成功，False检验失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'goodbyeMessageButtonStatus')
        element = pm().find_element_by_id(id=id)
        if element.get_text() == 'Off':
            return True
        else:
            return False

    def openGoodByeMessageButton(self):
        """
        打开Goodbye Message（附带校验）
        :return: True打开成功，False打开失败
        """
        self.swipeUpVoiceAssistantPage()
        if self.checkGoodByeMessageStatusIsOn():
            return True
        else:
            self.clickGoodByeMessageButton()
            if self.checkGoodByeMessageStatusIsOn():
                return True
            else:
                return False

    def closeGoodByeMessageButton(self):
        """
        关闭Goodbye Message（附带校验）
        :return: True关闭成功，False关闭失败
        """
        self.swipeUpVoiceAssistantPage()
        if self.checkGoodByeMessageStatusIsOff():
            return True
        else:
            self.clickGoodByeMessageButton()
            if self.checkGoodByeMessageStatusIsOff():
                return True
            else:
                return False

    def clickTirePressureMonitoringAlarmButton(self):
        """
        点击胎压报警开关
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'tirePreesureAlarmButton')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def checkTirePressureMonitoringAlarmStatusIsOn(self):
        """
        检测TirePressureMonitoringAlarm状态是On
        :return: True检验成功，False检验失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'tirePreesureAlarmText')
        element = pm().find_element_by_id(id=id)
        if element.get_text() == 'On':
            return True
        else:
            return False

    def checkTirePressureMonitoringAlarmStatusIsOff(self):
        """
        检测TirePressureMonitoringAlarm状态是Off
        :return: True检验成功，False检验失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'tirePreesureAlarmText')
        element = pm().find_element_by_id(id=id)
        if element.get_text() == 'Off':
            return True
        else:
            return False

    def openTirePressureMonitoringAlarmButton(self):
        """
        打开TirePressureMonitoringAlarm（附带校验）
        :return: True打开成功，False打开失败
        """
        self.swipeDownVoiceAssistantPage()
        if self.checkTirePressureMonitoringAlarmStatusIsOn():
            return True
        else:
            self.clickTirePressureMonitoringAlarmButton()
            if self.checkTirePressureMonitoringAlarmStatusIsOn():
                return True
            else:
                return False

    def closeTirePressureMonitoringAlarmButton(self):
        """
        关闭TirePressureMonitoringAlarm（附带校验）
        :return: True关闭成功，False关闭失败
        """
        self.swipeDownVoiceAssistantPage()
        if self.checkTirePressureMonitoringAlarmStatusIsOff():
            return True
        else:
            self.clickTirePressureMonitoringAlarmButton()
            if self.checkTirePressureMonitoringAlarmStatusIsOff():
                return True
            else:
                return False

    def clickLowBatteryAlarmButton(self):
        """
        点击低电量报警开关
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'lowBatteryAlarmButton')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def checkLowBatteryAlarmStatusIsOn(self):
        """
        检测Low Battery Alarm状态是On
        :return: True检验成功，False检验失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'lowBatteryAlarmText')
        element = pm().find_element_by_id(id=id)
        if element.get_text() == 'On':
            return True
        else:
            return False

    def checkLowBatteryAlarmStatusIsOff(self):
        """
        检测Low Battery Alarm状态是Off
        :return: True检验成功，False检验失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'lowBatteryAlarmText')
        element = pm().find_element_by_id(id=id)
        if element.get_text() == 'Off':
            return True
        else:
            return False

    def openLowBatteryAlarmButton(self):
        """
        打开LowBatteryAlarm（附带校验）
        :return: True打开成功，False打开失败
        """
        self.swipeDownVoiceAssistantPage()
        if self.checkLowBatteryAlarmStatusIsOn():
            return True
        else:
            self.clickLowBatteryAlarmButton()
            if self.checkLowBatteryAlarmStatusIsOn():
                return True
            else:
                return False

    def closeLowBatteryAlarmButton(self):
        """
        关闭LowBatteryAlarm（附带校验）
        :return: True关闭成功，False关闭失败
        """
        self.swipeDownVoiceAssistantPage()
        if self.checkLowBatteryAlarmStatusIsOff():
            return True
        else:
            self.clickLowBatteryAlarmButton()
            if self.checkLowBatteryAlarmStatusIsOff():
                return True
            else:
                return False

    def clickLowFuelAlertButton(self):
        """
        点击低油量报警开关
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'lowFuelAlertButton')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def checkLowFuelAlertStatusIsOn(self):
        """
        检测LowFuelAlert状态是On
        :return: True检验成功，False检验失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'lowFuelAlertText')
        element = pm().find_element_by_id(id=id)
        if element.get_text() == 'On':
            return True
        else:
            return False

    def checkLowFuelAlertStatusIsOff(self):
        """
        检测LowFuelAlert状态是Off
        :return: True检验成功，False检验失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'lowFuelAlertText')
        element = pm().find_element_by_id(id=id)
        if element.get_text() == 'Off':
            return True
        else:
            return False

    def openLowFuelAlertButton(self):
        """
        打开LowFuelAlert（附带校验）
        :return: True打开成功，False打开失败
        """
        self.swipeDownVoiceAssistantPage()
        if self.checkLowFuelAlertStatusIsOn():
            return True
        else:
            self.clickLowFuelAlertButton()
            if self.checkLowFuelAlertStatusIsOn():
                return True
            else:
                return False

    def closeLowFuelAlertButton(self):
        """
        关闭LowFuelAlert（附带校验）
        :return: True关闭成功，False关闭失败
        """
        self.swipeDownVoiceAssistantPage()
        if self.checkLowFuelAlertStatusIsOff():
            return True
        else:
            self.clickLowFuelAlertButton()
            if self.checkLowFuelAlertStatusIsOff():
                return True
            else:
                return False

    def clickOneShotCommandButton(self):
        """
        点击OneShotCommand开关
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'OneShotCommandButton')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def checkOneShotCommandStatusIsOn(self):
        """
        检测OneShotCommand状态是On
        :return: True检验成功，False检验失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'OneShotCommandText')
        element = pm().find_element_by_id(id=id)
        if element.get_text() == 'On':
            return True
        else:
            return False

    def checkOneShotCommandStatusIsOff(self):
        """
        检测OneShotCommand状态是Off
        :return: True检验成功，False检验失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'OneShotCommandText')
        element = pm().find_element_by_id(id=id)
        if element.get_text() == 'Off':
            return True
        else:
            return False

    def openOneShotCommandButton(self):
        """
        打开OneShotCommand（附带校验）
        :return: True打开成功，False打开失败
        """
        self.swipeDownVoiceAssistantPage()
        if self.checkOneShotCommandStatusIsOn():
            return True
        else:
            self.clickOneShotCommandButton()
            if self.checkOneShotCommandStatusIsOn():
                return True
            else:
                return False

    def closeOneShotCommandButton(self):
        """
        关闭OneShotCommand（附带校验）
        :return: True关闭成功，False关闭失败
        """
        self.swipeDownVoiceAssistantPage()
        if self.checkOneShotCommandStatusIsOff():
            return True
        else:
            self.clickOneShotCommandButton()
            if self.checkOneShotCommandStatusIsOff():
                return True
            else:
                return False



    def clickAboutMG(self):
        """
        滑动查找Setting页面中的AboutMG栏
        :return: True点击成功，False点击失败
        """
        elementName = pm().readConfigByModuleAndKey('india_D90', 'settingsPage_recyclerView_txt',
                                                    'AboutMG')  # 子页面名称
        listId = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'menuList')  # 右侧子页面列表
        elist = pm().find_element_by_id(id=listId)
        element = pm().find_element_by_text(elementName)
        if element:
            return pm().click_by_element(element=element)
        else:
            pm().swipe_to_end_by_id(id=listId)  # 先将列表划至最下方
            for i in range(2):
                newElement = pm().find_element_by_text(elementName)
                if newElement:
                    return pm().click_by_element(newElement)
                else:
                    pm().swipe_up_by_element(elist)  # 滑动右侧列表
            return False

    def clickISmartVersionInfo(self):
        """
        点击查看版本信息（点击打开，再次点击收起）
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'versionInfo')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickPrivacyPolicy(self):
        """
        点击查看Privacy Policy信息
        :return:  True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'privacyPolicy')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickServiceTerms(self):
        """
        点击查看serviceTerms信息
        :return:  True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'serviceTerms')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickEndUserLicenseAgreement(self):
        """
        点击查看endUserLicenseAgreement信息
        :return:  True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'settingsPage', 'endUserLicenseAgreement')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def changeToSettingAccoutPageFromMorePage50times(self):
        """
        压力测试（首页>More>setting>account底部页面 50次）
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
                print(str(i) + ' Fail ' + homeActivity)
                k = k + 1
            homePage().clickMore()  # 点击More页面
            time.sleep(1)
            morePageActivity = pm().get_Current_Activity()
            if morePageActivity == 'com.saicmotor.launcher.view.MoreActivity':
                pass
            else:
                print(str(i) + ' Fail ' + morePageActivity)
                k = k + 1
            time.sleep(1)
            morePage.clickSetting()  # 点击Setting页面
            time.sleep(1)
            settingPageActivity = pm().get_Current_Activity()
            if settingPageActivity == 'com.saicmotor.settings.ui.MainActivity':
                pass
            else:
                print(str(i) + ' Fail ' + morePageActivity)
                k = k + 1
            self.clickAccount()  # 点击Account
            self.swipeToAccountBeginning()  # 先划至Account顶部
            self.swipeToAccountEnd()  # 划至Account底部
            time.sleep(1)
        if k == 0:
            return True
        else:
            print('Fail times: ' + str(k))
            return False

    def changeToSettingBTPageFromMorePage50times(self):
        """
        压力测试（首页>More>setting>Bt页面打开关闭BT50次）
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
                print(str(i) + ' Fail ' + homeActivity)
                k = k + 1
            homePage().clickMore()  # 点击More页面
            time.sleep(1)
            morePageActivity = pm().get_Current_Activity()
            if morePageActivity == 'com.saicmotor.launcher.view.MoreActivity':
                pass
            else:
                print(str(i) + ' Fail ' + morePageActivity)
                k = k + 1
            time.sleep(1)
            morePage.clickSetting()  # 点击Setting页面
            time.sleep(1)
            settingPageActivity = pm().get_Current_Activity()
            if settingPageActivity == 'com.saicmotor.settings.ui.MainActivity':
                pass
            else:
                print(str(i) + ' Fail ' + settingPageActivity)
                k = k + 1
            self.clickBluetooth()  # 点击BT页面
            time.sleep(1)
            self.openBTButton()  # 打开蓝牙开关
            time.sleep(1)
            self.closeBTButton()  # 关闭蓝牙开关
        if k == 0:
            return True
        else:
            print('Fail times: ' + str(k))
            return False

    def changeToSettingNetWorkPageFromMorePage50times(self):
        """
        压力测试（首页>More>setting>Network页面连接wifi关闭wifi 50次）
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
                print(str(i) + ' Fail ' + homeActivity)
                k = k + 1
            homePage().clickMore()  # 点击More页面
            time.sleep(1)
            morePageActivity = pm().get_Current_Activity()
            if morePageActivity == 'com.saicmotor.launcher.view.MoreActivity':
                pass
            else:
                print(str(i) + ' Fail ' + morePageActivity)
                k = k + 1
            time.sleep(1)
            morePage.clickSetting()  # 点击Setting页面
            time.sleep(1)
            settingPageActivity = pm().get_Current_Activity()
            if settingPageActivity == 'com.saicmotor.settings.ui.MainActivity':
                pass
            else:
                print(str(i) + ' Fail ' + settingPageActivity)
                k = k + 1
            self.clickNetwork()  # 点击wifi页面
            time.sleep(1)
            self.openWifiButton()  # 打开WIFI开关
            time.sleep(5)
            # self.swipeWifiConnectListToEnding()  # 下滑置底
            self.swipeWifiConnectListTobeginning()  # 上划置顶
            time.sleep(1)
            self.clickNetWorkDevicesByWifiName('SOIMT-OA-NET')  # 点击wifi链接
            time.sleep(1)
            self.inputWifiPassword('Oa-Net-8ued6#79$')
            time.sleep(1)
            self.clickOK()
            # time.sleep(1)
            # self.swipeWifiConnectListTobeginning()  # 上划置顶
            time.sleep(5)
            self.deleteWifiConnectByName('SOIMT-OA-NET')  # 删除链接
            time.sleep(1)
            self.clickOK()
            time.sleep(1)
            self.closeWifiButton()  # 关闭wifi开关
            time.sleep(1)
        if k == 0:
            return True
        else:
            print('Fail times: ' + str(k))
            return False

    def changeToSettingThemePageFromMorePage50times(self):
        """
        压力测试（首页>More>setting>Bt页面打开关闭BT50次）
        :return: True，False
        """
        k = 0
        for i in range(50):
            homePage().clickScreenHardKeyHomeButton(self)  # 点击Home硬按键
            time.sleep(1)
            homeActivity = pm().get_Current_Activity(self)
            if homeActivity == 'com.saicmotor.launcher.view.MainActivity':
                pass
            else:
                print(str(i) + ' Fail ' + homeActivity)
                k = k + 1
            homePage().clickMore(self)  # 点击More页面
            time.sleep(1)
            morePageActivity = pm().get_Current_Activity(self)
            if morePageActivity == 'com.saicmotor.launcher.view.MoreActivity':
                pass
            else:
                print(str(i) + ' Fail ' + morePageActivity)
                k = k + 1
            time.sleep(1)
            morePage.clickSetting()  # 点击Setting页面
            time.sleep(1)
            settingPageActivity = pm().get_Current_Activity(self)
            if settingPageActivity == 'com.saicmotor.settings.ui.MainActivity':
                pass
            else:
                print(str(i) + ' Fail ' + settingPageActivity)
                k = k + 1
            self.clickTheme()  # 点击BT页面
            time.sleep(1)
            self.chooseThemeBusinnesGrey()  # 切换皮肤
            time.sleep(1)
            self.chooseThemeMysteriousPurple()  # 切换皮肤
        if k == 0:
            return True
        else:
            print('Fail times: ' + str(k))
            return False

    def changeToSettingSoundPageToneEffectFromMorePage50times(self):
        """
        压力测试（首页>More>setting>Sound页面切换各种音效 50次）
        :return: True，False
        """
        k = 0
        for i in range(50):
            homePage().clickScreenHardKeyHomeButton(self)  # 点击Home硬按键
            time.sleep(1)
            homeActivity = pm().get_Current_Activity(self)
            if homeActivity == 'com.saicmotor.launcher.view.MainActivity':
                pass
            else:
                print(str(i) + ' Fail ' + homeActivity)
                k = k + 1
            homePage().clickMore(self)  # 点击More页面
            time.sleep(1)
            morePageActivity = pm().get_Current_Activity(self)
            if morePageActivity == 'com.saicmotor.launcher.view.MoreActivity':
                pass
            else:
                print(str(i) + ' Fail ' + morePageActivity)
                k = k + 1
            time.sleep(1)
            morePage.clickSetting()  # 点击Setting页面
            time.sleep(1)
            settingPageActivity = pm().get_Current_Activity(self)
            if settingPageActivity == 'com.saicmotor.settings.ui.MainActivity':
                pass
            else:
                print(str(i) + ' Fail ' + settingPageActivity)
                k = k + 1
            self.clickSound()  # 点击BT页面
            self.clickToneEffectPage()
            self.clickClassicMode()  # 切换皮肤
            self.clickPopMode()  # 切换皮肤
            self.clickVocalMode()  # 切换皮肤
            self.clickJazzMode()  # 切换皮肤
            self.clickRockMode()  # 切换皮肤
            self.clickManualMode()  # 切换皮肤
            self.clickReset()  # 切换皮肤
        if k == 0:
            return True
        else:
            print('Fail times: ' + str(k))
            return False

    def changeToSettingSoundPageVolumeFromMorePage50times(self):
        """
        压力测试（首页>More>setting>Sound页面Volume页面上滑、下滑50次）
        :return: True，False
        """
        k = 0
        for i in range(50):
            homePage().clickScreenHardKeyHomeButton(self)  # 点击Home硬按键
            time.sleep(1)
            homeActivity = pm().get_Current_Activity(self)
            if homeActivity == 'com.saicmotor.launcher.view.MainActivity':
                pass
            else:
                print(str(i) + ' Fail ' + homeActivity)
                k = k + 1
            homePage().clickMore(self)  # 点击More页面
            time.sleep(1)
            morePageActivity = pm().get_Current_Activity(self)
            if morePageActivity == 'com.saicmotor.launcher.view.MoreActivity':
                pass
            else:
                print(str(i) + ' Fail ' + morePageActivity)
                k = k + 1
            time.sleep(1)
            morePage.clickSetting()  # 点击Setting页面
            time.sleep(1)
            settingPageActivity = pm().get_Current_Activity(self)
            if settingPageActivity == 'com.saicmotor.settings.ui.MainActivity':
                pass
            else:
                print(str(i) + ' Fail ' + settingPageActivity)
                k = k + 1
            self.clickSound()  # 点击BT页面
            self.clickVolumePage()
            self.swipeUpVolumePage()  # 切换皮肤
            self.swipeDownVolumePage()  # 切换皮肤
        if k == 0:
            return True
        else:
            print('Fail times: ' + str(k))
            return False

    def changeToSettingTimePageFromMorePage50times(self):
        """
        压力测试（首页>More>setting>Sound页面Time页面打开关闭时间自动校准50次）
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
                print(str(i) + ' Fail ' + homeActivity)
                k = k + 1
            homePage().clickMore()  # 点击More页面
            time.sleep(1)
            morePageActivity = pm().get_Current_Activity()
            if morePageActivity == 'com.saicmotor.launcher.view.MoreActivity':
                pass
            else:
                print(str(i) + ' Fail ' + morePageActivity)
                k = k + 1
            time.sleep(1)
            morePage.clickSetting()  # 点击Setting页面
            time.sleep(1)
            settingPageActivity = pm().get_Current_Activity()
            if settingPageActivity == 'com.saicmotor.settings.ui.MainActivity':
                pass
            else:
                print(str(i) + ' Fail ' + settingPageActivity)
                k = k + 1
            self.clickTime()  # 点击BT页面
            self.openAutoTimeZone()  # 打开自动校准
            time.sleep(1)
            self.closeAutoTimeZone()  # 关闭自动校准
        if k == 0:
            return True
        else:
            print('Fail times: ' + str(k))
            return False

    def changeToSettingDisplayPageFromMorePage50times(self):
        """
        压力测试（首页>More>setting>Sound页面display页面50次）
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
                print(str(i) + ' Fail ' + homeActivity)
                k = k + 1
            homePage().clickMore()  # 点击More页面
            time.sleep(1)
            morePageActivity = pm().get_Current_Activity()
            if morePageActivity == 'com.saicmotor.launcher.view.MoreActivity':
                pass
            else:
                print(str(i) + ' Fail ' + morePageActivity)
                k = k + 1
            time.sleep(1)
            morePage.clickSetting()  # 点击Setting页面
            time.sleep(1)
            settingPageActivity = pm().get_Current_Activity()
            if settingPageActivity == 'com.saicmotor.settings.ui.MainActivity':
                pass
            else:
                print(str(i) + ' Fail ' + settingPageActivity)
                k = k + 1
            self.clickDisplay()  # 点击display页面
            time.sleep(1)

        if k == 0:
            return True
        else:
            print('Fail times: ' + str(k))
            return False

    def changeToSettingUpdatePageFromMorePage50times(self):
        """
        压力测试（首页>More>setting>Sound页面Update页面50次）
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
                print(str(i) + ' Fail ' + homeActivity)
                k = k + 1
            homePage().clickMore()  # 点击More页面
            time.sleep(1)
            morePageActivity = pm().get_Current_Activity()
            if morePageActivity == 'com.saicmotor.launcher.view.MoreActivity':
                pass
            else:
                print(str(i) + ' Fail ' + morePageActivity)
                k = k + 1
            time.sleep(1)
            morePage.clickSetting()  # 点击Setting页面
            time.sleep(1)
            settingPageActivity = pm().get_Current_Activity()
            if settingPageActivity == 'com.saicmotor.settings.ui.MainActivity':
                pass
            else:
                print(str(i) + ' Fail ' + settingPageActivity)
                k = k + 1
            self.clickUpdate()  # 点击display页面
            time.sleep(1)
            self.clickUpdateBackButton()
        if k == 0:
            return True
        else:
            print('Fail times: ' + str(k))
            return False

    def changeToSettingUpdatePageFromMorePage50times(self):
        """
        压力测试（首页>More>setting>Sound页面Update页面50次）
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
                print(str(i) + ' Fail ' + homeActivity)
                k = k + 1
            homePage().clickMore()  # 点击More页面
            time.sleep(1)
            morePageActivity = pm().get_Current_Activity()
            if morePageActivity == 'com.saicmotor.launcher.view.MoreActivity':
                pass
            else:
                print(str(i) + ' Fail ' + morePageActivity)
                k = k + 1
            time.sleep(1)
            morePage.clickSetting()  # 点击Setting页面
            time.sleep(1)
            settingPageActivity = pm().get_Current_Activity()
            if settingPageActivity == 'com.saicmotor.settings.ui.MainActivity':
                pass
            else:
                print(str(i) + ' Fail ' + settingPageActivity)
                k = k + 1
            self.clickUSBStorage()  # 点击display页面
            time.sleep(1)
        if k == 0:
            return True
        else:
            print('Fail times: ' + str(k))
            return False

    def changeToSettingUserManualPageFromMorePage50times(self):
        """
        压力测试（首页>More>setting>Sound页面UserManual页面50次）
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
                print(str(i) + ' Fail ' + homeActivity)
                k = k + 1
            homePage().clickMore()  # 点击More页面
            time.sleep(1)
            morePageActivity = pm().get_Current_Activity()
            if morePageActivity == 'com.saicmotor.launcher.view.MoreActivity':
                pass
            else:
                print(str(i) + ' Fail ' + morePageActivity)
                k = k + 1
            time.sleep(1)
            morePage.clickSetting()  # 点击Setting页面
            time.sleep(1)
            settingPageActivity = pm().get_Current_Activity()
            if settingPageActivity == 'com.saicmotor.settings.ui.MainActivity':
                pass
            else:
                print(str(i) + ' Fail ' + settingPageActivity)
                k = k + 1
            self.clickUserManual()  # 点击display页面
            time.sleep(1)
        if k == 0:
            return True
        else:
            print('Fail times: ' + str(k))
            return False

    def changeToSettingVoiceAssistantPageFromMorePage50times(self):
        """
        压力测试（首页>More>setting>Sound页面VoiceAssistant页面50次）
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
                print(str(i) + ' Fail ' + homeActivity)
                k = k + 1
            homePage().clickMore()  # 点击More页面
            time.sleep(1)
            morePageActivity = pm().get_Current_Activity()
            if morePageActivity == 'com.saicmotor.launcher.view.MoreActivity':
                pass
            else:
                print(str(i) + ' Fail ' + morePageActivity)
                k = k + 1
            time.sleep(1)
            morePage.clickSetting()  # 点击Setting页面
            time.sleep(1)
            settingPageActivity = pm().get_Current_Activity()
            if settingPageActivity == 'com.saicmotor.settings.ui.MainActivity':
                pass
            else:
                print(str(i) + ' Fail ' + settingPageActivity)
                k = k + 1
            self.clickVoiceAssistant()  # 点击display页面
            time.sleep(1)
        if k == 0:
            return True
        else:
            print('Fail times: ' + str(k))
            return False

    def changeToSettingFactoryResetPageFromMorePage50times(self):
        """
        压力测试（首页>More>setting>Sound页面FactoryReset页面50次）
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
                print(str(i) + ' Fail ' + homeActivity)
                k = k + 1
            homePage().clickMore()  # 点击More页面
            time.sleep(1)
            morePageActivity = pm().get_Current_Activity()
            if morePageActivity == 'com.saicmotor.launcher.view.MoreActivity':
                pass
            else:
                print(str(i) + ' Fail ' + morePageActivity)
                k = k + 1
            time.sleep(1)
            morePage.clickSetting()  # 点击Setting页面
            time.sleep(1)
            settingPageActivity = pm().get_Current_Activity()
            if settingPageActivity == 'com.saicmotor.settings.ui.MainActivity':
                pass
            else:
                print(str(i) + ' Fail ' + settingPageActivity)
                k = k + 1
            self.clickFactoryReset()  # 点击FactoryReset页面
            time.sleep(1)
        if k == 0:
            return True
        else:
            print('Fail times: ' + str(k))
            return False

    def changeToSettingAboutMGPageFromMorePage50times(self):
        """
        压力测试（首页>More>setting>Sound页面AboutMG页面50次）
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
                print(str(i) + ' Fail ' + homeActivity)
                k = k + 1
            homePage().clickMore()  # 点击More页面
            time.sleep(1)
            morePageActivity = pm().get_Current_Activity()
            if morePageActivity == 'com.saicmotor.launcher.view.MoreActivity':
                pass
            else:
                print(str(i) + ' Fail ' + morePageActivity)
                k = k + 1
            time.sleep(1)
            morePage.clickSetting()  # 点击Setting页面
            time.sleep(1)
            settingPageActivity = pm().get_Current_Activity()
            if settingPageActivity == 'com.saicmotor.settings.ui.MainActivity':
                pass
            else:
                print(str(i) + ' Fail ' + settingPageActivity)
                k = k + 1
            self.clickAboutMG()  # 点击AboutMG页面
            time.sleep(1)
        if k == 0:
            return True
        else:
            print('Fail times: ' + str(k))
            return False
