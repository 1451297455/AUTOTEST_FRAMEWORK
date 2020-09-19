# -*- coding: utf-8 -*-
# AS23P inbox页面方法
from UIconfig.Base import Base
from page.PublicMethod import PublicMethod as pm
import UIconfig.logger as loggers

logger = loggers.Logger()


class thailand_AS23P_inboxPage(Base):

    # 点击 Travel_Plan title
    def clickTravel_Plan(self):
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'Inbox_resourcedId', 'Travel_Plan')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    # 点击 POI title
    def clickPOI(self):
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'Inbox_resourcedId', 'POI')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    # 点击 Message title
    def clickMessage(self):
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'Inbox_resourcedId', 'Message')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    # 点击 MG_News title
    def clickMG_News(self):
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'Inbox_resourcedId', 'MG_News')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)
