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

background = [pygame.image.load("images/bg1.jpg").convert()]
background[0] = pygame.transform.rotate(background[0], 90)

"""                                            IMAGES LOAD    STOP                                                      """
Map = 0

n = Network()
player = n.getP()


def screen_draw(win2):
    win2.blit(background[Map], [0, 0])
    player2.draw(win2)
    player.draw(win2)
    player.move()
    '''if player2.is_right:
        win2.blit(standing[0], [player2.x - 20, player2.y - 10])
    else:
        win2.blit(standing[1], [player2.x - 20, player2.y - 10])
    player.draw(win2)
    if player.is_right:
        win2.blit(standing[0], [player.x - 20, player.y - 10])
    else:
        win2.blit(standing[1], [player.x - 20, player.y - 10])
'''
    '''player.draw(win2)
    if player.walk_count + 1 >= 24:
        player.walk_count = 0
        # pygame.draw.rect(win, (0, 100, 0), (player.x, player.y, player. width, player.height))
    if player.is_left:
        win2.blit(runL[player.walk_count // 4], [player.x - 20, player.y - 10])
        player.walk_count += 1
    elif player.is_right:
        win2.blit(runR[player.walk_count // 4], [player.x - 20, player.y - 10])
        player.walk_count += 1
    else:
        if player2.is_right:
            win2.blit(standing[0], [player2.x - 20, player2.y - 10])
        else:
            win2.blit(standing[1], [player2.x - 20, player2.y - 10])
        if player.is_right:
            win2.blit(standing[0], [player.x - 20, player.y - 10])
        else:
            win2.blit(standing[1], [player.x - 20, player.y - 10])
    '''
    pygame.display.update()


clock = pygame.time.Clock()

run2 = True


while run2:
    clock.tick(24)
    player2 = n.send(player)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run2 = False

    screen_draw(win2)
pygame.quit()
