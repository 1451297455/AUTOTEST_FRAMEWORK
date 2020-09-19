# -*- coding: utf-8 -*-
# AS23P CallCentre页面方法
from UIconfig.Base import Base
from page.PublicMethod import PublicMethod as pm
import UIconfig.logger as loggers

logger = loggers.Logger()


class thailand_AS23P_callCentrePage(Base):

    # 点击Cancel卡片
    def clickCancel(self):
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'CallCentre_resourceId', 'Cancel')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    # 点击OK卡片
    def clickOK(self):
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'CallCentre_resoureceId', 'Ok')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)
