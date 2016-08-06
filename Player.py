#!/usr/local/env python
# coding=utf-8
'''
 Author: Archer
 File: Player.py
 Desc: 对PyGame的音频播放功能的封装
 Date: 6/Aug/2016
'''
import pygame

class Player(object):
    AudioFile = None
    State = None # play, paused, stopped

    def __init__(self, audioFile):
        self.AudioFile = audioFile
        self.initMixer()

    #　播放
    def Play(self):
        if self.State == 'play':
            return False
        elif self.State == 'paused':
            return False
        elif self.State == 'stopped':
            return False

        self.State = 'play'
        self.playmusic(self.AudioFile)
        return True

    # 暂停
    def Pause(self):
        """ temporarily stop music playback"""
        if self.State == 'paused':
            return False
        elif self.State == 'stopped':
            return False

        self.State = 'paused'
        pygame.mixer.music.pause()

        return True

    # 重新播放
    def Resume(self):
        """ unpause temporarily stopped music playback"""
        if self.State == 'stopped':
            return False
        elif self.State == 'play':
            return False

        self.State = 'play'
        pygame.mixer.music.unpause()
        return True

    # 停止
    def Stop(self):
        if self.State == 'stopped':
            return False

        self.State = 'stopped'
        self.stopmusic()
        return True

    # 快进
    def Forward(self):
        pass
    # 快退
    def Backward(self):
        pass

    #　获取音量值
    def GetVolume(self):
        return pygame.mixer.music.get_volume()

    # 增加音量
    def IncreaseVolume(self):
        current = pygame.mixer.music.get_volume()
        if current == 1.0:
            return False
        elif current >= 1.0:
            return False

        if 1.0 - current < 0.1:
            pygame.mixer.music.set_volume(1.0)
        else:
            pygame.mixer.music.set_volume(current + 0.1)

        return True

    # 减少音量
    def DecreaseVolume(self):
        current = pygame.mixer.music.get_volume()
        if current == 0.0:
            return False

        if current <= 0.1:
            pygame.mixer.music.set_volume(0.0)
        else:
            pygame.mixer.music.set_volume(current - 0.1)

        return True

    def playsound(self, soundfile):
        """Play sound through default mixer channel in blocking manner.
           This will load the whole sound into memory before playback
        """
        pygame.init()
        pygame.mixer.init()
        sound = pygame.mixer.Sound(soundfile)
        clock = pygame.time.Clock()
        sound.play()
        while pygame.mixer.get_busy():
            print "Playing..."
            clock.tick(1000)

    def playmusic(self, soundfile):
        """Stream music with mixer.music module in blocking manner.
           This will stream the sound from disk while playing.
        """
        pygame.init()
        pygame.mixer.init()
        clock = pygame.time.Clock()
        pygame.mixer.music.load(soundfile)
        pygame.mixer.music.play()
        # while pygame.mixer.music.get_busy():
        #     #print "Playing..."
        #     clock.tick(1000)

    def stopmusic(self):
        """stop currently playing music"""
        pygame.mixer.music.stop()

    def getmixerargs(self):
        pygame.mixer.init()
        freq, size, chan = pygame.mixer.get_init()
        return freq, size, chan

    def initMixer(self):
    	BUFFER = 3072  # audio buffer size, number of samples since pygame 1.8.
    	FREQ, SIZE, CHAN = self.getmixerargs()
    	pygame.mixer.init(FREQ, SIZE, CHAN, BUFFER)
