import pygame
from network import Network
from player import Player
import os

x = 220
y = 100
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)

pygame.init()
font = pygame.font.Font('images/Roboto-Black.ttf', 16)
win = pygame.display.set_mode((400, 200))
pygame.display.set_caption("Launcher")
enter_name = font.render('Enter Player name : ', False, (255, 255, 255))
run = True
playername = ""
name = ""


def screendraw(win):
    win.fill([30, 30, 30])
    win.blit(enter_name, [10, 30])
    block = font.render(playername, True, (0, 0, 0))
    pygame.draw.rect(win, (200, 200, 200), (160, 30, 150, 20))
    win.blit(block, [160, 30])
    #pygame.draw.rect(win, (0, 100, 0), (150, 100, 100, 30))
    #win.blit(font.render('START', True, (0, 0, 0)), [170, 105])
    pygame.display.update()


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.unicode.isalpha():
                playername += event.unicode
                # name = playername
            elif event.key == pygame.K_BACKSPACE:
                # name = playername
                playername = playername[:-1]
            elif event.key == pygame.K_RETURN:
                name = playername
                playername = ""
        '''if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] >= 150 and pygame.mouse.get_pos()[1] >= 100:
                if pygame.mouse.get_pos()[0] <= 250 and pygame.mouse.get_pos()[1] <= 130:
                    flag = 1
'''
    screendraw(win)
pygame.quit()


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
player.name = name


def screen_draw(win2):
    win2.blit(background[Map], [0, 0])
    pygame.draw.line(win2, (0, 0, 0), (0, 130), (SW, 130), 2)
    pygame.draw.line(win2, (0, 0, 0), (SW / 2, 0), (SW / 2, 130), 3)
    win2.blit(playername, [10, 30])
    win2.blit(score, [10, 55])
    win2.blit(playername, [SW/2 + 10, 30])
    win2.blit(score, [SW/2 + 10, 55])
    if player.xs == 150:
        win2.blit(name1, [200, 30])
        win2.blit(name2, [675, 30])
        win2.blit(score1, [580, 55])
        win2.blit(score2, [110, 55])
    if player.xs == 850:
        win2.blit(name1, [675, 30])
        win2.blit(name2, [200, 30])
        win2.blit(score1, [110, 55])
        win2.blit(score2, [580, 55])
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
                if player01.x + 45 == (player02.x + i) and ((player01.y - 10) < player02.y < player01.y + 10):
                    player02.is_dying = True
                    player02.is_dead = True
        if player01.facing == 'left':
            for i in range(48):
                if player01.x - 15 == ((player02.x + 38) - i) and ((player01.y - 10) < player02.y < player01.y + 10):
                    player02.is_dying = True
                    player02.is_dead = True

    elif player02.melee:
        if player02.facing == 'left':
            for i in range(38):
                if player01.x + 45 == (player02.x + i) and ((player02.y - 50) < player01.y < player02.y + 50):
                    player01.is_dying = True
                    player01.is_dead = True
        if player02.facing == 'right':
            for i in range(48):
                if player01.x - 15 == ((player02.x + 38) - i) and ((player02.y - 50) < player01.y < player02.y + 50):
                    player01.is_dying = True
                    player01.is_dead = True

    else:
        return False


clock = pygame.time.Clock()
run2 = True

while run2:
    clock.tick(24)
    player2 = n.send(player)
    name1 = font.render(player.name, False, (255, 255, 255))
    score1 = font.render(str(player.score), False, (255, 255, 255))
    name2 = font.render(player2.name, False, (255, 255, 255))
    score2 = font.render(str(player2.score), False, (255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run2 = False
    screen_draw(win2)
pygame.quit()

