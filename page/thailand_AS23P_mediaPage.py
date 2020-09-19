# -*- coding: utf-8 -*-
# AS23P 音乐页面方法
from UIconfig.Base import Base
from page.PublicMethod import PublicMethod as pm
import os
import logging
import UIconfig.logger as loggers

logger = loggers.Logger()


class thailand_AS23P_mediaPage(Base):

    # 点击进入MySongs标题
    def clickMySongsItems(self):
        Xpath = pm().readConfigByModuleAndKey('thailand_AS23P', 'media_resourceId', 'mySongs')
        element = pm().find_element_by_Xpath(Xpath=Xpath)
        return pm().click_by_element(element)

    # 点击进入AllSongs标题
    def clickAllSongsItems(self):
        Xpath = pm().readConfigByModuleAndKey('thailand_AS23P', 'media_resourceId', 'allSongs')
        element = pm().find_element_by_Xpath(Xpath=Xpath)
        return pm().click_by_element(element)

    # 点击进入Folder标题
    def clickFolderItems(self):
        Xpath = pm().readConfigByModuleAndKey('thailand_AS23P', 'media_resourceId', 'folder')
        element = pm().find_element_by_Xpath(Xpath=Xpath)
        return pm().click_by_element(element)

    # 点击进入Favorites标题
    def clickFavoritesItems(self):
        Xpath = pm().readConfigByModuleAndKey('thailand_AS23P', 'media_resourceId', 'favorites')
        element = pm().find_element_by_Xpath(Xpath=Xpath)
        return pm().click_by_element(element)

    # 点击进入Recents标题
    def clickRecentsItems(self):
        Xpath = pm().readConfigByModuleAndKey('thailand_AS23P', 'media_resourceId', 'recents')
        element = pm().find_element_by_Xpath(Xpath=Xpath)
        return pm().click_by_element(element)

    # 点击多媒体页面下一首按键
    def clickNextSongButton(self):
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'homePage_resourceId', 'nextSongButton')
        element = pm().find_element_by_text(name)
        return pm().click_by_element(element=element)

    # 点击多媒体页面上一首按键
    def clickPrevSongButton(self):
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'homePage_resourceId', 'prevSongButton')
        element = pm().find_element_by_text(name)
        return pm().click_by_element(element=element)

    # 点击多媒体页面播放/暂停按键（待改进：通过当前状态判断播放暂停）
    def clickPlayButton(self):
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'homePage_resourceId', 'playButton')
        element = pm().find_element_by_text(name)
        return pm().click_by_element(element=element)

    # 通过KeyEvent控制音乐播放
    def playMusicByKeyCode(self):
        shell = pm().readConfigByModuleAndKey('thailand_AS23P', 'media_resourceId', 'playMusic')
        # logger.info('shell: ' + shell)
        os.system(shell)

    # 通过KeyEvent控制音乐暂停
    def pauseMusicByKeyCode(self):
        shell = pm().readConfigByModuleAndKey('thailand_AS23P', 'media_resourceId', 'pauseMusic')
        # logger.info('shell: ' + shell)
        os.system(shell)

    # 选择popList音源
    def openPOPList(self):
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'media_resourceId', 'POPLIST')
        element = pm().find_element_by_id(name)
        return pm().click_by_element(element=element)

    # 选择Usb1音源
    def changeToUSB1Music(self):
        Xpath = pm().readConfigByModuleAndKey('thailand_AS23P', 'media_resourceId', 'USB1MUSIC_POPWINDOW')
        element = pm().find_element_by_Xpath(Xpath=Xpath)
        return pm().click_by_element(element=element)

    # 选择Usb2音源
    def changeToUSB2Music(self):
        Xpath = pm().readConfigByModuleAndKey('thailand_AS23P', 'media_resourceId', 'USB2MUSIC_POPWINDOW')
        element = pm().find_element_by_Xpath(Xpath=Xpath)
        return pm().click_by_element(element=element)

    # 选择BTmusic音源
    def changeToBTMusic(self):
        Xpath = pm().readConfigByModuleAndKey('thailand_AS23P', 'media_resourceId', 'BTMUSIC_POPWINDOW')
        element = pm().find_element_by_Xpath(Xpath=Xpath)
        return pm().click_by_element(element=element)

    # 选择ONLINE_MUSIC音源
    def changeToOnlineMusic(self):
        Xpath = pm().readConfigByModuleAndKey('thailand_AS23P', 'media_resourceId', 'ONLINE_MUSIC_POPWINDOW')
        element = pm().find_element_by_Xpath(Xpath=Xpath)
        return pm().click_by_element(element=element)

    # 修改播放列表1名称
    def editPlaylist1(self):
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'media_resourceId', 'playListEdit1')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    # 修改播放列表2名称
    def editPlaylist2(self):
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'media_resourceId', 'playListEdit2')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    # 修改播放列表3名称
    def editPlaylist3(self):
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'media_resourceId', 'playListEdit3')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    # Cancel
    def mediaCancel(self):
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'media_resourceId', 'mediaCancel')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    # OK
    def mediaOk(self):
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'media_resourceId', 'mediaOk')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    # 点击播放列表1
    def openPlaylist1(self):
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'media_resourceId', 'playlist1')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    # 点击播放列表2
    def openPlaylist2(self):
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'media_resourceId', 'playlist2')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    # 点击播放列表3
    def openPlaylist3(self):
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'media_resourceId', 'playlist3')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    # Favorites页面播放状态(根据歌曲名称点击该歌曲播放状态按键)
    def changeSongStatusInFavoritesPageByText(self, text):
        Xpath = pm().readConfigByModuleAndKey('thailand_AS23P', 'media_resourceId', 'favoritesPagePlayButton')
        Xpath = Xpath.replace("tempString", text)
        # logger.info(id)
        element = pm().find_element_by_Xpath(Xpath=Xpath)
        return pm().click_by_element(element=element)

    # Favorites页面添加歌曲按键(根据歌曲名称点击该歌曲添加按键)
    def cancelFavoriteSongInFavoritesPageByText(self, text):
        Xpath = pm().readConfigByModuleAndKey('thailand_AS23P', 'media_resourceId', 'favoritesPageCollectionButton')
        Xpath = Xpath.replace("tempString", text)
        # logger.info(id)
        element = pm().find_element_by_Xpath(Xpath=Xpath)
        return pm().click_by_element(element=element)

    # Favorites页面添加歌曲按键(根据歌曲名称点击该歌曲添加按键)
    def addSongToFavoriteListInFavoritesPageByText(self, text):
        Xpath = pm().readConfigByModuleAndKey('thailand_AS23P', 'media_resourceId', 'favoritesPageAddButton')
        Xpath = Xpath.replace("tempString", text)
        # logger.info(id)
        element = pm().find_element_by_Xpath(Xpath=Xpath)
        return pm().click_by_element(element=element)

    # Favorites页面close按键
    def clickClose(self):
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'media_resourceId', 'close')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    # 获取第一个list中的歌曲名称
    def getFirstSongNameInMediaList(self):
        firstTextXpath = pm().readConfigByModuleAndKey('thailand_AS23P', 'media_resourceId',
                                                       'firstItems')  # 获取list中第一个Items名称的Xpath
        # #logger.info('==' + firstTextXpath)
        try:
            element = pm().find_element_by_Xpath(Xpath=firstTextXpath)  # 根据Xpath获取第一个元素
            songName = element.get_text()
        except Exception as e:
            logging.info(e)
            return None
        return songName  # 根据元素获取该元素名称

    # 在mediaList中滑到最上方(仅限用于media中的listview)
    def swipMediaListToBeginning(self):
        firstSongName = self.getFirstSongNameInMediaList()  # 滑动前获取一次首行歌曲名称
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'media_resourceId', 'ListView')
        element = pm().find_element_by_id(id=id)
        pm().swipe_down_by_element(element=element)  # 滑动一次
        songName = self.getFirstSongNameInMediaList()  # 获取名称
        while firstSongName != songName or firstSongName is None or songName is None:  # 比较两次滑动名称
            # logger.info('swipe')
            firstSongName = songName  # 交替赋值
            pm().swipe_down_by_element(element=element)
            songName = self.getFirstSongNameInMediaList()
        else:
            # logger.info('==' + str(firstSongName))
            # logger.info('==' + str(songName))
            return True
