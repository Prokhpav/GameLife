from .Input import *
import numpy as np


class Colors:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)


class Globals:
    screen = pygame.display.set_mode((600, 600))
    timer = pygame.time.Clock()

    speed = 5

    max_size = (60, 60)
    desk = np.zeros(max_size)
    max_size = (max_size[0] - 1, max_size[1] - 1)
    desk.dtype = np.int64
    alive = set()
