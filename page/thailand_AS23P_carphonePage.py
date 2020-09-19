# -*- coding: utf-8 -*-
# AS23P Carphone页面方法
from UIconfig.Base import Base
from page.PublicMethod import PublicMethod as pm
import UIconfig.logger as loggers

logger = loggers.Logger()


class thailand_AS23P_carphonePage(Base):

    # 点击Carphone页面KeyPad标题
    def clickCarPhoneKeyPadTitle(self):
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'CarPhone_resourcedId', 'KEYPAD')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    # 点击Carphone页面Recents标题
    def clickRecentsTitle(self):
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'CarPhone_resourcedId', 'RECENTS')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    # 点击Carphone页面Contacts标题
    def clickContactsTitle(self):
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'CarPhone_resourcedId', 'CONTACTS')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)
