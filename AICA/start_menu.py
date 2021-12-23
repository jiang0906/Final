import pygame
import os
from settings import *
from story import *
from select_mode import *
from score import *
from game_1 import *
from game_2 import *
from result import *

# 音樂&遊戲初始化
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
pygame.mixer.init()
pygame.display.init()

# 滑鼠點擊
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
        # button
        self.start_btn = Buttons(0, 0, WIN_WIDTH, WIN_HEIGHT/2)
        self.score_btn = Buttons(0, WIN_HEIGHT/2, WIN_WIDTH, WIN_HEIGHT/2)
        # music and sound
        self.sound = pygame.mixer.Sound(os.path.join(SOUND_PATH,'MenuMusic.mp3'))
        # return mode
        self.mode = []

    def play_music(self):
        pygame.mixer.music.load(os.path.join(SOUND_PATH, 'MenuMusic.mp3'))
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        self.sound.set_volume(0.5)

    def menu_run(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.init()
        run = True
        clock = pygame.time.Clock()
        pygame.display.set_caption("火影結印大賽")
        self.play_music()
        while run:
            clock.tick(FPS)
            self.menu_win.blit(START_BG, (0, 0))
            x, y = pygame.mouse.get_pos()
            for event in pygame.event.get():
                # 點擊視窗叉叉結束遊戲
                if event.type == pygame.QUIT:
                    run = False

                # 滑鼠點擊
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_btn.clicked(x, y):
                        story = Story()
                        # story.run()
                        select = SelectMode()
                        select.run()
                        if 'game_1' in select.mode:
                            game1 = Game1()
                            game1.run()
                        if 'game_2' in select.mode:
                            game2 = Game2()
                            game2.run()
                        result = Result()
                        result.run()
                        run = True
                                            
                    if self.score_btn.clicked(x, y):
                        score = Score()
                        score.run()
                    

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


