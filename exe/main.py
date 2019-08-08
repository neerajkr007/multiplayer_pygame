import pygame
from network import Network

pygame.init()
SH = 600
SW = 950

win = pygame.display.set_mode((SW, SH))
pygame.display.set_caption("testing")

background = [pygame.image.load("bg1.jpg").convert()]
background[0] = pygame.transform.rotate(background[0], 90)

Map = 0


class Player(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity = 5
        self.height = 40
        self.width = 15

    def draw(self, win):
        pygame.draw.rect(win, (0, 0, 0), (self.x, self.y, self.width, self.height))

    def move(self):
        if keys[pygame.K_w] and player1.y >= 150:
            player1.y -= player1.velocity
        if keys[pygame.K_d] and player1.x <= SW - player1.width - 2 and (not(230 <= player1.x <= 340 and 430 <= player1.y <= 500)):
            player1.x += player1.velocity
        if keys[pygame.K_s] and player1.y <= 455 and (not(230 <= player1.x <= 340 and 420 <= player1.y <= 500)):
            player1.y += player1.velocity
        if keys[pygame.K_a] and player1.x >= 2 and (not(245 <= player1.x <= 355 and 430 <= player1.y <= 500)):
            player1.x -= player1.velocity
        if keys[pygame.K_SPACE]:
            pass
        """""
        if keys[pygame.K_UP] and player2.y >= 150:
            player2.y -= player2.velocity
        if keys[pygame.K_RIGHT] and player2.x <= SW - player2.width - 2 and (not(230 <= player2.x <= 340 and 430 <= player2.y <= 500)):
            player2.x += player2.velocity
        if keys[pygame.K_DOWN] and player2.y <= 455 and (not(230 <= player2.x <= 340 and 420 <= player2.y <= 500)):
            player2.y += player2.velocity
        if keys[pygame.K_LEFT] and player2.x >= 2 and (not(245 <= player2.x <= 355 and 430 <= player2.y <= 500)):
            player2.x -= player2.velocity
        if keys[pygame.K_SPACE]:
            pass"""


def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])


def screen_draw(win):
    win.blit(background[Map], [0, 0])
    player1.draw(win)
    player2.draw(win)
    pygame.display.update()


clock = pygame.time.Clock()

run = True
n = Network()
startPos = read_pos(n.getPos())
player1 = Player(startPos[0], startPos[1])
player2 = Player(350, 300)
players = [player1, player2]
while run:

    clock.tick(30)

    player2_pos = read_pos(n.send(make_pos((player1.x, player1.y))))
    player2.x = player2_pos[0]
    player2.y = player2_pos[1]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    player1.move()
    screen_draw(win)

pygame.quit()

