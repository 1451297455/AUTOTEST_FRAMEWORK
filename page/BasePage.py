import os
import time
import uiautomator2 as u2
import logging
from uiautomator2 import UiObjectNotFoundError


class BasePage(object):
    d = None

    @classmethod
    def set_driver(self, dri):
        self.d = u2.connect(dri)
        # self.d.healthcheck()
        # self.d.debug = True
        # self.d.settings['wait_timeout'] = 10.0

    def get_driver(self):
        return self.d

    @classmethod
    def watch_device(self, keyword):

        '''
        如果存在元素则自动点击
        :param keyword: exp: keyword="yes|允许|好的|跳过"
        '''
        self.d.watchers.watched = False
        for i in keyword.split("|"):
            self.d.watcher(i).when(text=i).click(text=i)
        print('Starting watcher,parameter is %s' % keyword.split("|"))
        self.d.watchers.watched = True
        time.sleep(2)

    @classmethod
    def unwatch_device(self):
        '''关闭watcher '''
        # print('Stop all watcher')
        self.d.watchers.remove()
        self.d.watchers.watched = False

    def _find_element_by_swipe(self, direction, value, element=None, steps=0.2, max_swipe=6):
        """
        :param direction: swip direction exp: right left up down
        :param value: The value of the UI element location strategy. exp: d(text='Logina')
        :param element: UI element, if None while swipe window of phone
        :param steps: steps of swipe for Android, The lower the faster
        :param max_swipe: the max times of swipe
        :return: UI element
        """
        times = max_swipe
        for i in range(times):
            try:
                if value.exists:
                    return value
                else:
                    raise UiObjectNotFoundError
            except UiObjectNotFoundError:
                if direction == 'up':
                    self.d.swipe_up(element=element, steps=steps)
                elif direction == 'down':
                    self.d.swipe_down(element=element, steps=steps)
                elif direction == 'left':
                    self.d.swipe_left(element=element, steps=steps)
                elif direction == 'right':
                    self.d.swipe_right(element=element, steps=steps)
                if i == times - 1:
                    raise UiObjectNotFoundError

    def _find_element_by_id(self, id):
        element = None
        try:
            start = time.process_time()
            element = self.d(resourceId=id)
            end = time.process_time()
            # logging.info('different is %6.3f' % (end - start))
        except:
            element = None
        finally:
            return element

    def _find_element_by_text(self, text):
        element = None
        try:
            element = self.d(text=text)
        except:
            element = None
        finally:
            return element

    def find_element_by_description(self, description):
        element = None
        try:
            element = self.d(description=description)
        except:
            element = None
        finally:
            return element

    def find_element_by_ClassName(self, className):
        element = None
        try:
            element = self.d(className=className)
            print(element)
        except:
            element = None
        finally:
            return element

    def find_element_by_Xpath(self, Xpath):
        element = []
        try:
            start = time.process_time()
            element = self.d.xpath(Xpath)
            end = time.process_time()
        except:
            element = None
        finally:
            return element

    def find_element_by_swipe_up(self, value, element=None, steps=0.2, max_swipe=6):
        return self._find_element_by_swipe('up', value,
                                           element=element, steps=steps, max_swipe=max_swipe)

    def find_element_by_swipe_down(self, value, element=None, steps=0.2, max_swipe=6):
        return self._find_element_by_swipe('down', value,
                                           element=element, steps=steps, max_swipe=max_swipe)

    def find_element_by_swipe_left(self, value, element=None, steps=0.2, max_swipe=6):
        return self._find_element_by_swipe('left', value,
                                           element=element, steps=steps, max_swipe=max_swipe)

    def find_element_by_swipe_right(self, value, element=None, steps=0.2, max_swipe=6):
        return self._find_element_by_swipe('right', value,
                                           element=element, steps=steps, max_swipe=max_swipe)

    def find_element_by_id(self, id):
        return self._find_element_by_id(id)

    def find_element_by_text(self, text):
        return self._find_element_by_text(text)

    def clickByCoordinate(self, X, Y):
        return self.d.click(X, Y)

    def input_text(self, element, text):
        return element.set_text(text)

    def get_text(self, element):
        return element.get_text()

    @classmethod
    def screenshot(self, screenshot_name):
        '''截图并打印特定格式的输出，保证用例显示截图'''
        date_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        screenshot_name = screenshot_name + "_" + date_time + '.PNG'
        path = os.path.join(os.path.abspath('.') + "/screen/", screenshot_name)
        self.d.screenshot(path)
        print('IMAGE:' + screenshot_name)
