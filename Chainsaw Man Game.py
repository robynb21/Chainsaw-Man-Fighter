import pygame, sys
from Button import Button

pygame.init()

SCREEN = pygame.display.set_mode((320, 180), pygame.RESIZABLE)
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/ChainsawBackground.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(10).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(160, 65))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(160, 115), 
                            text_input="BACK", font=get_font(15), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()
    
def options():
    while True:
        
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        p1_select = False
        p2_select = False
        char_select = False
        
        AKI_ICON = Button(image=pygame.image.load("assets/aki sprite.png"), pos=(160, 65),
                          text_input="", font=get_font(15), base_color="Black", hovering_color="Green")
        AKI_ICON.changeColor(OPTIONS_MOUSE_POS)
        AKI_ICON.update(SCREEN)

        AKI_SELECT = Button(image=None, pos=(160, 85), 
                            text_input="AKI", font=get_font(7), base_color="Black", hovering_color="Green")

        AKI_SELECT.changeColor(OPTIONS_MOUSE_POS)
        AKI_SELECT.update(SCREEN)

        DENJI_ICON = Button(image=pygame.image.load("assets/denji sprite.png"), pos=(80, 65),
                          text_input="", font=get_font(15), base_color="Black", hovering_color="Green")
        DENJI_ICON.changeColor(OPTIONS_MOUSE_POS)
        DENJI_ICON.update(SCREEN)

        DENJI_SELECT = Button(image=None, pos=(80, 85), 
                            text_input="DENJI", font=get_font(7), base_color="Black", hovering_color="Green")

        DENJI_SELECT.changeColor(OPTIONS_MOUSE_POS)
        DENJI_SELECT.update(SCREEN)

        POWER_ICON = Button(image=pygame.image.load("assets/power sprite.png"), pos=(240, 65),
                          text_input="", font=get_font(15), base_color="Black", hovering_color="Green")
        POWER_ICON.changeColor(OPTIONS_MOUSE_POS)
        POWER_ICON.update(SCREEN)

        POWER_SELECT = Button(image=None, pos=(240, 85), 
                            text_input="POWER", font=get_font(7), base_color="Black", hovering_color="Green")

        POWER_SELECT.changeColor(OPTIONS_MOUSE_POS)
        POWER_SELECT.update(SCREEN)
        
        OPTIONS_TEXT = get_font(10).render("CHOOSE YOUR CHARACTERS.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(midtop=(160, 0))
        
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(160, 115), 
                            text_input="BACK", font=get_font(15), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(20).render("CHAINSAW MUGEN", True, "#e46f34")
        MENU_RECT = MENU_TEXT.get_rect(center=(160, 25))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(160, 62.5), 
                            text_input="PLAY", font=get_font(15), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(160, 100), 
                            text_input="CHARACTERS", font=get_font(15), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(160, 137.5), 
                            text_input="QUIT", font=get_font(15), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()
