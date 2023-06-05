import pygame
import sys

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Walking Animation")

BG = pygame.image.load("assets/ChainsawBackground.png")

white = (255, 255, 255)
WALK_RIGHT = [pygame.image.load('assets/R1.png'), pygame.image.load('assets/R2.png'), pygame.image.load('assets/R3.png'), pygame.image.load('assets/R4.png'), pygame.image.load('assets/R5.png'), pygame.image.load('assets/R6.png'), pygame.image.load('assets/R7.png'), pygame.image.load('assets/R8.png'), pygame.image.load('assets/R9.png')]
WALK_LEFT = [pygame.image.load('assets/L1.png'), pygame.image.load('assets/L2.png'), pygame.image.load('assets/L3.png'), pygame.image.load('assets/L4.png'), pygame.image.load('assets/L5.png'), pygame.image.load('assets/L6.png'), pygame.image.load('assets/L7.png'), pygame.image.load('assets/L8.png'), pygame.image.load('assets/L9.png')]
CHAR = pygame.image.load('assets/standing.png')

x = 25
y = 330
WIDTH = 384
HEIGHT = 384
VEL = 5

font = pygame.font.Font("assets/font.ttf", 20)
Player_1 = font.render('Player 1', True, white)
textRect = Player_1.get_rect()
textRect.topleft = (30, 80)

Player_2 = font.render('Player 2', True, white)
textRect_2 = Player_2.get_rect()
textRect_2.topright = (1110, 80)


CLOCK = pygame.time.Clock()

IS_JUMP = False
JUMP_COUNT = 10

LEFT = False
RIGHT = False
WALK_COUNT = 0

def redrawGameWindow():
    global WALK_COUNT
    
    SCREEN.blit(BG, (0,0))  
    if WALK_COUNT + 1 >= 45:
        WALK_COUNT = 0
        
    if LEFT:  
        SCREEN.blit(WALK_LEFT[WALK_COUNT//5], (x,y))
        WALK_COUNT += 1                          
    elif RIGHT:
        SCREEN.blit(WALK_RIGHT[WALK_COUNT//5], (x,y))
        WALK_COUNT += 1
    else:
        SCREEN.blit(CHAR, (x, y))
        WALK_COUNT = 0
    
class HealthBar():
  def __init__(self, x, y, w, h, max_hp):
    self.x = x
    self.y = y
    self.w = w
    self.h = h
    self.hp = max_hp
    self.max_hp = max_hp

  def draw(self, surface):
    #calculate health ratio
    ratio = self.hp / self.max_hp
    pygame.draw.rect(surface, "red", (self.x, self.y, self.w, self.h))
    pygame.draw.rect(surface, "green", (self.x, self.y, self.w * ratio, self.h))

health_bar = HealthBar(30, 30, 300, 40, 100)

class HealthBar2():
  def __init__(self, x_2, y_2, w_2, h_2, max_hp_2):
    self.x_2 = x_2
    self.y_2 = y_2
    self.w_2 = w_2
    self.h_2 = h_2
    self.hp_2 = max_hp_2
    self.max_hp_2 = max_hp_2

  def draw_2(self, surface):
    #calculate health ratio
    ratio_2 = self.hp_2 / self.max_hp_2
    pygame.draw.rect(surface, "red", (self.x_2, self.y_2, self.w_2, self.h_2))
    pygame.draw.rect(surface, "green", (self.x_2, self.y_2, self.w_2* ratio_2, self.h_2))

health_bar_2 = HealthBar2(950, 30, 300, 40, 100)

RUN = True

global hp_perc_1
global hp_perc_2

hp_perc_1 = 100
hp_perc_2 = 100

while RUN:
    CLOCK.tick(45)

    SCREEN.blit(Player_1, textRect)
    SCREEN.blit(Player_2, textRect_2)
    
    health_bar.hp = hp_perc_1
    health_bar.draw(SCREEN)

    health_bar_2.hp_2 = hp_perc_2
    health_bar_2.draw_2(SCREEN)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > VEL:
        x -= VEL
        LEFT = True
        RIGHT = False

    elif keys[pygame.K_RIGHT] and x < 850 - VEL:
        x += VEL
        LEFT = False
        RIGHT = True

    else:
        LEFT = False
        RIGHT = False
        WALK_COUNT = 0

    if not(IS_JUMP):
        if keys[pygame.K_UP]:
            IS_JUMP = True
            LEFT = False
            RIGHT = False
            WALK_COUNT = 0
    else:
        if JUMP_COUNT >= -10:
            y -= (JUMP_COUNT * abs(JUMP_COUNT)) * 0.5
            JUMP_COUNT -= 1
        else:
            JUMP_COUNT = 10
            IS_JUMP = False
            
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
    redrawGameWindow()

pygame.quit()

