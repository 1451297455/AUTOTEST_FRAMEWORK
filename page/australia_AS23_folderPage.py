# -*- coding: utf-8 -*-
from UIconfig.Base import Base
from page.PublicMethod import PublicMethod as pm
from page.india_D90_homePage import india_D90_homePage as homePage
from page.india_D90_morePage import morePage
import time, os
import UIconfig.logger as loggers

logger = loggers.Logger()
os.path.abspath('.')


class australia_AS23_folderPage(Base):

    def clickVideo(self):
        """
        点击进入视频目录
        :return: True点击成功，False点击失败
        """
        Video_Xpath = pm().readConfigByModuleAndKey('australia_AS23', 'Folder_resourceId', 'Video_Xpath')
        element = pm().find_element_by_Xpath(Xpath=Video_Xpath)
        return pm().click_by_element(element)

    def clickPicture(self):
        """
        点击进入图片目录
        :return:True点击成功，False点击失败
        """
        Picture_Xpath = pm().readConfigByModuleAndKey('australia_AS23', 'Folder_resourceId', 'Picture_Xpath')
        element = pm().find_element_by_Xpath(Xpath=Picture_Xpath)
        return pm().click_by_element(element)

    def clickDocument(self):
        """
        点击进入文档目录
        :return:True点击成功，False点击失败
        """
        Document_Xpath = pm().readConfigByModuleAndKey('australia_AS23', 'Folder_resourceId', 'Document_Xpath')
        element = pm().find_element_by_Xpath(Xpath=Document_Xpath)
        return pm().click_by_element(element)

    def clickFloderSpinner(self):
        """
        点击切换USB1/2栏
        :return: True，False
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'Folder_resourceId', 'DeviceList')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def changeToUsb1(self):
        """
        切换至USB1页面
        :return: True，False
        """
        self.clickFloderSpinner()
        id = pm().readConfigByModuleAndKey('australia_AS23', 'Folder_resourceId', 'DeviceTitle')
        element = pm().find_element_by_idAndText(id=id, text='USB 1')
        return pm().click_by_element(element=element)

    def changeToUsb2(self):
        """
        切换至USB2页面
        :return: True，False
        """
        self.clickFloderSpinner()
        id = pm().readConfigByModuleAndKey('australia_AS23', 'Folder_resourceId', 'DeviceTitle')
        element = pm().find_element_by_idAndText(id=id, text='USB 2')
        return pm().click_by_element(element=element)

    def swipeToFolderPageBeginning(self):
        """
        滑动至Folder页面顶部
        :return: True，False
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'Folder_resourceId', 'FolderViewPage')
        pm().swipe_to_beginning_by_id(id=id)

    def swipeToFolderPageEnd(self):
        """
        滑动至Folder页面顶部
        :return: True，False
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'Folder_resourceId', 'FolderViewPage')
        pm().swipe_to_end_by_id(id=id)

    def getFolderList(self):
        """
        获取该Folder页面下各文件夹列表
        :return: list
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'Folder_resourceId', 'FolderViewPage')
        return pm().find_element_by_id(id=id).child()

    def clickBackToLastItem(self):
        """
        点击文件夹中的返回按键（蓝色图标）
        :return: True,False
        """
        childs = self.getFolderList()
        id = pm().readConfigByModuleAndKey('australia_AS23', 'Folder_resourceId', 'BackButton')
        element = pm().find_element_by_id(id=id)
        if element is not None:
            return pm().click_by_element(element=element)
        else:
            return False

    def clickItemInVideoPageByName(self, name):
        """
        Videos页面中根据文件名称点击打开该文件（用于Folder中U盘文件夹操作）
        注：该方法需要新途供应商将itemName的clickable打开后才可使用，预计要10月中旬
        :return: True,False
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'Folder_resourceId', 'VideoPageItemId')
        element = pm().find_element_by_idAndText(id=id, text=name)
        return pm().click_by_element(element=element)

    def clickItemInPicturesAndDocumentPageByName(self, name):
        """
        Pictures、Documents页面中根据文件名称点击打开该文件（用于Folder中U盘文件夹操作）
        注：该方法需要新途供应商将itemName的clickable打开后才可使用，预计要10月中旬
        :return: True,False
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'Folder_resourceId', 'ItemName')
        element = pm().find_element_by_idAndText(id=id, text=name)
        return pm().click_by_element(element=element)

    def clickClosePictureButton(self):
        """
        关闭图片
        :return: True,False
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'Folder_resourceId', 'CloseButton')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

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

    def clickRotateButton(self):
        """
        旋转图片
        :return: True,False
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'Folder_resourceId', 'RotateButton')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickLeftPictureButton(self):
        """
        点击上一张图片
        :return: True,False
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'Folder_resourceId', 'LeftPictureButton')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def clickRightPictureButton(self):
        """
        点击下一张图片
        :return: True,False
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'Folder_resourceId', 'RightPictureButton')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def closeDocument(self):
        """
        关闭文档
        :return: True,False
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'Folder_resourceId', 'CloseDocumentButton')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def swipeDocumentToDown(self):
        """
        向下滑动文档页面
        :return: True，False
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'Folder_resourceId', 'DocumentContent')
        element = pm().find_element_by_id(id=id)
        return pm().swipe_down_by_element(element=element)

    def swipeDocumentToUp(self):
        """
        向下滑动文档页面
        :return: True，False
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'Folder_resourceId', 'DocumentContent')
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
            self.clickItemInVideoPageByName(name)  # 通过名称点击播放视频
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
            self.clickItemInVideoPageByName(name)  # 通过名称点击播放视频
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
            self.clickItemInVideoPageByName(name)  # 通过名称点击播放视频
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
            self.clickItemInVideoPageByName(name)  # 通过名称点击播放视频
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
            self.clickItemInVideoPageByName(name)  # 通过名称点击文档
            time.sleep(1)
            self.swipeDocumentToUp()  # 下滑查看
            time.sleep(1)
        if k == 0:
            return True
        else:
            logger.info('Fail times: ' + str(k))
            return False


folderPage = australia_AS23_folderPage()
