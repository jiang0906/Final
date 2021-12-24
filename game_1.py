import pygame
import random
import time
import os
import globals
from pygame import *
from moviepy.editor import *
from settings import *

# 音樂&遊戲初始化
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
pygame.mixer.init()


# 設置圖片
class Picture:
    def __init__(self,x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def clicked(self, x: int, y: int) -> bool:
        return True if self.rect.collidepoint(x, y) else False

    def draw(self, win):
        win.blit(self.image, self.rect)


# 計時模式
class Game1:
    def __init__(self):
        self.material_dict = material_dict  # load material from settings.py
        pygame.mixer.init()
        pygame.display.init()
        self.game_win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.button = Picture(WIN_WIDTH / 2, WIN_HEIGHT / 2, GAME_BG)
        self.sound = pygame.mixer.Sound(os.path.join(SOUND_PATH, 'GameMusic.mp3'))
        self.gesture_dict = {}

    def play_music(self):
        pygame.mixer.init()
        pygame.mixer.music.load(os.path.join(SOUND_PATH, 'GameMusic.mp3'))
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

    def run(self):
        pygame.init()
        clock = pygame.time.Clock()
        run = True
        x, y = pygame.mouse.get_pos()
        self.play_music()

        random_index = choose_topic(self.material_dict)  # choose a random topic
        topic = self.material_dict[random_index]['topic']

        n = 0  # gesture answered
        t = 0  # topic answered
        # score = 0
        sec = 0
        milliseconds = 0
        while run:  
            pygame.display.set_caption("火影結印大賽-計時")
            clock.tick(FPS)        
            topic[n].draw(self.game_win)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            # 題目
                if event.type == MOUSEBUTTONDOWN:
                    if self.button.clicked(x, y) and n < 5:
                        n += 1
                        run = True
                    if n >= 5:
                        self.material_dict[random_index]['is_used'] = True  # mark topic is used
                        clip = self.material_dict[random_index]['clip']  # play video of corresponding index
                        clip.preview()
                        clip.close
                        n = 0  # reset gesture answer number
                        t += 1  # topic right
                        # score += 1
                        random_index = choose_topic(self.material_dict)  # choose unused topic randomly
                        topic = self.material_dict[random_index]['topic']

                        run = True

                    if t >= 3:  # 總共3題
                        globals.sec = sec
                        run = False
                        
            # 計分(答對題數)
            # ...

            # 計時(正數like碼表)
            # 目前不太準?
            if milliseconds > 1000:
                sec += 1
                milliseconds -= 1000
                # print("{}".format(seconds))
            font = pygame.font.SysFont("simhei", 50)
            text_surface = font.render(str(sec), True, BLACK)
            self.game_win.blit(text_surface, (550, 10))

            milliseconds += clock.tick_busy_loop(
                60)  # returns the time since the last time we called the function, and limits the frame rate to 60FPS

            pygame.display.update()
        # pygame.quit()
