# -*- coding: utf-8 -*-
# 印度D90天气
from page.BasePage import BasePage
from page.publicMethod import publicMethod as pm
from config import india_D90_propertiseConfig
from page import homePage as home
import datetime, time


class india_D90_weatherPage(BasePage):

    # 点击刷新天气页面
    def clickRefresh(self):
        element = pm.find_element_by_id(self, id=india_D90_propertiseConfig.weatherPageConfig.get('Refresh'))
        print("Refresh Weather")
        return pm.click_by_element(self, element=element)

    # 点击收听天气播报页面
    def clickWeatherVoice(self):
        element = pm.find_element_by_id(self, id=india_D90_propertiseConfig.weatherPageConfig.get('Voice'))
        print("Weather Voice")
        return pm.click_by_element(self, element=element)

    # 点击搜索天气页面
    def clickWeatherSearch(self):
        element = pm.find_element_by_id(self, id=india_D90_propertiseConfig.weatherPageConfig.get('Search'))
        print("Refresh Weather")
        return pm.click_by_element(self, element=element)

        # 点击搜索页面搜索按钮

    def clickSearchSearch(self):
        element = pm.find_element_by_id(self, id=india_D90_propertiseConfig.weatherPageConfig.get('PositionSearch'))
        print("Refresh Weather")
        return pm.click_by_element(self, element=element)

    # 点击天气设置页面
    def clickSetting(self):
        element = pm.find_element_by_id(self, id=india_D90_propertiseConfig.weatherPageConfig.get('Setting'))
        print("Weather Setting")
        return pm.click_by_element(self, element=element)

    # 点击获取当前地点天气
    def clickLocalPosition(self):
        element = pm.find_element_by_id(self, id=india_D90_propertiseConfig.weatherPageConfig.get('Position'))
        print("Weather Local Position")
        return pm.click_by_element(self, element=element)

    # 点击获取当前地点天气
    def clickBackButton(self):
        element = pm.find_element_by_id(self, id=india_D90_propertiseConfig.weatherPageConfig.get('Back'))
        print("Back")
        return pm.click_by_element(self, element=element)

    # 选择摄氏度
    def chooseTemperatureC(self):
        element = pm.find_element_by_id(self, id=india_D90_propertiseConfig.weatherPageConfig.get('TemperatureC'))
        print("TemperatureC")
        return pm.click_by_element(self, element=element)

    # 选择华氏
    def chooseTemperatureF(self):
        element = pm.find_element_by_id(self, id=india_D90_propertiseConfig.weatherPageConfig.get('TemperatureF'))
        print("TemperatureF")
        return pm.click_by_element(self, element=element)

    # 选择公制
    def chooseMetric(self):
        element = pm.find_element_by_id(self, id=india_D90_propertiseConfig.weatherPageConfig.get('Metric'))
        print("Metric")
        return pm.click_by_element(self, element=element)

    # 选择英制
    def chooseImperial(self):
        element = pm.find_element_by_id(self, id=india_D90_propertiseConfig.weatherPageConfig.get('Imperial'))
        print("Imperial")
        return pm.click_by_element(self, element=element)

    # 检查天气预警打开状态是否异常
    def checkOpenWeatherWarning(self):
        isSwitch = pm.find_element_by_id(self, id=india_D90_propertiseConfig.weatherPageConfig.get('isSwitch'))
        element = pm.find_element_by_id(self, id=india_D90_propertiseConfig.weatherPageConfig.get('WeatherAlarm'))
        if 'ON' in element.get_text() and 'On' in isSwitch.get_text():
            print('Open Status')
            return True
        else:
            print('Alarm False')
            return False

    # 检查天气预警关闭状态是否异常
    def checkCloseWeatherWarning(self):
        isSwitch = pm.find_element_by_id(self, id=india_D90_propertiseConfig.weatherPageConfig.get('isSwitch'))
        element = pm.find_element_by_id(self, id=india_D90_propertiseConfig.weatherPageConfig.get('WeatherAlarm'))
        if 'OFF' in element.get_text() and 'Off' in isSwitch.get_text():
            print('Close Status')
            return True
        else:
            print('Open Status')
            return False

    # 打开天气预警按钮
    def openWeatherWarning(self):
        if self.checkOpenWeatherWarning() == True:  # 天气预警已经打开直接返回True
            print('already open')
            return True
        else:
            element = pm.find_element_by_id(self, id=india_D90_propertiseConfig.weatherPageConfig.get('WeatherAlarm'))
            print("Open Weather Warning")
            pm.click_by_element(self, element=element)
            if self.checkOpenWeatherWarning() == True:
                print("Open Weather Warning Success")
                return True
            else:
                print("Open Weather Warning Fail")
                return False

    # 关闭天气预警按钮
    def closeWeatherWarning(self):
        if self.checkCloseWeatherWarning() == True:  # 天气预警已经打开直接返回True
            print('already close')
            return True
        else:
            element = pm.find_element_by_id(self, id=india_D90_propertiseConfig.weatherPageConfig.get('WeatherAlarm'))
            print("Close Weather Warning")
            pm.click_by_element(self, element=element)
            if self.checkCloseWeatherWarning() == True:
                print("Close Weather Warning Success")
                return True
            else:
                print("Close Weather Warning Fail")
                return False

    # 比较天气详情页面和首页天气是否信息一致
    def compareWeather(self):
        locationName = pm.find_element_by_id(self, id=india_D90_propertiseConfig.weatherPageConfig.get(
            'LocationCityName')).get_text()
        locationTemperature = pm.find_element_by_id(self, id=india_D90_propertiseConfig.weatherPageConfig.get(
            'LocationTemperature')).get_text()
        LocationTemperatureUnit = pm.find_element_by_id(self, id=india_D90_propertiseConfig.weatherPageConfig.get(
            'LocationTemperatureUnit')).get_text()
        locationMainTemperatureTypes = pm.find_element_by_id(self, id=india_D90_propertiseConfig.weatherPageConfig.get(
            'LocationMainTemperatureTypes')).get_text()
        print('-Location-' + locationName)
        print('-Location-' + locationTemperature)
        print('-Location-' + LocationTemperatureUnit)
        print('-Location-' + locationMainTemperatureTypes)
        pm.Home(self)
        time.sleep(1)
        HomePageCityName = pm.find_element_by_id(self, id=india_D90_propertiseConfig.homePageConfig.get(
            'HomePageCityName')).get_text()
        HomePageTemperature = pm.find_element_by_id(self, id=india_D90_propertiseConfig.homePageConfig.get(
            'HomePageTemperature')).get_text()
        HomePageTemperatureUnit = pm.find_element_by_id(self, id=india_D90_propertiseConfig.homePageConfig.get(
            'HomePageTemperatureUnit')).get_text()
        HomePageMainTemperatureTypes = pm.find_element_by_id(self, id=india_D90_propertiseConfig.homePageConfig.get(
            'HomePageMainTemperatureTypes')).get_text()
        print('=HomePage=' + HomePageCityName)
        print('=HomePage=' + HomePageTemperature)
        print('=HomePage=' + HomePageTemperatureUnit)
        print('=HomePage=' + HomePageMainTemperatureTypes)
        if locationName == HomePageCityName and locationTemperature == HomePageTemperature and LocationTemperatureUnit == HomePageTemperatureUnit and locationMainTemperatureTypes == HomePageMainTemperatureTypes:
            print('True')
            return True
        else:
            print('False')
            return False

    # 设置天气单位C后检查是否生效
    def changeTemperatureTypeToC(self):
        self.clickSetting()  # 进入天气设置页面
        element_C = pm.find_element_by_id(self, id=india_D90_propertiseConfig.weatherPageConfig.get('TemperatureC'))
        element_Back = pm.find_element_by_id(self, id=india_D90_propertiseConfig.weatherPageConfig.get('Back'))
        pm.click_by_element(self, element=element_C)  # 设置单位C
        pm.click_by_element(self, element=element_Back)  # 返回天气详情页面
        print("start Compare")
        self.compareWeather()

    # 设置天气单位F后检查是否生效
    def changeTemperatureTypeToF(self):
        self.clickSetting()  # 进入天气设置页面
        element_F = pm.find_element_by_id(self, id=india_D90_propertiseConfig.weatherPageConfig.get('TemperatureF'))
        element_Back = pm.find_element_by_id(self, id=india_D90_propertiseConfig.weatherPageConfig.get('Back'))
        pm.click_by_element(self, element=element_F)  # 设置单位F
        pm.click_by_element(self, element=element_Back)  # 返回天气详情页面
        self.compareWeather()

    # 检查5天天气日期排序是否正确
    def checkWeather5Day(self):
        # 天气日期模版
        days = {'MON': ['MON', 'TUE', 'WED', 'THU', 'FRI'], 'TUE': ['TUE', 'WED', 'THU', 'FRI', 'SAT'],
                'WED': ['WED', 'THU', 'FRI', 'SAT', 'SUN'], 'THU': ['THU', 'FRI', 'SAT', 'SUN', 'MON'],
                'FRI': ['FRI', 'SAT', 'SUN', 'MON', 'TUE'], 'SAT': ['SAT', 'SUN', 'MON', 'WED', 'WED'],
                'SUN': ['SUN', 'MON', 'TUE', 'WED', 'THU']}
        # 获取页面天气日期排序
        day2 = pm.find_element_by_id(self, id=india_D90_propertiseConfig.weatherPageConfig.get('Day2')).get_text()
        day3 = pm.find_element_by_id(self, id=india_D90_propertiseConfig.weatherPageConfig.get('Day3')).get_text()
        day4 = pm.find_element_by_id(self, id=india_D90_propertiseConfig.weatherPageConfig.get('Day4')).get_text()
        day5 = pm.find_element_by_id(self, id=india_D90_propertiseConfig.weatherPageConfig.get('Day5')).get_text()
        day6 = pm.find_element_by_id(self, id=india_D90_propertiseConfig.weatherPageConfig.get('Day6')).get_text()
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

    '''
        def getWeatherData(self, i):
            return pm.find_element_by_id(self, id=india_D90_propertiseConfig.weatherPageConfig.get('Day' + str(i)))
    '''

    # 检查刷新时间格式
    def checkRefreshTime(self):
        element = pm.find_element_by_id(self, id=india_D90_propertiseConfig.weatherPageConfig.get('refreshTime'))
        time = element.get_text()
        # time = '17:20:08 22/03/2020'
        print(time)
        print(datetime.datetime.strptime(time, '%d/%m/%Y %H:%M:%S'))

    # 查看5个默认地区天气情况
    def checkIndiaCityName(self):
        Mumbai = pm._find_element_by_text(self, text='Mumbai').exists()
        Bengaluru = pm._find_element_by_text(self, text='Bengaluru').exists()
        NewDelhi = pm._find_element_by_text(self, text='New Delhi').exists()
        Chennai = pm._find_element_by_text(self, text='Chennai').exists()
        Hyderabad = pm._find_element_by_text(self, text='Hyderabad').exists()
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

    # 查看默认地区天气情况
    def checkDefaultCityWeather(self, cityName):
        defaultCityName = pm._find_element_by_text(self, text=cityName)
        if defaultCityName.exists():
            print('cityName is exist!')
            pm.click_by_element(self, element=defaultCityName)
            locationCityName = pm.find_element_by_id(self, id=india_D90_propertiseConfig.weatherPageConfig.get(
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

    # 天气页面输入地区名称搜索当地天气
    def searchCityByCityName(self, cityName):
        element = pm.find_element_by_id(self,
                                        id=india_D90_propertiseConfig.weatherPageConfig.get('inputCityName'))  # 选择输入框
        pm.inputText(self, element, cityName)  # 输入框中传入地点名称
        positionSearch = pm.find_element_by_id(self, id=india_D90_propertiseConfig.weatherPageConfig.get(
            'PositionSearch'))  # 搜索按钮
        pm.click_by_element(self, positionSearch)  # 点击搜索该地区
        firstAddress = pm.find_element_by_id(self,
                                             id=india_D90_propertiseConfig.weatherPageConfig.get('ChooseFirstPosition'))
        addressName = firstAddress.get_text()
        print('addressName： ' + addressName)
        pm.click_by_element(self, firstAddress)
        self.clickSearch()  # 回到搜索区域天气页面
        print('click Search')
        element = pm._find_element_by_text(self, text=addressName)
        print('element Name: ' + element.get_text())
        return element.exists()

    # 进入天气app
    def GotoWeatherPage(self):
        if pm.Home(self):
            weather = pm.find_element_by_id(self, id=india_D90_propertiseConfig.homePageConfig.get('Weather'))
            return pm.click_by_element(self, weather)
        return False

    # 获取主页天气的定位
    def getHomeWeatherLocation(self):
        if pm.Home(self):
            city = pm.find_element_by_id(self, id='com.saicmotor.launcher:id/tv_city')
            return pm.get_text_by_element(self, city)
        return False

    # 搜索输入框输入文本
    def inputSearchText(self, text):
        searchBox = pm.find_element_by_id(self, id=india_D90_propertiseConfig.weatherPageConfig.get('inputCityName'))
        return pm.inputText(self, searchBox, text)

    def getInputSearchText(self):
        searchBox = pm.find_element_by_id(self, id=india_D90_propertiseConfig.weatherPageConfig.get('inputCityName'))
        return pm.get_text_by_element(self, searchBox)

    def checkWeatherPage(self):
        return pm.checkPage(self, india_D90_propertiseConfig.weatherPageConfig.get('weatherActivity'))

    def checkWeatherSearhPage(self):
        return pm.checkPage(self, india_D90_propertiseConfig.weatherPageConfig.get('weatherSearchActivity'))

    def checkWeatherSettingPage(self):
        return pm.checkPage(self, india_D90_propertiseConfig.weatherPageConfig.get('weatherSettingActivity'))

    def getWeatherLocation(self):
        return pm.get_text_by_element(self, india_D90_propertiseConfig.weatherPageConfig.get('LocationCityName'))

    def waitWeatherRefresh(self, times):
        times = int(times)
        location = home.homePage.getWeatherLocation(self)
        for i in range(times):
            time.sleep(1)
            location2 = home.homePage.getWeatherLocation(self)
            if location != location2:
                return True
        return False

    def clickDefaultCity(self, text):
        city = pm.find_element_by_text(self, text=text)
        return pm.click_by_element(self, city)

    def getRefreshtime(self):
        refreshtime = pm.find_element_by_id(self, id=india_D90_propertiseConfig.weatherPageConfig.get('refreshTime'))
        return pm.get_text_by_element(self, refreshtime)

    def checkTimeFormat(self):
        times = self.getRefreshtime(self)
        return time.strptime(times, "%d/%m/%Y %H:%M:%S")

    def getWeatherPageTemperature(self):
        LocationTemperature = pm.find_element_by_id(self, india_D90_propertiseConfig.weatherPageConfig.get(
            'LocationTemperature'))
        return pm.get_text_by_element(self, LocationTemperature)
        # if __name__ == '__main__':
    # homePage.clickHome()
    # india_D90_weatherPage = india_D90_weatherPage()
    # india_D90_weatherPage.checkWeather5Day()

    # pass
