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
font = pygame.font.SysFont('images/Roboto-Black.ttf', 25)

win2 = pygame.display.set_mode((SW, SH))
pygame.display.set_caption("testing")
"""                                            IMAGES LOAD    START                                                     """

background = [pygame.image.load("images/bg1.jpg").convert()]
background[0] = pygame.transform.rotate(background[0], 90)

"""                                            IMAGES LOAD    STOP                                                      """
Map = 0

n = Network()
player = n.getP()


def screen_draw(win2):
    win2.blit(background[Map], [0, 0])
    pygame.draw.line(win2, (0, 0, 0), (0, 130), (SW, 130), 2)
    pygame.draw.line(win2, (0, 0, 0), (SW / 2, 0), (SW / 2, 130), 3)
    win2.blit((font.render('Player Name : ', False, (0, 0, 0))), [10, 30])
    player.move(win2)
    if player2.melee:
        player2.do_melee(win2)
    else:
        player2.draw(win2)
    if player.melee:
        player.do_melee(win2)
    else:
        player.draw(win2)
    # print(player.x, player2.x)
    pygame.display.update()


def collision(player01, player02):
    if player01.melee:
        if player01.facing == 'right':
            for i in range(38):
                if player01.x + 45 == (player02.x + i):
                    return True
        if player01.facing == 'left':
            for i in range(48):
                if player01.x - 15 == ((player02.x + 38) - i):
                    return True
    elif player02.melee:
        if player02.facing == 'left':
            for i in range(38):
                if player01.x + 45 == (player02.x + i):
                    return True
        if player02.facing == 'right':
            for i in range(48):
                if player01.x - 15 == ((player02.x + 38) - i):
                    return True
    else:
        return False


clock = pygame.time.Clock()

run2 = True

while run2:
    clock.tick(24)
    player2 = n.send(player)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run2 = False
    collision(player, player2)
    screen_draw(win2)
pygame.quit()
