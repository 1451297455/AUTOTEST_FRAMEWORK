# -*- coding: utf-8 -*-
# AS23 音乐页面方法
from UIconfig.Base import Base
from page.PublicMethod import PublicMethod as pm
import os
import time
import UIconfig.logger as loggers

logger = loggers.Logger()


class australia_AS23_mediaPage(Base):

    def clickMySongsPage(self):
        """
        点击进入MySongs标题
        :return: True,False
        """
        Xpath = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId', 'mySongs')
        element = pm().find_element_by_Xpath(Xpath=Xpath)
        return pm().click_by_element(element)

    def clickAllSongsPage(self):
        """
        点击进入AllSongs标题
        :return: True,False
        """
        Xpath = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId', 'allSongs')
        element = pm().find_element_by_Xpath(Xpath=Xpath)
        return pm().click_by_element(element)

    def clickFolderPage(self):
        """
        点击进入Folder标题
        :return: True,False
        """
        Xpath = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId', 'folder')
        element = pm().find_element_by_Xpath(Xpath=Xpath)
        return pm().click_by_element(element)

    def clickFavoritesPage(self):
        """
        点击进入Favorites标题
        :return: True,False
        """
        Xpath = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId', 'favorites')
        element = pm().find_element_by_Xpath(Xpath=Xpath)
        return pm().click_by_element(element)

    def clickRecentsPage(self):
        """
        点击进入Recents标题
        :return: True,False
        """
        Xpath = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId', 'recents')
        element = pm().find_element_by_Xpath(Xpath=Xpath)
        return pm().click_by_element(element)

    def choosePlayList1(self):
        """
        点击播放列表1
        :return: True,False
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId', 'playlist1')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def choosePlayList2(self):
        """
        点击播放列表2
        :return: True,False
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId', 'playlist2')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def choosePlayList3(self):
        """
        点击播放列表3
        :return: True,False
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId', 'playlist3')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def openEditPlayList1NamePage(self):
        """
        修改播放列表1名称
        :return: True,False
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId', 'editPlayList1')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def openEditPlayList2NamePage(self):
        """
        修改播放列表2名称
        :return: True,False
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId', 'editPlayList2')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def openEditPlayList3NamePage(self):
        """
        修改播放列表3名称
        :return: True,False
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId', 'editPlayList3')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickPlayAll(self):
        """
        点击PlayALL按键
        :return: True, False
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId', 'playAll')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickRemoveAll(self):
        """
        点击RemoveALL按键
        :return: True, False
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId', 'removeAll')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickOK(self):
        """
        OK
        :return: True,False
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId', 'mediaOk')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickCancel(self):
        """
        Cancel
        :return: True,False
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId', 'mediaCancel')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def getPlayList1Name(self):
        """
        获取PlayList1名称
        :return: True,False
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId', 'playList1Name')
        element = pm().find_element_by_id(id=id)
        return pm().get_text(element)

    def getPlayList2Name(self):
        """
        获取PlayList2名称
        :return: True,False
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId', 'playList2Name')
        element = pm().find_element_by_id(id=id)
        return pm().get_text(element)

    def getPlayList3Name(self):
        """
        获取PlayList3名称
        :return: True,False
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId', 'playList3Name')
        element = pm().find_element_by_id(id=id)
        return pm().get_text(element)

    def deleteSongBySwipeName(self, name):
        """
        左滑歌曲打开删除模式（只用于滑动删除playList中的歌曲）
        :param name: 歌名、
        :return: True,False
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId', 'songName')
        element = pm().find_element_by_idAndText(id=id, text=name)
        return pm().swipe_left_by_element(element=element)

    def clickDeleteSongButton(self):
        """
        删除歌单列表中的歌曲（用于左滑后点击红色删除按键）
        :return: True, False
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId', 'deleteSongButton')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickPreSong(self):
        """
        点击上一首音乐按键（附带歌曲名称变换校验）
        :return: True, False
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId', 'preButton')
        element = pm().find_element_by_id(id=id)
        songNameBeforeChange = self.getCurrentSongName()
        pm().click_by_element(element=element)
        songNameAfterChange = self.getCurrentSongName()
        if songNameAfterChange == songNameBeforeChange:
            return False
        else:
            return True

    def clickNextSong(self):
        """
        点击下一首音乐按键（附带歌曲名称变换校验）
        :return:
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId', 'nextButton')
        element = pm().find_element_by_id(id=id)
        songNameBeforeChange = self.getCurrentSongName()
        pm().click_by_element(element=element)
        songNameAfterChange = self.getCurrentSongName()
        if songNameAfterChange == songNameBeforeChange:
            return False
        else:
            return True

    def getCurrentSongName(self):
        """
        获取当前播放歌曲名称
        :return: True, False
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId', 'currentSongName')
        element = pm().find_element_by_id(id=id)
        return pm().get_text(element)

    def clickPlayButton(self):
        """
        点击多媒体页面播放/暂停按键（待改进：通过当前状态判断播放暂停）
        :return: True,False
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'homePage_resourceId', 'playButton')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickCurrentSongHeartIcon(self):
        """
        点击收藏按键
        :return: True, False
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'homePage_resourceId', 'FavoriteButton')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def changeCycleMode(self):
        """
        切换播放模式按键
        :return: True, False
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'homePage_resourceId', 'cycleMode')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickMusicSpinner(self):
        """
        选择Source音源切换按键
        :return: True,False
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId', 'SourceName')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def getCurrentSourceName(self):
        """
        获取当前音源名称
        :return: 音源名称
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId', 'SourceName')
        element = pm().find_element_by_id(id=id)
        if element is not None:
            return pm().get_text(element)
        else:
            return None

    def changeToUsb1Music(self):
        """
        选择Usb1音源
        :return: True,False
        """
        if self.getCurrentSourceName() == 'USB1 MUSIC':
            return True
        else:
            self.clickMusicSpinner()
            id = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId', 'SourceItem')
            element = pm().find_element_by_idAndText(id=id, text='USB1 MUSIC')
            return pm().click_by_element(element=element)

    def changeToUsb2Music(self):
        """
        选择Usb2音源
        :return: True,False
        """
        if self.getCurrentSourceName() == 'USB2 MUSIC':
            return True
        else:
            self.clickMusicSpinner()
            id = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId', 'SourceItem')
            element = pm().find_element_by_idAndText(id=id, text='USB2 MUSIC')
            return pm().click_by_element(element=element)

    def changeToBtMusic(self):
        """
        选择BTmusic音源
        :return: True,False
        """
        if self.getCurrentSourceName() == 'BT MUSIC':
            return True
        else:
            self.clickMusicSpinner()
            id = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId', 'SourceItem')
            element = pm().find_element_by_idAndText(id=id, text='BT MUSIC')
            return pm().click_by_element(element=element)

    def changeToOnlineMusic(self):
        """
        选择ONLINE_MUSIC音源
        :return: True,False
        """
        if self.getCurrentSourceName() == 'ONLINE MUSIC':
            return True
        else:
            self.clickMusicSpinner()
            id = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId', 'SourceItem')
            element = pm().find_element_by_idAndText(id=id, text='ONLINE MUSIC')
            return pm().click_by_element(element=element)

    def addSongToPlayList1(self):
        """
        点击收藏至列表1
        :return:
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId', 'addToList1')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def addSongToPlayList2(self):
        """
        点击收藏至列表2
        :return:
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId', 'addToList2')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def addSongToPlayList3(self):
        """
        点击收藏至列表3
        :return:
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId', 'addToList3')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def closePlayList(self):
        """
        点击X关闭添加至收藏列表按键
        :return:
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId', 'close')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def inputTextToPlayList(self, name):
        """
        在输入框中输入值
        :param name: 传入值
        :return: True 传入成功 False传入失败
        """
        enterPathId = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId', 'enterPath')
        enterElement = pm().find_element_by_id(id=enterPathId)
        return pm().inputText(enterElement, name)

    def editPlayList1Name(self, name):
        """
        根据传入名称修改playList1列表名称
        :param name: 名称
        :return: True, False
        """
        self.openEditPlayList1NamePage()
        self.inputTextToPlayList(name=name)
        time.sleep(1)
        pm().back()
        time.sleep(1)
        self.clickOK()
        textId = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId', 'playList1Name')
        try:
            text = pm().find_element_by_id(id=textId).get_text()  # PlayList 名称可以传入空值，此处catch异常
        except:
            return True
        if text in name and len(text) <= 20:  # D90 输出长度校验
            return True
        else:
            return False

    def editPlayList2Name(self, name):
        """
        根据传入名称修改playList2列表名称
        :param name: 名称
        :return: True, False
        """
        self.openEditPlayList2NamePage()
        self.inputTextToPlayList(name=name)
        time.sleep(1)
        pm().back()
        time.sleep(1)
        self.clickOK()
        textId = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId', 'playList2Name')
        try:
            text = pm().find_element_by_id(id=textId).get_text()  # PlayList 名称可以传入空值，此处catch异常
        except:
            return True
        if text in name and len(text) <= 20:  # D90 输出长度校验
            return True
        else:
            return False

    def editPlayList3Name(self, name):
        """
        根据传入名称修改playList3列表名称
        :param name: 名称
        :return: True,False
        """
        self.openEditPlayList3NamePage()
        self.inputTextToPlayList(name=name)
        time.sleep(1)
        pm().back()
        time.sleep(1)
        self.clickOK()
        textId = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId', 'playList3Name')
        try:
            text = pm().find_element_by_id(id=textId).get_text()  # PlayList 名称可以传入空值，此处catch异常
        except:
            return True
        if text in name and len(text) <= 20:  # D90 输出长度校验
            return True
        else:
            return False

    def getTheLastSongNameInListView(self):
        """
        查找歌单中最后一首歌曲名称（用于检测是否歌单已经划至底部）
        :return: True, False
        """
        songNameId = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId', 'songName')
        element = pm().find_element_by_id(id=songNameId)
        return element[len(element) - 1].get_text()

    def checkSongByNameInFavPageIsExist(self, name):
        """
        根据歌名查找歌曲(找到返回True/未找到返回False)
        :param name: 歌曲名称
        :return: True, False
        """
        if name == '':
            return False
        textId = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId', 'songName')
        playListId = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId', 'playList')
        playListElement = pm().find_element_by_id(playListId)
        pm().swipe_to_beginning()
        # 上划至顶部
        while True:
            element = pm().find_element_by_text(text=name)
            # logger.info(element.info())
            if element is not None:
                return True
            else:
                songNameBeforeSwipe = self.getTheLastSongNameInListView()
                pm().swipe_up_by_element(playListElement)
                songNameAfterSwipe = self.getTheLastSongNameInListView()
                if songNameAfterSwipe == songNameBeforeSwipe:  # 当前已划至底部
                    return False
                else:  # 未划至底部继续比较
                    continue

    def clickPlaySongByNameInMySongs(self, name):
        """
        根据歌名查找歌曲并点击该歌曲Play按键（用于MySongs页面）
        :param name: 歌曲名称
        :return: True, False
        """
        if name == '':
            return False
        textId = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId', 'songName')
        playListId = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId', 'playList')
        element = pm().find_element_by_idAndText(id=textId, text=name)  # 根据名称和元素ID定位该歌曲
        playListElement = pm().find_element_by_id(playListId)
        pm().swipe_down_by_element(element=playListElement)  # 上划至顶部
        while True:
            if element.exists:
                elements = pm().find_element_by_id(id=textId)  # 获取符合id的元素集
                for i in range(len(elements)):
                    if elements[i].get_text() == name:
                        index = i + 1  # 下标+1等于该元素定位位置
                        playXpath1 = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId',
                                                                   'mySongPlaySongXpath1')
                        playXpath2 = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId',
                                                                   'mySongPlaySongXpath2')
                        playXpath = playXpath1 + str(index) + playXpath2
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

    def clickFavButtonByNameInMySongs(self, name):
        """
        根据歌名查找歌曲并点击该歌曲收藏按键（用于MySongs页面）
        :param name: 歌曲名称
        :return: True, False
        """
        if name == '':
            return False
        pm().swipe_to_beginning()
        textId = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId', 'songName')
        playListId = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId', 'playList')
        element = pm().find_element_by_idAndText(id=textId, text=name)  # 根据名称和元素ID定位该歌曲
        playListElement = pm().find_element_by_id(playListId)
        while True:
            if element.exists:
                elements = pm().find_element_by_id(id=textId)  # 获取符合id的元素集
                for i in range(len(elements)):
                    if elements[i].get_text() == name:
                        index = i + 1  # 下标+1等于该元素定位位置
                        playXpath1 = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId',
                                                                   'mySongFavIconXpath1')
                        playXpath2 = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId',
                                                                   'mySongFavIconXpath2')
                        playXpath = playXpath1 + str(index) + playXpath2
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
        textId = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId', 'songName')
        playListId = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId', 'playList')
        element = pm().find_element_by_idAndText(id=textId, text=name)  # 根据名称和元素ID定位该歌曲
        playListElement = pm().find_element_by_id(playListId)
        while True:
            if element.exists:
                elements = pm().find_element_by_id(id=textId)  # 获取符合id的元素集
                for i in range(len(elements)):
                    if elements[i].get_text() == name:
                        index = i + 1  # 下标+1等于该元素定位位置
                        playXpath1 = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId',
                                                                   'playSongXpath1')
                        playXpath2 = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId',
                                                                   'playSongXpath2')
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

    def clickFavButtonByName(self, name):
        """
        根据歌名查找歌曲并点击该歌曲收藏按键（除MySongs页面以外）
        :param name: 歌曲
        :return: True, False
        """
        if name == '':
            return False
        pm().swipe_to_beginning()
        textId = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId', 'songName')
        playListId = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId', 'playList')
        element = pm().find_element_by_idAndText(id=textId, text=name)  # 根据名称和元素ID定位该歌曲
        playListElement = pm().find_element_by_id(playListId)
        while True:
            if element.exists:
                elements = pm().find_element_by_id(id=textId)  # 获取符合id的元素集
                for i in range(len(elements)):
                    if elements[i].get_text() == name:
                        index = i + 1  # 下标+1等于该元素定位位置
                        logger.info(str(index))
                        playXpath1 = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId',
                                                                   'favIconXpath1')
                        playXpath2 = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId',
                                                                   'favIconXpath2')
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

    def clickAddToPlayListByName(self, name):
        """
        根据歌名查找歌曲并点击该歌曲打开添加列表（除MySongs页面以外）
        :param name: 歌曲名称
        :return: True,False
        """
        if name == '':
            return False
        pm().swipe_to_beginning()
        textId = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId', 'songName')
        playListId = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId', 'playList')
        element = pm().find_element_by_idAndText(id=textId, text=name)  # 根据名称和元素ID定位该歌曲
        playListElement = pm().find_element_by_id(playListId)
        while True:
            if element.exists:
                elements = pm().find_element_by_id(id=textId)  # 获取符合id的元素集
                for i in range(len(elements)):
                    if elements[i].get_text() == name:
                        index = i + 1  # 下标+1等于该元素定位位置
                        playXpath1 = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId',
                                                                   'addToPlayListXpath1')
                        playXpath2 = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId',
                                                                   'addToPlayListXpath2')
                        playXpath = playXpath1 + str(index) + playXpath2
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

    def checkSongIsPlaying(self):
        """
        校验歌曲是否处于播放状态（根据播放时间判断是否处于播放状态）
        :return: True, False
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId', 'startTime')
        element = pm().find_element_by_id(id=id)
        timeBeforeWait = pm().get_text(element)
        time.sleep(4)
        timeAfterWait = pm().get_text(element)
        if timeBeforeWait != timeAfterWait:
            return True
        else:
            return False

    def checkSongIsPaused(self):
        """
        校验歌曲是否处于暂停状态（根据播放时间判断是否处于暂停状态）
        :return: True, False
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId', 'startTime')
        element = pm().find_element_by_id(id=id)
        timeBeforeWait = pm().get_text(element)
        time.sleep(4)
        timeAfterWait = pm().get_text(element)
        if timeBeforeWait == timeAfterWait:
            return True
        else:
            return False

    def playMusicByKeyCode(self):
        """
        通过KeyEvent控制音乐播放
        """
        shell = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId', 'playMusic')
        os.system(shell)

    def pauseMusicByKeyCode(self):
        """
        通过KeyEvent控制音乐暂停
        """
        shell = pm().readConfigByModuleAndKey('australia_AS23', 'media_resourceId', 'pauseMusic')
        os.system(shell)
