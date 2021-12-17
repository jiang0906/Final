import pygame
import os

from pygame import display

from settings import *
from story import *
from select_mode import *
from game.game_1 import *
from game.game_2 import *

# 音樂&遊戲初始化
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
pygame.mixer.init()

# 測試階段，滑鼠點擊
class Buttons:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def clicked(self, x: int, y: int) -> bool:
        if self.rect.collidepoint(x, y):
            return True
        return False


class StartMenu:
    def __init__(self):
        # win
        self.menu_win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        # background
        self.bg = START_BG
        # button
        self.start_btn = Buttons(0, 0, WIN_WIDTH, WIN_HEIGHT)
        # music and sound
        self.sound = pygame.mixer.Sound(os.path.join(SOUND_PATH,'GameMusic.mp3'))
        # return mode
        self.mode = []

    def play_music(self):
        pygame.mixer.music.load(os.path.join(SOUND_PATH, 'GameMusic.mp3'))
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        self.sound.set_volume(0.5)

    def menu_run(self):
        run = True
        clock = pygame.time.Clock()
        pygame.display.set_caption("火影結印大賽")
        self.play_music()
        while run:
            clock.tick(FPS)
            self.menu_win.blit(self.bg, (0, 0))
            x, y = pygame.mouse.get_pos()
            for event in pygame.event.get():
                # 點擊視窗叉叉結束遊戲
                if event.type == pygame.QUIT:
                    run = False

                # 滑鼠點擊
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_btn.clicked(x, y):
                        story = Story()
                        story.run()
                        select = SelectMode()
                        select.run()
                        if 'game_1' in select.mode:
                            game1 = Game1()
                            game1.run()
                        if 'game_2' in select.mode:
                            game2 = Game2()
                            game2.run()

            pygame.display.update()
        pygame.quit()
                        
                        
                # 手勢辨識
                # 遊戲走向:故事/排行榜/結束遊戲

                # if 手勢為1:
                #    story = Story()
                #    story.run()
                #    select = SelectMode()
                #    select.run()
                # if 手勢為2:
                #    排行榜
                # if 手勢為3:
                #    run = False'''


