# -*- coding: utf-8 -*-
# AS23P 维保页面方法
from UIconfig.Base import Base
from page.PublicMethod import PublicMethod as pm
import UIconfig.logger as loggers

logger = loggers.Logger()


class thailand_AS23P_passionServicePage(Base):

    # 点击进入Dealer
    def clickGoToDealer(self):
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'PassionService_resourceId', 'Go_To_Dealer')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    # 点击进入MyReservation
    def clickMyReservation(self):
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'PassionService_resourceId', 'My_Reservation')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    # 点击进入Maintenance Record
    def clickMaintenanceRecord(self):
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'PassionService_resourceId', 'Maintenance_Record')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    # 点击拨打D2D电话
    def clickCallD2D(self):
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'PassionService_resourceId', 'CallD2D')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    # 点击gotodealer中的Back按键
    def clickBack(self):
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'PassionService_resourceId', 'Back')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    # 点击gotodealer中的MGDealer按键
    def clickMGDealer(self):
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'PassionService_resourceId', 'MG_DEALER')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    # 点击gotodealer中的MobileService按键
    def clickMobileService(self):
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'PassionService_resourceId', 'MOBILE_SERVICE')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)
