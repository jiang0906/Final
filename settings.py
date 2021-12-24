import pygame
import os
from moviepy.editor import *
import random


# 設置圖片
class Picture:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def clicked(self, x: int, y: int) -> bool:
        return True if self.rect.collidepoint(x, y) else False

    def draw(self, win):
        win.blit(self.image, self.rect)


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
START_BG = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, 'startmenu.jpeg')),
                                  (WIN_WIDTH, WIN_HEIGHT))

# score image
SCORE_BG = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, 'img.png')), (WIN_WIDTH, WIN_HEIGHT))

# select mode image
SELECT_BG = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, 'select.png')), (WIN_WIDTH, WIN_HEIGHT))

# game images
GAME_BG = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, 'game_sample.png')),
                                 (WIN_WIDTH, WIN_HEIGHT))

# image_dict = {}
material_dict = {}
index_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'I', 'J']


def load_material(idx):
    temp_dict = {}
    gesture_list = []
    for i in range(6):
        img = pygame.transform.scale(pygame.image.load('image/' + idx + f'{i}.png'), (WIN_WIDTH, WIN_HEIGHT))
        gesture_list.append(Picture(WIN_WIDTH / 2, WIN_HEIGHT / 2, img))

    temp_dict['topic'] = gesture_list
    temp_dict['clip'] = VideoFileClip('video/' + idx + '_video.mp4', audio=False)
    temp_dict['is_used'] = False
    return temp_dict


def choose_topic(temp_dict):
    random_index = random.choice(index_list)
    while temp_dict[random_index]['is_used']:
        random_index = random.choice(index_list)
    return random_index


'''
for index in index_list:
    image_dict[index] = load_image(index)
'''

for index in index_list:
    material_dict[index] = load_material(index)

'''
material_dict = 
{
    'A':
        {
            'topic':
            'clip':
            'is_used':
        }
    'B':
        {
            'topic':
            'clip':
            'is_used':
        }
    .
    .
    .
    'J':
        {
            'topic':
            'clip':
            'is_used':
        }
}
'''

# result image
RESULT_BG = []
for i in range(11):
    RESULT_BG.append(pygame.transform.scale(pygame.image.load(f'image/result{i}.png'), (WIN_WIDTH, WIN_HEIGHT)))
RESULT_TIME_BG = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, 'result_time.png')), (WIN_WIDTH, WIN_HEIGHT))
# color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
