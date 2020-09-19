import os

import pygame
from UIconfig.Base import Base
from page.PublicMethod import PublicMethod as pm
import time
import UIconfig.logger as loggers

logger = loggers.Logger()


class india_D90_voice(Base):

    def wakeUpVoice(self):
        '''
        唤醒语音，通过'adb shell input keyevent 290'
        :return: 语音唤起返回True，唤起失败返回False
        '''
        os.system('adb shell input keyevent 290')
        time.sleep(2)
        element = pm().find_element_by_id('com.saicmotor.voicevui:id/user_speak_ll')
        if element is not None:
            return True
        else:
            return False

    def playVoice(self, file):
        '''
        初始化音频播放器
        播放该路径下的声音文件，播放 2 秒后自动停止

        :param file 音频文件的文件名
        :return 播放成功返回True，播放失败返回False
        '''
        for (dirpath, dirnames, filenames) in os.walk(os.path.abspath('.') + '/audio/'):
            if file in filenames:
                file = dirpath + '/' + file
                pygame.mixer.init()
                pygame.mixer.music.load(file)
                pygame.mixer.music.play()
                time.sleep(5)
                return True
            else:
                continue
        return False

    def checkVoice(self):
        '''
        检查语音是否启动
        :return: 启动返回True，未启动返回False
        '''
        element = pm().find_element_by_id('com.saicmotor.voicevui:id/drag_anchor_layout')
        if element is not None:
            return True
        else:
            return False
