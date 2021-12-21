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
SELECT_BG = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, 'select.png')), (WIN_WIDTH, WIN_HEIGHT))

# game images
GAME_BG = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, 'game_sample.png')), (WIN_WIDTH, WIN_HEIGHT))
A_IMAGE = []
for i in range(6):
    A_IMAGE.append(pygame.transform.scale(pygame.image.load(f"AICA/image/A{i}.png"), (WIN_WIDTH, WIN_HEIGHT)))
B_IMAGE = []
for i in range(6):
    B_IMAGE.append(pygame.transform.scale(pygame.image.load(f"AICA/image/B{i}.png"), (WIN_WIDTH, WIN_HEIGHT)))
C_IMAGE = []
for i in range(6):
    C_IMAGE.append(pygame.transform.scale(pygame.image.load(f"AICA/image/C{i}.png"), (WIN_WIDTH, WIN_HEIGHT)))
D_IMAGE = []
for i in range(6):
    D_IMAGE.append(pygame.transform.scale(pygame.image.load(f"AICA/image/D{i}.png"), (WIN_WIDTH, WIN_HEIGHT)))
E_IMAGE = []
for i in range(6):
    E_IMAGE.append(pygame.transform.scale(pygame.image.load(f"AICA/image/E{i}.png"), (WIN_WIDTH, WIN_HEIGHT)))
F_IMAGE = []
for i in range(6):
    F_IMAGE.append(pygame.transform.scale(pygame.image.load(f"AICA/image/F{i}.png"), (WIN_WIDTH, WIN_HEIGHT)))
G_IMAGE = []
for i in range(6):
    G_IMAGE.append(pygame.transform.scale(pygame.image.load(f"AICA/image/G{i}.png"), (WIN_WIDTH, WIN_HEIGHT)))
H_IMAGE = []
for i in range(6):
    H_IMAGE.append(pygame.transform.scale(pygame.image.load(f"AICA/image/H{i}.png"), (WIN_WIDTH, WIN_HEIGHT)))
I_IMAGE = []
for i in range(6):
    I_IMAGE.append(pygame.transform.scale(pygame.image.load(f"AICA/image/I{i}.png"), (WIN_WIDTH, WIN_HEIGHT)))
J_IMAGE = []
for i in range(6):
    J_IMAGE.append(pygame.transform.scale(pygame.image.load(f"AICA/image/J{i}.png"), (WIN_WIDTH, WIN_HEIGHT)))

# result image
RESULT_BG = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, 'result.jpg')), (WIN_WIDTH, WIN_HEIGHT))

# color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)