# -*- coding: utf-8 -*-
from UIconfig.Base import Base
from page.PublicMethod import PublicMethod as pm
from page.india_D90_homePage import india_D90_homePage as homePage
import time, os

os.path.abspath('.')


class india_D90_ACPage(Base):

    def clickPassengerTempPlusButton(self):
        """
        点击乘客座位温度+
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'ACPage', 'PassengerTempPlusId')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    def clickPassengerTempMinusButton(self):
        """
        点击乘客座位温度-
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'ACPage', 'PassengerTempMinusId')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    def clickDriverTempPlusButton(self):
        """
        点击主驾座位温度+
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'ACPage', 'DriverTempPlusId')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    def clickDriverTempMinusButton(self):
        """
        点击主驾座位温度-
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'ACPage', 'DriverTempMinusId')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    def clickAutoButton(self):
        """
        点击Auto按键
        :return: True，False
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'ACPage', 'AutoId')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    def clickACButton(self):
        """
        点击AC按键
        :return: True，False
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'ACPage', 'ACId')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    def clickFront_RearButton(self):
        """
        点击Front/Rear切换按键
        :return: True，False
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'ACPage', 'FrontRearId')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    def clickBlowPlusButton(self):
        """
        点击风量+
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'ACPage', 'BlowPlusId')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    def clickBlowMinusButton(self):
        """
        点击风量-
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'ACPage', 'BlowMinusId')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    def getBlowSpeedLevel(self):
        """
        获取风量值
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'ACPage', 'BlowSpeedId')
        element = pm().find_element_by_id(id=id)
        if element is not None:
            return pm().get_text(element)
        else:
            return None

    def clickFrontDeforst(self):
        """
        点击吹窗模式
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'ACPage', 'BlowSpeedId')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    def clickSyncButton(self):
        """
        点击主副驾温度同步按键
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'ACPage', 'SyncId')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    def clickSyncButton(self):
        """
        点击温度吹风模式按键
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'ACPage', 'CycleMode')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    def getPassengerTempText(self):
        """
        获取副驾温度值
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'ACPage', 'PassengerTempText')
        element = pm().find_element_by_id(id=id)
        if element is not None:
            return pm().get_text(element)
        else:
            return None

    def getDriverTempText(self):
        """
        获取主驾温度值
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'ACPage', 'DriverTempText')
        element = pm().find_element_by_id(id=id)
        if element is not None:
            return pm().get_text(element)
        else:
            return None

    def getOutsideTempText(self):
        """
        获取外界温度值
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'ACPage', 'OutSideTempText')
        element = pm().find_element_by_id(id=id)
        if element is not None:
            return pm().get_text(element)
        else:
            return None



