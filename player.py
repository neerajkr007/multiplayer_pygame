import pygame

pygame.display.init()
"""                                            IMAGES LOAD    START                                                     """

standing = [pygame.image.load('images/IdleR.png'), pygame.image.load('images/IdleL.png')]

runR = [pygame.image.load('images/Run1R.png'), pygame.image.load('images/Run2R.png'),
        pygame.image.load('images/Run3R.png'),
        pygame.image.load('images/Run4R.png'), pygame.image.load('images/Run5R.png'),
        pygame.image.load('images/Run6R.png'),
        pygame.image.load('images/Run7R.png'), pygame.image.load('images/Run8R.png')]
runL = [pygame.image.load('images/Run1L.png'), pygame.image.load('images/Run2L.png'),
        pygame.image.load('images/Run3L.png'),
        pygame.image.load('images/Run4L.png'), pygame.image.load('images/Run5L.png'),
        pygame.image.load('images/Run6L.png'),
        pygame.image.load('images/Run7L.png'), pygame.image.load('images/Run8L.png')]
meleeR = [pygame.image.load('images/melee1R.png'), pygame.image.load('images/melee2R.png'),
          pygame.image.load('images/melee3R.png'),
          pygame.image.load('images/melee4R.png'), pygame.image.load('images/melee5R.png'),
          pygame.image.load('images/melee6R.png'),
          pygame.image.load('images/melee7R.png'), pygame.image.load('images/melee8R.png')]
meleeL = [pygame.image.load('images/melee1L.png'), pygame.image.load('images/melee2L.png'),
          pygame.image.load('images/melee3L.png'),
          pygame.image.load('images/melee4L.png'), pygame.image.load('images/melee5L.png'),
          pygame.image.load('images/melee6L.png'),
          pygame.image.load('images/melee7L.png'), pygame.image.load('images/melee8L.png')]
dead = [pygame.image.load('images/dead1.png'), pygame.image.load('images/dead2.png'), pygame.image.load('images/dead3.png'),
        pygame.image.load('images/dead4.png'), pygame.image.load('images/dead5.png'), pygame.image.load('images/dead6.png'),
        pygame.image.load('images/dead7.png'), pygame.image.load('images/dead8.png'), pygame.image.load('images/dead9.png'),
        pygame.image.load('images/dead10.png')]
"""                                            IMAGES LOAD    STOP                                                      """


class Player(object):
    def __init__(self, x, y, color, facing):
        self.x = x
        self.xs = x
        self.y = y
        self.ys = y
        self.color = color
        self.velocity = 5
        self.height = 60
        self.width = 38
        self.walk_count = 0
        self.melee_count = 0
        self.death_count = 0
        self.facing = facing
        self.is_right = False
        self.is_left = False
        self.melee = False
        self.is_dying = False
        self.is_dead = False
        self.revive = 1

    def draw(self, win2, x):
        if self.walk_count + 1 >= 24:
            self.walk_count = 0

        if self.is_left:
            win2.blit(runL[self.walk_count // 3], (self.x - 20, self.y - 10))
            self.walk_count += 1
        elif self.is_right:
            win2.blit(runR[self.walk_count // 3], (self.x - 20, self.y - 10))
            self.walk_count += 1
        else:
            if self.facing == 'right':
                win2.blit(standing[0], [self.x - 20, self.y - 10])
            elif self.facing == 'left':
                win2.blit(standing[1], [self.x - 20, self.y - 10])
        if self.is_dead:
            self.x = self.xs
            self.is_dead = False
        else:
            self.x = x

    def do_melee(self, win2):
        if self.melee_count + 1 >= 24:
            self.melee_count = 0
            self.melee = False

        if self.facing == 'left'and self.melee:
            win2.blit(meleeL[self.melee_count // 3], (self.x - 20, self.y - 10))
            self.melee_count += 1
        elif self.facing == 'right' and self.melee:
            win2.blit(meleeR[self.melee_count // 3], (self.x - 20, self.y - 10))
            self.melee_count += 1

        else:
            if self.facing == 'right':
                win2.blit(standing[0], [self.x - 20, self.y - 10])
            elif self.facing == 'left':
                win2.blit(standing[1], [self.x - 20, self.y - 10])

    def do_death(self, win2):
        if self.death_count + 1 >= 28:
            self.death_count = 0
            self.is_dying = False
            self.revive -= 1
            if self.revive > 0:
                self.is_dead = False
                print('yo')
        win2.blit(dead[self.death_count // 3], (self.x - 20, self.y - 10))
        self.death_count += 1

    '''def do_revive(self, win2):
        if self.facing == 'right':
                win2.blit(standing[0], [self.xs - 20, self.ys - 10])
        elif self.facing == 'left':
                win2.blit(standing[1], [self.xs - 20, self.ys - 10])'''

    def move(self, win2):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.y >= 150:
            self.y -= self.velocity
            if self.facing == 'right':
                self.is_right = True
                self.is_left = False
            else:
                self.is_left = True
                self.is_right = False
        elif keys[pygame.K_s] and self.y <= 455 and (not (230 <= self.x <= 340 and 400 <= self.y <= 500)):
            self.y += self.velocity
            if self.facing == 'right':
                self.is_right = True
                self.is_left = False
            else:
                self.is_left = True
                self.is_right = False
        elif keys[pygame.K_d] and self.x <= 950 - self.width - 2 and (not (230 <= self.x <= 340 and 410 <= self.y <= 500)):
            self.facing = 'right'
            self.x += self.velocity
            self.is_right = True
            self.is_left = False
        elif keys[pygame.K_a] and self.x >= 2 and (not (245 <= self.x <= 355 and 410 <= self.y <= 500)):
            self.facing = 'left'
            self.x -= self.velocity
            self.is_left = True
            self.is_right = False
        elif keys[pygame.K_SPACE]:
            self.melee = True
        else:
            self.is_left = False
            self.is_right = False
