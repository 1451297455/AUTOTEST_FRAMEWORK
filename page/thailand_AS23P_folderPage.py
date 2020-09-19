# -*- coding: utf-8 -*-
# AS23P 文件管理页面方法
from UIconfig.Base import Base
from page.PublicMethod import PublicMethod as pm
import time
import UIconfig.logger as loggers

logger = loggers.Logger()


class thailand_AS23P_folderPage(Base):

    # 点击切换USB连接
    def clickDevicesList(self):
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'Folder_resourceId', 'DeviceList')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    # 点击选择USB1
    def changeToUSB1(self):
        self.clickDevicesList()
        time.sleep(1)
        Xpath = pm().readConfigByModuleAndKey('thailand_AS23P', 'Folder_resourceId', 'Device_USB1')
        element = pm().find_element_by_Xpath(Xpath=Xpath)
        return pm().click_by_element(element)

    # 点击选择USB2
    def changeToUSB2(self):
        self.clickDevicesList()
        time.sleep(1)
        Xpath = pm().readConfigByModuleAndKey('thailand_AS23P', 'Folder_resourceId', 'Device_USB2')
        element = pm().find_element_by_Xpath(Xpath=Xpath)
        return pm().click_by_element(element)

    # 点击Folder页面video标题
    def clickVideoTitle(self):
        Xpath = pm().readConfigByModuleAndKey('thailand_AS23P', 'Folder_resourceId', 'Video_Xpath')
        element = pm().find_element_by_Xpath(Xpath=Xpath)
        return pm().click_by_element(element)

    # 点击Folder页面document标题
    def clickPictureTitle(self):
        Xpath = pm().readConfigByModuleAndKey('thailand_AS23P', 'Folder_resourceId', 'Picture_Xpath')
        element = pm().find_element_by_Xpath(Xpath=Xpath)
        return pm().click_by_element(element)

    # 点击Folder页面picture标题
    def clickDocumentTitle(self):
        Xpath = pm().readConfigByModuleAndKey('thailand_AS23P', 'Folder_resourceId', 'Document_Xpath')
        element = pm().find_element_by_Xpath(Xpath=Xpath)
        return pm().click_by_element(element)
