import pygame
from settings import *

# 限時模式
class Game2:
    def __init__(self):
        self.game_win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.bg = GAME_BG

    def run(self):
        pygame.init()
        run = True
        while run:
            self.game_win.blit(self.bg, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            # 題目
            # ...

            # 計分(答對題數)
            # ...

            # 計時(倒數)
            # ...
                    

            pygame.display.update()
        pygame.quit()
            

