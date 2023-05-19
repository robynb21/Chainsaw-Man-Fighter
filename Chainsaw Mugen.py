import pygame, sys
from Button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/ChainsawBackground.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(40).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(100, 35), 
                            text_input="BACK", font=get_font(25), base_color="White", hovering_color="Green")

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

        p1_character = " "
        p1_select = False
        p2_select = False
        char_select = False

        AKI_ICON = Button(image=pygame.image.load("assets/aki sprite.png"), pos=(640, 260),
                              text_input="", font=get_font(15), base_color="Black", hovering_color="Green")
        AKI_ICON.changeColor(OPTIONS_MOUSE_POS)
        AKI_ICON.update(SCREEN)

        AKI_SELECT = Button(image=None, pos=(640, 350), 
                                text_input="AKI", font=get_font(28), base_color="Black", hovering_color="Green")

        AKI_SELECT.changeColor(OPTIONS_MOUSE_POS)
        AKI_SELECT.update(SCREEN)

        DENJI_ICON = Button(image=pygame.image.load("assets/denji sprite.png"), pos=(320, 260),
                              text_input="", font=get_font(15), base_color="Black", hovering_color="Green")
        DENJI_ICON.changeColor(OPTIONS_MOUSE_POS)
        DENJI_ICON.update(SCREEN)

        DENJI_SELECT = Button(image=None, pos=(320, 350), 
                                text_input="DENJI", font=get_font(28), base_color="Black", hovering_color="Green")

        DENJI_SELECT.changeColor(OPTIONS_MOUSE_POS)
        DENJI_SELECT.update(SCREEN)

        POWER_ICON = Button(image=pygame.image.load("assets/power sprite.png"), pos=(960, 260),
                              text_input="", font=get_font(15), base_color="Black", hovering_color="Green")
        POWER_ICON.changeColor(OPTIONS_MOUSE_POS)
        POWER_ICON.update(SCREEN)

        POWER_SELECT = Button(image=None, pos=(960, 350), 
                                text_input="POWER", font=get_font(28), base_color="Black", hovering_color="Green")

        POWER_SELECT.changeColor(OPTIONS_MOUSE_POS)
        POWER_SELECT.update(SCREEN)
            
        OPTIONS_TEXT = get_font(40).render("CHOOSE YOUR CHARACTERS.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(midtop=(640, 50))
        
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(60), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
                    
                if DENJI_SELECT.checkForInput(OPTIONS_MOUSE_POS):
                    p1_select == True
                    p1_character == "DENJI"
                    
                if AKI_SELECT.checkForInput(OPTIONS_MOUSE_POS):
                    p1_select == True
                    p1_character == "AKI"
                    
                if POWER_SELECT.checkForInput(OPTIONS_MOUSE_POS):
                    p1_select == True
                    p1_character == "POWER"

        if p1_character == "POWER":
            POW_CHOOSE_TEXT = get_font(40).render("PLAYER 1: POWER", True, "Black")
            POW_CHOOSE_RECT = POW_CHOOSE_TEXT.get_rect(midbottom=(640, 600))
            SCREEN.blit(POW_CHOOSE_TEXT, POW_CHOOSE_RECT)
            pygame.display.update()
            options()

        if p1_character == "AKI":
            AKI_CHOOSE_TEXT = get_font(40).render("PLAYER 1: AKI", True, "Black")
            AKI_CHOOSE_RECT = AKI_CHOOSE_TEXT.get_rect(midbottom=(640, 600))
            SCREEN.blit(AKI_CHOOSE_TEXT, AKI_CHOOSE_RECT)
            pygame.display.update()
            options()

        if p1_character == "DENJI":
            DEN_CHOOSE_TEXT = get_font(40).render("PLAYER 1: DENJI", True, "Black")
            DEN_CHOOSE_RECT = DEN_CHOOSE_TEXT.get_rect(midbottom=(640, 600))
            SCREEN.blit(DEN_CHOOSE_TEXT, DEN_CHOOSE_RECT)
            pygame.display.update()
            options()  

        pygame.display.update()
                     


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(80).render("CHAINSAW MUGEN", True, "#e46f34")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(60), base_color="#fdfd96", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                            text_input="FIGHTERS", font=get_font(60), base_color="#fdfd96", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(60), base_color="#fdfd96", hovering_color="White")

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
