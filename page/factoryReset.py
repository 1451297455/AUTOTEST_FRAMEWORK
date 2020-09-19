# -*- coding: utf-8 -*-
from UIconfig.Base import Base
from page.PublicMethod import PublicMethod as pm
import UIconfig.logger as loggers

logger = loggers.Logger()


class factoryReset(Base):
    # 点击User Manual，滑动查找
    # def gotoFactoryResetPage(self):
    #     pm().stopApp(conf.settingsPage.get('packageName'))  # kill settings 页面缓存
    #     pm().openApp(conf.settingsPage.get('packageName'))
    #     time.sleep(2)
    #     for i in range(5):
    #         elist = pm().find_element_by_id(self, id=conf.settingsPage.get('menuList'))
    #         Manual = pm().find_element_by_text(self, text=conf.factoryReset.get('factoryResetPage'))
    #         if Manual:
    #             return pm().click_by_element(self, Manual)
    #         time.sleep(1)
    #         pm().swipe_up_by_element(self, elist)
    #     return False

    def clickFactoryReset(self):
        FactoryReset = pm().find_element_by_id(id='com.saicmotor.settings:id/btn_reset_factory')
        return pm().click_by_element(FactoryReset)

    def clickSystemReset(self):
        SystemReset = pm().find_element_by_id(id='com.saicmotor.settings:id/btn_reset_system')
        return pm().click_by_element(SystemReset)

    def clickVehicleReset(self):
        VehicleReset = pm().find_element_by_id(id='com.saicmotor.settings:id/btn_reset_vehicle')
        return pm().click_by_element(VehicleReset)

    def clickDialogOK(self):
        Ok = pm().find_element_by_id(id='com.saicmotor.settings:id/dialog_btn_ok')
        return pm().click_by_element(Ok)

    def clickDialogCancel(self):
        Cancel = pm().find_element_by_id(id='com.saicmotor.settings:id/dialog_btn_cancel')
        return pm().click_by_element(Cancel)
