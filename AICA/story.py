import pygame
import time
from moviepy.editor import *
from settings import *

class Story:
    def __init__(self):
        self.quit = False

    def run(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(FPS)
            # 點擊視窗叉叉關閉
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    self.quit = True
                # 播放故事影片
                clip = VideoFileClip('AICA/video/story.mp4', audio=False)
                clip.preview()
                clip.close()
                run = False
                                             
            pygame.display.update()
