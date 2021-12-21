import pygame
import random
from pygame import *
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
        self.game_win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.button = Picture(WIN_WIDTH/2, WIN_HEIGHT/2, GAME_BG)
        self.A = []
        for i in range(6):
            self.A.append(Picture(WIN_WIDTH/2, WIN_HEIGHT/2, A_IMAGE[i]))
        self.B = []
        for i in range(6):
            self.B.append(Picture(WIN_WIDTH/2, WIN_HEIGHT/2, B_IMAGE[i]))
        self.C = []
        for i in range(6):
            self.C.append(Picture(WIN_WIDTH/2, WIN_HEIGHT/2, C_IMAGE[i]))
        self.D = []
        for i in range(6):
            self.D.append(Picture(WIN_WIDTH/2, WIN_HEIGHT/2, D_IMAGE[i]))
        self.E = []
        for i in range(6):
            self.E.append(Picture(WIN_WIDTH/2, WIN_HEIGHT/2, E_IMAGE[i]))
        self.F = []
        for i in range(6):
            self.F.append(Picture(WIN_WIDTH/2, WIN_HEIGHT/2, F_IMAGE[i]))
        self.G = []
        for i in range(6):
            self.G.append(Picture(WIN_WIDTH/2, WIN_HEIGHT/2, G_IMAGE[i]))
        self.H = []
        for i in range(6):
            self.H.append(Picture(WIN_WIDTH/2, WIN_HEIGHT/2, H_IMAGE[i]))
        self.I = []
        for i in range(6):
            self.I.append(Picture(WIN_WIDTH/2, WIN_HEIGHT/2, I_IMAGE[i]))
        self.J = []
        for i in range(6):
            self.J.append(Picture(WIN_WIDTH/2, WIN_HEIGHT/2, J_IMAGE[i]))
        self.topic = [self.A, self.B, self.C, self.D, self.E, 
                    self.F, self.G, self.H, self.I, self.J]
        self.A_video = VideoFileClip('AICA/video/A_video.mp4', audio=False)
        self.G_video = VideoFileClip('AICA/video/G_video.mp4', audio=False)
        self.C_video = VideoFileClip('AICA/video/C_video.mp4', audio=False)
        self.H_video = VideoFileClip('AICA/video/H_video.mp4', audio=False)
        self.I_video = VideoFileClip('AICA/video/I_video.mp4', audio=False)
        self.video = [self.A_video, self.G_video, self.C_video, self.H_video, self.I_video]

    def play_music(self):
        pygame.mixer.init()
        pygame.mixer.music.load(os.path.join(SOUND_PATH, 'GameMusic.mp3'))
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        self.sound.set_volume(0.5)

    def run(self):
        pygame.init()
        run = True
        clock = pygame.time.Clock()
        x, y = pygame.mouse.get_pos()
        self.play_music()
        topic = random.choice(self.topic)
        n = 0
        t = 0   
        while run:
            pygame.display.set_caption("火影結印大賽")    
            clock.tick()     
            topic[n].draw(self.game_win)
            start = time.time()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            # 題目
            # ...
                if event.type == MOUSEBUTTONDOWN:
                    if self.button.clicked(x, y) and n < 6:
                        n += 1
                        run = True
                    if n >= 6:
                        clip = random.choice(self.video)
                        clip.preview()
                        clip.close
                        n = 0
                        t += 1
                        topic = random.choice(self.topic)
                        run = True

                    
            # 題目
            # ...

            # 計分(答對題數)
            # ...

            # 計時(倒數)
            # ...
                    

            pygame.display.update()
        pygame.quit()
            

