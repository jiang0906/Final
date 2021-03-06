import pygame
import globals
from settings import *
from game_2 import Game2


# 滑鼠點擊用
class Buttons:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def clicked(self, x: int, y: int) -> bool:
        if self.rect.collidepoint(x, y):
            return True
        return False


class Result2:
    def __init__(self):
        pygame.mixer.init()
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
            pygame.display.set_caption("火影結印大賽-得分題數")
            clock.tick(FPS)
            score = globals.score
            # print(score)
            self.result_win.blit(RESULT_BG[score], (0, 0))
            # self.result_win.blit(RESULT_BG, (0, 0))
            x, y = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.result_btn.clicked(x, y):
                        run = False

            # read file
            path = 'score.txt'
            f = open(path, 'r')  # 'w+' means read and write, can overwrite the file

            scoreList = []
            for line in f.readlines():
                scoreList.append(int(line))
                print(line)
            f.close()

            score = globals.score
            scoreList.append(score)
            repeat = False
            for i in range(3):
                if (scoreList[i] == scoreList[3]):
                    repeat = True
            if (not repeat):
                scoreList.sort(reverse=True)
                # print(scoreList)
                f = open(path, 'w')
                for line in range(3):
                    f.write(str(scoreList[line]) + '\n')

            pygame.display.update()
        # pygame.quit()
