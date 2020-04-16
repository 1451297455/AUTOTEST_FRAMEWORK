from page.BasePage import BasePage
from page.publicMethod import publicMethod as pm
import time

Map = 'com.tomtom.alishanapp'
Weather = 'com.saicmotor.weathers'


class map(BasePage):

    def openMap(self):
        pm.openApp(Map)

    def stopMap(self):
        pm.stopApp(Map)

    def findText(self):
        element = pm.find_element_by_text(self, 'Cancel')
        time.sleep(10)
        if element.exists():
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
            pm.screenshot('error')
            print(pm.get_text_by_element(self, element))
            return True

    def getToast(self):
        text = pm.get_toast_message()
        if text != None:
            print(text)
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
