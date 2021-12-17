import pygame
from settings import *

# 滑鼠點擊用
class Buttons:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def clicked(self, x: int, y: int) -> bool:
        if self.rect.collidepoint(x, y):
            return True
        return False


class SelectMode:
    def __init__(self):
        self.select_win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.game1_btn = Buttons(0, 0, WIN_WIDTH/2, WIN_HEIGHT)
        self.game2_btn = Buttons(WIN_WIDTH/2, 0, WIN_WIDTH/2, WIN_HEIGHT)
        self.bg = SELECT_BG
        # return mode
        self.mode = []
        

    def run(self):
        run = True
        while run:
            self.select_win.blit(self.bg, (0, 0))
            x, y = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    
                # 滑鼠測試用
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.game1_btn.clicked(x, y):
                        self.mode.append('game_1')
                        run = False
                        
                    if self.game2_btn.clicked(x, y):
                        self.mode.append('game_2')   
                        run = False

                # 手勢辨識
                '''
                if 手勢為左:
                    回傳一個值至startmenu 或是 另開一個model
                if 手勢為右:
                    回傳一個值至startmenu 或是 另開一個model
                '''

            pygame.display.update()    
        pygame.quit()