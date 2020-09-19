import os
from UIconfig.Base import Base
import subprocess
import configparser
import UIconfig.logger as loggers

logger = loggers.Logger()


# import Run
class PublicMethod(Base):
    @classmethod
    def back(self):
        '''点击返回
        页面没有加载完的时候，会出现返回失败的情况，使用前确认页面加载完成'''
        '''home, back, left, right, up, down, center, menu, search, enter,
            delete(or del), recent(recent apps), volume_up, volume_down,
            volume_mute, camera, power.'''
        try:
            self.d.press('back')
            return True
        except:
            return False

    @classmethod
    def menu(self):
        try:
            self.d.press("menu")
            return True
        except:
            return False

    @classmethod
    def left(self):
        try:
            self.d.press("left")
            return True
        except:
            return False

    @classmethod
    def right(self):
        try:
            self.d.press("right")
            return True
        except:
            return False

    @classmethod
    def up(self):
        try:
            self.d.press("up")
            return True
        except:
            return False

    @classmethod
    def down(self):
        try:
            self.d.press("down")
            return True
        except:
            return False

    @classmethod
    def center(self):
        try:
            self.d.press("center")
            return True
        except:
            return False

    @classmethod
    def search(self):
        try:
            self.d.press("search")
            return True
        except:
            return False

    @classmethod
    def enter(self):
        try:
            self.d.press("enter")
            return True
        except:
            return False

    @classmethod
    def delete(self):
        try:
            self.d.press("delete")
            return True
        except:
            return False

    @classmethod
    def recent(self):
        try:
            self.d.press("recent")
            return True
        except:
            return False

    @classmethod
    def volume_up(self):
        try:
            self.d.press("volume_up")
            return True
        except:
            return False

    @classmethod
    def volume_down(self):
        try:
            self.d.press("volume_down")
            return True
        except:
            return False

    @classmethod
    def volume_mute(self):
        try:
            self.d.press("volume_mute")
            return True
        except:
            return False

    @classmethod
    def camera(self):
        try:
            self.d.press("camera")
            return True
        except:
            return False

    @classmethod
    def power(self):
        try:
            self.d.press("power")
            return True
        except:
            return False

    def Home(self):
        '''点击home
                点击home 键，回到主界面'''
        try:
            self.d.press("home")
            return True
        except:
            return False

    @classmethod
    def identify(self):
        self.d.open_identify()

    @classmethod
    def get_toast_message(self):
        message = self.d.toast.get_message(3, 3)
        logger.info(message)
        self.d.toast.reset()
        return message

    @classmethod
    def openApp(self, package):
        try:
            self.d.app_start(package)
        except Exception as e:
            logger.info(e)
            return False

    @classmethod
    def stopApp(self, package):
        try:
            self.d.app_stop(package)
        except Exception as e:
            logger.info(e)
            return False

    @classmethod
    def set_fastinput_ime(self):
        try:
            self.d.set_fastinput_ime(True)
        except Exception as e:
            logger.info(e)
            return False

    @classmethod
    def set_original_ime(self):
        self.d.set_fastinput_ime(False)

    @staticmethod
    def find_message(elements, text):
        '''查找元素列表中是否存在 text'''
        count = elements.count
        while count > 0:
            count = count - 1
            message = elements[count].info['text']
            if text in message:
                return True
            elif count == 0:
                return False
        else:
            return False

    def _get_window_size(self):
        window = self.d.window_size()
        x = window[0]
        y = window[1]
        return x, y

    @staticmethod
    def _get_element_size(element):
        # rect = element.info['visibleBounds']
        rect = element.info['bounds']
        # logger.info(rect)
        x_center = (rect['left'] + rect['right']) / 2
        y_center = (rect['bottom'] + rect['top']) / 2
        x_left = rect['left']
        y_up = rect['top']
        x_right = rect['right']
        y_down = rect['bottom']

        return x_left, y_up, x_center, y_center, x_right, y_down

    def _swipe(self, fromX, fromY, toX, toY, steps):
        self.d.swipe(fromX, fromY, toX, toY, steps)

    def swipe_to_end(self):
        self.d(scrollable=True).scroll.toEnd()

    def swipe_to_end_by_id(self, id=None):
        self.d(scrollable=True, resourceId=id).scroll.toEnd()

    def swipe_to_beginning(self):
        self.d(scrollable=True).scroll.toBeginning()

    def swipe_to_beginning_by_id(self, id=None):
        self.d(scrollable=True, resourceId=id).scroll.toBeginning()

    def swipe_backto_description(self, text):
        self.d(scrollable=True).scroll.to(text=text)

    def swipe_forwardto_description(self, text):
        self.d(scrollable=True).scroll.forward.to(text=text)

    def swipe_up(self, count=1):
        """
        swipe up
        :param element: UI element, if None while swipe window of phone
        :param steps: steps of swipe for Android, The lower the faster
        :return: None
        """
        try:
            for i in range(int(count)):
                x, y = self._get_window_size()
                fromX = 0.5 * x
                fromY = 0.5 * y
                toX = 0.5 * x
                toY = 0.25 * y
                self._swipe(fromX, fromY, toX, toY, 0.5)
                return True
        except:
            return False

    def swipe_up_by_element(self, element=None):
        """
        swipe up
        :param element: UI element, if None while swipe window of phone
        :param steps: steps of swipe for Android, The lower the faster
        :return: None
        """
        if element:
            rect = element.info['bounds']
            x_center = (rect['right'] - rect['left']) / 2 + rect['left']
            y_center = (rect['bottom'] - rect['top']) / 2 + rect['top']
            x_left = rect['left']
            y_up = rect['top']
            x_right = rect['right']
            y_down = rect['bottom']
            # logger.info(x_center)
            # logger.info(y_down - 50)
            # logger.info(y_up)
            self.d.swipe(x_center, (y_down - y_up) * 3 / 4, x_center, y_up, 0.5)
            return True
        return False

    def swipe_down_by_element(self, element=None):
        """
        swipe down
        :param element: UI element, if None while swipe window of phone
        :param steps: steps of swipe for Android, The lower the faster
        :return: None
        """
        if element:
            rect = element.info['bounds']
            x_center = (rect['right'] - rect['left']) / 2 + rect['left']
            y_center = (rect['bottom'] - rect['top']) / 2 + rect['top']
            x_left = rect['left']
            y_up = rect['top']
            x_right = rect['right']
            y_down = rect['bottom']
            self.d.swipe(x_center, (y_down - y_up) / 4, x_center, y_down, 0.5)
            return True
        return False

    def swipe_down(self, count=1):
        """
        swipe down
        :param element: UI element, if None while swipe window of phone
        :param steps: steps of swipe for Android, The lower the faster
        :return: None
        """
        try:
            for i in range(int(count)):
                x, y = self._get_window_size()
                fromX = 0.5 * x
                fromY = 0.5 * y
                toX = 0.5 * x
                toY = 0.75 * y

                self._swipe(fromX, fromY, toX, toY, 0.5)
                return True
        except:
            return False

    def swipe_left(self, count=1):
        """
                swipe left
                :param count: swipe times,default once
                :return: None
                """
        try:
            for i in range(int(count)):
                x, y = self._get_window_size()
                fromX = 0.9 * x
                fromY = 0.5 * y
                toX = 0.2 * x
                toY = 0.5 * y
                self._swipe(fromX, fromY, toX, toY, 0.25)
                return True
        except:
            return False

    def swipe_left_by_element(self, element=None):
        """
        swipe left
        :param element: UI element, if None while swipe window of phone
        :param steps: steps of swipe for Android, The lower the faster
        :return: None
        """
        if element:
            rect = element.info['bounds']
            x_center = (rect['right'] - rect['left']) / 2 + rect['left']
            y_center = (rect['bottom'] - rect['top']) / 2 + rect['top']
            x_left = rect['left']
            y_up = rect['top']
            x_right = rect['right']
            y_down = rect['bottom']
            self.d.swipe(x_center, y_center, x_left, y_center, 0.5)
            return True
        return False

    def swipe_right(self, count=1):
        """
        swipe right
        :param count:
        :return: None
        """
        try:
            for i in range(int(count)):
                x, y = self._get_window_size()
                fromX = 0.2 * x
                fromY = 0.5 * y
                toX = 0.8 * x
                toY = 0.5 * y
                self._swipe(fromX, fromY, toX, toY, 0.5)
                return True
        except:
            return False

    def swipe_right_by_element(self, element=None):
        """
        swipe right
        :param element: UI element, if None while swipe window of phone
        :param steps: steps of swipe for Android, The lower the faster
        :return: None
        """
        if element:
            rect = element.info['bounds']
            x_center = (rect['right'] - rect['left']) / 2 + rect['left']
            y_center = (rect['bottom'] - rect['top']) / 2 + rect['top']
            x_left = rect['left']
            y_up = rect['top']
            x_right = rect['right']
            y_down = rect['bottom']
            self.d.swipe(x_center, y_center, x_right, y_center, 0.5)
            return True
        return False

    def click_by_element(self, element):
        try:
            element.click()
            # element.click_exists(timeout=1)
            # logger.info('click')
            # time.sleep(1)
            return True
        except Exception as e:
            # logger.info(e)
            # time.sleep(1)
            return False

    def long_click_by_element(self, element):
        try:
            element.long_click()
            return True
        except Exception as e:
            return False

    def get_text_by_element(self, element):
        if element is None:
            return False
        return element.get_text()

    def get_Current_Activity(self):
        return self.d.app_current().get('activity')

    def inputText(self, element, text):
        if element is None:
            return False
        if element.exists:
            element.clear_text()
            element.set_text(text)
            return True
        return False

    def input_text_by_adb(self, text):
        """
        用于输入框中输入特殊字符方法
        :param element: 输入框元素
        :param text: 输入字符串
        :return: True 默认成功 False输入框不存在
        """
        os.system("adb shell input text " + text)
        return True

    def escapeKeyBoard_by_adb(self):
        """
        收起软键盘
        :return: True 点击成功
        """
        os.system("adb shell input keyevent KEYCODE_ESCAPE")
        return True

    def checkPage(self, activity):
        '''
        start = time.process_time()
        time.sleep(2)
        currentAct = str(self.d.app_current().get('activity'))
        logging.info(currentAct)
        logging.info(activity)
        if currentAct == activity:
            result = True
        else:
            result = False
        logging.info('activity compare result ' + result)
        end = time.process_time()
        logging.info('Take %6.3f' % (end - start))
        '''
        # logger.info(str(self.d.app_current()))
        return str(self.d.app_current().get('activity')) == activity

    # 按键操作（方控、钢琴键）
    def pressButtenByKeyevent(self, keyevent):
        subprocess.Popen(keyevent, shell=True)

    # 通过模块名、键定位读取配置文件（注：暂时写死配置文件路径）
    def readConfigByModuleAndKey(self, project, module, key):
        path = 'UIconfig/' + project + '_propertiseConfig.ini'
        # logger.info(path)
        config = configparser.ConfigParser()
        try:
            config.read_file(open(path, encoding='UTF8'))
            value = config.get(module, key)
        except Exception as e:
            # logger.info('error ' + str(e))
            return False
        # logger.info(value)
        return str(value)

    # 读取整个module
    def readConfigItemsByModule(self, project, module):
        path = 'UIconfig/' + project + '_propertiseConfig.ini'
        config = configparser.ConfigParser()
        try:
            config.read_file(open(path, encoding='UTF8'))
            value = config.items(module)
        except Exception as e:
            return False
        # logger.info(value)
        return value


pm = PublicMethod()
