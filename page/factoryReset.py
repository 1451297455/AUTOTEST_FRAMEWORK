# -*- coding: utf-8 -*-
from page.BasePage import BasePage
from page.publicMethod import publicMethod as pm
import time
from config import india_D90_propertiseConfig as conf


class factoryReset(BasePage):

    # 点击User Manual，滑动查找
    def clickFactoryReset(self):
        pm.stopApp(conf.userManualPage.get('packageName'))
        pm.openApp(conf.userManualPage.get('packageName'))
        time.sleep(2)
        for i in range(5):
            elist = pm.find_element_by_id(self, id=conf.userManualPage.get('menuList'))
            Manual = pm.find_element_by_text(self, text=conf.userManualPage.get('titleText'))
            if Manual:
                return pm.click_by_element(self, Manual)
            time.sleep(1)
            pm.swipe_up_by_element(self, elist)
        return False

    def clickFactoryReset(self):
        FactoryReset = pm.find_element_by_Xpath(self, Xpath=conf.factoryReset.get('FactoryReset'))
        return pm.click_by_element(self, FactoryReset)

    def clickSystemReset(self):
        SystemReset = pm.find_element_by_Xpath(self, Xpath=conf.factoryReset.get('SystemReset'))
        return pm.click_by_element(self, SystemReset)

    def clickVehicleReset(self):
        VehicleReset = pm.find_element_by_Xpath(self, Xpath=conf.factoryReset.get('VehicleReset'))
        return pm.click_by_element(self, VehicleReset)

    def clickDialogOK(self):
        Ok = pm.find_element_by_id(self, id='com.saicmotor.settings:id/dialog_btn_ok')
        return pm.click_by_element(self, Ok)

    def clickDialogCancel(self):
        Cancel = pm.find_element_by_id(self, id='com.saicmotor.settings:id/dialog_btn_cancel')
        return pm.click_by_element(self, Cancel)
