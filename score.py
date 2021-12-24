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


class Score:
    def __init__(self):
        self.score_win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.score_btn = Buttons(0, 0, WIN_WIDTH, WIN_HEIGHT)

    def play_music(self):
        pygame.mixer.init()
        pygame.mixer.music.load(os.path.join(SOUND_PATH, 'MenuMusic.mp3'))
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

    def run(self):
        run = True
        clock = pygame.time.Clock()
        self.play_music()

        # read file
        path = 'score.txt'
        f = open(path, 'r')  # 'w+' means read and write, can overwrite the file

        scoreList = []
        for line in f.readlines():
            scoreList.append(int(line))
            print(line)
        f.close()

            # orange color(224,150,1)
            # blue color (99,124,165)

        # cost time
        # read file
        path = 'time.txt'
        f = open(path, 'r')  # 'w+' means read and write, can overwrite the file

        timeList = []
        for line in f.readlines():
            timeList.append(int(line))
            print(line)
        f.close()



        while run:
            pygame.display.set_caption("火影結印大賽-排行榜")
            clock.tick(FPS)
            self.score_win.blit(SCORE_BG, (0, 0))
            font = pygame.font.SysFont("simhei", 80)
            text = font.render(str(scoreList[0]), True, (224, 150, 1))  # text, , font color, back color
            self.score_win.blit(text, (480, 505))  # position
            font = pygame.font.SysFont("simhei", 50)
            text = font.render(str(scoreList[1]), True, (224, 150, 1))  # text, , font color, back color
            self.score_win.blit(text, (280, 530))  # position
            font = pygame.font.SysFont("simhei", 50)
            text = font.render(str(scoreList[2]), True, (224, 150, 1))  # text, , font color, back color
            self.score_win.blit(text, (710, 525))  # position
            # time
            font = pygame.font.SysFont("simhei", 80)
            text = font.render(str(timeList[0]), True, (99, 124, 165))  # text, , font color, back color
            self.score_win.blit(text, (460, 210))  # position
            font = pygame.font.SysFont("simhei", 50)
            text = font.render(str(timeList[1]), True, (99, 124, 165))  # text, , font color, back color
            self.score_win.blit(text, (265, 235))  # position
            font = pygame.font.SysFont("simhei", 50)
            text = font.render(str(timeList[2]), True, (99, 124, 165))  # text, , font color, back color
            self.score_win.blit(text, (700, 230))

            x, y = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.score_btn.clicked(x, y):
                        run = False

            pygame.display.update()
        # pygame.quit()
