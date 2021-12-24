import pygame
import time
from moviepy.editor import *
from settings import *


class Story:
    def play_music(self):
        pygame.mixer.init()
        pygame.mixer.music.load(os.path.join(SOUND_PATH, 'MenuMusic.mp3'))
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

    def run(self):
        pygame.init()
        run = True
        clock = pygame.time.Clock()
        self.play_music()
        while run:
            clock.tick(FPS)
            # 點擊視窗叉叉關閉
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                # 播放故事影片
                clip = VideoFileClip('video/story.mp4', audio=False)
                clip.preview()
                clip.close()
                run = False
                break

            pygame.display.update()
        pygame.quit()
