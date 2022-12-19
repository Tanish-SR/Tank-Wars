import pygame, sys
from Button import Button
from subprocess import call

pygame.init()

SCREEN = pygame.display.set_mode((1000,800))
pygame.display.set_caption("HOME")

BG = pygame.image.load("BACKGROUND.jpg")
BG = pygame.transform.scale(BG,(1000,800))
def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("Beckman-Free.otf", size)

def calling():
    file_name = call(["python","main.py"])
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        # SCREEN.fill("black")
        BG1=pygame.image.load("OPTION PG BG.png")
        SCREEN.blit(BG1, (0, 0))

        
        C1 = Button(image=pygame.image.load("PLAYER BUTTON/CONTROL1835.png"), pos=(500, 50), text_input="CONTROLS", font=get_font(30), base_color="White",
                    hovering_color="Black")
        C1.changeColor(OPTIONS_MOUSE_POS)
        C1.update(SCREEN)


        P1 = Button(image=pygame.image.load("PLAYER BUTTON/UPDATE_P1.png"), pos=(220, 130), text_input="PLAYER ", font=get_font(30), base_color="White",
                    hovering_color="Green") #PLAYER 1 DISPLAY BUTTON
        P1.changeColor(OPTIONS_MOUSE_POS)
        P1.update(SCREEN)

        P2 = Button(image=pygame.image.load("PLAYER BUTTON/UPDATEP2.png"), pos=(800, 130), text_input="PLAYER ", font=get_font(30), base_color="White",
                    hovering_color="Red") #PLAYER 2 DISPLAY BUTTON
        P2.changeColor(OPTIONS_MOUSE_POS)
        P2.update(SCREEN)

        B1 = Button(image=None, pos=(200, 270), text_input="   D   -   RIGHT", font=get_font(30), base_color="White",
                      hovering_color="Green")
        B1.changeColor(OPTIONS_MOUSE_POS)
        B1.update(SCREEN)

        B2 = Button(image=None, pos=(200, 230), text_input="Q  - FIRE ", font=get_font(30), base_color="White",
                      hovering_color="Green")
        B2.changeColor(OPTIONS_MOUSE_POS)
        B2.update(SCREEN)

        B3 = Button(image=None, pos=(200, 310), text_input="A   -  LEFT", font=get_font(30), base_color="White",
                    hovering_color="Green")
        B3.changeColor(OPTIONS_MOUSE_POS)
        B3.update(SCREEN)

        B4 = Button(image=None, pos=(200, 360), text_input="          W  -  TURRENT UP", font=get_font(30),
                    base_color="White",
                    hovering_color="Green")
        B4.changeColor(OPTIONS_MOUSE_POS)
        B4.update(SCREEN)

        B5 = Button(image=None, pos=(200, 400), text_input="                 S   -  TURRENT DOWN", font=get_font(30), base_color="White",
                    hovering_color="Green")
        B5.changeColor(OPTIONS_MOUSE_POS)
        B5.update(SCREEN)

        B5 = Button(image=None, pos=(200, 440), text_input="         R   -  POWER UP", font=get_font(30),
                    base_color="White",
                    hovering_color="Green")
        B5.changeColor(OPTIONS_MOUSE_POS)
        B5.update(SCREEN)

        B6 = Button(image=None, pos=(200, 480), text_input="              E   -  POWER DOWN", font=get_font(30),
                    base_color="White",
                    hovering_color="Green")
        B6.changeColor(OPTIONS_MOUSE_POS)
        B6.update(SCREEN)


     #P2 CONTRLOLS :

        PB1 = Button(image=None, pos=(750, 230), text_input="SYMBOL [/]  -   FIRE", font=get_font(30),
                      base_color="White", hovering_color="Red")
        PB1.changeColor(OPTIONS_MOUSE_POS)
        PB1.update(SCREEN)

        PB2=Button(image=None,pos=(750,270),text_input=" ARROW [>]  -   RIGHT",font=get_font(30),base_color="White",hovering_color="Red")
        PB2.changeColor(OPTIONS_MOUSE_POS)
        PB2.update(SCREEN)

        PB3 = Button(image=None, pos=(750, 310), text_input=" ARROW [<]  -   LEFT", font=get_font(30),
                     base_color="White", hovering_color="Red")
        PB3.changeColor(OPTIONS_MOUSE_POS)
        PB3.update(SCREEN)

        PB4 = Button(image=None, pos=(750, 350), text_input=" ARROW [UP]  -   TURRENT UP", font=get_font(30),
                     base_color="White", hovering_color="Red")
        PB4.changeColor(OPTIONS_MOUSE_POS)
        PB4.update(SCREEN)

        PB5 = Button(image=None, pos=(750, 390), text_input=" ARROW [DOWN] - TURRENT DOWN", font=get_font(30),
                     base_color="White", hovering_color="Red")
        PB5.changeColor(OPTIONS_MOUSE_POS)
        PB5.update(SCREEN)

        PB6 = Button(image=None, pos=(750, 430), text_input=" SYMBOL [.]  -   POWER UP", font=get_font(30),
                     base_color="White", hovering_color="Red")
        PB6.changeColor(OPTIONS_MOUSE_POS)
        PB6.update(SCREEN)

        PB7 = Button(image=None, pos=(750, 470), text_input=" SYMBOL [,]  -   POWER DOWN", font=get_font(30),
                     base_color="White", hovering_color="Red")
        PB7.changeColor(OPTIONS_MOUSE_POS)
        PB7.update(SCREEN)


        OPTIONS_BACK = Button(image=None, pos=(50, 50),
                            text_input="BACK", font=get_font(25), base_color="White", hovering_color="Green")

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

        MENU_TEXT = get_font(100).render("TANK WARS", True, "#FFFFFF")
        MENU_RECT = MENU_TEXT.get_rect(center=(500, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("TANKER BUTTON/UPDATED12 PLAY BUTTON.png"), pos=(520, 250),
                            text_input="PLAY", font=get_font(45), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("TANKER BUTTON/UPDATED OPTION BUTTON (1).png"), pos=(510, 400),
                            text_input="OPTIONS", font=get_font(45), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("TANKER BUTTON/UPDATED2 QUIT BUTTON.png"), pos=(530, 550),
                            text_input="QUIT", font=get_font(45), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        #quitter
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    calling()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()