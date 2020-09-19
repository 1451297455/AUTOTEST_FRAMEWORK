# -*- coding: utf-8 -*-
from UIconfig.Base import Base
from page.PublicMethod import PublicMethod as pm

import time, os
import UIconfig.logger as loggers

logger = loggers.Logger()

os.path.abspath('.')


class australia_AS23_morePage(Base):

    def clickFolder(self):
        """
        点击进入Folder目录
        :return: True点击成功，False点击失败
        """
        text = pm().readConfigByModuleAndKey('australia_AS23', 'More_resourceId', 'Folder')
        element = pm().find_element_by_idAndText(id=id, text=text)
        return pm().click_by_element(element)

    def clickInbox(self):
        """
        点击进入INBOX目录
        :return:True点击成功，False点击失败
        """
        text = pm().readConfigByModuleAndKey('australia_AS23', 'More_resourceId', 'Inbox')
        element = pm()._find_element_by_text(text=text)
        return pm().click_by_element(element)

    def clickVehicleSetting(self):
        """
        点击进入Vehicle SETTING目录
        :return:True点击成功，False点击失败
        """
        text = pm().readConfigByModuleAndKey('australia_AS23', 'More_resourceId', 'VehicleSetting')
        element = pm()._find_element_by_text(text=text)
        return pm().click_by_element(element)

    def clickMaintenanceService(self):
        """
        点击进入MaintenanceService目录
        :return:True点击成功，False点击失败
        """
        text = pm().readConfigByModuleAndKey('australia_AS23', 'More_resourceId', 'MaintenanceService')
        element = pm()._find_element_by_text(text=text)
        return pm().click_by_element(element)


morePage = australia_AS23_morePage()
