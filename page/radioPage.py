# -*- coding: utf-8 -*-
from page.BasePage import BasePage
from page.publicMethod import publicMethod as pm
import time


class radioPage(BasePage):

    # 点击进入收音机Favorite列表
    def clickEnterFavouritePage(self):
        if pm.find_element_by_id(self, id="com.archermind.saic.radio:id/img_radio_amfm_favourite_selector").exists():
            print("Already in FavouritePage")
            return True
        else:
            element = pm.find_element_by_id(self, id="com.archermind.saic.radio:id/tx_radio_amfm_favourite")
            print("Click EnterFavouritePage")
            pm.click_by_element(self, element=element)
            if pm.find_element_by_id(self,
                                     id="com.archermind.saic.radio:id/img_radio_amfm_favourite_selector").exists():
                print("Enter FavouritePage")
                return True
            else:
                print("Fail to Enter FavouritePage")
                return False

    # 点击进入收音机All列表
    def clickEnterAllPage(self):
        if pm.find_element_by_id(self, id="com.archermind.saic.radio:id/img_radio_amfm_all_selector").exists():
            print("Already in AllPage")
            return True
        else:
            element = pm.find_element_by_id(self, id="com.archermind.saic.radio:id/tx_radio_amfm_all")
            print("Click EnterAllPage")
            pm.click_by_element(self, element=element)
            if pm.find_element_by_id(self,
                                     id="com.archermind.saic.radio:id/img_radio_amfm_all_selector").exists():
                print("Enter AllPage")
                return True
            else:
                print("Fail to Enter AllPage")
                return False

    # 点击搜索电台
    def clickSearchRadio(self):
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        element = pm.find_element_by_id(self, id="com.archermind.saic.radio:id/btn_radio_amfm_search")
        print("Click SearchRadio")
        pm.click_by_element(self, element=element)
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        while True:
            if pm.find_element_by_id(self, id="com.archermind.saic.radio:id/btn_radio_scan_dialog_cancel").exists():
                time.sleep(5)  # 等待搜台
                print("sleep 5s")
            else:
                print("Finish Serach ")
                break
        if pm._find_element_by_text(self, "No Frequency").get_text() == "No Frequency":  # 如果界面有No Frequency显示，说明没有搜到电台
            print("No Frequency")
            return False
        else:
            print("Success to Serach")
            return True

    # 获取当前播放调频电台数值
    def getCurrentChannle(self):
        channel = pm.find_element_by_id(self, id="com.archermind.saic.radio:id/tx_radio_amfm_hz_number").get_text()
        channelType = pm.find_element_by_id(self, id="com.archermind.saic.radio:id/radio_spinner_text").get_text()
        print(channel)
        return channelType + " " + channel

    # 比较实际电台与预期电台（用于FM、AM步进比较）
    def checkFMChannelAfterStepAdd(self):
        channel1 = int(self.getCurrentChannle())
        channel2 = int(self.clickStepAdd())
        absResult = channel1 - channel2
        if absResult == 0.1:
            return True
        else:
            return False

    # 比较实际电台与预期电台（用于FM、AM步减比较）
    def checkFMChannelAfterStepMinus(self):
        channel1 = int(self.getCurrentChannle())
        channel2 = int(self.clickStepMinus())
        absResult = channel1 - channel2
        if absResult == 0.1:
            return True
        else:
            return False

    # 比较实际电台与预期电台（用于FM、AM步进比较）
    def checkAMChannelAfterStepAdd(self):
        channel1 = int(self.getCurrentChannle())
        channel2 = int(self.clickStepAdd())
        absResult = channel1 - channel2
        if absResult == 9:
            return True
        else:
            return False

    # 比较实际电台与预期电台（用于FM、AM步减比较）
    def checkAMChannelAfterStepMinus(self):
        channel1 = int(self.getCurrentChannle())
        channel2 = int(self.clickStepMinus())
        absResult = channel1 - channel2
        if absResult == 9:
            return True
        else:
            return False

    # 点击步进+
    def clickStepAdd(self):
        element = pm.find_element_by_id(self, id="com.archermind.saic.radio:id/btn_radio_amfm_add")
        print("Click StepAdd")
        return pm.click_by_element(self, element=element)

    # 点击步进-
    def clickStepMinus(self):
        element = pm.find_element_by_id(self, id="com.archermind.saic.radio:id/btn_radio_amfm_minus")
        print("Click StepMinus")
        return pm.click_by_element(self, element=element)

    # 点击上一个有效电台
    def clickLastStation(self):
        element = pm.find_element_by_id(self, id="com.archermind.saic.radio:id/btn_radio_amfm_last")
        print("Click LastStation")
        currentChannel = self.getCurrentChannle()  # 获取当前电台调频
        print("currentChannel " + currentChannel)
        pm.click_by_element(self, element=element)
        while True:
            if pm.find_element_by_id(self, id="com.archermind.saic.radio:id/btn_radio_search_dialog_cancel").exists():
                time.sleep(3)  # 等待搜台
                print("sleep 3s")
            else:
                channelAfterStep = self.getCurrentChannle()  # 点击事件后的电台调频
                print("channelAfterStep " + channelAfterStep)
                break
        if currentChannel == channelAfterStep:  # 电台没有变化
            return False
        else:
            return True

    # 点击下一个有效电台
    def clickNextStation(self):
        element = pm.find_element_by_id(self, id="com.archermind.saic.radio:id/btn_radio_amfm_next")
        print("Click NextStation")
        currentChannel = self.getCurrentChannle()  # 获取当前电台调频
        pm.click_by_element(self, element=element)
        channelAfterStep = self.getCurrentChannle()  # 点击事件后的电台调频
        print("currentChannel " + currentChannel)
        while True:
            if pm.find_element_by_id(self, id="com.archermind.saic.radio:id/btn_radio_search_dialog_cancel").exists():
                time.sleep(3)  # 等待搜台
                print("sleep 3s")
            else:
                channelAfterStep = self.getCurrentChannle()  # 点击事件后的电台调频
                print("channelAfterStep " + channelAfterStep)
                break
        if currentChannel == channelAfterStep:  # 电台没有变化
            return False
        else:
            return True

    # 点击暂停电台(点击后能查到播放图标表示状态切换成功)
    def clickPauseStation(self):
        element = pm.find_element_by_id(self, id="com.archermind.saic.radio:id/btn_radio_amfm_pause")
        print("Click PauseStation")
        pm.click_by_element(self, element=element)
        if pm.find_element_by_id(self, id="com.archermind.saic.radio:id/btn_radio_amfm_play").exists:
            print('change status to Pause success')
            return True
        else:
            return False

    # 点击播放电台
    def clickPlayStation(self):
        element = pm.find_element_by_id(self, id="com.archermind.saic.radio:id/btn_radio_amfm_play")
        print("Click PlayStation")
        pm.click_by_element(self, element=element)
        if pm.find_element_by_id(self, id="com.archermind.saic.radio:id/btn_radio_amfm_pause").exists:
            print('change status to Play success')
            return True
        else:
            return False

    # 切换AM FM DRM调频
    def changeRadio(self):
        element = pm.find_element_by_id(self, id="com.archermind.saic.radio:id/radio_spinner")
        print("Click changeRadio")
        return pm.click_by_element(self, element=element)

    # 切换FM调频
    def changeToFM(self):
        self.changeRadio()
        element = pm.find_element_by_id(self, id="com.archermind.saic.radio:id/btn_fm")
        print("Click changeToFM")
        pm.click_by_element(self, element=element)
        time.sleep(0.5)
        if pm.find_element_by_id(self, id="com.archermind.saic.radio:id/tx_radio_amfm_hz_type").get_text() == 'MHz':
            print('change status to FM success')
            return True
        else:
            return False

    # 切换AM调频
    def changeToAM(self):
        self.changeRadio()
        element = pm.find_element_by_id(self, id="com.archermind.saic.radio:id/btn_am")
        print("Click changeToAM")
        pm.click_by_element(self, element=element)
        time.sleep(0.5)
        if pm.find_element_by_id(self, id="com.archermind.saic.radio:id/tx_radio_amfm_hz_type").get_text() == 'KHz':
            print('change status to AM success')
            return True
        else:
            pm.find_element_by_id(self, id="com.archermind.saic.radio:id/tx_radio_amfm_hz_type").get_text()
            return False

    # 切换DRM调频
    def changeToDRM(self):
        element = pm.find_element_by_id(self, id="com.archermind.saic.radio:id/btn_fm")
        print("Click changeToDRM")
        return pm.click_by_element(self, element=element)

    # 点击收藏AM FM收音机电台
    def clickCollectAMFMHeartIcon(self):
        element = pm.find_element_by_id(self,
                                        id="com.archermind.saic.radio:id/btn_radio_amfm_non_heart")  # 获取未收藏图标进行判断当前是否需要收藏
        if element.exists():
            print("Click Collect")
            pm.click_by_element(self, element=element)
            elementAfterClick = pm.find_element_by_id(self,
                                                      id="com.archermind.saic.radio:id/btn_radio_amfm_heart")  # 获取已收藏图标进行判断是否已被收藏
            if elementAfterClick.exists():
                print("Collected Success")
                return True
            else:
                return False
        else:
            print("Already Collected")
            return True

    # 取消AM FM收藏
    def clickCancelAMFMHeartIcon(self):
        element = pm.find_element_by_id(self,
                                        id="com.archermind.saic.radio:id/btn_radio_amfm_heart")  # 获取已收藏图标进行判断当前是否需要被取消收藏
        if element.exists():
            print("Click UnCollect")
            pm.click_by_element(self, element=element)
            elementAfterClick = pm.find_element_by_id(self,
                                                      id="com.archermind.saic.radio:id/btn_radio_amfm_non_heart")  # 获取未收藏图标进行判断是否已被取消收藏
            if elementAfterClick.exists():
                print("UnCollected Success")
                return True
            else:
                return False
        else:
            print("Already UnCollected")
            return True

    # 点击收藏DRM收音机电台
    def clickCollectDRMHeartIcon(self):
        element = pm.find_element_by_id(self, id="com.archermind.saic.radio:id/non_favorite_image")
        print("Click clickCollectDRMHeartIcon")
        return pm.click_by_element(self, element=element)

    # 取消DRM收藏
    def clickCancelDRMHeartIcon(self):
        element = pm.find_element_by_id(self, id="com.archermind.saic.radio:id/favorite_image")
        status = element.info['focusable']
        print("Click clickCancelDRMHeartIcon")
        return pm.click_by_element(self, element=element)

    # 取消自动搜台
    def cancelScan(self):
        element = pm._find_element_by_text(self, text="Cancel")
        # status = element.info['focusable']
        print("Click cancelScan")
        return pm.click_by_element(self, element=element)

    # 检查AM波段尺的调频是否正确
    def checkAMBand(self):
        element531 = pm.find_element_by_id(self, id="com.archermind.saic.radio:id/tx_radio_amfm_522").info['text']
        element738 = pm.find_element_by_id(self, id="com.archermind.saic.radio:id/tx_radio_amfm_850").info['text']
        element1071 = pm.find_element_by_id(self, id="com.archermind.saic.radio:id/tx_radio_amfm_1100").info['text']
        element1404 = pm.find_element_by_id(self, id="com.archermind.saic.radio:id/tx_radio_amfm_1360").info['text']
        element1629 = pm.find_element_by_id(self, id="com.archermind.saic.radio:id/tx_radio_amfm_1620").info['text']
        print(type(element1629))
        if element531 == '531' and element738 == '738' and element1071 == '1071' and element1404 == '1404' and element1629 == '1629':
            print('True ' + element531 + ' ' + element738 + ' ' + element1071 + ' ' + element1404 + ' ' + element1629)
            return True
        else:
            print('False ' + element531 + ' ' + element738 + ' ' + element1071 + ' ' + element1404 + ' ' + element1629)
            return False

    # 检查FM波段尺的调频是否正确
    def checkFMBand(self):
        element531 = pm.find_element_by_id(self, id="com.archermind.saic.radio:id/tx_radio_amfm_522").info['text']
        element738 = pm.find_element_by_id(self, id="com.archermind.saic.radio:id/tx_radio_amfm_850").info['text']
        element1071 = pm.find_element_by_id(self, id="com.archermind.saic.radio:id/tx_radio_amfm_1100").info['text']
        element1404 = pm.find_element_by_id(self, id="com.archermind.saic.radio:id/tx_radio_amfm_1360").info['text']
        element1629 = pm.find_element_by_id(self, id="com.archermind.saic.radio:id/tx_radio_amfm_1620").info['text']
        print(type(element1629))
        if element531 == '87.5' and element738 == '91.6' and element1071 == '97.8' and element1404 == '104.0' and element1629 == '108.0':
            print('True ' + element531 + ' ' + element738 + ' ' + element1071 + ' ' + element1404 + ' ' + element1629)
            return True
        else:
            print('False ' + element531 + ' ' + element738 + ' ' + element1071 + ' ' + element1404 + ' ' + element1629)
            return False

    # 检查DRM波段尺的调频是否正确
    def checkDRMBand(self):
        element531 = pm.find_element_by_id(self, id="com.archermind.saic.radio:id/tx_radio_amfm_522").info['text']
        element738 = pm.find_element_by_id(self, id="com.archermind.saic.radio:id/tx_radio_amfm_850").info['text']
        element1071 = pm.find_element_by_id(self, id="com.archermind.saic.radio:id/tx_radio_amfm_1100").info['text']
        element1404 = pm.find_element_by_id(self, id="com.archermind.saic.radio:id/tx_radio_amfm_1360").info['text']
        element1629 = pm.find_element_by_id(self, id="com.archermind.saic.radio:id/tx_radio_amfm_1620").info['text']
        print(type(element1629))
        if element531 == '531' and element738 == '738' and element1071 == '1071' and element1404 == '1404' and element1629 == '1602':
            print('True ' + element531 + ' ' + element738 + ' ' + element1071 + ' ' + element1404 + ' ' + element1629)
            return True
        else:
            print('False ' + element531 + ' ' + element738 + ' ' + element1071 + ' ' + element1404 + ' ' + element1629)
            return False

    # 向右滑动Radio Favorite收藏列表
    def swipRightFavorite(self):
        BasePage.d(className="android.support.v7.widget.RecyclerView").swipe('right', steps=5)

    # 向左滑动Radio Favorite收藏列表
    def swipLeftFavorite(self):
        BasePage.d(className="android.support.v7.widget.RecyclerView").swipe('left', steps=5)

    # 向左滑到Radio Favorite收藏列表最左侧
    def swipeToTheEndOfLeftFavorite(self):
        # 获取当前收藏页面第一个频道
        nameStr = BasePage.d(className="android.support.v7.widget.RecyclerView").child(
            className="android.widget.RelativeLayout").child(className="android.widget.TextView").get_text()
        print("Current Channel ：" + nameStr)
        while True:
            self.swipRightFavorite()
            nameAfterSwip = BasePage.d(className="android.support.v7.widget.RecyclerView").child(
                className="android.widget.RelativeLayout").child(className="android.widget.TextView").get_text()
            print(nameAfterSwip)
            if nameAfterSwip != nameStr:  # 比较频道，如果不同后者赋值前者继续进行滑动比较
                print("Channle Before Swip ：" + nameStr)
                print("Channle After Swip ：" + nameAfterSwip)
                nameStr = nameAfterSwip
            else:
                print("Channle Before Swip：" + nameStr)
                print("Channle After Swip：" + nameAfterSwip)
                print("Already to the end of Left")
                break

    # 向左滑动确认是否是Favorite最后一页
    def comfirmIsTheEndOfRightFavoritePage(self):
        # 获取当前收藏页面第一个频道
        nameStr = BasePage.d(className="android.support.v7.widget.RecyclerView").child(
            className="android.widget.RelativeLayout").child(className="android.widget.TextView").get_text()
        print("Current Channel ：" + nameStr)
        self.swipLeftFavorite()
        nameAfterSwip = BasePage.d(className="android.support.v7.widget.RecyclerView").child(
            className="android.widget.RelativeLayout").child(className="android.widget.TextView").get_text()
        print(nameAfterSwip)
        if nameAfterSwip != nameStr:  # 比较频道，如果不同后者赋值前者继续进行滑动比较
            print("Channle Before Swip ：" + nameStr)
            print("Channle After Swip ：" + nameAfterSwip)
            return False
        else:
            print("Channle Before Swip：" + nameStr)
            print("Channle After Swip：" + nameAfterSwip)
            print("Already to the end of Right")
            return True

    # 比较收音机电台是否在Favorite列表中
    def compareRadioChannelisExist(self, channel):
        number = 1  # 初始值
        flag = False
        while number <= 6:
            nameStr = pm.find_element_by_Xpath(self,
                                               Xpath='//*[@resource-id="com.archermind.saic.radio:id/recycler_view_favorite"]'
                                                     '/android.widget.RelativeLayout[' + str(
                                                   number) + ']/android.widget.TextView').get_text()
            print(nameStr)
            if channel != nameStr:  # 比较频道，如果不同后者赋值前者继续进行比较
                print("Enter Channel ：" + channel)
                print("Position : Channel : " + str(number) + "  " + nameStr)
                print('number :' + str(number))
                number += 1
            else:
                print("Enter Channel ：" + channel)
                print("Position : Channel : " + str(number) + "  " + nameStr)
                print("Already get")
                flag = True
                break
        return flag

    # 滑动查找指定调频是否在收藏列表中已经保存成功
    def isExistsInFavoriteListByChannel(self, channel):
        result = False
        self.swipeToTheEndOfLeftFavorite()  # 先滑到最左侧Favorite起点\
        while True:
            flag = self.compareRadioChannelisExist(channel)  # 比较电台
            if flag != True:
                self.comfirmIsTheEndOfRightFavoritePage()  # 左划至下一页并确认不是最后一页
            else:
                result = flag  # 已经找到指定电台并赋返回值True
                break
        return result

    # 滑动查找指定调频是否在收藏列表中已经保存成功
    def isCurrentChannleExistsInFavoriteList(self):
        result = False
        currentChannel = self.getCurrentChannle()
        print("currentChannel " + currentChannel)
        self.swipeToTheEndOfLeftFavorite()  # 先滑到最左侧Favorite起点\
        while True:
            flag = self.compareRadioChannelisExist(currentChannel)  # 比较电台
            if flag != True:
                self.comfirmIsTheEndOfRightFavoritePage()  # 左划至下一页并确认不是最后一页
            else:
                result = flag  # 已经找到指定电台并赋返回值True
                break
        return result

        # elements=BasePage.d.xpath('//*[starts-with(text(), "FM ")]')
        # name1 = elements[0].child(className="android.widget.TextView").get_text()
        # name2 = elements[1].child(className="android.widget.TextView").get_text()
        # name3 = elements[2].child(className="android.widget.TextView").get_text()

        # print(name2)
        # print(name3)
        # for ele in elements:

        # name = element.child(className="android.widget.RelativeLayout").child(className="android.widget.TextView").get_text()
        # name = pm.get_text_by_element(self, element[1])
        # print("name = " + str(name))
        print("---")

    '''
    ————————————————————————————
    '''

    # 点击进入MUSIC
    def clickVehicle(self):
        element = pm._find_element_by_text(self, text="MUSIC")
        print("Click MUSIC")
        return pm.click_by_element(self, element=element)

    # 点击进入MG iSMART
    def clickMG(self):
        element = pm._find_element_by_text(self, "MG iSMART")
        print("Click MG iSMART")
        return pm.click_by_element(self, element=element)

    # 点击进入MG Radio
    def clickRadio(self):
        element = pm._find_element_by_text(self, "Radio")
        print("Click Radio")
        return pm.click_by_element(self, element=element)

    # 点击进入BT Phone
    def clickBT_Phone(self):
        element = pm._find_element_by_text(self, "BT Phone")
        print("Click BT Phone")
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
        element = pm._find_element_by_text(self, text="Vehicle Setting")
        print("Click Vehicle_setting")
        return pm.click_by_element(self, element=element)

    # 点击进入Folder
    def clickFolder(self):
        element = pm._find_element_by_text(self, text="Folder")
        print("Click Folder")
        return pm.click_by_element(self, element=element)

    '''
    #点击进入Inbox
    def clickInbox(self):
        element = pm._find_element_by_text(self, text="Inbox")
        print("Click Inbox")
        return pm.click_by_element(self, element=element)
    '''

    # 滑动点击进入Inbox
    def clickInbox(self):
        # 获取主页右侧RecyclerView并上拉
        BasePage._find_element_by_ClassName(self, className="android.support.v7.widget.RecyclerView").swipe('up',
                                                                                                            steps=1)
        print("swipe test")
        element = pm._find_element_by_text(self, text="Inbox")
        print("swipe Inbox")
        return pm.click_by_element(self, element=element)

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


if __name__ == '__main__':
    # homePage.clickHome()
    pass
