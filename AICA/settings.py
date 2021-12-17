import pygame
import os


# screen size
WIN_WIDTH = 1100
WIN_HEIGHT = 618

# frame rate
FPS = 60

# path
IMAGE_PATH = os.path.join(os.path.dirname(__file__), 'image')
SOUND_PATH = os.path.join(os.path.dirname(__file__), 'sound')
VIDEO_PATH = os.path.join(os.path.dirname(__file__), 'video')

# menu image
START_BG = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, 'startmenu.jpeg')), (WIN_WIDTH, WIN_HEIGHT))

# select mode image
SELECT_BG = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, 'select.jpeg')), (WIN_WIDTH, WIN_HEIGHT))

# game images
GAME_BG = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, 'game_sample.png')), (WIN_WIDTH, WIN_HEIGHT))


# color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)