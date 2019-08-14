import pygame
from network import Network
from player import Player
import os
import time

x = 220
y = 100
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)

'''pygame.init()

win = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Launcher")
enter_name = font.render('Enter Player name : ', False, (255, 255, 255))
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    win.blit(enter_name, [10, 30])
pygame.quit()
'''
pygame.init()
SH = 600
SW = 950
font = pygame.font.Font('images/Roboto-Black.ttf', 30)
win2 = pygame.display.set_mode((SW, SH))
pygame.display.set_caption("testing")
"""                                            IMAGES LOAD    START                                                     """

background = [pygame.image.load("images/bg1.jpg").convert()]
background[0] = pygame.transform.rotate(background[0], 90)

"""                                            IMAGES LOAD    STOP                                                      """
Map = 0

n = Network()
player = n.getP()
playername = font.render('Player Name : ', False, (255, 255, 255))
score = font.render('score : ', False, (255, 255, 255))


def screen_draw(win2):
    win2.blit(background[Map], [0, 0])
    pygame.draw.line(win2, (0, 0, 0), (0, 130), (SW, 130), 2)
    pygame.draw.line(win2, (0, 0, 0), (SW / 2, 0), (SW / 2, 130), 3)
    win2.blit(playername, [10, 30])
    win2.blit(score, [10, 55])
    win2.blit(playername, [SW/2 + 10, 30])
    win2.blit(score, [SW/2 + 10, 55])
    player.move(win2)
    collision(player, player2)
    if player2.melee:
        player2.do_melee(win2)
    elif player2.is_dying:
        player2.do_death(win2)
    elif player2.is_dead:
        player2.draw(win2, player2.x)
    else:
        player2.draw(win2, player2.x)
    if player.melee:
        player.do_melee(win2)
    elif player.is_dying:
        player.do_death(win2)
    elif player.is_dead:
        player.draw(win2, player.x)
    else:
        player.draw(win2, player.x)
    pygame.display.update()


def collision(player01, player02):
    if player01.melee:
        if player01.facing == 'right':
            for i in range(38):
                if player01.x + 45 == (player02.x + i):
                    player02.is_dying = True
                    player02.is_dead = True
        if player01.facing == 'left':
            for i in range(48):
                if player01.x - 15 == ((player02.x + 38) - i):
                    player02.is_dying = True
                    player02.is_dead = True
                '''else:
                    player02.is_dying = False
                    player02.is_dead = False'''
    elif player02.melee:
        if player02.facing == 'left':
            for i in range(38):
                if player01.x + 45 == (player02.x + i):
                    player01.is_dying = True
                    player01.is_dead = True
        if player02.facing == 'right':
            for i in range(48):
                if player01.x - 15 == ((player02.x + 38) - i):
                    player01.is_dying = True
                    player01.is_dead = True
                '''else:
                    player01.is_dying = False
                    player01.is_dead = False'''
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
    screen_draw(win2)
pygame.quit()
