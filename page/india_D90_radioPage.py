# -*- coding: utf-8 -*-
from UIconfig.Base import Base
from page.PublicMethod import PublicMethod as pm
from page.india_D90_homePage import india_D90_homePage as homePage
import time
import os
import UIconfig.logger as loggers

logger = loggers.Logger()
os.path.abspath('.')


class india_D90_radioPage(Base):

    # 点击进入收音机Favorite列表
    def clickFavouritePage(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'FAVORITE')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    # 点击进入收音机All列表
    def clickAllPage(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'ALL')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    # 点击搜索电台
    def clickSearchRadioWithCheck(self):
        logger.info(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        id = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'SearchButton')
        element = pm().find_element_by_id(id=id)
        pm().click_by_element(element=element)
        logger.info(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        cancelId = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'CancelSearchButton')
        while True:
            if pm().find_element_by_id(id=cancelId) is not None:
                time.sleep(5)  # 等待搜台
                logger.info("searching")
            else:
                logger.info("Finish Serach ")
                break
        NoFrequency = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'NoFrequency')
        if pm()._find_element_by_text(NoFrequency) is None:  # 如果界面有No Frequency显示，说明没有搜到电台
            logger.info("No Frequency")
            return False
        else:
            logger.info("Success to Serach")
            return True

    # 点击搜索电台
    def clickSearchRadioWithoutCheck(self):
        """
        点击自动搜台（无搜台过程校验）
        :return: True搜台点击成功,False搜台点击失败
        """
        logger.info(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        id = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'SearchButton')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def cancelScan(self):
        """
        取消自动搜台
        :return: True点击成功 ,False点击失败
        """
        cancelId = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'CancelSearchButton')
        element = pm()._find_element_by_id(id=cancelId)
        return pm().click_by_element(element=element)

    def getCurrentChannle(self):
        """
        获取当前播放调频电台FM/AM+数值
        :return: 如FM 97.2,AM 103
        """
        radioNumberId = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'RadioNumber')
        RadioSpinnerTextId = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'RadioSpinnerText')
        channel = pm().find_element_by_id(id=radioNumberId).get_text()
        RadioSpinnerText = pm().find_element_by_id(id=RadioSpinnerTextId).get_text()
        logger.info(RadioSpinnerText + " " + channel)
        return RadioSpinnerText + " " + channel

    def getCurrentChannleNum(self):
        """
        获取当前播放调频电台数值部分
        :return: 如：97.2
        """
        radioNumberId = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'RadioNumber')
        channel = pm().find_element_by_id(id=radioNumberId).get_text()
        logger.info(channel)
        return channel

    def getCurrentDrmChannle(self):
        """
        获取当前播放调频电台DRM/DRM+数值
        :return: 如DRM 549
        """
        radioNumberId = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'RadioDrmNumber')
        RadioSpinnerTextId = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'RadioSpinnerText')
        channel = pm().find_element_by_id(id=radioNumberId).get_text()
        RadioSpinnerText = pm().find_element_by_id(id=RadioSpinnerTextId).get_text()
        logger.info(RadioSpinnerText + " " + channel)
        return RadioSpinnerText + " " + channel

    def getCurrentDrmChannleNum(self):
        """
        获取当前DRM播放调频电台数值部分
        :return: 如：549
        """
        radioNumberId = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'RadioDrmNumber')
        channel = pm().find_element_by_id(id=radioNumberId).get_text()
        logger.info(channel)
        return channel

    def checkFMChannelAfterStepAdd(self):
        """
        比较实际电台与预期电台（用于FM、AM步进比较）
        :return:
        """
        channel1 = float(self.getCurrentChannleNum())
        logger.info(channel1)
        self.clickStepAdd()
        channel2 = float(self.getCurrentChannleNum())
        logger.info(channel2)
        absResult = abs(round(channel1 - channel2, 1))
        logger.info(absResult)
        if absResult == 0.1:
            return True
        else:
            return False

    # 比较实际电台与预期电台（用于FM、AM步减比较）
    def checkFMChannelAfterStepMinus(self):
        channel1 = float(self.getCurrentChannleNum())
        logger.info(channel1)
        self.clickStepMinus()
        channel2 = float(self.getCurrentChannleNum())
        logger.info(channel2)
        absResult = abs(round(channel1 - channel2, 1))
        logger.info(absResult)
        if absResult == 0.1:
            return True
        else:
            return False

    def checkAMDRMChannelAfterStepAdd(self):
        """
        比较实际电台与预期电台（用于AM、DRM步进值9比较）
        :return: True正确，False错误
        """
        channel1 = float(self.getCurrentChannleNum())
        logger.info(channel1)
        self.clickDrmStepAdd()
        channel2 = float(self.getCurrentChannleNum())
        logger.info(channel2)
        absResult = abs(round(channel1 - channel2, 1))
        logger.info(absResult)
        if absResult == 9:
            return True
        else:
            return False

    def checkAMDRMChannelAfterStepMinus(self):
        """
        # 比较实际电台与预期电台（用于FM、AM步减值9比较）
        :return: True正确，False错误
        """
        channel1 = float(self.getCurrentChannleNum())
        logger.info(channel1)
        self.clickDrmStepMinus()
        channel2 = float(self.getCurrentChannleNum())
        logger.info(channel2)
        absResult = abs(round(channel1 - channel2, 1))
        logger.info(absResult)
        if absResult == 9:
            return True
        else:
            return False

    # 点击步进+
    def clickStepAdd(self):
        stepAddId = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'RadioAdd')
        element = pm().find_element_by_id(id=stepAddId)
        logger.info("Click StepAdd")
        return pm().click_by_element(element=element)

    # 点击步进-
    def clickStepMinus(self):
        radioMinusId = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'RadioMinus')
        element = pm().find_element_by_id(id=radioMinusId)
        logger.info("Click StepMinus")
        return pm().click_by_element(element=element)

    # 点击上一个有效电台
    def clickLastStation(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'LastChannel')
        cancelId = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'CancelSearchButton')
        element = pm().find_element_by_id(id=id)
        logger.info("Click LastStation")
        currentChannel = self.getCurrentChannle()  # 获取当前电台调频
        logger.info("currentChannel " + currentChannel)
        pm().click_by_element(element=element)
        while True:
            if pm().find_element_by_id(id=cancelId) is not None:
                time.sleep(3)  # 等待搜台
                logger.info("sleep 3s")
            else:
                channelAfterStep = self.getCurrentChannle()  # 点击事件后的电台调频
                logger.info("channelAfterStep " + channelAfterStep)
                break
        if currentChannel == channelAfterStep:  # 电台没有变化
            return False
        else:
            return True

    # 点击下一个有效电台
    def clickNextStation(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'NextChannel')
        cancelId = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'CancelSearchButton')
        element = pm().find_element_by_id(id=id)
        logger.info("Click NextStation")
        currentChannel = self.getCurrentChannle()  # 获取当前电台调频
        pm().click_by_element(element=element)
        logger.info("currentChannel " + currentChannel)
        while True:
            if pm().find_element_by_id(id=cancelId) is not None:
                time.sleep(3)  # 等待搜台
                logger.info("sleep 3s")
            else:
                channelAfterStep = self.getCurrentChannle()  # 点击事件后的电台调频
                logger.info("channelAfterStep " + channelAfterStep)
                break
        if currentChannel == channelAfterStep:  # 电台没有变化
            return False
        else:
            return True

    def clickDrmStepAdd(self):
        """
        点击步进+
        :return: True点击成功，False点击失败
        """
        stepAddId = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'RadioDrmAdd')
        element = pm().find_element_by_id(id=stepAddId)
        logger.info("Click StepAdd")
        return pm().click_by_element(element=element)

    def clickDrmStepMinus(self):
        """
        点击步进-
        :return: True点击成功，False点击失败
        """
        radioMinusId = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'RadioDrmMinus')
        element = pm().find_element_by_id(id=radioMinusId)
        logger.info("Click StepMinus")
        return pm().click_by_element(element=element)

    def clickLastDrmStation(self):
        """
        点击上一个DRM有效电台
        :return: True点击成功,False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'LastDrmChannel')
        cancelId = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'CancelSearchButton')
        element = pm().find_element_by_id(id=id)
        logger.info("Click LastStation")
        currentChannel = self.getCurrentDrmChannle()  # 获取当前电台调频
        logger.info("currentChannel " + currentChannel)
        pm().click_by_element(element=element)
        while True:
            if pm().find_element_by_id(id=cancelId) is not None:
                time.sleep(3)  # 等待搜台
                logger.info("sleep 3s")
            else:
                channelAfterStep = self.getCurrentDrmChannle()  # 点击事件后的电台调频
                logger.info("channelAfterStep " + channelAfterStep)
                break
        if currentChannel == channelAfterStep:  # 电台没有变化
            return False
        else:
            return True

    def clickNextDrmStation(self):
        """
        点击下一个有效电台
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'NextDrmChannel')
        cancelId = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'CancelSearchButton')
        element = pm().find_element_by_id(id=id)
        logger.info("Click NextStation")
        currentChannel = self.getCurrentDrmChannle()  # 获取当前电台调频
        pm().click_by_element(element=element)
        logger.info("currentChannel " + currentChannel)
        while True:
            if pm().find_element_by_id(id=cancelId) is not None:
                time.sleep(3)  # 等待搜台
                logger.info("sleep 3s")
            else:
                channelAfterStep = self.getCurrentDrmChannle()  # 点击事件后的电台调频
                logger.info("channelAfterStep " + channelAfterStep)
                break
        if currentChannel == channelAfterStep:  # 电台没有变化
            return False
        else:
            return True

    def checkRadioStatusIsPlaying(self):
        """
        检查Radio是否播放状态
        :return: True播放中，False暂停中
        """
        playId = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'PlayButton')
        element = pm().find_element_by_id(id=playId)
        if element is not None:
            return False
        else:
            return True

    def checkRadioStatusIsPausing(self):
        """
        检查Radio是否暂停状态
        :return: True播放中，False暂停中
        """
        pauseId = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'PauseButton')
        element = pm().find_element_by_id(id=pauseId)
        if element is not None:
            return False
        else:
            return True

    # 点击暂停电台(点击后能查到播放图标表示状态切换成功)
    def clickPauseStation(self):
        pauseId = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'PauseButton')
        element = pm().find_element_by_id(id=pauseId)
        logger.info("Click PauseStation")
        pm().click_by_element(element=element)
        playId = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'PlayButton')
        if pm().find_element_by_id(id=playId) is not None:
            logger.info('change status to Pause success')
            return True
        else:
            return False

    # 点击播放电台
    def clickPlayStation(self):
        playId = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'PlayButton')
        element = pm().find_element_by_id(id=playId)
        logger.info("Click PlayStation")
        pm().click_by_element(element=element)
        pauseId = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'PauseButton')
        if pm().find_element_by_id(id=pauseId) is not None:
            logger.info('change status to Play success')
            return True
        else:
            return False

    # 切换AM FM DRM调频
    def changeRadio(self):
        radioSpinner = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'RadioSpinner')
        element = pm().find_element_by_id(id=radioSpinner)
        logger.info("Click changeRadio")
        return pm().click_by_element(element=element)

    # 切换FM调频
    def changeToFM(self):
        self.changeRadio()
        FM = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'FM')
        element = pm().find_element_by_id(id=FM)
        logger.info("Click changeToFM")
        pm().click_by_element(element=element)
        time.sleep(0.5)
        radioTypeId = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'RadioType')
        if pm().find_element_by_id(id=radioTypeId).get_text() == 'MHz':
            logger.info('change status to FM success')
            return True
        else:
            return False

    # 切换AM调频
    def changeToAM(self):
        self.changeRadio()
        AM = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'AM')
        element = pm().find_element_by_id(id=AM)
        logger.info("Click changeToAM")
        pm().click_by_element(element=element)
        time.sleep(0.5)
        radioTypeId = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'RadioType')
        if pm().find_element_by_id(id=radioTypeId).get_text() == 'KHz':
            logger.info('change status to AM success')
            return True
        else:
            return False

    # 切换DRM调频
    def changeToDRM(self):
        self.changeRadio()
        DRM = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'DRM')
        element = pm().find_element_by_id(id=DRM)
        logger.info("Click changeToDRM")
        pm().click_by_element(element=element)
        time.sleep(0.5)
        radioTypeId = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'RadioType')
        if pm().find_element_by_id(id=radioTypeId).get_text() == 'KHz':
            logger.info('change status to AM success')
            return True
        else:
            return False

    # 点击收藏AM FM收音机电台
    def clickCollectAMFMHeartIcon(self):
        noFavorite = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'FmAmNoFavorite')
        favorite = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'FmAmFavorite')
        element = pm().find_element_by_id(id=noFavorite)  # 获取未收藏图标进行判断当前是否需要收藏
        if element is not None:
            logger.info("Click Collect")
            pm().click_by_element(element=element)
            elementAfterClick = pm().find_element_by_id(id=favorite)  # 获取已收藏图标进行判断是否已被收藏
            if elementAfterClick is not None:
                logger.info("Collected Success")
                return True
            else:
                return False
        else:
            logger.info("Already Collected")
            return True

    # 取消AM FM收藏
    def clickCancelAMFMHeartIcon(self):
        noFavorite = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'FmAmNoFavorite')
        favorite = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'FmAmFavorite')
        element = pm().find_element_by_id(id=favorite)  # 获取已收藏图标进行判断当前是否需要被取消收藏
        if element is not None:
            logger.info("Click UnCollect")
            pm().click_by_element(element=element)
            elementAfterClick = pm().find_element_by_id(id=noFavorite)  # 获取未收藏图标进行判断是否已被取消收藏
            if elementAfterClick is not None:
                logger.info("UnCollected Success")
                return True
            else:
                return False
        else:
            logger.info("Already UnCollected")
            return True

    # 点击收藏DRM收音机电台
    def clickCollectDRMHeartIcon(self):
        noFavorite = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'DrmNoFavorite')
        favorite = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'DrmFavorite')
        element = pm().find_element_by_id(id=noFavorite)
        if element is not None:
            pm().click_by_element(element=element)
            elementAfterClick = pm().find_element_by_id(id=favorite)  # 获取未收藏图标进行判断是否已被取消收藏
            if elementAfterClick is not None:
                logger.info("Collected Success")
                return True
            else:
                return False
        else:
            logger.info("Already UnCollected")
            return True

    # 取消DRM收藏
    def clickCancelDRMHeartIcon(self):
        noFavorite = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'DrmNoFavorite')
        favorite = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'DrmFavorite')
        element = pm().find_element_by_id(id=favorite)
        if element is not None:
            pm().click_by_element(element=element)
            elementAfterClick = pm().find_element_by_id(id=favorite)  # 获取未收藏图标进行判断是否已被取消收藏
            if elementAfterClick is not None:
                logger.info("UnCollected Success")
                return True
            else:
                return False
        else:
            logger.info("Already UnCollected")
            return True

    def checkAMBand(self):
        """
        检查AM波段尺的调频是否正确（531 711 900 1080 1260 1449 1629）
        :return: True正确，False
        """
        RadioNumber1 = pm().find_element_by_id(id=pm().readConfigByModuleAndKey('india_D90', 'radioPage',
                                                                                'RadioNumber1')).info['text']
        RadioNumber2 = pm().find_element_by_id(id=pm().readConfigByModuleAndKey('india_D90', 'radioPage',
                                                                                'RadioNumber2')).info['text']
        RadioNumber3 = pm().find_element_by_id(id=pm().readConfigByModuleAndKey('india_D90', 'radioPage',
                                                                                'RadioNumber3')).info['text']
        RadioNumber4 = pm().find_element_by_id(id=pm().readConfigByModuleAndKey('india_D90', 'radioPage',
                                                                                'RadioNumber4')).info['text']
        RadioNumber5 = pm().find_element_by_id(id=pm().readConfigByModuleAndKey('india_D90', 'radioPage',
                                                                                'RadioNumber5')).info['text']
        RadioNumber6 = pm().find_element_by_id(id=pm().readConfigByModuleAndKey('india_D90', 'radioPage',
                                                                                'RadioNumber6')).info['text']
        RadioNumber7 = pm().find_element_by_id(id=pm().readConfigByModuleAndKey('india_D90', 'radioPage',
                                                                                'RadioNumber7')).info['text']
        if RadioNumber1 == '531' and RadioNumber2 == '711' and RadioNumber3 == '900' and RadioNumber4 == '1080' and RadioNumber5 == '1260' and RadioNumber6 == '1449' and RadioNumber7 == '1629':
            return True
        else:
            return False

    def checkFMBand(self):
        """
        检查FM波段尺的调频是否正确（87.5 91.0 94.4 97.8 101.2 104.6 108.0）
        :return: True正确，False错误
        """
        RadioNumber1 = pm().find_element_by_id(id=pm().readConfigByModuleAndKey('india_D90', 'radioPage',
                                                                                'RadioNumber1')).info['text']
        RadioNumber2 = pm().find_element_by_id(id=pm().readConfigByModuleAndKey('india_D90', 'radioPage',
                                                                                'RadioNumber2')).info['text']
        RadioNumber3 = pm().find_element_by_id(id=pm().readConfigByModuleAndKey('india_D90', 'radioPage',
                                                                                'RadioNumber3')).info['text']
        RadioNumber4 = pm().find_element_by_id(id=pm().readConfigByModuleAndKey('india_D90', 'radioPage',
                                                                                'RadioNumber4')).info['text']
        RadioNumber5 = pm().find_element_by_id(id=pm().readConfigByModuleAndKey('india_D90', 'radioPage',
                                                                                'RadioNumber5')).info['text']
        RadioNumber6 = pm().find_element_by_id(id=pm().readConfigByModuleAndKey('india_D90', 'radioPage',
                                                                                'RadioNumber6')).info['text']
        RadioNumber7 = pm().find_element_by_id(id=pm().readConfigByModuleAndKey('india_D90', 'radioPage',
                                                                                'RadioNumber7')).info['text']
        if RadioNumber1 == '87.5' and RadioNumber2 == '91.0' and RadioNumber3 == '94.4' and RadioNumber4 == '97.8' and RadioNumber5 == '101.2' and RadioNumber6 == '104.6' and RadioNumber7 == '108.0':
            return True
        else:
            return False

    # 检查DRM波段尺的调频是否正确
    def checkDRMBand(self):
        """
        检查DRM波段尺的调频是否正确（531 711 891 1071 1442 1602）
        :return:
        """
        RadioNumber1 = pm().find_element_by_id(id=pm().readConfigByModuleAndKey('india_D90', 'radioPage',
                                                                                'RadioNumber1')).info['text']
        RadioNumber2 = pm().find_element_by_id(id=pm().readConfigByModuleAndKey('india_D90', 'radioPage',
                                                                                'RadioNumber2')).info['text']
        RadioNumber3 = pm().find_element_by_id(id=pm().readConfigByModuleAndKey('india_D90', 'radioPage',
                                                                                'RadioNumber3')).info['text']
        RadioNumber4 = pm().find_element_by_id(id=pm().readConfigByModuleAndKey('india_D90', 'radioPage',
                                                                                'RadioNumber4')).info['text']
        RadioNumber5 = pm().find_element_by_id(id=pm().readConfigByModuleAndKey('india_D90', 'radioPage',
                                                                                'RadioNumber5')).info['text']
        RadioNumber6 = pm().find_element_by_id(id=pm().readConfigByModuleAndKey('india_D90', 'radioPage',
                                                                                'RadioNumber6')).info['text']
        RadioNumber7 = pm().find_element_by_id(id=pm().readConfigByModuleAndKey('india_D90', 'radioPage',
                                                                                'RadioNumber7')).info['text']
        if RadioNumber1 == '531' and RadioNumber2 == '711' and RadioNumber3 == '891' and RadioNumber4 == '1071' and RadioNumber5 == '1251' and RadioNumber6 == '1442' and RadioNumber7 == '1602':
            return True
        else:
            return False

    # 向右滑动Radio All收藏列表
    def swipRightAllPage(self):
        resourceId = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'AllPageList')
        Base.d(resourceId=resourceId).swipe('right', steps=5)

    # 向左滑动Radio Favorite收藏列表
    def swipLeftAllPage(self):
        resourceId = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'AllPageList')
        Base.d(resourceId=resourceId).swipe('left', steps=5)

    def clickChannelByNumberInAllPage(self, Num):
        """
        根据传入序号点击电台()
        :param Num: 传入电台序号(1~10)，实际下标（0-9）
        :return: True点击成功， False点击失败
        """
        resourceId = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'AllPageList')
        element = pm().find_element_by_id(id=resourceId)
        elements = element.child(className='android.widget.RelativeLayout')
        return pm().click_by_element(element=elements[int(Num) - 1])

    # 向右滑动Radio Favorite收藏列表
    def swipRightFavorite(self):
        className = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'FavPageList')
        logger.info(className)
        Base.d(className=className).swipe('right', steps=5)

    # 向左滑动Radio Favorite收藏列表
    def swipLeftFavorite(self):
        className = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'FavPageList')
        Base.d(className=className).swipe('left', steps=5)

    # 向左滑到Radio Favorite收藏列表最左侧
    def swipeToTheEndOfLeftFavorite(self):
        # 获取当前收藏页面第一个频道
        className = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'recyclerViewAll')
        classNameChildren = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'recyclerViewAllChildren')
        classNameChildrenText = pm().readConfigByModuleAndKey('india_D90', 'radioPage',
                                                              'recyclerViewAllChildrenTextView')
        nameStr = Base.d(className=className).child(
            className=classNameChildren).child(className=classNameChildrenText).get_text()
        logger.info("Current Channel ：" + nameStr)
        while True:
            self.swipRightFavorite()
            nameAfterSwip = Base.d(className=className).child(
                className=classNameChildren).child(className=classNameChildrenText).get_text()
            logger.info(nameAfterSwip)
            if nameAfterSwip != nameStr:  # 比较频道，如果不同后者赋值前者继续进行滑动比较
                logger.info("Channle Before Swip ：" + nameStr)
                logger.info("Channle After Swip ：" + nameAfterSwip)
                nameStr = nameAfterSwip
            else:
                logger.info("Channle Before Swip：" + nameStr)
                logger.info("Channle After Swip：" + nameAfterSwip)
                logger.info("Already to the end of Left")
                break

    # 向左滑动确认是否是Favorite最后一页
    def comfirmIsTheEndOfRightFavoritePage(self):
        # 获取当前收藏页面第一个频道
        className = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'recyclerViewAll')
        classNameChildren = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'recyclerViewAllChildren')
        classNameChildrenText = pm().readConfigByModuleAndKey('india_D90', 'radioPage',
                                                              'recyclerViewAllChildrenTextView')
        nameStr = Base.d(className=className).child(
            className=classNameChildren).child(className=classNameChildrenText).get_text()
        logger.info("Current Channel ：" + nameStr)
        self.swipLeftFavorite()
        nameAfterSwip = Base.d(className=className).child(
            className=classNameChildren).child(className=classNameChildrenText).get_text()
        logger.info(nameAfterSwip)
        if nameAfterSwip != nameStr:  # 比较频道，如果不同后者赋值前者继续进行滑动比较
            logger.info("Channle Before Swip ：" + nameStr)
            logger.info("Channle After Swip ：" + nameAfterSwip)
            return False
        else:
            logger.info("Channle Before Swip：" + nameStr)
            logger.info("Channle After Swip：" + nameAfterSwip)
            logger.info("Already to the end of Right")
            return True

    def compareRadioChannelIsExist(self, channel):
        """
        比较收音机电台是否在Favorite列表中
        :param channel: 传入channel调频 如FM 97.2
        :return: True匹配成功，False匹配失败
        """
        logger.info('channel : ' + channel)
        channelNumid = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'FavPageChannelNum')
        element = pm().find_element_by_idAndText(id=channelNumid, text=channel)
        logger.info(element.exists())
        return element.exists()

    # 滑动查找指定调频是否在收藏列表中已经保存成功
    def isExistsInFavoriteListByChannel(self, channel):
        result = False
        self.swipeToTheEndOfLeftFavorite()  # 先滑到最左侧Favorite起点\
        while True:
            flag = self.compareRadioChannelIsExist(channel)  # 比较电台
            if not flag:
                self.comfirmIsTheEndOfRightFavoritePage()  # 左划至下一页并确认不是最后一页
            else:
                result = flag  # 已经找到指定电台并赋返回值True
                break
        return result

    # 根据传入调频+数字查找是否跳转成功，传入AM或FM，数字部分（供语音调用）
    def checkChannelAndNumber(self, channel, number):
        elementChannel = pm().find_element_by_text(channel)
        elementNumber = pm().find_element_by_text(number)
        if elementChannel.exists() and elementNumber.exists():
            return True
        else:
            return False

    # 判断当前页面是否处于Fav收藏页面，Fav页面返回True（判断Favorite页标题下是否有高亮Title）
    def checkCurrentPageIsFavoritePage(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'FavPage')
        element = pm().find_element_by_id(id=id)
        if element is not None:
            return True
        else:
            return False

    # 判断当前页面中是否有已收藏心号（用于判断当前播放调频是否已经被收藏）
    def checkFMAMFavoriteIconIsExist(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'FmAmFavorite')
        element = pm().find_element_by_id(id=id)
        if element is not None:
            return True
        else:
            return False

    # 判断当前页面中是否有已收藏心号（用于判断当前播放调频是否已经被收藏）
    def checkFMAMFavoriteIconIsNotExist(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'FmAmFavorite')
        element = pm().find_element_by_id(id=id)
        if element is None:
            return True
        else:
            return False

    # 判断是否正在播放收音机（用于判断当前播放调频是否正在播放）
    def checkRadioIsPlaying(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'PlayButton')
        element = pm().find_element_by_id(id=id)
        if element is not None:
            return True
        else:
            return False

    # 判断当前是否处于FM页面
    def checkCurrentPageIsFmPage(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'RadioSpinnerText')
        element = pm().find_element_by_id(id=id)
        if element.get_text() == 'FM':
            return True
        else:
            return False

    # 判断当前是否处于AM页面
    def checkCurrentPageIsAmPage(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'RadioSpinnerText')
        element = pm().find_element_by_id(id=id)
        if element.get_text() == 'AM':
            return True
        else:
            return False

    # 判断当前是否处于DRM页面
    def checkCurrentPageIsDrmPage(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'RadioSpinnerText')
        element = pm().find_element_by_id(id=id)
        if element.get_text() == 'DRM':
            return True
        else:
            return False

    def changeToRadioAndSearchFMChannel50times(self):
        """
        压力测试（首页>Radio页面FM自动搜台，50次）
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
            homePage().clickRadio()  # 进入radio
            time.sleep(1)
            radioActivity = pm().get_Current_Activity()
            if radioActivity == 'com.saicmotor.radio.view.CarRadioMainActivity':
                pass
            else:
                logger.info(str(i) + ' Fail ' + radioActivity)
                k = k + 1
            self.changeToFM()  # 切换至FM
            time.sleep(1)
            self.clickSearchRadioWithCheck()  #
        if k == 0:
            return True
        else:
            logger.info('Fail times: ' + str(k))
            return False

    def changeToRadioAndSearchAMChannel50times(self):
        """
        压力测试（首页>Radio页面AM自动搜台，50次）
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
            homePage().clickRadio()  # 进入radio
            time.sleep(1)
            radioActivity = pm().get_Current_Activity()
            if radioActivity == 'com.saicmotor.radio.view.CarRadioMainActivity':
                pass
            else:
                logger.info(str(i) + ' Fail ' + radioActivity)
                k = k + 1
            self.changeToAM()  # 切换至AM
            time.sleep(1)
            self.clickSearchRadioWithCheck()  #
        if k == 0:
            return True
        else:
            logger.info('Fail times: ' + str(k))
            return False

    def changeToRadioCollectFMChannelCancelChannel50times(self):
        """
        压力测试（首页>Radio页面Fm收藏、取消收藏电台，50次）
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
            homePage().clickRadio()  # 进入radio
            time.sleep(1)
            radioActivity = pm().get_Current_Activity()
            if radioActivity == 'com.saicmotor.radio.view.CarRadioMainActivity':
                pass
            else:
                logger.info(str(i) + ' Fail ' + radioActivity)
                k = k + 1
            self.changeToFM()  # 切换至FM
            time.sleep(1)
            self.clickCollectAMFMHeartIcon()  # 收藏
            time.sleep(2)
            self.clickCancelAMFMHeartIcon()  # 取消收藏
            time.sleep(1)
        if k == 0:
            return True
        else:
            logger.info('Fail times: ' + str(k))
            return False

    def changeToRadioCollectAMChannelCancelChannel50times(self):
        """
        压力测试（首页>Radio页面Fm收藏、取消收藏电台，50次）
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
            homePage().clickRadio()  # 进入radio
            time.sleep(1)
            radioActivity = pm().get_Current_Activity()
            if radioActivity == 'com.saicmotor.radio.view.CarRadioMainActivity':
                pass
            else:
                logger.info(str(i) + ' Fail ' + radioActivity)
                k = k + 1
            self.changeToAM()  # 切换至AM
            time.sleep(1)
            self.clickCollectAMFMHeartIcon()  # 收藏
            time.sleep(2)
            self.clickCancelAMFMHeartIcon()  # 取消收藏
            time.sleep(1)
        if k == 0:
            return True
        else:
            logger.info('Fail times: ' + str(k))
            return False


radioPage = india_D90_radioPage()

if __name__ == '__main__':
    # homePage().clickHome()
    pass
