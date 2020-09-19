import uiautomator2 as u2
import time, os

from uiautomator2 import UiObjectNotFoundError

from UIconfig import info


class Base:
    """
    uitautomator2 基础类，包含初始化驱动，常用方法
    """

    d = None

    @classmethod
    def set_driver(cls, add):
        """
           初始化Base类，同时默认连接驱动
           :param add:  设备驱动ID

        """
        cls.d = u2.connect(add)
        cls.d.implicitly_wait(3.0)

    def get_driver(self):
        """
        返回已连接设备信息
        :return:
        """
        return self.d

    def app_start(self, pkg):
        """
          启动APP
          :param pkg:  应用包名
          :return: 启动成功返回True,启动失败返回False
        """
        try:
            self.d.app_start(package_name=pkg, stop=True, use_monkey=True, wait=True)
            return self.d.app_current().get('package') == pkg
        except Exception as e:
            print(e)
            return False

    def app_stop(self, pkg):
        """
        停止app
        :param pkg: 要停止的APP包名
        :return:  成功返回True，失败返回False
        """
        try:
            self.d.app_stop(pkg)
            return self.d.app_current().get('package') != pkg
        except Exception as e:
            print(e)
            return False

    def app_wait(self, pkg, timeout=10):
        """
        启动APP，并等待app进入前台运行
        :param timeout: 等待超时时间
        :param pkg: 待启动APP的包名
        :return: 启动成功返回True，失败返回False
        """
        return self.d.app_wait(package_name=pkg, front=True, timeout=timeout) != 0

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

    def watch(self, watcher_name, xpath, force):
        """
        监控设备执行情况
        :param watcher_name:
        :param xpath:
        :param force:
        :return:
        """
        self.d.watcher(watcher_name).when(xpath=xpath).when(force).click()

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
            # start = time.process_time()
            element = self.d(resourceId=id)
            # end = time.process_time()
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

    def find_element_by_id(self, id):
        """
        通过元素的resourceID查找元素
        :param source_id: 待查找元素的ID
        :return: 查找到返回element，查找失败返回 None
        """
        if self.d(resourceId=id).wait(timeout=3):
            return self.d(resourceId=id)
        return None

    def find_element_by_xpath(self, xpath):
        """
        通过元素的xpath查找元素
        :param xpath: 待查找元素的xpath
        :return: 查找到返回element，查找失败返回 None
        """

        if self.d.xpath(xpath):
            return self.d.xpath(xpath)
        return None

    def find_element_by_text(self, text):
        """
        通过元素的text查找元素
        :param text: 待查找元素的text
        :return: 查找到返回element，查找失败返回 None
        """
        if self.d(text=text).wait(timeout=4):
            return self.d(text=text)
        return None

    def find_element_by_class_name(self, class_name):
        """
        通过元素的class_name查找元素
        :param class_name: 待查找元素的class_name
        :return: 查找到返回element，查找失败返回 None
        """
        if self.d(className=class_name).wait(timeout=4):
            return self.d(className=class_name)
        return None

    def find_element_by_description(self, description):
        """
        通过元素的description查找元素
        :param description: 待查找元素的description
        :return: 查找到返回element，查找失败返回 None
        """
        if self.d(description=description).wait(timeout=4):
            return self.d(description=description)
        return None

    def find_element_by_ClassName(self, className):
        element = None
        try:
            element = self.d(className=className)
            # print(element)
        except:
            element = None
        finally:
            return element

    def find_element_by_Xpath(self, Xpath):
        element = []
        try:
            element = self.d.xpath(Xpath)
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

    # 通过id和text定位元素
    def find_element_by_idAndText(self, id, text):
        element = None
        try:
            # start = time.process_time()
            element = self.d(resourceId=id, text=text)
            # end = time.process_time()
            # logging.info('different is %6.3f' % (end - start))
        except:
            element = None
        finally:
            return element

    def clickByCoordinate(self, X, Y):
        return self.d.click(X, Y)

    def click_element(self, element=None):
        """
        点击元素
        :param element:
        :return: 点击成功返沪True，点击失败返回False
        """
        if element is None:
            return False
        try:
            element.click(timeout=5)
            return True
        except Exception as e:
            print(e)
            return False

    def get_text(self, element=None, attribute='text'):
        """
        获取对象的属性值
        :param attribute: 属性的key值
        :param element:  对象
        :return: 返回string类型的属性value值
        """
        if element is None:
            return False
        return element.info[attribute]

    def input_text(self, element, text):
        return element.set_text(text)

    @classmethod
    def screenshot(self, screenshot_name):
        '''截图并打印特定格式的输出，保证用例显示截图'''
        date_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        screenshot_name = screenshot_name + "_" + date_time + '.PNG'
        screenpath = os.path.abspath('.') + "/screen/"
        if not os.path.exists(screenpath):
            os.makedirs(screenpath)
        path = os.path.join(screenpath, screenshot_name)
        self.d.screenshot(path)
        info.pic = screenshot_name
        print('IMAGE:' + screenshot_name)
