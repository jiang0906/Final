import pygame
from settings import *


# 計時模式
class Game1:
    def __init__(self):
        self.game_win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.bg = GAME_BG

    def run(self):
        pygame.init()
        run = True
        frame_count = 0
        font = pygame.font.Font(None, 70)
        clock = pygame.time.Clock()
        while run:
            self.game_win.blit(self.bg, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            # 題目
            # ...

            # 計分(答對題數)
            # ...

            # 計時(正數like碼表)
            # 目前不太準?
            '''     
            total_seconds = frame_count // FPS
            output_string = "{}".format(total_seconds)
            text_surface = font.render(output_string, True, BLACK)
            self.game_win.blit(text_surface, (550, 10))
            frame_count += 1
            clock.tick(FPS)
            '''

            pygame.display.flip()
        pygame.quit()
        