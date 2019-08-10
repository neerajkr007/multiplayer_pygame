import pygame
from network import Network
from player import Player
import os

x = 220
y = 100
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)

'''pygame.init()

win = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Launcher")

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
'''
pygame.init()
SH = 600
SW = 950

win2 = pygame.display.set_mode((SW, SH))
pygame.display.set_caption("testing")
"""                                            IMAGES LOAD    START                                                     """

background = [pygame.image.load("bg1.jpg").convert()]
background[0] = pygame.transform.rotate(background[0], 90)

"""                                            IMAGES LOAD    STOP                                                      """
Map = 0


def screen_draw(win2):
    win2.blit(background[Map], [0, 0])
    player2.draw(win2)
    player.draw(win2)
    pygame.display.update()


clock = pygame.time.Clock()

run2 = True
n = Network()


player = n.getP()
while run2:
    player2 = n.send(player)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run2 = False

    player.move()
    screen_draw(win2)
    clock.tick(30)

pygame.quit()
