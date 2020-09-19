# -*- coding: utf-8 -*-
# AS23P lifeStyle页面方法
from UIconfig.Base import Base
from page.PublicMethod import PublicMethod as pm
import UIconfig.logger as loggers

logger = loggers.Logger()


class thailand_AS23P_lifeStylePage(Base):

    # 点击News卡片
    def clickNewsCard(self):
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'lifeStyel_resourceId', 'News')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    # 点击Lottery卡片
    def clickLotteryCard(self):
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'lifeStyel_resourceId', 'Lottery')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    # 点击左上角lifeStyle按键返回上一页
    def clickLifeStyleBackToHomePage(self):
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'lifeStyel_resourceId', 'Lottery')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    # 点击右上角lifeStyle Subscribe按键进入订阅页面
    def clickLifeStyleSubscribeButton(self):
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'lifeStyel_resourceId', 'Subscribe')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    # 点击右上角Exit按键退出lifeStyle Edit页面
    def clickLifeStylesExitButton(self):
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'lifeStyel_resourceId', 'Exit')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)
