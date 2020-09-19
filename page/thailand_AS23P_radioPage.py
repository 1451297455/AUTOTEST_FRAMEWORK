# -*- coding: utf-8 -*-
# AS23P Radio页面方法
from UIconfig.Base import Base
from page.PublicMethod import PublicMethod as pm
import UIconfig.logger as loggers

logger = loggers.Logger()


class thailand_AS23P_radioPage(Base):

    # Radio页面点击搜台按键
    def clickRadioScaning(self):
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'radioPage_resourceId', 'Radio_ScanningButton')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    # 选择调频FM
    def changeToFM(self):
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'radioPage_resourceId', 'ChannelTitle')
        # logger.info('id ' + id)
        element = pm().find_element_by_id(id=id)
        pm().click_by_element(element=element)
        fmId = pm().readConfigByModuleAndKey('thailand_AS23P', 'radioPage_resourceId', 'FM')
        # logger.info('fmId ' + fmId)
        fm = pm().find_element_by_id(id=fmId)
        return pm().click_by_element(element=fm)

    # 选择调频AM
    def changeToAM(self):
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'radioPage_resourceId', 'ChannelTitle')
        amId = pm().readConfigByModuleAndKey('thailand_AS23P', 'radioPage_resourceId', 'AM')
        element = pm().find_element_by_id(id=id)
        pm().click_by_element(element=element)
        am = pm().find_element_by_id(id=amId)
        return pm().click_by_element(element=am)

    # 打开ALL调频列表
    def openAllList(self):
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'radioPage_resourceId', 'All')
        # logger.info('all id: ' + id)
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    # 打开Favorite调频列表
    def openFavoriteList(self):
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'radioPage_resourceId', 'FAVOURITE')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)
