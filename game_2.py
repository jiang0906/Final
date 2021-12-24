import pygame
import random
import time
import globals
from pygame import MOUSEBUTTONDOWN
from moviepy.editor import *
from settings import *


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


# 限時模式
class Game2:
    def __init__(self):
        self.material_dict = material_dict  # load material from settings.py
        pygame.mixer.init()
        pygame.display.init()
        self.game_win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.button = Picture(WIN_WIDTH / 2, WIN_HEIGHT / 2, GAME_BG)
        self.sound = pygame.mixer.Sound(os.path.join(SOUND_PATH, 'GameMusic.mp3'))
        self.score = 0

    def play_music(self):
        pygame.mixer.init()
        pygame.mixer.music.load(os.path.join(SOUND_PATH, 'GameMusic.mp3'))
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

    def run(self):
        pygame.init()
        run = True
        clock = pygame.time.Clock()
        x, y = pygame.mouse.get_pos()
        self.play_music()

        random_index = choose_topic(self.material_dict)  # choose a random topic
        topic = self.material_dict[random_index]['topic']

        n = 0
        seconds = 200
        milliseconds = 0
        while run:
            pygame.display.set_caption("火影結印大賽-限時")    
            clock.tick()     
            topic[n].draw(self.game_win)         
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            # 題目
            # ...
                if event.type == MOUSEBUTTONDOWN:
                    if self.button.clicked(x, y) and n < 5:
                        n += 1
                        run = True
                    if n >= 5:
                        self.material_dict[random_index]['is_used'] = True  # mark topic is used
                        clip = self.material_dict[random_index]['clip']  # play video of corresponding index
                        clip.preview()
                        clip.close
                        n = 0
                        globals.score += 1
                        random_index = choose_topic(self.material_dict)  # choose unused topic randomly
                        topic = self.material_dict[random_index]['topic']

                        # self.end_time[0] = scorea
                        # print(self.end_time[0])
                        run = True



            # 計分(答對題數)
            # ...
            font = pygame.font.SysFont("simhei", 50)
            text_surface = font.render(f'score:{str(globals.score)}', True, BLACK)
            self.game_win.blit(text_surface, (500, 550))


            # 計時(倒數)
            # ...
            if milliseconds > 1000:
                seconds -= 1
                milliseconds -= 1000

            text_surface = font.render(str(seconds), True, BLACK)
            self.game_win.blit(text_surface, (550, 10))

            milliseconds += clock.tick_busy_loop(
                60)  # returns the time since the last time we called the function, and limits the frame rate to 60FPS

            if seconds == 0:
                run = False

            pygame.display.update()
        # pygame.quit()
            

