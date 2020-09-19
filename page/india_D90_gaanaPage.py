# -*- coding: utf-8 -*-
from UIconfig.Base import Base
from page.PublicMethod import PublicMethod as pm
import time
import os
import UIconfig.logger as loggers

logger = loggers.Logger()
os.path.abspath('.')


class india_D90_gaanaPage(Base):

    def clickGaanaHome(self):
        """
        点击进入gaana Home列表
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaHome')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickGaanaSearch(self):
        """
        点击进入gaana Search列表
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaSearch')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickGaanaRadio(self):
        """
        点击进入gaana Radio列表
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaRadio')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickGaanaMyMusic(self):
        """
        点击进入gaana MyMusic列表
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaMyMusic')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def openGaanaCategories(self):
        """
        打开Gaana Categories页面（带校验）
        :return: True打开成功，False打开失败
        """
        playlistId = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaMyMusicMenuPlaylists')
        playlistElement = pm().find_element_by_id(id=playlistId)
        if playlistElement is not None:  # playlist列表存在表示该页面已经打开
            return True
        else:
            categoriesId = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaCategories')
            categoriesElement = pm().find_element_by_id(id=categoriesId)
            return pm().click_by_element(element=categoriesElement)

    def clickEnterGaanaPlaylist(self):
        """
        点击进入gaana MyMusic列表Playlist栏
        :return: True点击成功，False点击失败
        """
        playlistId = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaMyMusicMenuPlaylists')
        playlistElement = pm().find_element_by_id(id=playlistId)
        return pm().click_by_element(element=playlistElement)

    def clickDownloadInMyMusicPage(self):
        """
        点击Gaana MyMusic页面中的Download图标
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaMyMusicPageDownload')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickFavoritesInMyMusicPage(self):
        """
        点击Gaana MyMusic页面中的Favorites图标
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaMyMusicPageFav')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def chooseSONGSItemInFavorites(self):
        """
        点击Gaana MyMusic页面中的Favorites中的Songs栏
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaFavoriteItems')
        element = pm().find_element_by_idAndText(id=id, text='SONGS')
        return pm().click_by_element(element=element)

    def chooseALBUMSItemInFavorites(self):
        """
        点击Gaana MyMusic页面中的Favorites中的ALBUMS栏
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaFavoriteItems')
        element = pm().find_element_by_idAndText(id=id, text='ALBUMS')
        return pm().click_by_element(element=element)

    def choosePLAYLISTSItemInFavorites(self):
        """
        点击Gaana MyMusic页面中的Favorites中的PLAYLISTS栏
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaFavoriteItems')
        element = pm().find_element_by_idAndText(id=id, text='PLAYLISTS')
        return pm().click_by_element(element=element)

    def chooseRADIOSItemInFavorites(self):
        """
        点击Gaana MyMusic页面中的Favorites中的RADIOS栏
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaFavoriteItems')
        element = pm().find_element_by_idAndText(id=id, text='RADIOS')
        return pm().click_by_element(element=element)

    def chooseARTISTSItemInFavorites(self):
        """
        点击Gaana MyMusic页面中的Favorites中的ARTISTS栏
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaFavoriteItems')
        element = pm().find_element_by_idAndText(id=id, text='ARTISTS')
        return pm().click_by_element(element=element)

    def chooseOCCASIONSItemInFavorites(self):
        """
        点击Gaana MyMusic页面中的Favorites中的OCCASIONS栏
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaFavoriteItems')
        element = pm().find_element_by_idAndText(id=id, text='OCCASIONS')
        return pm().click_by_element(element=element)

    def chooseALLItemInPlaylists(self):
        """
        点击playlists中的ALL列表
        :return:
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaFavoriteItems')
        element = pm().find_element_by_idAndText(id=id, text='ALL')
        return pm().click_by_element(element=element)

    def chooseBYMEItemInPlaylists(self):
        """
        点击playlists中的BY ME列表
        :return:
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaFavoriteItems')
        element = pm().find_element_by_idAndText(id=id, text='BY ME')
        return pm().click_by_element(element=element)

    def chooseFAVORITESItemInPlaylists(self):
        """
        点击playlists中的FAVORITES列表
        :return:
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaFavoriteItems')
        element = pm().find_element_by_idAndText(id=id, text='FAVORITES')
        return pm().click_by_element(element=element)

    def chooseDOWNLOADSItemInPlaylists(self):
        """
        点击playlists中的DOWNLOADS列表
        :return:
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaFavoriteItems')
        element = pm().find_element_by_idAndText(id=id, text='DOWNLOADS')
        return pm().click_by_element(element=element)

    def getMusicTrackElements(self):
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaFavoriteTrackName')
        elements = pm().find_element_by_id(id=id)
        return elements

    def CompareTrackNameWithCurrentMusicName(self):
        """
        比较Favorites列表中歌曲名称与当前歌曲名称
        :return: True收藏成功，False收藏失败
        """
        currentName = self.getCurrentSongName()
        trackNameElements = self.getMusicTrackElements()
        logger.info(len(trackNameElements))
        for i in trackNameElements:
            logger.info(i.get_text())
            if i.get_text() in currentName:
                logger.info(i.get_text())
                return True
                break
        return False

    def clickGaanaSearchButton(self):
        """
        点击进入gaana SearchButton列表
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaSearchButton')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickGaanaSettingButton(self):
        """
        点击进入gaana SettingButton列表
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaSettingButton')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickGaanaLoginUserIcon(self):
        """
        点击进入gaana LoginButton按键跳转登录
        :return: True点击成功，False点击失败
        """
        if self.checkCurrentAlreadyLogin():
            return True
        else:
            self.clickGaanaSettingButton()
            id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaLoginUser')
            element = pm().find_element_by_id(id=id)
            return pm().click_by_element(element=element)

    def getLoginSubscriptionText(self):
        """
        查找gaanaLoginSubscription字段名称
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaLoginSubscription')
        element = pm().find_element_by_id(id=id)
        return element.get_text()

    def checkCurrentAlreadyLogin(self):
        """
        查看是否已登录
        :return: True已登录，False未登录
        """
        self.clickGaanaSettingButton()
        self.clickGaanaLeftMenuSetting()
        result = self.checkLogOutButtonIsExist()
        self.clickBackToLastPage()
        return result

    def clickSkipButton(self):
        """
        点击登录页面中Skip按键跳出登录
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaSkipLogin')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def choosePhoneNumberToLogin(self):
        """
        点击选择PhoneNumber登录方式
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaLoginByPhoneNumber')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def chooseMailToLogin(self):
        """
        点击选择邮箱登录方式
        :return: True登录成功，False登录失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaLoginByMail')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def inputPhoneNumberText(self, text):
        """
        搜索输入框输入文本（输入电话号码）
        :param text: 输入电话号码
        :return: True传入成功，False传入失败
        """
        searchBox = pm().find_element_by_id(id=pm().readConfigByModuleAndKey('india_D90', 'GaanaPage',
                                                                             'gaanaPhoneNumberInputText'))
        return pm().inputText(searchBox, text)

    def clickOTPButton(self):
        """
        点击确认登录（电话号码登录方式）

        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaOTPButton')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def inputEmailText(self, text):
        """
        搜索输入框输入文本（输入邮箱）
        :param text: 输入邮箱地址
        :return: True传入成功，False传入失败
        """
        searchBox = pm().find_element_by_id(id=pm().readConfigByModuleAndKey('india_D90', 'GaanaPage',
                                                                             'gaanaMailInputText'))
        return pm().inputText(searchBox, text)

    def inputEmailPassword(self, text):
        """
        输入密码点击submit
        :param text: 密码
        :return: True传入成功，False传入失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaPasswordBoard')
        passwordBoard = pm().find_element_by_id(id=id)
        pm().inputText(passwordBoard, text)
        element = pm().find_element_by_description(description='Submit')
        return pm().click_by_element(element=element)

    def skipAccountDeviceLimit(self):
        """
        检查是否有账号多地登录的提示（调用：clickDeviceLimitManage）
        :return: True跳过成功，False跳过失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaAccountDevicePanel')
        element = pm().find_element_by_id(id=id)
        if element is not None:
            return self.clickDeviceLimitManage()
        else:
            return True

    def clickDeviceLimitManage(self):
        """
        点击账号多地登录的提示页面Manage按键
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaDeviceLimitManage')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickDeviceLimitCancel(self):
        """
        点击账号多地登录的提示页面Cancel按键
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaDeviceLimitCancel')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickMailContinueButton(self):
        """
        点击确认登录（邮箱登录方式）
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaMailContinue')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickOK(self):
        """
        点击ok按键(根据匹配OK文本内容的按键，用于点击弹框的OK按键)
        :return: True点击成功，False点击失败
        """
        element = pm().find_element_by_text(text='OK')
        return pm().click_by_element(element=element)

    def clickCANCEL(self):
        """
        点击CANCEL按键(根据匹配CANCEL文本内容的按键，用于点击弹框的CANCEL按键)
        :return: True点击成功，False点击失败
        """
        element = pm().find_element_by_text(text='CANCEL')
        return pm().click_by_element(element=element)

    def clickGaanaLeftMenuSetting(self):
        """
        点击进入gaana LeftMenuSetting按键
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaLeftMenuSetting')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickGaanaLeftSongLanguage(self):
        """
        点击进入gaana LeftSongLanguage按键
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'LeftSongLanguage')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickGaanaLeftDispLanguage(self):
        """
        点击进入gaana LeftDispLanguage按键
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaLeftDispLanguage')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickGaanaLeftAPPTheme(self):
        """
        点击进入gaana gaanaLeftTheme按键
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaLeftTheme')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def getGaanaSwitchThemeName(self):
        """
        获取Gaana当前皮肤名称
        :return: 返回皮肤名称
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaSwitchTheme')
        element = pm().find_element_by_id(id=id)
        return element.get_text()

    def clickGaanaSwitchThemeButton(self):
        """
        点击进入gaana SwitchTheme按键
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaSwitchThemeButton')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickGaanaParentLayout(self, number):
        """
        点击进入gaana Parent列表
        :param number: 传入需要点击的列表序号：1、2或3等
        :return: True点击成功，False点击失败
        """
        Xpath = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaParentLayout') + number + ']'
        logger.info(Xpath)
        element = pm().find_element_by_Xpath(Xpath)
        return pm().click_by_element(element=element)

    def clickGaanaPlay(self):
        """
        点击进入gaana Play
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaPlay')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickGaanaNext(self):
        """
        点击gaana Next一曲
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaNext')
        element = pm().find_element_by_id(id=id)
        songNameBeforeChange = self.getCurrentSongName()
        pm().click_by_element(element=element)
        songNameAfterChange = self.getCurrentSongName()
        if songNameAfterChange == songNameBeforeChange:
            return False
        else:
            return True

    def clickGaanaPre(self):
        """
        点击gaana Pre一曲
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaPre')
        element = pm().find_element_by_id(id=id)
        songNameBeforeChange = self.getCurrentSongName()
        pm().click_by_element(element=element)
        songNameAfterChange = self.getCurrentSongName()
        if songNameAfterChange == songNameBeforeChange:
            return False
        else:
            return True

    def clickGaanaRepeat(self):
        """
        点击gaana Repeat
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaRepeat')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickGaanaShuffle(self):
        """
        点击gaana shuffle 随机
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaShuffle')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def getCurrentSongName(self):
        """
        获取歌曲名称（用于比较切歌后是否歌曲切换）
        :return: 返回歌曲名称
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaSongNameAtGaanaPage')
        element = pm().find_element_by_id(id=id)
        return element.get_text()

    def clickGaanaMenuLayout(self):
        """
        点击进入gaana MenuLayout
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaMenuLayout')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickGaanaAddPlayList(self):
        """
        点击gaana AddPlayList按键
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaAddPlayList')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def createNewPlaylist(self):
        """
        点击创建歌单
        :return:
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaCreatePlaylist')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def inputPlaylistName(self, text):
        """
        传入text创建歌曲列表
        :return: True 传入成功，False传入失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaInputTextToCreatePlaylist')
        element = pm().find_element_by_id(id=id)
        return pm().input_text(element=element, text=text)

    def inputSearchBoxText(self, text):
        """
        在搜索框内传入名称搜索内容
        :param text: 名称、艺术家、专辑
        :return: True传入成功，False传入失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaSearchText')
        element = pm().find_element_by_id(id=id)
        return pm().input_text(element=element, text=text)

    def clickKeyBoardGo(self):
        """
        点击键盘Go跳转页面
        :return: True点击成功, False点击失败
        """
        element = pm().find_element_by_description(description='Go')
        return pm().click_by_element(element=element)

    def clickPlaylistItemsOption(self, text):
        """
        根据playlist名称定位至option并点击
        :param text: playlist名称
        :return:  True点击成功，False点击失败
        """
        element = pm().find_element_by_text(text=text)
        optionElement = element.sibling(resourceId='com.gaana:id/clickoptionImage')
        return pm().click_by_element(element=optionElement)

    def clickDone(self):
        """
        点击创建歌单页面Done按键
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaDone')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickBackButton(self):
        """
        点击创建歌单页面X按键返回
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaBackToLastPageFromCreateList')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def swipeHeaderToBeginning(self):

        # element = pm().find_element_by_id( id='com.gaana:id/viewProductIconOverlay')
        return pm().swipe_to_end_by_id(id='com.gaana:id/viewProductIconOverlay')

    def swipePlaylistToBeginning(self):
        """
        滑动至Playlist开头部分
        :return: True滑动成功，False滑动失败
        """
        # headId = pm().readConfigByModuleAndKey( 'india_D90', 'GaanaPage', 'gaanaFavoriteTrackName')
        # pm().swipe_to_beginning_by_id( id=headId)

        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaPlaylistQueue')
        return pm().swipe_to_beginning_by_id(id=id)

    def swipePlaylistToEnd(self):
        """
        滑动至Playlist结尾部分
        :return: True滑动成功，False滑动失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaPlaylistQueue')
        return pm().swipe_to_end_by_id(id=id)

    def clickDeletePlayList(self):
        """
        点击删除歌曲列表
        :return: True删除成功，False删除失败
        """
        self.swipePlaylistToEnd()
        time.sleep(3)
        self.swipePlaylistToEnd()
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaPlayListItem')
        element = pm().find_element_by_idAndText(id=id, text='Delete Playlist')
        return pm().click_by_element(element=element)

    def clickGaanaDownload(self):
        """
        点击gaana Download按键
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaDownload')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def checkGaanaMusicDownLoaded(self):
        """
        检查gaana音乐是否已经下载了
        :return:
        """
        self.clickGaanaDownload()
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaDownloadDialog')
        element = pm().find_element_by_id(id=id)
        if element is not None:

            return True
        else:
            return False

    def clickGaanaFavButton(self):
        """
        点击gaana FavButton按键
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaFavButton')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickGaanaQueue(self):
        """
        点击gaana Queue按键
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaQueue')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def checkGaanaQueueIsExist(self):
        """
        点击gaana Queue list是否存在
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaQueueList')
        element = pm().find_element_by_id(id=id)
        if element is not None:
            return True
        else:
            return False

    def closeGaanaQueueList(self):
        """
        收起gaana Queue list
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaQueueName')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickTrendingByName(self, name):
        """
        根据名称查找Search页面中默认搜索项内容
        :param name: Kedarnath此类Gaana现有搜索关键词
        :return:True点击成功，False无此项内容，无法点击
        """
        # id = pm().readConfigByModuleAndKey( 'india_D90', 'GaanaPage', 'gaannaTrendingSongName')
        pm().swipe_to_beginning()
        element = pm().find_element_by_text(text=name)
        if element.exists:
            return pm().click_by_element(element=element)
        else:
            recyclerid = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaSearchRecyclerView')
            element = pm().find_element_by_id(id=recyclerid)
            pm().swipe_up_by_element(element=element)
            element = pm().find_element_by_text(text=name)
            if element.exists:
                return pm().click_by_element(element=element)
            else:
                return False

    def checkTitleName(self, text):
        """
        查看Title名称是否与传入一致
        :param text: 传入title名称
        :return: True一致，False不一致
        """
        TrendingTitle = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaTrendingTitle')
        element = pm().find_element_by_id(id=TrendingTitle)
        if element is not None:
            if element.get_text() == text:
                return True
            else:
                return False
        else:
            return False

    def clickGaanaBackButton(self):
        """
        点击返回上一页按键
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaBackIcon')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def chooseGaanaItems(self, name, number):
        """
        选择Gaana音乐页面中的栏目并播放
        :param name: 传入栏目名称
        :param number: 子栏目序号
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaSearchRecyclerView')
        xpath1 = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaHomePageItemsXpath1')
        xpath2 = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaHomePageItemsXpath2')
        xpath = xpath1 + name + xpath2 + number + ']'
        logger.info(xpath)
        element = pm().find_element_by_id(id=id)
        pm().swipe_to_beginning()
        for i in range(10):
            element = pm().find_element_by_text(text=name)
            if element.exists:
                logger.info('True')
                element = pm().find_element_by_Xpath(Xpath=xpath)
                return pm().click_by_element(element=element)
                break
            else:
                element = pm().find_element_by_id(id=id)
                pm().swipe_up_by_element(element=element)
        return False

    def checkSongIsPlaying(self):
        """
        校验歌曲是否处于播放状态（根据播放时间判断是否处于播放状态）
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaMediaStartTime')
        element = pm().find_element_by_id(id=id)
        timeBeforeWait = element.get_text()
        time.sleep(4)
        timeAfterWait = element.get_text()
        if timeBeforeWait != timeAfterWait:
            return True
        else:
            return False

    def checkSongIsPause(self):
        """
        校验歌曲是否处于暂停状态（根据播放时间判断是否处于暂停状态）
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaMediaStartTime')
        element = pm().find_element_by_id(id=id)
        timeBeforeWait = element.get_text()
        time.sleep(4)
        timeAfterWait = element.get_text()
        if timeBeforeWait == timeAfterWait:
            return True
        else:
            return False

    def checkLogOutButtonIsExist(self):
        """
        查看logout按键是否存在
        :return: True存在，False不存在
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaLogoutButton')
        element = pm().find_element_by_id(id=id)
        if element is not None:
            return True
        else:
            return False

    def clickLogOutButton(self):
        """
        点击logout登出按键
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaLogoutButton')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickSongLanguage(self):
        """
        点击Setting页面中的SongLanguage
        :return: True点击成功，False点击失败
        """
        element = pm().find_element_by_text(text='Song Language')
        return pm().click_by_element(element=element)

    def clickDisplayLanguage(self):
        """
        点击Setting页面中的Display Language
        :return: True点击成功，False点击失败
        """
        element = pm().find_element_by_text(text='Display Language')
        return pm().click_by_element(element=element)

    def chooseSongLanguageByName(self, name):
        """
        根据传入名称选择歌曲语言（
        :param name: 例如：Hindi、English等）
        :return: True点击成功，False点击失败
        """
        element = pm().find_element_by_text(text=name)
        return pm().click_by_element(element=element)

    def clickContinue(self):
        """
        点击Continue按键确认已经选择的音乐项
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaSettingContinue')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickBackToLastPage(self):
        """
        点击左上角返回按键返回至Setting页面（用于gaana菜单中的返回按键）
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaBackButtonUseInSettingPage')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickDisplayLanguage(self):
        """
        点击进入DisplayLanguage页面
        :return: True点击成功，False点击失败
        """
        element = pm().find_element_by_text(text='Display Language')
        return pm().click_by_element(element=element)

    def clickContinueInDisplayLanguage(self):
        """
        点击DisplayLanguage页面中的Continue
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaContinueButtonInDisplayLanguage')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickBackToLastPageInDisplayLanguage(self):
        """
        点击DisplayLanguage页面中的返回按键（该方法只用于DisplayLanguage）
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaBackButtonUseInDisplayLanguage')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickPlaybackSettings(self):
        """
        点击进入Playback Settings页面
        :return: True点击成功，False点击失败
        """
        element = pm().find_element_by_text(text='Playback Settings')
        return pm().click_by_element(element=element)

    def clickRestrictButton(self):
        """
        点击PlayBack Setting页面中的Resitrict开关
        :return: True点击成功，False点击失败
        """
        xpath = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaPlayBackSettingXpath1')
        element = pm().find_element_by_Xpath(Xpath=xpath)
        return pm().click_by_element(element=element)

    def clickDataSaveModeButton(self):
        """
        点击PlayBack Setting页面中的Data Save Mode开关
        :return: True点击成功，False点击失败
        """
        xpath = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaPlayBackSettingXpath2')
        element = pm().find_element_by_Xpath(Xpath=xpath)
        return pm().click_by_element(element=element)

    def clickAutoPlayButton(self):
        """
        点击PlayBack Setting页面中的Auto Play开关
        :return: True点击成功，False点击失败
        """
        xpath = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaPlayBackSettingXpath3')
        element = pm().find_element_by_Xpath(Xpath=xpath)
        return pm().click_by_element(element=element)

    def clickHighResolutionSpinner(self):
        """
        点击PlayBack Setting页面中Download over下拉列表
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaPlayBackSettingSpinner')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def chooseWifi(self):
        """
        选择Download over中的wifi模式
        :return: True点击成功，False点击失败
        """
        self.clickHighResolutionSpinner()
        element = pm().find_element_by_text(text='WiFi only')
        return pm().click_by_element(element=element)

    def choose3G(self):
        """
        选择Download over中的3G模式
        :return: True点击成功，False点击失败
        """
        self.clickHighResolutionSpinner()
        element = pm().find_element_by_text(text='3G and above')
        return pm().click_by_element(element=element)

    def choose2G(self):
        """
        选择Download over中的2G模式
        :return: True点击成功，False点击失败
        """
        self.clickHighResolutionSpinner()
        element = pm().find_element_by_text(text='2G and above')
        return pm().click_by_element(element=element)

    def clickSongQualitySpinner(self):
        """
        点击打开音频质量下拉列表
        :return: True点击成功，False点击失败
        """
        xpath = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaSongQualityXpath')
        element = pm().find_element_by_Xpath(Xpath=xpath)
        return pm().click_by_element(element=element)

    def chooseAuto(self):
        """
        点击Auto质量
        :return: True点击成功，False点击失败
        """
        self.clickSongQualitySpinner()
        element = pm().find_element_by_text(text='Auto')
        return pm().click_by_element(element=element)

    def chooseHighDefinition(self):
        """
        点击High Definition质量
        :return: True点击成功，False点击失败
        """
        self.clickSongQualitySpinner()
        element = pm().find_element_by_text(text='High Definition')
        return pm().click_by_element(element=element)

    def chooseHigh(self):
        """
        点击High质量
        :return: True点击成功，False点击失败
        """
        self.clickSongQualitySpinner()
        element = pm().find_element_by_text(text='High')
        return pm().click_by_element(element=element)

    def chooseMedium(self):
        """
        点击Medium质量
        :return: True点击成功，False点击失败
        """
        self.clickSongQualitySpinner()
        element = pm().find_element_by_text(text='Medium')
        return pm().click_by_element(element=element)

    def chooseLow(self):
        """
        点击Low质量
        :return: True点击成功，False点击失败
        """
        self.clickSongQualitySpinner()
        element = pm().find_element_by_text(text='Low')
        return pm().click_by_element(element=element)

    def clickNightModeSpinner(self):
        """
        点击Setting列表中NightMode下拉列表
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaNightModeSpinner')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def chooseOn(self):
        """
        选择NightMode下拉列表On
        :return: True点击成功，False点击失败
        """
        self.clickNightModeSpinner()
        pm().find_element_by_idAndText(id='android:id/text1', text='On')

    def chooseOff(self):
        """
        选择NightMode下拉列表Off
        :return: True点击成功，False点击失败
        """
        self.clickNightModeSpinner()
        pm().find_element_by_idAndText(id='android:id/text1', text='Off')

    def chooseAutomaticAtSunset(self):
        """
        选择NightMode下拉列表AutomaticAtSunset
        :return: True点击成功，False点击失败
        """
        self.clickNightModeSpinner()
        pm().find_element_by_idAndText(id='android:id/text1', text='Automatic at sunset')

    def checkIsLogin(self):
        """
        检查未登录时弹出的话术框（检测SignUp按键，如果有SignUp按键则未登录，返回True）
        :return: True未登录，False已登录
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaSignUpButton')
        element = pm().find_element_by_id(id=id)
        if element.exists():
            return True
        else:
            return False

    def clickAlbumsFristItemInSearchPage(self):
        """
        滑动查找Albums列表中第一个内容
        :return: True点击成功,False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaSearchRecyclerView')
        for i in range(3):
            pm().swipe_to_beginning_by_id(id=id)
        albumsElement = pm().find_element_by_text(text='Albums')
        if albumsElement.exists():
            gaanaSearchRecyclerView = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaSearchRecyclerView')
            recyclerElement = albumsElement.sibling(resourceId=gaanaSearchRecyclerView)
            childs = recyclerElement.child()
            gaanaFavoriteTrackName = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaFavoriteTrackName')
            element = childs[0].child(resourceId=gaanaFavoriteTrackName)
            return pm().click_by_element(element=element)
        else:
            return False

    def clickSongsListFristItemInSearchPage(self):
        """
        滑动查找Song列表中第一个内容
        :return: True点击成功,False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaSearchRecyclerView')
        for i in range(3):
            pm().swipe_to_beginning_by_id(id=id)
        gaanaSearchRefresh_layoutId = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage',
                                                                    'gaanaSearchRefresh_layout')
        recyclerViewelement = pm().find_element_by_id(id=gaanaSearchRefresh_layoutId)
        pm().swipe_up_by_element(element=recyclerViewelement)
        songsElement = pm().find_element_by_text(text='Songs')
        if songsElement.exists():
            gaanaSearchRecyclerView = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaSearchRecyclerView')
            recyclerElement = songsElement.sibling(resourceId=gaanaSearchRecyclerView)
            childs = recyclerElement.child()
            gaanaFavoriteTrackName = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaFavoriteTrackName')
            element = childs[0].child(resourceId=gaanaFavoriteTrackName)
            return pm().click_by_element(element=element)
        else:
            return False

    def clickArtistsFristItemInSearchPage(self):
        """
        滑动查找Artists列表中第一个内容
        :return: True点击成功,False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaSearchRecyclerView')
        for i in range(3):
            pm().swipe_to_end_by_id(id=id)
        ArtistsElement = pm().find_element_by_text(text='Artists')
        if ArtistsElement.exists():
            gaanaSearchRecyclerView = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaSearchRecyclerView')
            recyclerElement = ArtistsElement.sibling(resourceId=gaanaSearchRecyclerView)
            childs = recyclerElement.child()
            gaanaFavoriteTrackName = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaFavoriteTrackName')
            element = childs[0].child(resourceId=gaanaFavoriteTrackName)
            return pm().click_by_element(element=element)
        else:
            return False

    def clickPlayListsFristItemInSearchPage(self):
        """
        滑动查找PlayLists列表中第一个内容
        :return: True点击成功,False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaSearchRecyclerView')
        for i in range(3):
            pm().swipe_to_end_by_id(id=id)
        gaanaSearchRefresh_layoutId = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage',
                                                                    'gaanaSearchRefresh_layout')
        recyclerViewelement = pm().find_element_by_id(id=gaanaSearchRefresh_layoutId)
        pm().swipe_down_by_element(element=recyclerViewelement)
        playListElement = pm().find_element_by_text(text='Playlists')
        if playListElement.exists():
            gaanaSearchRecyclerView = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaSearchRecyclerView')
            recyclerElement = playListElement.sibling(resourceId=gaanaSearchRecyclerView)
            childs = recyclerElement.child()
            gaanaFavoriteTrackName = pm().readConfigByModuleAndKey('india_D90', 'GaanaPage', 'gaanaFavoriteTrackName')
            element = childs[0].child(resourceId=gaanaFavoriteTrackName)
            return pm().click_by_element(element=element)
        else:
            return False

    def clickGaanaMusicPlayPauseSong100times(self):
        """
        压力测试（播放、暂停gaana音乐。100次）
        :return: True，False
        """
        k = 0
        for i in range(100):
            result = self.clickGaanaPlay()
            time.sleep(3)
            if result:
                pass
            else:
                logger.info(str(i) + ' Fail to click Gaana Play')
                k = k + 1
        if k == 0:
            return True
        else:
            logger.info('Fail times: ' + str(k))
            return False

    def clickGaanaMusicPreSong100times(self):
        """
        压力测试（播放、暂停gaana音乐。100次）
        :return: True，False
        """
        k = 0
        for i in range(100):
            result = self.clickGaanaPre()
            time.sleep(3)
            if result:
                pass
            else:
                logger.info(str(i) + ' Fail to click Gaana Pre Button')
                k = k + 1
        if k == 0:
            return True
        else:
            logger.info('Fail times: ' + str(k))
            return False

    def clickGaanaMusicNextSong100times(self):
        """
        压力测试（播放、暂停gaana音乐。100次）
        :return: True，False
        """
        k = 0
        for i in range(100):
            result = self.clickGaanaNext()
            time.sleep(3)
            if result:
                pass
            else:
                logger.info(str(i) + ' Fail to click Gaana Pre Button')
                k = k + 1
        if k == 0:
            return True
        else:
            logger.info('Fail times: ' + str(k))
            return False
