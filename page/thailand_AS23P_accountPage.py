# -*- coding: utf-8 -*-
# AS23P SAIC帐号登录页面方法
from UIconfig.Base import Base
from page.PublicMethod import PublicMethod as pm
import UIconfig.logger as loggers

logger = loggers.Logger()


class thailand_AS23P_accountPage(Base):

    # 切换至帐号登录
    def changeToAccountLogin(self):
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'Account_resourceId', 'loginButton')  # 帐号登录button id
        element = pm().find_element_by_id(id=id)
        if element is None:  # 如果帐号登录button不存在则选择切换
            switchId = pm().readConfigByModuleAndKey('thailand_AS23P', 'Account_resourceId', 'switchButton')
            switchElement = pm().find_element_by_id(id=switchId)
            return pm().click_by_element(switchElement)
        else:
            # logger.info('already in Accountlogin')
            pass

    # 切换至扫码登录
    def changeToScanLogin(self):
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'Account_resourceId', 'loginButton')  # 帐号登录button id
        element = pm().find_element_by_id(id=id)
        if element is not None:  # 如果帐号登录button存在则选择切换
            switchId = pm().readConfigByModuleAndKey('thailand_AS23P', 'Account_resourceId', 'switchButton')
            switchElement = pm().find_element_by_id(id=switchId)
            return pm().click_by_element(switchElement)
        else:
            # logger.info('already in Accountlogin')
            pass

    # 输入帐号
    def enterUserName(self, username):
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'Account_resourceId', 'userName')
        element = pm().find_element_by_id(id=id)
        return pm().inputText(element, username)  # 输入框中传入Username

    # 输入密码
    def enterPassword(self, password):
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'Account_resourceId', 'password')
        element = pm().find_element_by_id(id=id)
        return pm().inputText(element, password)  # 输入框中传入Username

    # 点击帐号登录标题（该方法用于帐号登录输入密码后点击输入键盘以外的其他地方，收起键盘后方便点击登录。）
    def clickAccountTitle(self):
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'Account_resourceId', 'welcome_tv')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    # 点击登录
    def accountLogin(self):
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'Account_resourceId', 'loginButton')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    # 点击切换帐号
    def switchAccount(self):
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'Account_resourceId', 'switchAccount')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    # 点击退出帐号
    def logOut(self):
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'Account_resourceId', 'logOut')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    # 确保处于未登录状态
    # （仅用于脚本调试，当前脚本暂无法满足if逻辑判断后执行不同操作，故暂用此方法满足确保个人中心处于未登录状态后便于执行其他操作）
    def ensureLoginOut(self):
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'Account_resourceId', 'logOut')
        element = pm().find_element_by_id(id=id)
        if element is None:  # 如果有登出按键则帐号已经登录
            return True
        else:
            return self.logOut()  # 退出登录
