from pygame.draw import *
from random import randint
pygame.init()

FPS = 100 
screen = pygame.display.set_mode((1200, 800))

rect(screen, (255, 255, 255), (15, 45, 1170, 740), 5)

F = 0
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
BALLS = []
pygame.quit()
