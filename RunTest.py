from page.india_D90_weatherPage import india_D90_weatherPage
from page.test import map
from page.BasePage import BasePage as base

if __name__ == '__main__':
    # https://www.jianshu.com/p/7f2e474990d9
    d = base.set_driver("0a01600e82899a74")
    print("start")
    weather = india_D90_weatherPage()

    '''
    base.d(className="android.support.v7.widget.RecyclerView").\
        child(className="android.widget.RelativeLayout").\
        child_by_text('FM 87.9').click()
    publicMethod().Home()
    #publicMethod.volume_mute()
    #publicMethod.volume_down()
    #publicMethod.volume_up()
    #homePage.clickInbox()
    #publicMethod().Home()
    #homePage.clickSaicAccount()
    #publicMethod().Home()
    #radioPage.changeRadio()
    #radioPage.changeToAM()
    #radioPage.changeRadio()
    #radioPage.changeToFM()
    #radioPage.getFavIcon()
    #radioPage.checkFMBand()
    #radioPage.changeRadio()
    #radioPage.changeToDRM()
    #radioPage.clickSearchRadio()
    #radioPage.cancelScan()
    #radioPage.checkAMBand()
    #radioPage.checkFMBand()
    #radioPage.checkDRMBand()
    radioPage.swipeToTheEndOfLeftFavorite()
    radioPage.findChannleInFavoriteList('FM 93.2')
    print(radioPage.compareRadioChannelisExist('FM 89.3'))
    print(radioPage.findChannleInFavoriteList('FM 98.0'))
    homePage.clickRadio()
    radioPage.getCurrentChannle()
    radioPage.checkFMChannelAfterStepAdd()
    radioPage.clickPauseStation()
    radioPage.clickPlayStation()
    radioPage.changeRadio()
    radioPage.changeToFM()
    radioPage.clickCollectAMFMHeartIcon()
    radioPage.clickCancelAMFMHeartIcon()
    radioPage.isCurrentChannleExistsInFavoriteList()
    radioPage.clickEnterFavouritePage()
 '''
    weather.getHomeWeatherLocation()
    weather.GotoWeatherPage()
    weather.clickWeatherSearch()
    weather.inputSearchText("Chennai")
    weather.clickSearchSearch()
    # weather.checkWeatherPage()
    # weather.getWeatherLocation()
    # weather.checkWeatherSettingPage()
    # weather.checkWeatherSettingPage()
    # weather.checkWeatherSettingPage()
    # weather.checkWeatherSettingPage()
    # weather.checkWeatherSettingPage()