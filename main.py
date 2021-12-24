import pygame
from start_menu import StartMenu
from story import Story


if __name__ == '__main__':
    pygame.init()
    story = Story()
    story.run()
    m = StartMenu()
    m.run()



