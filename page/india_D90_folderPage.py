# -*- coding: utf-8 -*-
from UIconfig.Base import Base
from page.PublicMethod import PublicMethod as pm
from page.india_D90_homePage import india_D90_homePage as homePage
from page.india_D90_morePage import morePage
import time, os
import UIconfig.logger as loggers

logger = loggers.Logger()
os.path.abspath('.')


class india_D90_folderPage(Base):

    def clickVideo(self):
        """
        点击进入视频目录
        :return: True点击成功，False点击失败
        """
        text = pm().readConfigByModuleAndKey('india_D90', 'FolderPage', 'VideoPage')
        element = pm().find_element_by_text(text=text)
        return pm().click_by_element(element)

    def clickPicture(self):
        """
        点击进入图片目录
        :return:True点击成功，False点击失败
        """
        text = pm().readConfigByModuleAndKey('india_D90', 'FolderPage', 'PicturePage')
        element = pm().find_element_by_text(text=text)
        return pm().click_by_element(element)

    def clickDocument(self):
        """
        点击进入文档目录
        :return:True点击成功，False点击失败
        """
        text = pm().readConfigByModuleAndKey('india_D90', 'FolderPage', 'DocumentsPage')
        element = pm().find_element_by_text(text=text)
        return pm().click_by_element(element)

    def clickFloderSpinner(self):
        """
        点击音乐切换栏
        :return: True，False
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'FolderPage', 'MediaSource')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def changeToUsb1(self):
        """
        切换至USB1页面
        :return: True，False
        """
        self.clickFloderSpinner()
        id = pm().readConfigByModuleAndKey('india_D90', 'FolderPage', 'Usb1')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def changeToUsb2(self):
        """
        切换至USB1页面
        :return: True，False
        """
        self.clickFloderSpinner()
        id = pm().readConfigByModuleAndKey('india_D90', 'FolderPage', 'Usb2')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def changeToLocalFolder(self):
        """
        切换至LocalFolder页面
        :return: True，False
        """
        self.clickFloderSpinner()
        id = pm().readConfigByModuleAndKey('india_D90', 'FolderPage', 'LocalFolder')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def swipeToFolderPageBeginning(self):
        """
        滑动至Folder页面顶部
        :return: True，False
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'FolderPage', 'MediaList')
        return pm().swipe_to_beginning_by_id(id=id)

    def swipeToFolderPageEnd(self):
        """
        滑动至Folder页面顶部
        :return: True，False
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'FolderPage', 'MediaList')
        return pm().swipe_to_end_by_id(id=id)

    def openVedioByName(self, name):
        """
        通过文件名打开播放视频
        :param name:
        :return: True，False
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'FolderPage', 'FolderItemsName')
        element = pm().find_element_by_idAndText(id=id, text=name)
        if element.exists():
            elementClickLayout = element.sibling(resourceId='com.saicmotor.folder:id/item_click_layout')
            return pm().click_by_element(element=elementClickLayout)
        else:
            logger.info('Can not find ' + name)
            return False

    def openPictureByName(self, name):
        """
        通过图片名打开图片
        :param name:
        :return: True，False
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'FolderPage', 'FolderItemsName')
        element = Base().find_element_by_idAndText(id=id, text=name)
        if element.exists():
            elementClickLayout = element.sibling(resourceId='com.saicmotor.folder:id/item_click_layout')
            return pm().click_by_element(element=elementClickLayout)
        else:
            logger.info('Can not find ' + name)
            return False

    def clickNextPicture(self):
        """
        点击下一张图片按键
        :return: True,False
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'FolderPage', 'RightPage')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickPrePicture(self):
        """
        点击上一张图片按键
        :return: True,False
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'FolderPage', 'LeftPage')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def openDocumentByName(self, name):
        """
        通过文档名打开文档
        :param name:
        :return: True，False
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'FolderPage', 'FolderItemsName')
        element = pm().find_element_by_idAndText(id=id, text=name)
        if element.exists():
            elementClickLayout = element.sibling(resourceId='com.saicmotor.folder:id/item_click_layout')
            return pm().click_by_element(element=elementClickLayout)
        else:
            logger.info('Can not find ' + name)
            return False

    def swipeDocumentToDown(self):
        """
        向下滑动文档页面
        :return: True，False
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'FolderPage', 'DocumentPageList')
        element = pm().find_element_by_id(id=id)
        return pm().swipe_down_by_element(element=element)

    def swipeDocumentToUp(self):
        """
        向下滑动文档页面
        :return: True，False
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'FolderPage', 'DocumentPageList')
        element = pm().find_element_by_id(id=id)
        return pm().swipe_up_by_element(element=element)

    def changeToVideoClickNext50times(self, name):
        """
        压力测试（首页>more页面>folder>打开视频播放3秒>点击硬按键下一曲播放3秒，50次）
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
            homePage().clickMore()  # 点击dock栏More按键页面
            time.sleep(1)
            morePageActivity = pm().get_Current_Activity()
            if morePageActivity == 'com.saicmotor.launcher.view.MoreActivity':
                pass
            else:
                logger.info(str(i) + ' Fail ' + morePageActivity)
                k = k + 1
            morePage.clickFolder()  # 进入Folder
            time.sleep(1)
            self.changeToUsb2()
            time.sleep(1)
            self.clickVideo()  # 打开video页面
            self.openVedioByName(name)  # 通过名称点击播放视频
            time.sleep(3)
            homePage().clickWheelHardKeyNext()
            time.sleep(3)

        if k == 0:
            return True
        else:
            logger.info('Fail times: ' + str(k))
            return False

    def changeToVideoClickPre50times(self, name):
        """
        压力测试（首页>more页面>folder>打开视频播放3秒>点击硬按键上一曲播放3秒，50次）
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
            homePage().clickMore()  # 点击dock栏More按键页面
            time.sleep(1)
            morePageActivity = pm().get_Current_Activity()
            if morePageActivity == 'com.saicmotor.launcher.view.MoreActivity':
                pass
            else:
                logger.info(str(i) + ' Fail ' + morePageActivity)
                k = k + 1
            morePage.clickFolder()  # 进入Folder
            time.sleep(1)
            self.changeToUsb2()
            time.sleep(1)
            self.clickVideo()  # 打开video页面
            self.openVedioByName(name)  # 通过名称点击播放视频
            time.sleep(3)
            homePage().clickWheelHardKeyPre()
            time.sleep(3)

        if k == 0:
            return True
        else:
            logger.info('Fail times: ' + str(k))
            return False

    def changeToPictureClickNext50times(self, name):
        """
        压力测试（首页>more页面>folder>打开图片查看3秒>点击下一张查看3秒，50次）
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
            homePage().clickMore()  # 点击dock栏More按键页面
            time.sleep(1)
            morePageActivity = pm().get_Current_Activity()
            if morePageActivity == 'com.saicmotor.launcher.view.MoreActivity':
                pass
            else:
                logger.info(str(i) + ' Fail ' + morePageActivity)
                k = k + 1
            morePage.clickFolder()  # 进入Folder
            time.sleep(1)
            self.changeToUsb2()
            time.sleep(1)
            self.clickPicture()  # 打开Picture页面
            self.openPictureByName(name)  # 通过名称点击播放视频
            time.sleep(3)
            self.clickNextPicture()
            time.sleep(3)
        if k == 0:
            return True
        else:
            logger.info('Fail times: ' + str(k))
            return False

    def changeToPictureClickPre50times(self, name):
        """
        压力测试（首页>more页面>folder>打开图片查看3秒>点击上一张查看3秒，50次）
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
            homePage().clickMore()  # 点击dock栏More按键页面
            time.sleep(1)
            morePageActivity = pm().get_Current_Activity()
            if morePageActivity == 'com.saicmotor.launcher.view.MoreActivity':
                pass
            else:
                logger.info(str(i) + ' Fail ' + morePageActivity)
                k = k + 1
            morePage.clickFolder()  # 进入Folder
            time.sleep(1)
            self.changeToUsb2()
            time.sleep(1)
            self.clickPicture()  # 打开Picture页面
            self.openPictureByName(name)  # 通过名称点击播放视频
            time.sleep(3)
            self.clickPrePicture()
            time.sleep(3)
        if k == 0:
            return True
        else:
            logger.info('Fail times: ' + str(k))
            return False

    def changeToDocumentClickNext50times(self, name):
        """
        压力测试（首页>more页面>folder>打开图片查看3秒>点击下一张查看3秒，50次）
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
            homePage().clickMore()  # 点击dock栏More按键页面
            time.sleep(1)
            morePageActivity = pm().get_Current_Activity()
            if morePageActivity == 'com.saicmotor.launcher.view.MoreActivity':
                pass
            else:
                logger.info(str(i) + ' Fail ' + morePageActivity)
                k = k + 1
            morePage.clickFolder()  # 进入Folder
            time.sleep(1)
            self.changeToUsb2()  # 切换至usb2
            time.sleep(1)
            self.clickDocument()  # 打开文档页面
            self.openDocumentByName(name)  # 通过名称点击文档
            time.sleep(1)
            self.swipeDocumentToUp()  # 下滑查看
            time.sleep(1)
        if k == 0:
            return True
        else:
            logger.info('Fail times: ' + str(k))
            return False


folderPage = india_D90_folderPage()
