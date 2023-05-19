import pygame, sys

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Walking Animation")

BG = pygame.image.load("Assets/ChainsawBackground.png")

WALK_RIGHT = [pygame.image.load('Assets/R1.png'), pygame.image.load('Assets/R2.png'), pygame.image.load('Assets/R3.png'), pygame.image.load('Assets/R4.png'), pygame.image.load('Assets/R5.png'), pygame.image.load('Assets/R6.png'), pygame.image.load('Assets/R7.png'), pygame.image.load('Assets/R8.png'), pygame.image.load('Assets/R9.png')]
WALK_LEFT = [pygame.image.load('Assets/L1.png'), pygame.image.load('Assets/L2.png'), pygame.image.load('Assets/L3.png'), pygame.image.load('Assets/L4.png'), pygame.image.load('Assets/L5.png'), pygame.image.load('Assets/L6.png'), pygame.image.load('Assets/L7.png'), pygame.image.load('Assets/L8.png'), pygame.image.load('Assets/L9.png')]
CHAR = pygame.image.load('Assets/standing.png')

x = 25
y = 330
WIDTH = 384
HEIGHT = 384
VEL = 5

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
        
    pygame.display.update()

RUN = True

while RUN:
    CLOCK.tick(45)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > VEL:
        x -= VEL
        LEFT = True
        RIGHT = False

    elif keys[pygame.K_RIGHT] and x < 500 - VEL:
        x += VEL
        LEFT = False
        RIGHT = True

    else:
        LEFT = False
        RIGHT = False
        WALK_COUNT = 0

    if not(IS_JUMP):
        if keys[pygame.K_SPACE]:
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

    redrawGameWindow()

pygame.quit()
