# -*- coding: utf-8 -*-
# AS23P setting页面方法
from UIconfig.Base import Base
from page.PublicMethod import PublicMethod as pm
import UIconfig.logger as loggers

logger = loggers.Logger()


class thailand_AS23P_settingPage(Base):

    # 点击Setting中的System items
    def clickSystemItems(self):
        # logger.info('clickSystemItems')
        text = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'System')
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_resourceId', 'MainlistId')
        element = pm().find_element_by_idAndText(id=id, text=text)
        return pm().click_by_element(element)

    # 点击Setting中reset_system
    def clickResetSystem(self):
        # logger.info('clickResetSystem')
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_resourceId', 'ResetSystem')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    # 点击Setting中vehicle_system
    def clickResetVehicle(self):
        # logger.info('clickResetVehicle')
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_resourceId', 'ResetVehicle')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    # 点击Setting中Cancel
    def clickSettingCancel(self):
        # logger.info('clickSettingCancel')
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_resourceId', 'Cancel')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    # 点击Setting中OK
    def clickSettingOK(self):
        # logger.info('clickSettingOK')
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_resourceId', 'OK')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    # 点击Setting中的Language
    def clickLanguageItems(self):
        # logger.info('clickLanguageItems')
        text = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'Language')
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_resourceId', 'MainlistId')
        element = pm().find_element_by_idAndText(id=id, text=text)
        return pm().click_by_element(element)

    # 点击Setting中的Sound
    def clickSoundItems(self):
        # logger.info('clickSoundItems')
        text = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'Sound')
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_resourceId', 'MainlistId')
        element = pm().find_element_by_idAndText(id=id, text=text)
        return pm().click_by_element(element)

    # 点击ToneField
    def clickToneField(self):
        # logger.info('clickToneField')
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_resourceId', 'ToneFieldId')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    # 点击ToneEffect
    def clickToneEffect(self):
        # logger.info('clickToneEffect')
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_resourceId', 'ToneEffectId')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    # 点击VolumeId
    def clickVolume(self):
        # logger.info('clickVolume')
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_resourceId', 'VolumeId')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    # 点击Setting中的blueTooth
    def clickblueToothItems(self):
        # logger.info('clickSoundItems')
        text = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'BlueTooth')
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_resourceId', 'MainlistId')
        element = pm().find_element_by_idAndText(id=id, text=text)
        return pm().click_by_element(element)

    # 点击Setting中的time
    def clickTimeItems(self):
        # logger.info('clickSoundItems')
        text = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'Time')
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_resourceId', 'MainlistId')
        element = pm().find_element_by_idAndText(id=id, text=text)
        return pm().click_by_element(element)

    # 点击Setting中的time format
    def clickSetTheTime(self):
        # logger.info('click Set the Time ')
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_resourceId', 'TimeFormat')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    # 时间制式设置返回按键
    def clickBacktoTimeSet(self):
        # logger.info('clickBackToTimeSet')
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_resourceId', 'Back')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    # 选择24小时制
    def click24HTimeFormat(self):
        # logger.info('click24HTimeFormat')
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_resourceId', '24H')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    # 选择12小时制
    def click12HTimeFormat(self):
        # logger.info('click12HTimeFormat')
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_resourceId', '12H')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    # 选择手动设置时区On（仅用于泰文模式下）
    def clickSwitchAutoOn(self):
        # logger.info('click12HTimeFormat')
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_resourceId', 'AutoText')
        element = pm().find_element_by_id(id=id)
        On = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'On')
        autoText = element.get_text()
        if autoText == On:  # 如果已经打开则返回
            # logger.info('already On')
            return True
        else:  # 如果未打开Auto按键 则点击打开
            # logger.info('click On')
            autoButton = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_resourceId', 'SwitchAutoButton')
            element = pm().find_element_by_id(id=autoButton)
            return pm().click_by_element(element)

    # 选择手动设置时区Off（仅用于泰文模式下）
    def clickSwitchAutoOff(self):
        # logger.info('click12HTimeFormat')
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_resourceId', 'AutoText')
        element = pm().find_element_by_id(id=id)
        Off = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'Off')
        autoText = element.get_text()
        if autoText == Off:  # 如果已经打开则返回
            # logger.info('already Off')
            return True
        else:  # 如果未打开Auto按键 则点击打开
            # logger.info('click Off')
            autoButton = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_resourceId', 'SwitchAutoButton')
            element = pm().find_element_by_id(id=autoButton)
            return pm().click_by_element(element)

    # 点击Setting中的Display
    def clickDisplay(self):
        # logger.info('clickDisplay')
        text = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'Display')
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_resourceId', 'MainlistId')
        element = pm().find_element_by_idAndText(id=id, text=text)
        return pm().click_by_element(element)

    # 点击Setting中的Update
    def clickUpdate(self):
        # logger.info('clickDisplay')
        text = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'Update')
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_resourceId', 'MainlistId')
        element = pm().find_element_by_idAndText(id=id, text=text)
        return pm().click_by_element(element)

    # 点击Setting中的Usb Stroage
    def clickUSBStorage(self):
        # logger.info('clickUSB_Storage')
        text = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'USBStorage')
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_resourceId', 'MainlistId')
        element = pm().find_element_by_idAndText(id=id, text=text)
        text2 = element.get_text()
        return pm().click_by_element(element)

    # 点击Setting中的VoiceAssistant(注：泰国AS23P 100%基线版本暂无VoiceAssistant的泰语翻译，该方法只能待提供翻译版本后使用)
    def clickVoiceAssistant(self):
        # logger.info('clickVoiceAssistant')
        text = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'VoiceAssistant')
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_resourceId', 'MainlistId')
        element = pm().find_element_by_idAndText(id=id, text=text)
        text2 = element.get_text()
        return pm().click_by_element(element)

    # 点击Setting中的UserManual
    def clickUserManual(self):
        # logger.info('clickVoiceAssistant')
        text = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'UserManual')
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_resourceId', 'MainlistId')
        element = pm().find_element_by_idAndText(id=id, text=text)
        text2 = element.get_text()
        return pm().click_by_element(element)

    # 用户手册设置返回按键
    def clickBacktoUserManual(self):
        # logger.info('clickBackToTimeSet')
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_resourceId', 'Back')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    # 点击Setting中的AboutMG
    def clickAboutMG(self):
        # logger.info('clickAboutMG')
        text = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'AboutMG')
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_resourceId', 'MainlistId')
        element = pm().find_element_by_idAndText(id=id, text=text)
        return pm().click_by_element(element)
