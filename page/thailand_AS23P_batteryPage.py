# -*- coding: utf-8 -*-
# AS23P EV充电电量页面方法
from UIconfig.Base import Base
from page.PublicMethod import PublicMethod as pm
import UIconfig.logger as loggers

logger = loggers.Logger()


class thailand_AS23P_batteryPage(Base):

    # 点击Search Charging Station
    def clickSearchChargingStation(self):
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'Battery_resourceId', 'SearchChargingStation')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)
