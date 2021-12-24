import pygame
import globals
from settings import *

# 滑鼠點擊用
class Buttons:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def clicked(self, x: int, y: int) -> bool:
        if self.rect.collidepoint(x, y):
            return True
        return False

class Result1:
    def __init__(self):
        pygame.init()
        self.result_win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.result_btn = Buttons(0, 0, WIN_WIDTH, WIN_HEIGHT)

    def play_music(self):
        pygame.mixer.init()
        pygame.mixer.music.load(os.path.join(SOUND_PATH, 'MenuMusic.mp3'))
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

    def run(self):
        run = True
        clock = pygame.time.Clock()
        self.play_music()
        while run:
            pygame.init()
            pygame.display.set_caption("火影結印大賽-時間")
            clock.tick(FPS)
            sec = globals.sec
            self.result_win.blit(RESULT_TIME_BG, (0, 0))
            font = pygame.font.SysFont("simhei", 100)
            text = font.render(str(sec), True, BLACK)
            self.result_win.blit(text, (510, 310))

            x, y = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.result_btn.clicked(x, y):
                        run = False

            # read file
            path = 'time.txt'
            f = open(path, 'r')  # 'w+' means read and write, can overwrite the file

            timeList = []
            for line in f.readlines():
                timeList.append(int(line))
                print(line)
            f.close()

            sec = globals.sec
            timeList.append(sec)
            repeat = False
            for i in range(3):
                if (timeList[i] == timeList[3]):
                    repeat = True
            if (not repeat):
                timeList.sort()
                f = open(path, 'w')
                for line in range(3):
                    f.write(str(timeList[line]) + '\n')

            pygame.display.update()
        # pygame.quit()
