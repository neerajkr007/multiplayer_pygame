import pygame


class Bullet(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 4
        self.color = (255, 0, 0)
        self.vel = 10

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
