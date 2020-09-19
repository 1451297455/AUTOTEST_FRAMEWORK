# -*- coding: utf-8 -*-
from UIconfig.Base import Base
from page.PublicMethod import PublicMethod as pm
from page.india_D90_homePage import india_D90_homePage as homePage
import logging
import time
import os
import UIconfig.logger as loggers

logger = loggers.Logger()
os.path.abspath('.')


class india_D90_musicPage(Base):
    def __init__(self):
        self.module_logger = logging.getLogger('UITest.musicPage')

    # 点击MySongs页面
    def clickMySongsPage(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'mySongsPage')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    # 点击进入AllSongs页面
    def clickAllSongsPage(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'allSongsPage')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    # 点击进入folder页面
    def clickFolderPage(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'folderPage')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    # 点击进入Favourites页面
    def clickFavPage(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'favPage')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    # 点击进入Recents页面
    def clickRecentsPage(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'recentsPage')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    # 点击选择playList1列表
    def choosePlayList1(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'playList1')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    # 点击选择playList2列表
    def choosePlayList2(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'playList2')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    # 点击选择playList3列表
    def choosePlayList3(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'playList3')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    # 点击修改playList1列表名称页面
    def openEditPlayList1NamePage(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'editPlayList1')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    # 点击修改playList2列表名称页面
    def openEditPlayList2NamePage(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'editPlayList2')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    # 点击修改playList3列表名称页面
    def openEditPlayList3NamePage(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'editPlayList3')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    # 点击PlayALL按键
    def clickPlayAll(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'playAll')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    # 点击RemoveALL按键
    def clickRemoveAll(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'removeAll')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    # 点击OK
    def clickOK(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'ok')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    # 点击Cancel
    def clickCancel(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'cancel')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    # 获取PlayList1名称
    def getPlayList1Name(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'playList1Name')
        element = pm().find_element_by_id(id=id)
        return element.get_text()

    # 获取PlayList2名称
    def getPlayList2Name(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'playList2Name')
        element = pm().find_element_by_id(id=id)
        return element.get_text()

    # 获取PlayList3名称
    def getPlayList3Name(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'playList3Name')
        element = pm().find_element_by_id(id=id)
        return element.get_text()

    # 左滑歌曲打开删除模式（只用于滑动删除playList中的歌曲）
    def deleteSongBySwipeName(self, name):
        id = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'songName')
        element = pm().find_element_by_idAndText(id=id, text=name)
        return pm().swipe_left_by_element(element=element)

    # 删除歌单列表中的歌曲（用于左滑后点击红色删除按键）
    def clickDeleteSongButton(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'deleteSongButton')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    # 点击上一首音乐按键（附带歌曲名称变换校验）
    def clickPreSong(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'preButton')
        element = pm().find_element_by_id(id=id)
        songNameBeforeChange = self.getCurrentSongName()
        pm().click_by_element(element=element)
        songNameAfterChange = self.getCurrentSongName()
        if songNameAfterChange == songNameBeforeChange:
            return False
        else:
            return True

    # 点击下一首音乐按键（附带歌曲名称变换校验）
    def clickNextSong(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'nextButton')
        element = pm().find_element_by_id(id=id)
        songNameBeforeChange = self.getCurrentSongName()
        pm().click_by_element(element=element)
        songNameAfterChange = self.getCurrentSongName()
        if songNameAfterChange == songNameBeforeChange:
            return False
        else:
            return True

    # 获取当前播放歌曲名称
    def getCurrentSongName(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'currentSongName')
        element = pm().find_element_by_id(id=id)
        return element.get_text()

    # 点击播放音乐按键
    def clickPlayButton(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'playButton')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    # 点击收藏按键
    def clickCurrentSongHeartIcon(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'heartIcon')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    # 切换播放模式按键
    def changeCycleMode(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'cycleMode')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    # 点击音乐切换栏
    def clickMusicSpinner(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'musicSpinner')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    # 切换至USB1页面
    def changeToUsb1Music(self):
        self.clickMusicSpinner()
        id = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'usb1')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    # 切换至USB2页面
    def changeToUsb2Music(self):
        self.clickMusicSpinner()
        id = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'usb2')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    # 切换至bt音乐页面
    def changeToBtMusic(self):
        self.clickMusicSpinner()
        id = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'btMusic')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    # 切换至本地音乐页面
    def changeToLocalMusic(self):
        self.clickMusicSpinner()
        id = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'localMusic')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    # 切换至Gaana页面
    def changeToGaana(self):
        self.clickMusicSpinner()
        id = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'gaana')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    # 点击收藏至列表1
    def addSongToPlayList1(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'addToList1')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    # 点击收藏至列表2
    def addSongToPlayList2(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'addToList2')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    # 点击收藏至列表3
    def addSongToPlayList3(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'addToList3')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    # 点击X关闭添加至收藏列表按键
    def closePlayList(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'close')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    # U盘未连接时，话术检测
    def checkUsbMusicStringWithoutUsb(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'notokText')
        element = pm().find_element_by_id(id=id)
        if element.get_text() == 'USB is not connected.':
            return True
        else:
            return False

    def inputTextToPlayList(self, name):
        """
        在输入框中输入值
        :param name: 传入值
        :return: True 传入成功 False传入失败
        """
        enterPathId = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'enterPath')
        enterElement = pm().find_element_by_id(id=enterPathId)
        return pm().inputText(enterElement, name)

    # 根据传入名称修改playList1列表名称
    def editPlayList1Name(self, name):
        editId = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'editPlayList1')
        editElement = pm().find_element_by_id(id=editId)
        pm().click_by_element(element=editElement)  # 打开播放列表名称修改页面
        self.inputTextToPlayList(name=name)
        self.clickOK()
        textId = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'playList1Name')
        try:
            text = pm().find_element_by_id(id=textId).get_text()  # PlayList 名称可以传入空值，此处catch异常
        except:
            return True
        if text in name and len(text) <= 20:  # D90 输出长度校验
            return True
        else:
            return False

    # 根据传入名称修改playList1列表名称
    def editPlayList2Name(self, name):
        editId = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'editPlayList2')
        editElement = pm().find_element_by_id(id=editId)
        pm().click_by_element(element=editElement)  # 打开播放列表名称修改页面
        enterPathId = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'enterPath')
        enterElement = pm().find_element_by_id(id=enterPathId)
        pm().inputText(enterElement, name)
        self.clickOK()
        textId = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'playList2Name')
        try:
            text = pm().find_element_by_id(id=textId).get_text()  # PlayList 名称可以传入空值，此处catch异常
        except:
            return True
        if text in name and len(text) <= 20:  # D90 输出长度校验
            return True
        else:
            return False

    # 根据传入名称修改playList3列表名称
    def editPlayList3Name(self, name):
        editId = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'editPlayList3')
        editElement = pm().find_element_by_id(id=editId)
        pm().click_by_element(element=editElement)  # 打开播放列表名称修改页面
        enterPathId = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'enterPath')
        enterElement = pm().find_element_by_id(id=enterPathId)
        pm().inputText(enterElement, name)
        self.clickOK()
        textId = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'playList3Name')
        try:
            text = pm().find_element_by_id(id=textId).get_text()  # PlayList 名称可以传入空值，此处catch异常
        except:
            return True
        if text in name and len(text) <= 20:  # D90 输出长度校验
            return True
        else:
            return False

    # 查找歌单中最后一首歌曲名称（用于检测是否歌单已经划至底部）
    def getTheLastSongNameInListView(self):
        songNameId = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'songName')
        element = pm().find_element_by_id(id=songNameId)
        lastSongName = element[len(element) - 1].get_text()
        return lastSongName

    # 根据歌名查找歌曲(找到返回True/未找到返回False)
    def checkSongByNameInFavPageIsExist(self, name):
        if name == '':
            return False
        textId = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'songName')
        playListId = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'playList')
        element = pm().find_element_by_idAndText(id=textId, text=name)
        playListElement = pm().find_element_by_id(playListId)
        pm().swipe_down_by_element(element=playListElement)  # 上划至顶部
        while True:
            if element.exists:
                return True
            else:
                songNameBeforeSwipe = self.getTheLastSongNameInListView()
                pm().swipe_up_by_element(playListElement)
                songNameAfterSwipe = self.getTheLastSongNameInListView()
                if songNameAfterSwipe == songNameBeforeSwipe:  # 当前已划至底部
                    return False
                else:  # 未划至底部继续比较
                    continue

    # 根据歌名查找歌曲并点击该歌曲Play按键（用于MySongs页面）
    def clickPlaySongByNameInMySongs(self, name):
        if name == '':
            return False
        textId = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'songName')
        playListId = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'playList')
        element = pm().find_element_by_idAndText(id=textId, text=name)  # 根据名称和元素ID定位该歌曲
        playListElement = pm().find_element_by_id(playListId)
        pm().swipe_down_by_element(element=playListElement)  # 上划至顶部
        while True:
            if element.exists:
                elements = pm().find_element_by_id(id=textId)  # 获取符合id的元素集
                for i in range(len(elements)):
                    if elements[i].get_text() == name:
                        index = i + 1  # 下标+1等于该元素定位位置
                        playXpath1 = pm().readConfigByModuleAndKey('india_D90', 'MusicPage',
                                                                   'mySongPlaySongXpath1')
                        playXpath2 = pm().readConfigByModuleAndKey('india_D90', 'MusicPage',
                                                                   'mySongPlaySongXpath2')
                        playXpath = playXpath1 + str(index) + playXpath2
                        logger.info(playXpath)
                        playElement = pm().find_element_by_Xpath(Xpath=playXpath)
                        return pm().click_by_element(element=playElement)
                        break
                    else:
                        continue
            else:
                songNameBeforeSwipe = self.getTheLastSongNameInListView()
                pm().swipe_up_by_element(playListElement)
                songNameAfterSwipe = self.getTheLastSongNameInListView()
                if songNameAfterSwipe == songNameBeforeSwipe:  # 当前已划至底部
                    return False
                else:  # 未划至底部继续比较
                    continue

    # 根据歌名查找歌曲并点击该歌曲收藏按键（用于MySongs页面）
    def clickFavButtonByNameInMySongs(self, name):
        if name == '':
            return False
        pm().swipe_to_beginning()
        textId = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'songName')
        playListId = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'playList')
        element = pm().find_element_by_idAndText(id=textId, text=name)  # 根据名称和元素ID定位该歌曲
        playListElement = pm().find_element_by_id(playListId)
        while True:
            if element.exists:
                logger.info('1111')
                elements = pm().find_element_by_id(id=textId)  # 获取符合id的元素集
                for i in range(len(elements)):
                    if elements[i].get_text() == name:
                        index = i + 1  # 下标+1等于该元素定位位置
                        logger.info(str(index))
                        playXpath1 = pm().readConfigByModuleAndKey('india_D90', 'MusicPage',
                                                                   'mySongFavIconXpath1')
                        playXpath2 = pm().readConfigByModuleAndKey('india_D90', 'MusicPage',
                                                                   'mySongFavIconXpath2')
                        playXpath = playXpath1 + str(index) + playXpath2
                        logger.info(playXpath)
                        playElement = pm().find_element_by_Xpath(Xpath=playXpath)
                        return pm().click_by_element(element=playElement)
                        break
                    else:
                        continue
            else:
                songNameBeforeSwipe = self.getTheLastSongNameInListView()
                pm().swipe_up_by_element(playListElement)
                songNameAfterSwipe = self.getTheLastSongNameInListView()
                if songNameAfterSwipe == songNameBeforeSwipe:  # 当前已划至底部
                    return False
                else:  # 未划至底部继续比较
                    continue

    # 根据歌名查找歌曲并点击该歌曲Play按键（除MySongs页面以外）
    def clickPlaySongByName(self, name):
        if name == '':
            return False
        pm().swipe_to_beginning()
        textId = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'songName')
        playListId = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'playList')
        element = pm().find_element_by_idAndText(id=textId, text=name)  # 根据名称和元素ID定位该歌曲
        playListElement = pm().find_element_by_id(playListId)
        while True:
            if element.exists:
                elements = pm().find_element_by_id(id=textId)  # 获取符合id的元素集
                for i in range(len(elements)):
                    if elements[i].get_text() == name:
                        index = i + 1  # 下标+1等于该元素定位位置
                        playXpath1 = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'playSongXpath1')
                        playXpath2 = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'playSongXpath2')
                        playXpath = playXpath1 + str(index) + playXpath2
                        playElement = pm().find_element_by_Xpath(Xpath=playXpath)
                        return pm().click_by_element(element=playElement)
                    else:
                        continue
            else:
                songNameBeforeSwipe = self.getTheLastSongNameInListView()
                pm().swipe_up_by_element(playListElement)
                songNameAfterSwipe = self.getTheLastSongNameInListView()
                if songNameAfterSwipe == songNameBeforeSwipe:  # 当前已划至底部
                    return False
                else:  # 未划至底部继续比较
                    continue

    # 根据歌名查找歌曲并点击该歌曲收藏按键（除MySongs页面以外）
    def clickFavButtonByName(self, name):
        if name == '':
            return False
        pm().swipe_to_beginning()
        textId = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'songName')
        playListId = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'playList')
        element = pm().find_element_by_idAndText(id=textId, text=name)  # 根据名称和元素ID定位该歌曲
        playListElement = pm().find_element_by_id(playListId)
        while True:
            if element.exists:
                elements = pm().find_element_by_id(id=textId)  # 获取符合id的元素集
                for i in range(len(elements)):
                    if elements[i].get_text() == name:
                        index = i + 1  # 下标+1等于该元素定位位置
                        self.module_logger.info(str(index))
                        playXpath1 = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'favIconXpath1')
                        playXpath2 = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'favIconXpath2')
                        playXpath = playXpath1 + str(index) + playXpath2
                        self.module_logger.info(playXpath)
                        playElement = pm().find_element_by_Xpath(Xpath=playXpath)
                        return pm().click_by_element(element=playElement)
                    else:
                        continue
            else:
                songNameBeforeSwipe = self.getTheLastSongNameInListView()
                pm().swipe_up_by_element(playListElement)
                songNameAfterSwipe = self.getTheLastSongNameInListView()
                if songNameAfterSwipe == songNameBeforeSwipe:  # 当前已划至底部
                    return False
                else:  # 未划至底部继续比较
                    continue

    def clickAddToPlayListByName(self, name):
        """
        根据歌名查找歌曲并点击该歌曲打开添加列表（除MySongs页面以外）
        :param name: 歌曲名称
        :return: True,False
        """
        if name == '':
            return False
        pm().swipe_to_beginning()
        textId = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'songName')
        playListId = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'playList')
        element = pm().find_element_by_idAndText(id=textId, text=name)  # 根据名称和元素ID定位该歌曲
        if element is None:
            return False
        playListElement = pm().find_element_by_id(playListId)
        while True:
            if element.exists:
                elements = pm().find_element_by_id(id=textId)  # 获取符合id的元素集
                if elements is None:
                    return False
                for i in range(len(elements)):
                    if elements[i].get_text() == name:
                        index = i + 1  # 下标+1等于该元素定位位置
                        # logger.info(str(index))
                        playXpath1 = pm().readConfigByModuleAndKey('india_D90', 'MusicPage',
                                                                   'addToPlayListXpath1')
                        playXpath2 = pm().readConfigByModuleAndKey('india_D90', 'MusicPage',
                                                                   'addToPlayListXpath2')
                        playXpath = playXpath1 + str(index) + playXpath2
                        # logger.info(playXpath)
                        playElement = pm().find_element_by_Xpath(Xpath=playXpath)
                        return pm().click_by_element(element=playElement)
                    else:
                        continue
            else:
                songNameBeforeSwipe = self.getTheLastSongNameInListView()
                pm().swipe_up_by_element(playListElement)
                songNameAfterSwipe = self.getTheLastSongNameInListView()
                if songNameAfterSwipe == songNameBeforeSwipe:  # 当前已划至底部
                    return False
                else:  # 未划至底部继续比较
                    continue

    # 校验歌曲是否处于播放状态（根据播放时间判断是否处于播放状态）
    def checkSongIsPlaying(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'startTime')
        element = pm().find_element_by_id(id=id)
        timeBeforeWait = element.get_text()
        time.sleep(4)
        timeAfterWait = element.get_text()
        if timeBeforeWait != timeAfterWait:
            return True
        else:
            return False

    # 校验歌曲是否处于暂停状态（根据播放时间判断是否处于暂停状态）
    def checkSongIsPaused(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'MusicPage', 'startTime')
        element = pm().find_element_by_id(id=id)
        timeBeforeWait = element.get_text()
        time.sleep(4)
        timeAfterWait = element.get_text()
        if timeBeforeWait == timeAfterWait:
            return True
        else:
            return False

    def changeToMusicPageNextSong50Times(self):
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
                self.module_logger.info(str(i) + ' Fail ' + homeActivity)
                k = k + 1
            homePage().clickDockBarMusic()  # 点击dock栏Music按键页面
            time.sleep(1)
            musicPageActivity = pm().get_Current_Activity()
            if musicPageActivity == 'com.saicmotor.media.ui.ActivityMain':
                pass
            else:
                self.module_logger.info(str(i) + ' Fail ' + musicPageActivity)
                k = k + 1
            time.sleep(1)
            self.changeToUsb2Music()  # 切换至Usb2音源
            time.sleep(30)  # 等待30秒
            self.clickNextSong()  # 下一曲
            self.clickPlayButton()  # 点击暂停
        if k == 0:
            return True
        else:
            self.module_logger.info('Fail times: ' + str(k))
            return False

    def changeToMusicPagePreSong50Times(self):
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
                self.module_logger.info(str(i) + ' Fail ' + homeActivity)
                k = k + 1
            homePage().clickDockBarMusic()  # 点击dock栏Music按键页面
            time.sleep(1)
            musicPageActivity = pm().get_Current_Activity()
            if musicPageActivity == 'com.saicmotor.media.ui.ActivityMain':
                pass
            else:
                self.module_logger.info(str(i) + ' Fail ' + musicPageActivity)
                k = k + 1
            time.sleep(1)
            self.changeToUsb2Music()  # 切换至Usb2音源
            time.sleep(30)  # 等待30秒
            self.clickPreSong()  # 下一曲
            self.clickPlayButton()  # 点击暂停
        if k == 0:
            return True
        else:
            self.module_logger.info('Fail times: ' + str(k))
            return False

    def changeToMusicPageCollectSong50Times(self):
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
                self.module_logger.info(str(i) + ' Fail ' + homeActivity)
                k = k + 1
            homePage().clickDockBarMusic()  # 点击dock栏Music按键页面
            time.sleep(1)
            musicPageActivity = pm().get_Current_Activity()
            if musicPageActivity == 'com.saicmotor.media.ui.ActivityMain':
                pass
            else:
                self.module_logger.info(str(i) + ' Fail ' + musicPageActivity)
                k = k + 1
            time.sleep(1)
            self.changeToUsb2Music()  # 切换至Usb2音源
            time.sleep(1)
            self.clickCurrentSongHeartIcon()  # 点击收藏按键
            time.sleep(1)
            self.clickCurrentSongHeartIcon()  # 点击取消收藏
            self.clickPlayButton()  # 点击暂停
        if k == 0:
            return True
        else:
            self.module_logger.info('Fail times: ' + str(k))
            return False

    def changeToMusicPageAddToPlaylist1_50Times(self):
        """
        压力测试（首页>music页面>usb2 music>添加歌曲至playlist1>删除playlist1歌曲50次）
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
                self.module_logger.info(str(i) + ' Fail ' + homeActivity)
                k = k + 1
            homePage().clickDockBarMusic()  # 点击dock栏Music按键页面
            time.sleep(1)
            musicPageActivity = pm().get_Current_Activity()
            if musicPageActivity == 'com.saicmotor.media.ui.ActivityMain':
                pass
            else:
                self.module_logger.info(str(i) + ' Fail ' + musicPageActivity)
                k = k + 1
            time.sleep(1)
            self.changeToUsb2Music()  # 切换至Usb2音源
            time.sleep(1)
            self.clickAllSongsPage()  # 点击收藏按键
            time.sleep(1)
            self.clickAddToPlayListByName('1')  # 点击添加歌曲1至playlist1
            self.addSongToPlayList1()
            time.sleep(1)
            self.clickMySongsPage()
            self.choosePlayList1()
            time.sleep(1)
            self.clickRemoveAll()
            time.sleep(3)
            self.clickOK()
            self.clickPlayButton()
            time.sleep(1)
        if k == 0:
            return True
        else:
            self.module_logger.info('Fail times: ' + str(k))
            return False

    def changeToMusicPageAddToPlaylist2_50Times(self):
        """
        压力测试（首页>music页面>usb2 music>添加歌曲至playlist2>删除playlist2歌曲50次）
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
                self.module_logger.info(str(i) + ' Fail ' + homeActivity)
                k = k + 1
            homePage().clickDockBarMusic()  # 点击dock栏Music按键页面
            time.sleep(1)
            musicPageActivity = pm().get_Current_Activity()
            if musicPageActivity == 'com.saicmotor.media.ui.ActivityMain':
                pass
            else:
                self.module_logger.info(str(i) + ' Fail ' + musicPageActivity)
                k = k + 1
            time.sleep(1)
            self.changeToUsb2Music()  # 切换至Usb2音源
            time.sleep(1)
            self.clickAllSongsPage()  # 点击收藏按键
            time.sleep(1)
            self.clickAddToPlayListByName('1')  # 点击添加歌曲1至playlist2
            self.addSongToPlayList2()
            time.sleep(1)
            self.clickMySongsPage()
            self.choosePlayList2()
            time.sleep(1)
            self.clickRemoveAll()
            time.sleep(3)
            self.clickOK()
            self.clickPlayButton()
            time.sleep(1)
        if k == 0:
            return True
        else:
            self.module_logger.info('Fail times: ' + str(k))
            return False

    def changeToMusicPageAddToPlaylist3_50Times(self):
        """
        压力测试（首页>music页面>usb2 music>添加歌曲至playlist3>删除playlist3歌曲50次）
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
                self.module_logger.info(str(i) + ' Fail ' + homeActivity)
                k = k + 1
            homePage().clickDockBarMusic()  # 点击dock栏Music按键页面
            time.sleep(1)
            musicPageActivity = pm().get_Current_Activity()
            if musicPageActivity == 'com.saicmotor.media.ui.ActivityMain':
                pass
            else:
                self.module_logger.info(str(i) + ' Fail ' + musicPageActivity)
                k = k + 1
            time.sleep(1)
            self.changeToUsb2Music()  # 切换至Usb2音源
            time.sleep(1)
            self.clickAllSongsPage()  # 点击收藏按键
            time.sleep(1)
            self.clickAddToPlayListByName('1')  # 点击添加歌曲1至playlist2
            self.addSongToPlayList3()
            time.sleep(1)
            self.clickMySongsPage()
            self.choosePlayList3()
            time.sleep(1)
            self.clickRemoveAll()
            time.sleep(3)
            self.clickOK()
            self.clickPlayButton()
            time.sleep(1)
        if k == 0:
            return True
        else:
            self.module_logger.info('Fail times: ' + str(k))
            return False

    def changeToBTMusicPageNextMusic50Times(self):
        """
        压力测试（首页>music页面>BT music>下一首歌曲（蓝牙已连接）。50次）
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
                self.module_logger.info(str(i) + ' Fail ' + homeActivity)
                k = k + 1
            homePage().clickDockBarMusic()  # 点击dock栏Music按键页面
            time.sleep(1)
            musicPageActivity = pm().get_Current_Activity()
            if musicPageActivity == 'com.saicmotor.media.ui.ActivityMain':
                pass
            else:
                self.module_logger.info(str(i) + ' Fail ' + musicPageActivity)
                k = k + 1
            time.sleep(1)
            self.changeToBtMusic()
            time.sleep(1)
            self.clickNextSong()
            time.sleep(1)
            self.clickPlayButton()  # 点击暂停

        if k == 0:
            return True
        else:
            self.module_logger.info('Fail times: ' + str(k))
            return False

    def changeToBTMusicPagePreMusic50Times(self):
        """
        压力测试（首页>music页面>BT music>上一首歌曲（蓝牙已连接）。50次）
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
                self.module_logger.info(str(i) + ' Fail ' + homeActivity)
                k = k + 1
            homePage().clickDockBarMusic()  # 点击dock栏Music按键页面
            time.sleep(1)
            musicPageActivity = pm().get_Current_Activity()
            if musicPageActivity == 'com.saicmotor.media.ui.ActivityMain':
                pass
            else:
                self.module_logger.info(str(i) + ' Fail ' + musicPageActivity)
                k = k + 1
            time.sleep(1)
            self.changeToBtMusic()
            time.sleep(1)
            self.clickPreSong()
            time.sleep(1)
            self.clickPlayButton()  # 点击暂停

        if k == 0:
            return True
        else:
            self.module_logger.info('Fail times: ' + str(k))
            return False


musicPage = india_D90_musicPage()
