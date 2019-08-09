import pygame


class Player(object):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.velocity = 5
        self.height = 40
        self.width = 15
        self.status = "online"

    def draw(self, win2):
        pygame.draw.rect(win2, self.color, (self.x, self.y, self.width, self.height))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.y >= 150:
            self.y -= self.velocity
        if keys[pygame.K_d] and self.x <= 950 - self.width - 2 and (not(230 <= self.x <= 340 and 430 <= self.y <= 500)):
            self.x += self.velocity
        if keys[pygame.K_s] and self.y <= 455 and (not(230 <= self.x <= 340 and 420 <= self.y <= 500)):
            self.y += self.velocity
        if keys[pygame.K_a] and self.x >= 2 and (not(245 <= self.x <= 355 and 430 <= self.y <= 500)):
            self.x -= self.velocity
        if keys[pygame.K_SPACE]:
            pass
