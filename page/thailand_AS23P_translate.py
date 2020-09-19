# -*- coding: utf-8 -*-
# AS23P 翻译功能
from UIconfig.Base import Base
from page.PublicMethod import PublicMethod as pm
import UIconfig.logger as loggers

logger = loggers.Logger()


class thailand_AS23P_translate(Base):

    # 首页天气卡片泰语名称
    def checkHomePageWeather_txt(self):
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'homePage_txt', 'Weather')
        return pm().find_element_by_text(name).exists()

    # 首页EV电量卡片泰语名称
    def checkHomePageBattery_txt(self):
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'homePage_txt', 'Battery')
        return pm().find_element_by_text(name).exists()

    # 首页音乐卡片泰语名称
    def checkHomePageMusic_txt(self):
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'homePage_txt', 'Music')
        return pm().find_element_by_text(name).exists()

    # Radio页面all翻译检测
    def checkRadioPageAll_txt(self):
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'radioPage_txt', 'ALL')
        return pm().find_element_by_text(name).exists()

    # Radio页面all列表翻译检测
    def checkRadioPageAll_list_txt(self):
        ##logger.info('all list txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'radioPage_txt', 'ALL')
        return pm().find_element_by_text(name).exists()

    # Radio页面Favorite翻译检测
    def checkRadioPageFavorite_txt(self):
        ##logger.info('Favorite txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'radioPage_txt', 'Favorite')
        return pm().find_element_by_text(name).exists()

    # Radio页面Favorite列表翻译检测
    def checkRadioPageFavorite_list_txt(self):
        ##logger.info('Favorite list txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'radioPage_txt', 'Favorite')
        return pm().find_element_by_text(name).exists()

    # Radio页面No_Frequency翻译检测
    def checkRadioPageNo_Frequency_txt(self):
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'radioPage_txt', 'No_Frequency')
        return pm().find_element_by_text(name).exists()

    # Radio页面搜台话术翻译检测
    def checkRadioScanning_txt(self):
        ##logger.info('Scanning txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'radioPage_txt', 'Radio_Scanning')
        return pm().find_element_by_text(name).exists()

    # Radio页面搜台Cancel话术翻译检测
    def checkRadioCancel_txt(self):
        ##logger.info('Cancel txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'radioPage_txt', 'Cancel')
        return pm().find_element_by_text(name).exists()

    # BTPhone KeyPad页面Title话术检测
    def checkBTPhoneKeyPadTitle_txt(self):
        # logger.info('BTPhoneKeyPadTitle txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'btPhone_txt', 'keyPad')
        return pm().find_element_by_text(name).exists()

    # BTPhone KeyPad页面内容话术检测
    def checkBTPhoneKeyPadPage_txt(self):
        # logger.info('BTPhoneKeyPadPage txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'btPhone_txt', 'enter_your_number')
        return pm().find_element_by_text(name).exists()

    # BTPhone Recents页面Title话术检测
    def checkBTPhoneRecentsTitle_txt(self):
        # logger.info('BTPhoneRecentsTitle txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'btPhone_txt', 'recents')
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'BT_Phone_resourceId', 'RECENTS')
        element = pm().find_element_by_id(id=id)  # 通过resoucrdId定位名称再与翻译做比对
        resourceName = element.get_text()
        if name == resourceName:
            return True
        else:
            return pm().find_element_by_text(name).exists()

    # BTPhone Recents页面Page话术检测
    def checkBTPhoneRecentsPage_txt(self):
        ##logger.info('BTPhoneRecentsPage txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'btPhone_txt', 'recents')
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'BT_Phone_resourceId', 'RECENTS_Title')
        element = pm().find_element_by_id(id=id)  # 通过resoucrdId定位名称再与翻译做比对
        resourceName = element.get_text()
        if name == resourceName:
            return True
        else:
            return pm().find_element_by_text(name).exists()

    # BTPhone Recents页面内容话术1检测
    def checkBTPhoneRecentsStr1_txt(self):
        ##logger.info('BTPhoneRecentsStr1 txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'btPhone_txt', 'recents_str1')
        return pm().find_element_by_text(name).exists()

    # BTPhone Recents页面内容话术2检测
    def checkBTPhoneRecentsStr2_txt(self):
        ##logger.info('BTPhoneRecentsStr2 txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'btPhone_txt', 'recents_str2')
        return pm().find_element_by_text(name).exists()

    # BTPhone Contacts页面Title话术检测
    def checkBTPhoneContactsTitle_txt(self):
        ##logger.info('BTPhoneContactsTitle txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'btPhone_txt', 'contacts')
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'BT_Phone_resourceId', 'CONTACTS')
        element = pm().find_element_by_id(id=id)  # 通过resoucrdId定位名称再与翻译做比对
        resourceName = element.get_text()
        if name == resourceName:
            return True
        else:
            return pm().find_element_by_text(name).exists()

    # BTPhone Contacts页面Page话术检测
    def checkBTPhoneContactsPage_txt(self):
        ##logger.info('BTPhoneContactsPage txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'btPhone_txt', 'contacts')
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'BT_Phone_resourceId', 'CONTACTS_Title')
        element = pm().find_element_by_id(id=id)  # 通过resoucrdId定位名称再与翻译做比对
        resourceName = element.get_text()
        if name == resourceName:
            return True
        else:
            return pm().find_element_by_text(name).exists()

    # BTPhone Contacts页面内容话术1检测
    def checkBTPhoneContactsStr1_txt(self):
        # logger.info('BTPhoneContactsStr1 txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'btPhone_txt', 'contacts_str1')
        return pm().find_element_by_text(name).exists()

    # BTPhone Contacts页面内容话术2检测
    def checkBTPhoneContactsStr2_txt(self):
        # logger.info('BTPhoneContactsStr2 txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'btPhone_txt', 'contacts_str2')
        return pm().find_element_by_text(name).exists()

    # BTPhone Recents页面connect话术检测
    def checkBTPhoneConnectButton_txt(self):
        # logger.info('BTPhoneConnectButton txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'btPhone_txt', 'connect')
        return pm().find_element_by_text(name).exists()

    # BTPhone 蓝牙已连接话术（该方法用于蓝牙已连接但通讯录未同步状态）
    def checkBTPhone_BluetoothConnexted_txt(self):
        # logger.info('BTPhone_BluetoothConnexted txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'btPhone_txt', 'bluetooth_connected')
        return pm().find_element_by_text(name).exists()

    # BTPhone 允许同步通讯录话术（该方法用于蓝牙已连接但通讯录未同步状态）
    def checkBTPhone_AllowAddressBookStr_txt(self):
        # logger.info('BTPhone_BluetoothConnexted txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'btPhone_txt', 'Allow_address_book_str')
        return pm().find_element_by_text(name).exists()

    # BTPhone 同步按键话术
    def checkSynchronization_txt(self):
        # logger.info('Synchronization txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'btPhone_txt', 'synchronization')
        return pm().find_element_by_text(name).exists()

    # lifeStyle页面NEWS话术
    def checkNews_txt(self):
        # logger.info('News txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'lifeStyle_txt', 'News')
        return pm().find_element_by_text(name).exists()

    # lifeStyle页面Lottery话术
    def checkLottery_txt(self):
        # logger.info('Lottery txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'lifeStyle_txt', 'Lottery')
        # logger.info("Lottery : " + name)
        return pm().find_element_by_text(name).exists()

    # lifeStyle页面Sports话术
    def checkSports_txt(self):
        # logger.info('Sports txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'lifeStyle_txt', 'Sports')
        return pm().find_element_by_text(name).exists()

    # lifeStyle页面Travel话术
    def checkTravel_txt(self):
        ##logger.info('Travel txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'lifeStyle_txt', 'Travel')
        return pm().find_element_by_text(name).exists()

    # lifeStyle页面Auto话术
    def checkAuto_txt(self):
        # logger.info('Auto txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'lifeStyle_txt', 'Auto')
        return pm().find_element_by_text(name).exists()

    # lifeStyle页面Horoscope话术
    def checkHoroscope_txt(self):
        # logger.info('Horoscope txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'lifeStyle_txt', 'Horoscope')
        return pm().find_element_by_text(name).exists()

    # lifeStyle页面Subscribed话术
    def checkSubscribe_txt(self):
        # logger.info('Subscribe txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'lifeStyle_txt', 'Subscribe')
        return pm().find_element_by_text(name).exists()

    # lifeStyle页面Subscribed话术
    def checkNotSubscribe_txt(self):
        # logger.info('Not_Subscribe txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'lifeStyle_txt', 'Not_Subscribe')
        return pm().find_element_by_text(name).exists()

    # lifeStyle页面Lottery_Notification话术
    def checkLotteryNotification_txt(self):
        # logger.info('Lottery_Notification txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'lifeStyle_txt', 'Lottery_Notification')
        return pm().find_element_by_text(name).exists()

    # lifeStyle页面Subscribed话术
    def checkEdit_txt(self):
        # logger.info('Edit txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'lifeStyle_txt', 'Edit')
        return pm().find_element_by_text(name).exists()

    # call centre页面Cancel话术
    def checkCallCentreCancel(self):
        # logger.info('CallCentreCancel txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'CallCentre_txt', 'Cancel')
        return pm().find_element_by_text(name).exists()

    # call centre页面Call话术
    def checkCallCentreCall(self):
        # logger.info('CallCentreCall txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'CallCentre_txt', 'Call')
        return pm().find_element_by_text(name).exists()

    # CarPhone页面的KeyPad标题翻译
    def checkCarPhoneKeyPadTitle_txt(self):
        # logger.info('Carphone keypad txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'CallCentre_txt', 'keyPad')
        return pm().find_element_by_text(name).exists()

    # CarPhone KeyPad页面内容话术检测
    def checkCarPhoneKeyPadPage_txt(self):
        # logger.info('BTPhoneKeyPadPage txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'CallCentre_txt', 'enter_your_number')
        return pm().find_element_by_text(name).exists()

    # CarPhone Recents页面Title话术检测
    def checkCarPhoneRecentsTitle_txt(self):
        # logger.info('BTPhoneRecentsTitle txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'CarPhone_txt', 'recents_title')
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'CarPhone_resourcedId', 'RECENTS')
        element = pm().find_element_by_id(id=id)  # 通过resoucrdId定位名称再与翻译做比对
        resourceName = element.get_text()
        if name == resourceName:
            return True
        else:
            return pm().find_element_by_text(name).exists()

    # CarPhone Recents页面Page话术检测
    def checkCarPhoneRecentsPage_txt(self):
        # logger.info('BTPhoneRecentsPage txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'CarPhone_txt', 'recentsPage')
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'CarPhone_resourcedId', 'RECENTS_Title')
        element = pm().find_element_by_id(id=id)  # 通过resoucrdId定位名称再与翻译做比对
        resourceName = element.get_text()
        if name == resourceName:
            return True
        else:
            return pm().find_element_by_text(name).exists()

    # CarPhone Contacts页面Title话术检测
    def checkCarPhoneContactsTitle_txt(self):
        # logger.info('BTPhoneContactsTitle txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'CarPhone_txt', 'contacts_title')
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'CarPhone_resourcedId', 'CONTACTS')
        element = pm().find_element_by_id(id=id)  # 通过resoucrdId定位名称再与翻译做比对
        resourceName = element.get_text()
        if name == resourceName:
            return True
        else:
            return pm().find_element_by_text(name).exists()

    # CarPhone Recents页面Page话术检测
    def checkCarPhoneContactsPage_txt(self):
        # logger.info('BTPhoneRecentsPage txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'CarPhone_txt', 'contactsPage')
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'CarPhone_resourcedId', 'CONTACTS_Title')
        element = pm().find_element_by_id(id=id)  # 通过resoucrdId定位名称再与翻译做比对
        resourceName = element.get_text()
        if name == resourceName:
            return True
        else:
            return pm().find_element_by_text(name).exists()

    # Carphone MobileContacts话术检测
    def checkCarPhoneMobileContacts_txt(self):
        # logger.info('MobileContacts txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'CarPhone_txt', 'Mobile_Contacts')
        return pm().find_element_by_text(name).exists()

    # Carphone LocalContacts话术检测
    def checkCarPhoneLocalContacts_txt(self):
        # logger.info('LocalContacts txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'CarPhone_txt', 'Local_Contacts')
        return pm().find_element_by_text(name).exists()

    # Inbox TravelPlan翻译
    def checkInboxTravelPlan_txt(self):
        # logger.info('TravelPlan txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Inbox_txt', 'Travel_Plan')
        return pm().find_element_by_text(name).exists()

    # Inbox TravelPlan翻译
    def checkInboxMessage_txt(self):
        # logger.info('Message txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Inbox_txt', 'Message')
        return pm().find_element_by_text(name).exists()

    # Inbox TravelPlan翻译
    def checkInboxMG_News_txt(self):
        # logger.info('MG_News txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Inbox_txt', 'MG_News')
        return pm().find_element_by_text(name).exists()

    # Folder video翻译
    def checkVideo_txt(self):
        # logger.info('Video_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Folder_txt', 'VIDEOS')
        return pm().find_element_by_text(name).exists()

    # Folder document翻译
    def checkDocument_txt(self):
        # logger.info('Document_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Folder_txt', 'DOCUMENTS')
        return pm().find_element_by_text(name).exists()

    # Folder picture翻译
    def checkPicture_txt(self):
        # logger.info('Picture_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Folder_txt', 'PICTURES')
        return pm().find_element_by_text(name).exists()

    # Folder USB_is_not_connected翻译
    def checkNotUSBConnect_txt(self):
        # logger.info('USB_is_not_connected_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Folder_txt', 'USB_is_not_connected')
        return pm().find_element_by_text(name).exists()

    # Passion Service GoToDealer翻译
    def checkGoToDealer_txt(self):
        # logger.info('Go_To_Dealer_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'PassionService_txt', 'Go_To_Dealer')
        return pm().find_element_by_text(name).exists()

    # Passion Service My_Reservation翻译
    def checkMyReservation_txt(self):
        # logger.info('My_Reservation_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'PassionService_txt', 'My_Reservation')
        return pm().find_element_by_text(name).exists()

    # Passion Service Maintenance_Record翻译
    def checkMaintenanceRecord_txt(self):
        # logger.info('Maintenance_Record_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'PassionService_txt', 'Maintenance_Record')
        return pm().find_element_by_text(name).exists()

    # Passion Service Maintenance_Record翻译
    def checkMobileService_txt(self):
        # logger.info('MobileService_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'PassionService_txt', 'Mobile_Service')
        return pm().find_element_by_text(name).exists()

    # Passion Service Mobile_Service_str 翻译
    def checkMobileServiceStr_txt(self):
        # logger.info('Mobile_Service_Str_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'PassionService_txt', 'Mobile_Service_Str')
        return pm().find_element_by_text(name).exists()

    # Passion Service Booking_Time 翻译
    def checkBookingTime_txt(self):
        # logger.info('Mobile_Service_Str_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'PassionService_txt', 'Booking_Time')
        return pm().find_element_by_text(name).exists()

    # Passion Service Booking_Time_Str 翻译
    def checkBookingTimeStr_txt(self):
        # logger.info('Booking_Time_Str_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'PassionService_txt', 'Booking_Time_Str')
        return pm().find_element_by_text(name).exists()

    # Passion Service Go to dealer MG_DEALER键 翻译
    def checkMGDEALER_txt(self):
        # logger.info('MG_DEALER_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'PassionService_txt', 'MG_DEALER')
        return pm().find_element_by_text(name).exists()

    # Passion Service Go to dealer MOBILE_SERVICE键 翻译
    def checkMobileServiceInGotoDealerPage_txt(self):
        # logger.info('MOBILE_SERVICE_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'PassionService_txt', 'MOBILE_SERVICE')
        return pm().find_element_by_text(name).exists()

    # Battery卡片名称翻译
    def checkBattery_txt(self):
        # logger.info('Battery_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Battery_txt', 'BATTERY')
        return pm().find_element_by_text(name).exists()

    # Battery Information翻译
    def checkBatteryInformation_txt(self):
        # logger.info('Battery Information_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Battery_txt', 'Information')
        return pm().find_element_by_text(name).exists()

    # Battery RemainingTime翻译
    def checkBatteryRemainingTime_txt(self):
        # logger.info('Battery Remaining_Time_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Battery_txt', 'Remaining_Time')
        return pm().find_element_by_text(name).exists()

    # Battery Total_Range翻译
    def checkTotalRange_txt(self):
        # logger.info('Battery Total_Range_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Battery_txt', 'Total_Range')
        return pm().find_element_by_text(name).exists()

    # Battery Battery_Range翻译
    def checkBatteryRange_txt(self):
        # logger.info('Battery Battery_Range_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Battery_txt', 'Battery_Range')
        return pm().find_element_by_text(name).exists()

    # Battery Current翻译
    def checkBatteryCurrent_txt(self):
        # logger.info('Battery Current_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Battery_txt', 'Current')
        return pm().find_element_by_text(name).exists()

    # Battery Voltage翻译
    def checkBatteryVoltage_txt(self):
        # logger.info('Battery Voltage_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Battery_txt', 'Voltage')
        return pm().find_element_by_text(name).exists()

    # Battery ChargingType翻译
    def checkBatteryChargingType_txt(self):
        # logger.info('Battery Charging_Type_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Battery_txt', 'Charging_Type')
        return pm().find_element_by_text(name).exists()

    # Battery Search_For_Charging_Station翻译
    def checkBatterySearchForChargingStation_txt(self):
        # logger.info('Battery Search_For_Charging_Station_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Battery_txt', 'Search_For_Charging_Station')
        return pm().find_element_by_text(name).exists()

    # Battery Uncharged翻译
    def checkBatteryUncharged_txt(self):
        # logger.info('Battery Uncharged_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Battery_txt', 'Uncharged')
        return pm().find_element_by_text(name).exists()

    # AC Passenger翻译
    def checkACPassenger_txt(self):
        # logger.info('AC_Passenger_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'AC_txt', 'Passenger')
        return pm().find_element_by_text(name).exists()

    # AC Driver翻译
    def checkACDriver_txt(self):
        # logger.info('AC_Driver_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'AC_txt', 'Driver')
        return pm().find_element_by_text(name).exists()

    # AC OutSideTemp翻译
    def checkACOutSideTemp_txt(self):
        # logger.info('AC_OutSideTemp_txt')
        id = pm().readConfigByModuleAndKey('thailand_AS23P', 'AC_resourceId', 'outSide_temp')
        element = pm().find_element_by_id(id=id)
        outSideTempTxt = element.get_text()
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'AC_txt', 'OUTSIDE_TEMP')
        if name in outSideTempTxt:  # 由于抓取的外界温度喊数字部分故只比较话术
            return True
        else:
            return False

    # Setting System翻译
    def checkSystem_txt(self):
        # logger.info('System_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'System')
        return pm().find_element_by_text(name).exists()

    # Setting System Version_Information翻译
    def checkVersionInformation_txt(self):
        # logger.info('Version_Information_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'Version_Information')
        return pm().find_element_by_text(name).exists()

    # Setting System System_Reset翻译
    def checkSystemReset_txt(self):
        # logger.info('System_Reset_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'System_Reset')
        return pm().find_element_by_text(name).exists()

    # Setting System Vehicle_Reset翻译
    def checkVehicleReset_txt(self):
        # logger.info('Vehicle_Reset_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'Vehicle_Reset')
        return pm().find_element_by_text(name).exists()

    # Setting System 确认Reset System对话框话术
    def checkSystemResetStr_txt(self):
        # logger.info('reset_system_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'reset_system')
        return pm().find_element_by_text(name).exists()

    # Setting System 确认Reset Vehicle对话框话术
    def checkVehicleResetStr_txt(self):
        # logger.info('reset_vehicle_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'reset_vehicle')
        return pm().find_element_by_text(name).exists()

    # Setting System Reset按键翻译
    def checkResetButton_txt(self):
        # logger.info('ResetButton_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'Reset')
        return pm().find_element_by_text(name).exists()

    # Setting System Cancel按键翻译
    def checkSettingCancel_txt(self):
        # logger.info('ResetButton_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'Cancel')
        return pm().find_element_by_text(name).exists()

    # Setting System OK按键翻译
    def checkSettingOK_txt(self):
        # logger.info('ResetButton_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'OK')
        return pm().find_element_by_text(name).exists()

    # Setting Language翻译
    def checkSettingLanguage_txt(self):
        # logger.info('Language_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'Language')
        return pm().find_element_by_text(name).exists()

    # Setting Thai翻译
    def checkSettingThai_txt(self):
        # logger.info('Thai_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'Thai')
        return pm().find_element_by_text(name).exists()

    # Setting Select Language翻译
    def checkSelectLanguage_txt(self):
        # logger.info('Thai_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'Select_Language')
        return pm().find_element_by_text(name).exists()

    # Setting Sound 翻译
    def checkSound_txt(self):
        # logger.info('Sound_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'Sound')
        return pm().find_element_by_text(name).exists()

    # Setting Tone_Effect 翻译
    def checkToneEffect_txt(self):
        # logger.info('Tone_Effect_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'Tone_Effect')
        return pm().find_element_by_text(name).exists()

    # Setting Tone_Effect Reset 翻译
    def checkToneEffectReset_txt(self):
        # logger.info('Tone_Effect_Reset_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'Reset')
        return pm().find_element_by_text(name).exists()

    # Setting Tone_Field 翻译
    def checkToneField_txt(self):
        # logger.info('Tone_Field_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'Tone_Field')
        return pm().find_element_by_text(name).exists()

    # Setting Tone_Field Classic 翻译
    def checkClassic_txt(self):
        # logger.info('Classic_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'Classic')
        return pm().find_element_by_text(name).exists()

    # Setting Tone_Field Pop 翻译
    def checkPop_txt(self):
        # logger.info('Pop_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'Pop')
        return pm().find_element_by_text(name).exists()

    # Setting Tone_Field Vocal 翻译
    def checkVocal_txt(self):
        # logger.info('Vocal_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'Vocal')
        return pm().find_element_by_text(name).exists()

    # Setting Tone_Field Jazz 翻译
    def checkJazz_txt(self):
        # logger.info('Jazz_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'Jazz')
        return pm().find_element_by_text(name).exists()

    # Setting Tone_Field Rock 翻译
    def checkRock_txt(self):
        # logger.info('Rock_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'Rock')
        return pm().find_element_by_text(name).exists()

    # Setting Tone_Field Vocal 翻译
    def checkManual_txt(self):
        # logger.info('Manual_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'Manual')
        return pm().find_element_by_text(name).exists()

    # Setting Tone_Field Reset 翻译
    def checkToneFieldReset_txt(self):
        # logger.info('Manual_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'Reset')
        return pm().find_element_by_text(name).exists()

    # Setting Volume 翻译
    def checkVolume_txt(self):
        # logger.info('Volume_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'Volume')
        return pm().find_element_by_text(name).exists()

    # Setting Loudness 翻译
    def checkLoudness(self):
        # logger.info('Loudness_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'Loudness')
        return pm().find_element_by_text(name).exists()

    # Setting SystemNotification 翻译
    def checkSystemNotification(self):
        # logger.info('SystemNotification_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'SystemNotification')
        return pm().find_element_by_text(name).exists()

    # Setting SystemBeeps 翻译
    def checkSystemBeeps(self):
        # logger.info('SystemBeeps_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'SystemBeeps')
        return pm().find_element_by_text(name).exists()

    # Setting High 翻译
    def checkHigh(self):
        # logger.info('SystemHigh_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'High')
        return pm().find_element_by_text(name).exists()

    # Setting High 翻译
    def checkhLow(self):
        # logger.info('Low_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'Low')
        return pm().find_element_by_text(name).exists()

    # Setting Off 翻译
    def checkOff(self):
        # logger.info('Off_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'Off')
        return pm().find_element_by_text(name).exists()

    # Setting BlueTooth 翻译
    def checkBlueTooth(self):
        # logger.info('BlueTooth_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'BlueTooth')
        return pm().find_element_by_text(name).exists()

    # Setting BTName 翻译
    def checkBTName(self):
        # logger.info('BTName_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'BTName')
        return pm().find_element_by_text(name).exists()

    # Setting Time 翻译
    def checkTime(self):
        # logger.info('Time_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'Time')
        return pm().find_element_by_text(name).exists()

    # Setting SetTheTime 翻译
    def checkSetTheTime(self):
        # logger.info('SetTheTime_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'SetTheTime')
        return pm().find_element_by_text(name).exists()

    # Setting 12HourTime 翻译
    def check12HourTime(self):
        # logger.info('Set12HourTime_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', '12HourTime')
        return pm().find_element_by_text(name).exists()

    # Setting 24HourTime 翻译
    def check24HourTime(self):
        # logger.info('Set24HourTime_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', '24HourTime')
        return pm().find_element_by_text(name).exists()

    # Setting AutomaicTimeZone 翻译
    def checkAutomaicTimeZone(self):
        # logger.info('SetAutomaicTimeZone_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'AutomaicTimeZone')
        return pm().find_element_by_text(name).exists()

    # Setting TimeZone 翻译
    def checkTimeZone(self):
        # logger.info('SetTimeZone_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'TimeZone')
        return pm().find_element_by_text(name).exists()

    # Setting SetDate 翻译
    def checkSetDate(self):
        # logger.info('SetSetDate_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'SetDate')
        return pm().find_element_by_text(name).exists()

    # Setting SetTime 翻译
    def checkSetTime(self):
        # logger.info('SetSetTime_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'SetTime')
        return pm().find_element_by_text(name).exists()

    # Setting Display 翻译
    def checkDisplay(self):
        # logger.info('SetDisplay_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'Display')
        return pm().find_element_by_text(name).exists()

    # Setting BrightnessMode 翻译
    def checkBrightnessMode(self):
        # logger.info('SetBrightnessMode_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'BrightnessMode')
        return pm().find_element_by_text(name).exists()

    # Setting Day 翻译
    def checkDay(self):
        # logger.info('SetDay_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'Day')
        return pm().find_element_by_text(name).exists()

    # Setting Night 翻译
    def checkNight(self):
        # logger.info('SetNight_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'Night')
        return pm().find_element_by_text(name).exists()

    # Setting Auto 翻译
    def checkAuto(self):
        # logger.info('SetAuto_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'Auto')
        return pm().find_element_by_text(name).exists()

    # Setting Brightness 翻译
    def checkBrightness(self):
        # logger.info('SetBrightness_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'Brightness')
        return pm().find_element_by_text(name).exists()

    # Setting Update 翻译
    def checkUpdate(self):
        # logger.info('Update_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'Update')
        return pm().find_element_by_text(name).exists()

    # Setting Updatetext 翻译
    def checkUpdateText(self):
        # logger.info('Updatetext_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'UpdateText')
        return pm().find_element_by_text(name).exists()

    # Setting DetectNewVersions 翻译
    def checkDetectNewVersions(self):
        # logger.info('DetectNewVersions_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'DetectNewVersions')
        return pm().find_element_by_text(name).exists()

    # Setting 右侧栏UsbStorage 翻译
    def checkUsbStorage(self):
        # logger.info('Updatetext_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'USBStorage')
        return pm().find_element_by_text(name).exists()

    # Setting HelloMG 翻译
    def checkHelloMG(self):
        # logger.info('HelloMG_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'HelloMG')
        return pm().find_element_by_text(name).exists()

    # Setting WelcomeMessage 翻译
    def checkWelcomeMessage(self):
        # logger.info('HelloMG_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'WelcomeMessage')
        return pm().find_element_by_text(name).exists()

    # Setting Mode 翻译
    def checkMode(self):
        # logger.info('Mode_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'Mode')
        return pm().find_element_by_text(name).exists()

    # Setting Random 翻译
    def checkRandom(self):
        # logger.info('Random_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'Random')
        return pm().find_element_by_text(name).exists()

    # Setting Custom 翻译
    def checkCustom(self):
        # logger.info('Custom_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'Custom')
        return pm().find_element_by_text(name).exists()

    # Setting TirePressureMonitoringAlarm 翻译
    def checkTirePressureMonitoringAlarm(self):
        # logger.info('TirePressureMonitoringAlarm_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'TirePressureMonitoringAlarm')
        return pm().find_element_by_text(name).exists()

    # Setting LowFuelAlert 翻译
    def checkLowFuelAlert(self):
        # logger.info('LowFuelAlert_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'LowFuelAlert')
        return pm().find_element_by_text(name).exists()

    # Setting OneshotCommand 翻译
    def checkOneshotCommand(self):
        # logger.info('OneshotCommand_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'OneshotCommand')
        return pm().find_element_by_text(name).exists()

    # Setting UserManual 翻译
    def checkUserManual(self):
        # logger.info('UserManual_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'UserManual')
        return pm().find_element_by_text(name).exists()

    # Setting AboutMG 翻译
    def checkAboutMG(self):
        # logger.info('UserManual_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'AboutMG')
        return pm().find_element_by_text(name).exists()

    # Setting EndUserLicenseAgreement 翻译
    def checkEndUserLicenseAgreement(self):
        # logger.info('EndUserLicenseAgreement_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'EndUserLicenseAgreement')
        return pm().find_element_by_text(name).exists()

    # Setting PrivacyPolicy 翻译
    def checkPrivacyPolicy(self):
        # logger.info('PrivacyPolicy_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'PrivacyPolicy')
        return pm().find_element_by_text(name).exists()

    # Setting ServiceTerms 翻译
    def checkServiceTerms(self):
        # logger.info('ServiceTerms_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'ServiceTerms')
        return pm().find_element_by_text(name).exists()

    # Setting 右侧栏UsbStorage 翻译
    def checkUsbStorage(self):
        # logger.info('Updatetext_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'USBStorage')
        return pm().find_element_by_text(name).exists()

    # Setting USBStorageTitle 翻译
    def checkUSBStorageTitle(self):
        # logger.info('USBStorageTitle_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'USBStorageTitle')
        return pm().find_element_by_text(name).exists()

    # Setting USBIsNotConnected 翻译
    def checkUSBIsNotConnected(self):
        # logger.info('USBIsNotConnected_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'Setting_txt', 'USBIsNotConnected')
        return pm().find_element_by_text(name).exists()

    # Account Change To Account Login 翻译
    def checkChangeToAccountLogin(self):
        # logger.info('AccountLogin_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'account_txt', 'AccountLogin')
        return pm().find_element_by_text(name).exists()

    # Account Change To Scan Login 翻译
    def checkChangeToScanLogin(self):
        # logger.info('ScanLogin_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'account_txt', 'ScanLogin')
        return pm().find_element_by_text(name).exists()

    # Account QRCode_txt 翻译
    def checkQRCode_txt(self):
        # logger.info('QRCode_txt')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'account_txt', 'QRCode_txt')
        # logger.info('name: ' + name)
        return pm().find_element_by_text(name).exists()

    # Account UserName 翻译
    def checkUserName(self):
        # logger.info('Username')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'account_txt', 'Username')
        return pm().find_element_by_text(name).exists()

    # Account Password 翻译
    def checkPassword(self):
        # logger.info('Password')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'account_txt', 'Password')
        return pm().find_element_by_text(name).exists()

    # Account Login 翻译
    def checkLogin(self):
        # logger.info('Password')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'account_txt', 'Login')
        return pm().find_element_by_text(name).exists()

    # Account StartYourJourney
    def checkStartYourJourney(self):
        # logger.info('StartYourJourney')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'account_txt', 'StartYourJourney')
        return pm().find_element_by_text(name).exists()

    # Account Brand
    def checkBrand(self):
        # logger.info('Brand')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'account_txt', 'Brand')
        return pm().find_element_by_text(name).exists()

    # Account Model
    def checkModel(self):
        # logger.info('checkModel')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'account_txt', 'Model')
        return pm().find_element_by_text(name).exists()

    # Account Color
    def checkColor(self):
        # logger.info('checkColor')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'account_txt', 'Color')
        return pm().find_element_by_text(name).exists()

    # Account VIN
    def checkVin(self):
        # logger.info('checkVin')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'account_txt', 'VIN')
        return pm().find_element_by_text(name).exists()

    # Account EmergencyContactPerson
    def checkEmergencyContactPerson(self):
        # logger.info('checkEmergencyContactPerson')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'account_txt', 'EmergencyContactPerson')
        return pm().find_element_by_text(name).exists()

    # Account EmergencyContactPerson2
    def checkEmergencyContactPerson2(self):
        # logger.info('checkEmergencyContactPerson2')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'account_txt', 'EmergencyContactPerson2')
        return pm().find_element_by_text(name).exists()

    # Account LogOut
    def checkLogOut(self):
        # logger.info('LogOut')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'account_txt', 'LogOut')
        return pm().find_element_by_text(name).exists()

    # Account SwitchAccount
    def checkSwitchAccount(self):
        # logger.info('SwitchAccount')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'account_txt', 'SwitchAccount')
        return pm().find_element_by_text(name).exists()

    # Account VehicleName
    def checkVehicleName(self):
        # logger.info('SwitchAccount')
        name = pm().readConfigByModuleAndKey('thailand_AS23P', 'account_txt', 'VehicleName')
        return pm().find_element_by_text(name).exists()


if __name__ == '__main__':
    pass
