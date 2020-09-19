# -*- coding: utf-8 -*-
# 澳新AS23 Radio页面方法
from UIconfig.Base import Base
from page.PublicMethod import PublicMethod as pm
import time
import UIconfig.logger as loggers

logger = loggers.Logger()


class australia_AS23_radioPage(Base):

    def clickFavouritePage(self):
        """
        打开Favorite调频列表
        :return: True、False
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'radioPage_resourceId', 'FAVOURITE')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickAllPage(self):
        """
        打开ALL调频列表
        :return: True、False
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'radioPage_resourceId', 'All')
        # logger.info('all id: ' + id)
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickSearchRadioWithCheck(self):
        """
        点击搜索电台（带校验是否有搜到电台）
        :return:
        """
        logger.info(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        id = pm().readConfigByModuleAndKey('australia_AS23', 'radioPage_resourceId', 'SearchButton')
        element = pm().find_element_by_id(id=id)
        pm().click_by_element(element=element)
        logger.info(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        cancelId = pm().readConfigByModuleAndKey('australia_AS23', 'radioPage_resourceId', 'CancelSearchButton')
        while True:
            if pm().find_element_by_id(id=cancelId) is not None:
                time.sleep(5)  # 等待搜台
                logger.info("searching")
            else:
                logger.info("Finish Serach ")
                break
        NoFrequency = pm().readConfigByModuleAndKey('australia_AS23', 'radioPage_resourceId', 'NoFrequency')
        if pm()._find_element_by_text(NoFrequency) is None:  # 如果界面有No Frequency显示，说明没有搜到电台
            logger.info("No Frequency")
            return False
        else:
            logger.info("Success to Serach")
            return True

    def clickSearchRadioWithoutCheck(self):
        """
        点击自动搜台（无搜台过程校验）
        :return: True搜台点击成功,False搜台点击失败
        """
        logger.info(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        id = pm().readConfigByModuleAndKey('australia_AS23', 'radioPage_resourceId', 'SearchButton')
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
        radioNumberId = pm().readConfigByModuleAndKey('australia_AS23', 'radioPage_resourceId', 'RadioNumber')
        RadioSpinnerTextId = pm().readConfigByModuleAndKey('australia_AS23', 'radioPage_resourceId', 'RadioSpinnerText')
        channel = pm().find_element_by_id(id=radioNumberId).get_text()
        RadioSpinnerText = pm().find_element_by_id(id=RadioSpinnerTextId).get_text()
        logger.info(RadioSpinnerText + " " + channel)
        return RadioSpinnerText + " " + channel

    def getCurrentChannleNum(self):
        """
        获取当前播放调频电台数值部分
        :return: 如：97.2
        """
        radioNumberId = pm().readConfigByModuleAndKey('australia_AS23', 'radioPage_resourceId', 'RadioNumber')
        channel = pm().find_element_by_id(id=radioNumberId).get_text()
        logger.info(channel)
        return channel

    def checkFMChannelAfterStepAdd(self):
        """
        比较实际电台与预期电台（用于FM步进比较）
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

    def checkFMChannelAfterStepMinus(self):
        """
        比较实际电台与预期电台（用于FM步减比较）
        :return:
        """
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

    def checkAMChannelAfterStepAdd(self):
        """
        比较实际电台与预期电台（用于AM步进值9比较）
        :return: True正确，False错误
        """
        channel1 = float(self.getCurrentChannleNum())
        logger.info(channel1)
        self.clickStepAdd()
        channel2 = float(self.getCurrentChannleNum())
        logger.info(channel2)
        absResult = abs(round(channel1 - channel2, 1))
        logger.info(absResult)
        if absResult == 9:
            return True
        else:
            return False

    def checkAMChannelAfterStepMinus(self):
        """
        # 比较实际电台与预期电台（用于AM步减值9比较）
        :return: True正确，False错误
        """
        channel1 = float(self.getCurrentChannleNum())
        logger.info(channel1)
        self.clickStepMinus()
        channel2 = float(self.getCurrentChannleNum())
        logger.info(channel2)
        absResult = abs(round(channel1 - channel2, 1))
        logger.info(absResult)
        if absResult == 9:
            return True
        else:
            return False

    def clickStepAdd(self):
        """
        点击步进+
        :return: True、False
        """
        stepAddId = pm().readConfigByModuleAndKey('australia_AS23', 'radioPage_resourceId', 'RadioAdd')
        element = pm().find_element_by_id(id=stepAddId)
        logger.info("Click StepAdd")
        return pm().click_by_element(element=element)

    def clickStepMinus(self):
        """
        点击步进-
        :return: True、False
        """
        radioMinusId = pm().readConfigByModuleAndKey('australia_AS23', 'radioPage_resourceId', 'RadioMinus')
        element = pm().find_element_by_id(id=radioMinusId)
        logger.info("Click StepMinus")
        return pm().click_by_element(element=element)

    def clickLastStation(self):
        """
        点击上一个有效电台
        :return: True,False
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'radioPage_resourceId', 'LastChannel')
        cancelId = pm().readConfigByModuleAndKey('australia_AS23', 'radioPage_resourceId', 'CancelSearchButton')
        element = pm().find_element_by_id(id=id)
        logger.info("Click LastStation")
        currentChannel = self.getCurrentChannleNum()  # 获取当前电台调频
        logger.info("currentChannel " + currentChannel)
        pm().click_by_element(element=element)
        while True:
            if pm().find_element_by_id(id=cancelId) is not None:
                time.sleep(3)  # 等待搜台
                logger.info("sleep 3s")
            else:
                channelAfterStep = self.getCurrentChannleNum()  # 点击事件后的电台调频
                logger.info("channelAfterStep " + channelAfterStep)
                break
        if currentChannel == channelAfterStep:  # 电台没有变化
            return False
        else:
            return True

    def clickNextStation(self):
        """
        点击下一个有效电台
        :return: True,False
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'radioPage_resourceId', 'NextChannel')
        cancelId = pm().readConfigByModuleAndKey('australia_AS23', 'radioPage_resourceId', 'CancelSearchButton')
        element = pm().find_element_by_id(id=id)
        logger.info("Click NextStation")
        currentChannel = self.getCurrentChannleNum()  # 获取当前电台调频
        pm().click_by_element(element=element)
        logger.info("currentChannel " + currentChannel)
        while True:
            if pm().find_element_by_id(id=cancelId) is not None:
                time.sleep(3)  # 等待搜台
                logger.info("sleep 3s")
            else:
                channelAfterStep = self.getCurrentChannleNum()  # 点击事件后的电台调频
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
        playId = pm().readConfigByModuleAndKey('australia_AS23', 'radioPage_resourceId', 'PauseButton')
        element = pm().find_element_by_id(id=playId)
        if element is not None:
            return True
        else:
            return False

    def checkRadioStatusIsPausing(self):
        """
        检查Radio是否暂停状态
        :return: True播放中，False暂停中
        """
        pauseId = pm().readConfigByModuleAndKey('australia_AS23', 'radioPage_resourceId', 'PlayButton')
        element = pm().find_element_by_id(id=pauseId)
        if element is not None:
            return True
        else:
            return False

    def clickPauseStation(self):
        """
        点击暂停电台(点击后能查到播放图标表示状态切换成功)
        :return: True,False
        """
        pauseId = pm().readConfigByModuleAndKey('australia_AS23', 'radioPage_resourceId', 'PauseButton')
        element = pm().find_element_by_id(id=pauseId)
        logger.info("Click PauseStation")
        pm().click_by_element(element=element)
        playId = pm().readConfigByModuleAndKey('australia_AS23', 'radioPage_resourceId', 'PlayButton')
        if pm().find_element_by_id(id=playId) is not None:
            logger.info('change status to Pause success')
            return True
        else:
            return False

    def clickPlayStation(self):
        """
        点击播放电台
        :return: True,False
        """
        playId = pm().readConfigByModuleAndKey('australia_AS23', 'radioPage_resourceId', 'PlayButton')
        element = pm().find_element_by_id(id=playId)
        logger.info("Click PlayStation")
        pm().click_by_element(element=element)
        pauseId = pm().readConfigByModuleAndKey('australia_AS23', 'radioPage_resourceId', 'PauseButton')
        if pm().find_element_by_id(id=pauseId) is not None:
            logger.info('change status to Play success')
            return True
        else:
            return False

    def changeRadio(self):
        """
        # 切换AM FM调频
        :return: True, False
        """
        radioSpinner = pm().readConfigByModuleAndKey('australia_AS23', 'radioPage_resourceId', 'RadioSpinner')
        element = pm().find_element_by_id(id=radioSpinner)
        logger.info("Click changeRadio")
        return pm().click_by_element(element=element)

    def changeToFM(self):
        """
        切换FM调频
        :return: True, False
        """
        self.changeRadio()
        FM = pm().readConfigByModuleAndKey('australia_AS23', 'radioPage_resourceId', 'FM')
        element = pm().find_element_by_id(id=FM)
        logger.info("Click changeToFM")
        pm().click_by_element(element=element)
        time.sleep(0.5)
        radioTypeId = pm().readConfigByModuleAndKey('australia_AS23', 'radioPage_resourceId', 'RadioType')
        if pm().find_element_by_id(id=radioTypeId).get_text() == 'MHz':
            logger.info('change status to FM success')
            return True
        else:
            return False

    def changeToAM(self):
        """
        切换AM调频
        :return: True, False
        """
        self.changeRadio()
        AM = pm().readConfigByModuleAndKey('australia_AS23', 'radioPage_resourceId', 'AM')
        element = pm().find_element_by_id(id=AM)
        logger.info("Click changeToAM")
        pm().click_by_element(element=element)
        time.sleep(0.5)
        radioTypeId = pm().readConfigByModuleAndKey('australia_AS23', 'radioPage_resourceId', 'RadioType')
        if pm().find_element_by_id(id=radioTypeId).get_text() == 'KHz':
            logger.info('change status to AM success')
            return True
        else:
            return False

    def clickCollectAMFMHeartIcon(self):
        """
        点击收藏电台
        :return: True、False
        """
        noFavorite = pm().readConfigByModuleAndKey('australia_AS23', 'radioPage_resourceId', 'NoHeartIcon')
        favorite = pm().readConfigByModuleAndKey('australia_AS23', 'radioPage_resourceId', 'HeartIcon')
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

    def clickCancelAMFMHeartIcon(self):
        """
        点击取消收藏电台
        :return: True、False
        """
        noFavorite = pm().readConfigByModuleAndKey('australia_AS23', 'radioPage_resourceId', 'NoHeartIcon')
        favorite = pm().readConfigByModuleAndKey('australia_AS23', 'radioPage_resourceId', 'HeartIcon')
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

    def swipRightAllPage(self):
        """
        向右滑动Radio All收藏列表
        :return: True,False
        """
        resourceId = pm().readConfigByModuleAndKey('australia_AS23', 'radioPage_resourceId', 'AllPageList')
        Base.d(resourceId=id).swipe('right')
        return True

    def swipLeftAllPage(self):
        """
        向左滑动Radio All收藏列表
        :return: True,False
        """
        resourceId = pm().readConfigByModuleAndKey('australia_AS23', 'radioPage_resourceId', 'AllPageList')
        Base.d(resourceId=id).swipe('left')
        return True

    def clickChannelByNumberInAllPage(self, Num):
        """
        根据传入序号点击电台()
        :param Num: 传入电台序号(1~6)，实际下标（0-5）
        :return: True点击成功， False点击失败
        """
        resourceId = pm().readConfigByModuleAndKey('australia_AS23', 'radioPage_resourceId', 'AllPageList')
        element = pm().find_element_by_id(id=resourceId)
        elements = element.child(className='android.widget.RelativeLayout')
        return pm().click_by_element(element=elements[int(Num) - 1])

    def swipRightFavorite(self):
        """
        向右滑动Radio Favorite收藏列表
        :return: True,False
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'radioPage_resourceId', 'FavPageList')
        Base.d(resourceId=id).swipe('right')
        return True

    def swipLeftFavorite(self):
        """
        向左滑动Radio Favorite收藏列表
        :return: True,False
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'radioPage_resourceId', 'FavPageList')
        Base.d(resourceId=id).swipe('left')
        return True

    def swipeToTheEndOfLeftFavorite(self):
        """
        向左滑到Radio Favorite收藏列表最左侧
        :return:
        """
        # 获取当前收藏页面第一个频道
        className = pm().readConfigByModuleAndKey('australia_AS23', 'radioPage_resourceId', 'recyclerViewAll')
        classNameChildren = pm().readConfigByModuleAndKey('australia_AS23', 'radioPage_resourceId',
                                                          'recyclerViewAllChildren')
        classNameChildrenText = pm().readConfigByModuleAndKey('australia_AS23', 'radioPage_resourceId',
                                                              'recyclerViewAllChildrenTextView')
        while True:
            nameStr = Base.d(className=className).child(
                className=classNameChildren).child(className=classNameChildrenText).get_text()
            logger.info("Current Channel ：" + nameStr)
            self.swipRightFavorite()
            nameAfterSwip = Base.d(className=className).child(
                className=classNameChildren).child(className=classNameChildrenText).get_text()
            logger.info(nameAfterSwip)
            if nameAfterSwip != nameStr:  # 比较频道，如果不同后者赋值前者继续进行滑动比较
                logger.info("Channle Before Swip ：" + nameStr)
                logger.info("Channle After Swip ：" + nameAfterSwip)
                nameStr = nameAfterSwip
                continue
            else:
                logger.info("Channle Before Swip：" + nameStr)
                logger.info("Channle After Swip：" + nameAfterSwip)
                logger.info("Already to the end of Left")
                break
        return True

    def comfirmIsTheEndOfRightFavoritePage(self):
        """
        向右滑动确认是否是Favorite最后一页
        :return: True
        """
        # 获取当前收藏页面第一个频道
        className = pm().readConfigByModuleAndKey('australia_AS23', 'radioPage_resourceId', 'recyclerViewAll')
        classNameChildren = pm().readConfigByModuleAndKey('australia_AS23', 'radioPage_resourceId',
                                                          'recyclerViewAllChildren')
        classNameChildrenText = pm().readConfigByModuleAndKey('australia_AS23', 'radioPage_resourceId',
                                                              'recyclerViewAllChildrenTextView')
        while True:
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
            else:
                logger.info("Channle Before Swip：" + nameStr)
                logger.info("Channle After Swip：" + nameAfterSwip)
                logger.info("Already to the end of Right")
                break
        return True

    def compareRadioChannelIsExist(self, channel):
        """
        比较收音机电台是否在Favorite列表中
        :param channel: 传入channel调频 如FM 97.2 MHz AM 1611 KHz
        :return: True匹配成功，False匹配失败
        """
        channelNumid = pm().readConfigByModuleAndKey('australia_AS23', 'radioPage_resourceId', 'FavPageChannelNum')
        element = pm().find_element_by_idAndText(id=channelNumid, text=channel)
        return element.exists()

    def isExistsInFavoriteListByChannel(self, channel):
        """
        滑动查找指定调频是否在收藏列表中已经保存成功
        :param channel: 传入channel调频 如FM 97.2 MHz AM 1611 KHz
        :return: True匹配成功，False匹配失败
        """
        result = False
        self.swipeToTheEndOfLeftFavorite()  # 先滑到最左侧Favorite起点
        while True:
            logger.info('111')
            flag = self.compareRadioChannelIsExist(channel)  # 比较电台
            if not flag:
                self.comfirmIsTheEndOfRightFavoritePage()  # 左划至下一页并确认不是最后一页
            else:
                result = flag  # 已经找到指定电台并赋返回值True
                break
        return result

    def checkChannelAndNumber(self, channel, number):
        """
        根据传入调频+数字查找是否跳转成功，传入AM或FM，数字部分（供语音调用）
        :param channel: AM,FM
        :param number: 数字部分
        :return: True,False
        """
        elementChannel = pm().find_element_by_text(channel)
        elementNumber = pm().find_element_by_text(number)
        if elementChannel.exists() and elementNumber.exists():
            return True
        else:
            return False

    def checkCurrentPageIsFavoritePage(self):
        """
        判断当前页面是否处于Fav收藏页面，Fav页面返回True（判断Favorite页标题下是否有高亮Title）
        :return: True,False
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'radioPage_resourceId', 'FavPage')
        element = pm().find_element_by_id(id=id)
        if element is not None:
            return True
        else:
            return False

    def checkFMAMFavoriteIconIsExist(self):
        """
        判断当前页面中是否有已收藏心号（用于判断当前播放调频是否已经被收藏）
        :return: True,False
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'FmAmFavorite')
        element = pm().find_element_by_id(id=id)
        if element is not None:
            return True
        else:
            return False

    def checkFMAMFavoriteIconIsNotExist(self):
        """
        判断当前页面中是否有已收藏心号（用于判断当前播放调频是否已经被收藏）
        :return: True, False
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'radioPage', 'FmAmFavorite')
        element = pm().find_element_by_id(id=id)
        if element is None:
            return True
        else:
            return False

    def checkCurrentPageIsFmPage(self):
        """
        判断当前是否处于FM页面
        :return:
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'radioPage_resourceId', 'RadioSpinnerText')
        element = pm().find_element_by_id(id=id)
        if element.get_text() == 'FM':
            return True
        else:
            return False

    def checkCurrentPageIsAmPage(self):
        """
        判断当前是否处于AM页面
        :return:
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'radioPage_resourceId', 'RadioSpinnerText')
        element = pm().find_element_by_id(id=id)
        if element.get_text() == 'AM':
            return True
        else:
            return False
