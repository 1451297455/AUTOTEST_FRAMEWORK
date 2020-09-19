# -*- coding: utf-8 -*-
from UIconfig.Base import Base
from page.PublicMethod import PublicMethod as pm
import os, time
import UIconfig.logger as loggers

logger = loggers.Logger()
os.path.abspath('.')


class india_D90_shortPediaPage(Base):

    def chooseEnglishLanguage(self):
        """
        选择英语模式
        :return:
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'ShortPediaPage', 'ChooseEnglish')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    def chooseHindiLanguage(self):
        """
        选择Hindi模式
        :return:
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'ShortPediaPage', 'ChooseHindi')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    def choosePageByPageName(self, pageName):
        """
        根据页面名称（下方栏目名称），点击选择该页面
        :param pageName: DiscoverPage、MyFeedPage、ListenPage、TopPage、LanguagePage、ThemePage、BookmarkPage、
        :return: True、False
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'ShortPediaPage', pageName)
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    def chooseDiscoverItemByName(self, itemName):
        """
        根据Discover页面item名称，点击打开该栏目。
        :param itemName: All News、India、World Wide、Trending、Corona Virus、Crime、Politics、Sports、Technology、Business、Entertainment、Automobile、Startups、Travel、Miscellaneous
        :return: True、False
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'ShortPediaPage', 'DiscoverTitleId')
        element = pm().find_element_by_idAndText(id=id, text=itemName)
        return pm().click_by_element(element)

    def clickSearchNews(self):
        """
        点击SearchNews栏打开搜索页面
        :return: True,False
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'ShortPediaPage', 'SearchNews')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    def clickBackButton(self):
        """
        点击返回按键返回上一页
        :return: True,False
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'ShortPediaPage', 'BackButton')
        element = pm().find_element_by_id(id=id)
        return pm().click_by_element(element)

    def searchNewsByName(self, inputText):
        """
        搜索页面输入字段进行搜索
        :param inputText: 传入字段
        :return: True,False
        """
        element = pm().find_element_by_id(
            id=pm().readConfigByModuleAndKey('india_D90', 'ShortPediaPage',
                                             'SearchNews'))  # 选择输入框
        return pm().inputText(element, inputText)  # 输入框中传入地点名称

    def swipeShortPediaScreenRight(self):
        """
        右滑新闻页面
        :return: True，False
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'ShortPediaPage', 'ScreenLayout')
        element = pm().find_element_by_id(id=id)
        return pm().swipe_right_by_element(element=element)

    def swipeShortPediaScreenLeft(self):
        """
        左滑新闻页面
        :return: True，False
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'ShortPediaPage', 'ScreenLayout')
        element = pm().find_element_by_id(id=id)
        return pm().swipe_left_by_element(element=element)

    def clickAutoPlayButton(self):
        """
        点击自动播放按键
        :return: True，False
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'ShortPediaPage', 'AutoPlayButton')
        element = pm().find_element_by_id(id=id)
        return pm().swipe_left_by_element(element=element)

    def clickPreButton(self):
        """
        点击上一曲按键
        :return: True，False
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'ShortPediaPage', 'PreButton')
        element = pm().find_element_by_id(id=id)
        return pm().swipe_left_by_element(element=element)

    def clickPlayButton(self):
        """
        点击Play按键
        :return: True，False
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'ShortPediaPage', 'PlayButton')
        element = pm().find_element_by_id(id=id)
        return pm().swipe_left_by_element(element=element)

    def clickNextButton(self):
        """
        点击下一曲按键
        :return: True，False
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'ShortPediaPage', 'NextButton')
        element = pm().find_element_by_id(id=id)
        return pm().swipe_left_by_element(element=element)

    def clickCloseButton(self):
        """
        点击关闭按键
        :return: True，False
        """
        id = pm().readConfigByModuleAndKey('india_D90', 'ShortPediaPage', 'CloseButton')
        element = pm().find_element_by_id(id=id)
        return pm().swipe_left_by_element(element=element)
