# -*- coding: utf-8 -*-
# 印度D90天气
from page.PublicMethod import PublicMethod as pm
from page.australia_AS23_homePage import australia_AS23_homePage as homePage
from UIconfig.Base import Base
import datetime, time
import os

os.path.abspath('.')


class australia_AS23_weatherPage(Base):

    def clickRefresh(self):
        """
        点击刷新天气页面
        :return: True点击成功，False点击失败
        """
        element = pm().find_element_by_id(
            id=pm().readConfigByModuleAndKey('australia_AS23', 'WeatherPage', 'refresh'))
        return pm().click_by_element(element=element)

    def clickWeatherSearch(self):
        """
        点击搜索天气页面
        :return: True点击成功，False点击失败
        """
        element = pm().find_element_by_id(
            id=pm().readConfigByModuleAndKey('australia_AS23', 'WeatherPage', 'Search'))
        return pm().click_by_element(element=element)

    def clickPositionSearch(self):
        """
        点击搜索页面搜索按钮
        :return: True点击成功，False点击失败
        """
        element = pm().find_element_by_id(id=pm().readConfigByModuleAndKey('australia_AS23', 'WeatherPage',
                                                                           'SearchButton'))
        result = pm().click_by_element(element=element)
        return result

    def clickSetting(self):
        """
        点击天气设置页面
        :return:  True点击成功，False点击失败
        """
        element = pm().find_element_by_id(
            id=pm().readConfigByModuleAndKey('australia_AS23', 'WeatherPage', 'Setting'))
        return pm().click_by_element(element=element)

    def swipeToSettingBeginning(self):
        """
        滑动至Setting页面顶部
        """
        pm().swipe_to_beginning()

    def swipeToSettingEnding(self):
        """
        滑动至Setting页面顶部
        """
        pm().swipe_to_end()

    def clickLocalPosition(self):
        """
        点击获取当前地点天气(Weather搜索页面定位车机位置图标)
        :return:
        """
        element = pm().find_element_by_id(id=pm().readConfigByModuleAndKey('australia_AS23', 'WeatherPage',
                                                                           'SerachLocalPosition'))
        return pm().click_by_element(element=element)

    def clickBackButton(self):
        """
        回到上一层天气目录
        :return: True点击成功，False点击失败
        """
        element = pm().find_element_by_id(id=pm().readConfigByModuleAndKey('australia_AS23', 'WeatherPage', 'Back'))
        return pm().click_by_element(element=element)

    def chooseTemperatureC(self):
        """
        选择摄氏度
        :return: True点击成功，False点击失败
        """
        self.swipeToSettingEnding()
        element = pm().find_element_by_id(id=pm().readConfigByModuleAndKey('australia_AS23', 'WeatherPage',
                                                                           'TemperatureC'))
        return pm().click_by_element(element=element)

    def chooseTemperatureF(self):
        """
        选择华氏
        :return: True点击成功，False点击失败
        """
        self.swipeToSettingEnding()
        element = pm().find_element_by_id(id=pm().readConfigByModuleAndKey('australia_AS23', 'WeatherPage',
                                                                           'TemperatureF'))
        return pm().click_by_element(element=element)

    def chooseMetric(self):
        """
        选择公制
        :return: True点击成功，False点击失败
        """
        self.swipeToSettingEnding()
        element = pm().find_element_by_id(
            id=pm().readConfigByModuleAndKey('australia_AS23', 'WeatherPage', 'Metric'))
        return pm().click_by_element(element=element)

    def chooseImperial(self):
        """
        选择英制
        :return: True点击成功，False点击失败
        """
        self.swipeToSettingEnding()
        element = pm().find_element_by_id(
            id=pm().readConfigByModuleAndKey('australia_AS23', 'WeatherPage', 'Imperial'))
        return pm().click_by_element(element=element)

    def checkOpenWeatherWarning(self):
        """
        检查天气预警打开状态是否异常
        :return: True点击成功，False点击失败
        """
        isSwitch = pm().find_element_by_id(
            id=pm().readConfigByModuleAndKey('australia_AS23', 'WeatherPage', 'isSwitch'))
        element = pm().find_element_by_id(id=pm().readConfigByModuleAndKey('australia_AS23', 'WeatherPage',
                                                                           'WeatherAlarm'))
        if 'ON' in element.get_text() and 'On' in isSwitch.get_text():
            print('Open Status')
            return True
        else:
            print('Alarm False')
            return False

    def checkCloseWeatherWarning(self):
        """
        检查天气预警关闭状态是否异常
        :return: True点击成功，False点击失败
        """
        isSwitch = pm().find_element_by_id(
            id=pm().readConfigByModuleAndKey('australia_AS23', 'WeatherPage', 'isSwitch'))
        element = pm().find_element_by_id(id=pm().readConfigByModuleAndKey('australia_AS23', 'WeatherPage',
                                                                           'WeatherAlarm'))
        if 'OFF' in element.get_text() and 'Off' in isSwitch.get_text():
            print('Close Status')
            return True
        else:
            print('Open Status')
            return False

    def openWeatherWarning(self):
        """
        打开天气预警按钮
        :return: True点击成功，False点击失败
        """
        self.swipeToSettingBeginning()
        if self.checkOpenWeatherWarning() == True:  # 天气预警已经打开直接返回True
            print('already open')
            return True
        else:
            element = pm().find_element_by_id(id=pm().readConfigByModuleAndKey('australia_AS23', 'WeatherPage',
                                                                               'WeatherAlarm'))
            print("Open Weather Warning")
            pm().click_by_element(element=element)
            if self.checkOpenWeatherWarning() == True:
                print("Open Weather Warning Success")
                return True
            else:
                print("Open Weather Warning Fail")
                return False

    def closeWeatherWarning(self):
        """
        关闭天气预警按钮
        :return: True点击成功，False点击失败
        """
        self.swipeToSettingBeginning()
        if self.checkCloseWeatherWarning() == True:  # 天气预警已经打开直接返回True
            print('already close')
            return True
        else:
            element = pm().find_element_by_id(id=pm().readConfigByModuleAndKey('australia_AS23', 'WeatherPage',
                                                                               'WeatherAlarm'))
            print("Close Weather Warning")
            pm().click_by_element(element=element)
            if self.checkCloseWeatherWarning() == True:
                print("Close Weather Warning Success")
                return True
            else:
                print("Close Weather Warning Fail")
                return False

    def getAlarmStatus(self):
        """
        获取当前Weather Alarm状态
        :return: On ，Off
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'WeatherPage', 'isSwitch')
        element = pm().find_element_by_id(id=id)
        return element.get_text()

    def getBroadCastStatus(self):
        """
        获取当前Weather Broadcast状态
        :return: On ，Off
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'WeatherPage', 'broadCastStatus')
        element = pm().find_element_by_id(id=id)
        return element.get_text()

    def clickBroadCastButton(self):
        """
        点击Weather BroadCast Button
        :return: True点击成功，False点击失败
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'WeatherPage', 'broadCastButton')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element=element)

    def openWeatherBroadcastButton(self):
        """
        点击打开WeatherBroadcastButton
        :return: True打开成功，False打开失败
        """
        self.swipeToSettingBeginning()
        status = self.getBroadCastStatus()
        if status == 'On':
            return True
        else:
            self.clickBroadCastButton()
            statusAfterClick = self.getBroadCastStatus()
            if statusAfterClick == 'On':
                return True
            else:
                return False

    def closeWeatherBroadcastButton(self):
        """
        点击关闭WeatherBroadcastButton
        :return: True关闭成功，False关闭失败
        """
        self.swipeToSettingBeginning()
        status = self.getBroadCastStatus()
        if status == 'Off':
            return True
        else:
            self.clickBroadCastButton()
            statusAfterClick = self.getBroadCastStatus()
            if statusAfterClick == 'Off':
                return True
            else:
                return False

    def checkWeatherSettingIsDefault(self):
        """
        检查当前天气Setting页面是否是默认状态
        :return: True默认状态，False非默认状态或者是天气单位元素不全
        """
        self.swipeToSettingBeginning()
        broadCastStatus = self.getBroadCastStatus()
        alarmStatus = self.getAlarmStatus()
        self.clickBackButton()
        unit = self.getLocationTemperatureUnit()
        if unit is not None:
            if broadCastStatus == 'On' and alarmStatus == 'On' and unit == '℉':
                print(broadCastStatus)
                print(alarmStatus)
                print(unit)
                return True
            else:
                print(broadCastStatus)
                print(alarmStatus)
                return False
        else:
            return False

    def getLocationTemperatureUnit(self):
        """
        返回天气详情页面中天气单位
        :return: ℃摄氏度、℉华氏度
        """
        id = pm().readConfigByModuleAndKey('australia_AS23', 'WeatherPage', 'LocationTemperatureUnit')
        element = pm().find_element_by_id(id=id)
        if element is not None:
            return element.get_text()
        else:
            return None

    def compareWeather(self):
        """
        比较天气详情页面和首页天气是否信息一致
        :return: True点击成功，False点击失败
        """
        locationName = pm().find_element_by_id(id=pm().readConfigByModuleAndKey('australia_AS23', 'WeatherPage',
                                                                                'LocationCityName')).get_text()
        locationTemperature = pm().find_element_by_id(
            id=pm().readConfigByModuleAndKey('australia_AS23', 'WeatherPage',
                                             'LocationTemperature')).get_text()
        LocationTemperatureUnit = pm().find_element_by_id(
            id=pm().readConfigByModuleAndKey('australia_AS23', 'WeatherPage',
                                             'LocationTemperatureUnit')).get_text()
        locationMainTemperatureTypes = pm().find_element_by_id(id=pm().readConfigByModuleAndKey('australia_AS23',
                                                                                                'WeatherPage',
                                                                                                'LocationMainTemperatureTypes')).get_text()
        print('-Location- ' + locationName)
        print('-Location- ' + locationTemperature)
        print('-Location- ' + LocationTemperatureUnit)
        print('-Location- ' + locationMainTemperatureTypes)
        pm().Home()
        HomePageCityName = pm().find_element_by_id(id=pm().readConfigByModuleAndKey('australia_AS23',
                                                                                    'homePage_resourceId',
                                                                                    'HomePageCityName')).get_text()
        HomePageTemperature = pm().find_element_by_id(id=pm().readConfigByModuleAndKey('australia_AS23',
                                                                                       'homePage_resourceId',
                                                                                       'HomePageTemperature')).get_text()
        HomePageTemperatureUnit = pm().find_element_by_id(id=pm().readConfigByModuleAndKey('australia_AS23',
                                                                                           'homePage_resourceId',
                                                                                           'HomePageTemperatureUnit')).get_text()
        HomePageMainTemperatureTypesId = pm().readConfigByModuleAndKey('australia_AS23', 'homePage_resourceId',
                                                                       'HomePageTemperatureTypes')
        HomePageMainTemperatureElement = pm().find_element_by_id(id=HomePageMainTemperatureTypesId)
        HomePageMainTemperatureTypes = HomePageMainTemperatureElement.get_text()

        print('=HomePage= ' + HomePageCityName)
        print('=HomePage= ' + HomePageTemperature)
        print('=HomePage= ' + HomePageTemperatureUnit)
        print('=HomePage= ' + HomePageMainTemperatureTypes)
        if locationName == HomePageCityName and locationTemperature == HomePageTemperature and LocationTemperatureUnit == HomePageTemperatureUnit and locationMainTemperatureTypes == HomePageMainTemperatureTypes:
            print('compare result True')
            return True
        else:
            print('compare result False')
            return False

    def changeTemperatureTypeToC(self):
        """
        进入设置天气单位C后检查是否生效
        :return: True正确，False错误
        """
        self.clickSetting()  # 进入天气设置页面
        element_C = pm().find_element_by_id(id=pm().readConfigByModuleAndKey('australia_AS23', 'WeatherPage',
                                                                             'TemperatureC'))
        element_Back = pm().find_element_by_id(
            id=pm().readConfigByModuleAndKey('australia_AS23', 'WeatherPage', 'Back'))
        pm().click_by_element(element=element_C)  # 设置单位C
        pm().click_by_element(element=element_Back)  # 返回天气详情页面
        print("start Compare")
        return self.compareWeather()

    def changeTemperatureTypeToF(self):
        """
        进入设置天气单位F后检查是否生效
        :return: True正确，False错误
        """
        self.clickSetting()  # 进入天气设置页面
        element_F = pm().find_element_by_id(id=pm().readConfigByModuleAndKey('australia_AS23', 'WeatherPage',
                                                                             'TemperatureF'))
        element_Back = pm().find_element_by_id(
            id=pm().readConfigByModuleAndKey('australia_AS23', 'WeatherPage', 'Back'))
        pm().click_by_element(element=element_F)  # 设置单位F
        pm().click_by_element(element=element_Back)  # 返回天气详情页面
        return self.compareWeather()

    def checkWeather5Day(self):
        """
        检查5天天气日期排序是否正确
        :return: True正确，False错误
        """
        # D90天气日期模版
        days = {'MON': ['MON', 'TUE', 'WED', 'THU', 'FRI'], 'TUE': ['TUE', 'WED', 'THU', 'FRI', 'SAT'],
                'WED': ['WED', 'THU', 'FRI', 'SAT', 'SUN'], 'THU': ['THU', 'FRI', 'SAT', 'SUN', 'MON'],
                'FRI': ['FRI', 'SAT', 'SUN', 'MON', 'TUE'], 'SAT': ['SAT', 'SUN', 'MON', 'WED', 'WED'],
                'SUN': ['SUN', 'MON', 'TUE', 'WED', 'THU']}
        # 获取页面天气日期排序
        day2Id = pm().readConfigByModuleAndKey('australia_AS23', 'WeatherPage', 'day2')
        day3Id = pm().readConfigByModuleAndKey('australia_AS23', 'WeatherPage', 'day3')
        day4Id = pm().readConfigByModuleAndKey('australia_AS23', 'WeatherPage', 'day4')
        day5Id = pm().readConfigByModuleAndKey('australia_AS23', 'WeatherPage', 'day5')
        day6Id = pm().readConfigByModuleAndKey('australia_AS23', 'WeatherPage', 'day6')
        day2Element = pm().find_element_by_id(id=day2Id)
        day3Element = pm().find_element_by_id(id=day3Id)
        day4Element = pm().find_element_by_id(id=day4Id)
        day5Element = pm().find_element_by_id(id=day5Id)
        day6Element = pm().find_element_by_id(id=day6Id)
        day2 = day2Element.get_text()
        day3 = day3Element.get_text()
        day4 = day4Element.get_text()
        day5 = day5Element.get_text()
        day6 = day6Element.get_text()
        dayList = [day2, day3, day4, day5, day6]
        if days[day2] == dayList:
            print('True')
            print(dayList)
            print(days[day2])
            return True
        else:
            print('False')
            print(dayList)
            print(days[day2])
            return False

    def checkRefreshTime(self):
        """
        :return: 无
        """
        element = pm().find_element_by_id(
            id=pm().readConfigByModuleAndKey('australia_AS23', 'WeatherPage', 'refreshTime'))
        time = element.get_text()
        # time = '17:20:08 22/03/2020'
        print(time)
        print(datetime.datetime.strptime(time, '%d/%m/%Y %H:%M:%S'))

    def checkIndiaCityName(self):
        """
        查看5个默认地区天气情况
        :return: True正确，False错误
        """
        Mumbai = pm()._find_element_by_text(text='Mumbai').exists()
        Bengaluru = pm()._find_element_by_text(text='Bengaluru').exists()
        NewDelhi = pm()._find_element_by_text(text='New Delhi').exists()
        Chennai = pm()._find_element_by_text(text='Chennai').exists()
        Hyderabad = pm()._find_element_by_text(text='Hyderabad').exists()
        cityName = [Mumbai, Bengaluru, NewDelhi, Chennai, Hyderabad]
        if False in cityName:
            print('find False')
            print('Mumbai: ' + str(Mumbai))
            print('Bengaluru: ' + str(Bengaluru))
            print('NewDelhi: ' + str(NewDelhi))
            print('Chennai: ' + str(Chennai))
            print('Hyderabad: ' + str(Hyderabad))
            return False
        else:
            print('city Name correct')
            return True

    def checkDefaultCityWeather(self, cityName):
        '''
        查看默认地区天气情况
        :param cityName: 城市名称
        :return: True正确，False错误
        '''
        defaultCityName = pm()._find_element_by_text(text=cityName)
        if defaultCityName.exists():
            print('cityName is exist!')
            pm().click_by_element(element=defaultCityName)
            locationCityName = pm().find_element_by_id(
                id=pm().readConfigByModuleAndKey('australia_AS23', 'WeatherPage',
                                                 'LocationCityName')).get_text()  # 获取城市名称优先比较
            print('cityName: ' + cityName)
            print('LocationCityName: ' + locationCityName)
            if cityName == locationCityName:  # 获取城市名称优先比较，若城市名称错误，无需进行详细信息比较
                print('CityName is correct!')
                return self.compareWeather()
            else:
                print('CityName is not correct!')
                return False
        else:
            print('cityName is not exist!')
            return False

    def searchCityByCityName(self, cityName):
        """
        天气页面输入地区名称搜索当地天气
        :param cityName:
        :return: True地区存在，False地区不存在
        """
        element = pm().find_element_by_id(
            id=pm().readConfigByModuleAndKey('australia_AS23', 'WeatherPage',
                                             'inputCityName'))  # 选择输入框
        pm().inputText(element, cityName)  # 输入框中传入地点名称
        positionSearch = pm().find_element_by_id(id=pm().readConfigByModuleAndKey('australia_AS23', 'WeatherPage',
                                                                                  'PositionSearch'))  # 搜索按钮
        pm().click_by_element(positionSearch)  # 点击搜索该地区
        firstAddress = pm().find_element_by_id(id=pm().readConfigByModuleAndKey('australia_AS23', 'WeatherPage',
                                                                                'ChooseFirstPosition'))
        addressName = firstAddress.get_text()
        print('addressName： ' + addressName)
        pm().click_by_element(firstAddress)
        self.clickWeatherSearch()  # 回到搜索区域天气页面
        print('click Search')
        element = pm()._find_element_by_text(text=addressName)
        print('element Name: ' + element.get_text())
        return element.exists()

    def gotoWeatherPage(self):
        """
        进入天气app
        :return: True点击成功，False点击失败
        """
        if pm().Home():
            weather = pm().find_element_by_id(
                id=pm().readConfigByModuleAndKey('australia_AS23', 'WeatherPage', 'Weather'))
            return pm().click_by_element(weather)
        return False

    def getHomeWeatherLocation(self):
        """
        获取主页天气的定位
        :return: 返回地名，False当前不是Home主页页面
        """
        if pm().Home():
            city = pm().find_element_by_id(id=pm().readConfigByModuleAndKey('australia_AS23', 'WeatherPage',
                                                                            'HomePageCityName'))
            return pm().get_text_by_element(city)
        return False

    def checkWeatherLocationInHomePageIsNotNone(self):
        """
        判断车机首页天气是否为空
        :return: True地址非空，False地址为空
        """
        if pm().Home():
            city = pm().find_element_by_id(id=pm().readConfigByModuleAndKey('australia_AS23', 'WeatherPage',
                                                                            'HomePageCityName'))
            if city.get_text() is not None:
                print(city.get_text())
                return True
            else:
                return False
        return False

    def inputSearchText(self, text):
        """
        搜索输入框输入文本
        :return: True传入成功，False传入失败
        """
        searchBox = pm().find_element_by_id(id=pm().readConfigByModuleAndKey('australia_AS23', 'WeatherPage',
                                                                             'inputCityName'))
        return pm().inputText(searchBox, text)

    def inputSpecialText(self, text):
        """
        搜索框输入框输入特殊字符
        :param text: 输入字符
        :return: True传入成功，False传入失败
        """
        return pm().input_text_by_adb(text)

    def getInputSearchText(self):
        """
        获取输入框中的字符串
        :return: 返回输入框内字符串
        """
        searchBox = pm().find_element_by_id(id=pm().readConfigByModuleAndKey('australia_AS23', 'WeatherPage',
                                                                             'inputCityName'))
        return pm().get_text_by_element(searchBox)

    def getWeatherLocation(self):
        """
        获取首页定位信息
        :return: 返回字符串
        """
        element = pm().find_element_by_id(id=pm().readConfigByModuleAndKey('australia_AS23', 'WeatherPage',
                                                                           'HomePageCityName'))
        return pm().get_text_by_element(element)

    def getCityNameInWeatherPage(self):
        """
        获取天气页面定位城市名称
        :return: 天气页面定位城市名称
        """
        element = pm().find_element_by_id(id=pm().readConfigByModuleAndKey('australia_AS23', 'WeatherPage',
                                                                           'LocationCityName'))
        return pm().get_text_by_element(element)

    def waitWeatherRefresh(self, times):
        """
        传入时间（秒）等待，该方法用于等待天气刷新
        :return: True刷新前后定位不同，False刷新前后定位相同
        """
        times = int(times)
        location = self.getWeatherLocation()
        for i in range(times):
            time.sleep(1)
            location2 = self.getWeatherLocation()
            if location != location2:
                return True
        return False

    def clickDefaultCity(self, text):
        """
        根据城市名称查询当前页面中是否存在该城市名称
        :param text: 城市名称
        :return: True存在，False不存在
        """
        city = pm().find_element_by_text(text=text)
        return pm().click_by_element(city)

    def getRefreshtime(self):
        """
        点击刷新时间
        :return: True刷新成功，False刷新失败
        """
        refreshtime = pm().find_element_by_id(id=pm().readConfigByModuleAndKey('australia_AS23', 'WeatherPage',
                                                                               'refreshTime'))
        return pm().get_text_by_element(refreshtime)

    def checkTimeFormat(self):
        """
        检验时间格式
        :return: True时间格式正确，False时间格式错误
        """
        times = self.getRefreshtime()
        try:
            datetime.datetime.strptime(times, '%d/%m/%Y %H:%M:%S')
            return True
        except ValueError:
            return False

    def calculateRefreshTime(self, times_str):
        """检验60分钟刷新时间是否正确"""
        times_str = '03/08/2020 15:11:28'
        now = datetime.datetime.strptime(times_str, '%d/%m/%Y %H:%M:%S')
        lastTime = (now + datetime.timedelta(hours=1)).strftime('%d/%m/%Y %H:%M:%S')
        return lastTime

    def getWeatherPageTemperature(self):
        """
        获取天气页面温度值
        :return: 返回温度值
        """
        LocationTemperature = pm().find_element_by_id(
            id=pm().readConfigByModuleAndKey('australia_AS23', 'WeatherPage',
                                             'LocationTemperature'))
        return pm().get_text_by_element(LocationTemperature)

    def isWeakNetwork(self):
        """
        弱网Toast提示框内容判断 弱网情况下返回True
        :return:True弱网，False网络正常
        """
        weakNetStr = 'The network is not available, please check the network.'  # 弱网提示话术
        toastMessage = pm().get_toast_message()
        if toastMessage == weakNetStr:
            print('toastMessage: ' + toastMessage)
            return True
        else:
            print('NetWork is OK')
            return False

    def weatherPageChangeToNaviPage100Times(self):
        k = 0
        for i in range(5):
            homePage().clickWeather()
            weatherActivity = pm().get_Current_Activity()
            if weatherActivity == 'com.saicmotor.weathers.activity.MainActivity':
                pass
            else:
                print(str(i) + ' Fail ' + weatherActivity)
                k = k + 1
            homePage().clickHomeButton()
            homePage().clickNav()
            navActivity = pm().get_Current_Activity()
            if navActivity == 'hr.mireo.arthur.common.App':
                pass
            else:
                print(str(i) + ' Fail ' + navActivity)
                k = k + 1
            homePage().clickScreenHardKeyHomeButton()
        if k == 0:
            return True
        else:
            print('Fail times: ' + str(k))
            return False

    def weatherPageChangeTo360Page100Times(self):
        k = 0
        for i in range(100):
            homePage().clickWeather()
            time.sleep(1)
            weatherActivity = pm().get_Current_Activity()
            if weatherActivity == 'com.saicmotor.weathers.activity.MainActivity':
                pass
            else:
                print(str(i) + ' Fail ' + weatherActivity)
                k = k + 1
            homePage().clickHomeButton()
            homePage().click360AVM()
            time.sleep(1)
            status360 = homePage().checkClose360ButtonIsExist()
            if status360:
                pass
            else:
                print(str(i) + ' Fail 360')
                k = k + 1
            homePage().close360AVN()
            homePage().clickScreenHardKeyHomeButton()
        if k == 0:
            return True
        else:
            print('Fail times: ' + str(k))
            return False
