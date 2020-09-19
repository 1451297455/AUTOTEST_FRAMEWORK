# -*- coding: utf-8 -*-
# AS23P 蓝牙电话页面方法
from UIconfig.Base import Base
from page.PublicMethod import PublicMethod as pm
import UIconfig.logger as loggers

logger = loggers.Logger()


class thailand_AS23P_btphonePage(Base):

    # 点击 bt Keypad title
    def clickKeypad(self):
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'BT_Phone_resourceId', 'KEYPAD')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    # 点击 bt contacts title
    def clickContacts(self):
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'BT_Phone_resourceId', 'CONTACTS')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    # 点击 bt recents title
    def clickRecents(self):
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'BT_Phone_resourceId', 'RECENTS')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    # 点击Synchronization同步通讯录
    def clickSynchronizationButton(self):
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'BT_Phone_resourceId', 'SYNCHRONIZATION')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)
