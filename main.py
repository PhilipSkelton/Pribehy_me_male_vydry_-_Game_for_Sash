#       ╔════════════════════════╗
#       ║  𝒫říběhy mé malé vydry ║
#       ╚════════════════════════╝


#       main


import pygame, sys
from settings import *
from level import Level 
from button import Button 



# Initialise!! =================================================================================



# Pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("𝒫říběhy mé malé vydry")
clock = pygame.time.Clock()



# Loading Stuff In =============================================================================



# Background images
MenuBG = pygame.image.load("images/backgrounds/MenuBG.png").convert_alpha()
StartBG = pygame.image.load("images/backgrounds/StartBG.png").convert_alpha()
Level1BG = pygame.image.load("images/backgrounds/L1BG.png").convert_alpha()

BGimage = pygame.image.load("figuring out sprites/0.1level1PNG.png").convert()
BGimage2 = pygame.image.load("figuring out sprites/0.2level1PNG.png").convert_alpha()

# Text and button images
MenuIm = pygame.image.load("images/textandbuttons/MenuIm.png")
StartIm = pygame.image.load("images/textandbuttons/StartIm.png")



# Defining Variables and Functions =============================================================



# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Function to draw text on the screen
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

# Fonts for buttons
level_fonts = pygame.font.SysFont("cambria", 50)

# Scrolling Background Variables
BGscroll_left = False
BGscroll_right = False
BGscroll = 0
BGscroll_speed = 1

#def draw_bg(): 
#    width = BGimage.get_width()
#    for x in range(2):
#        screen.blit(BGimage,((x * width)- BGscroll,0))
#    screen.blit(BGimage,(-BGscroll),0)
#    screen.blit(BGimage2,(-BGscroll),0)


# Level Setup
level1 = Level(level_map1,screen)
level2 = Level(level_map2,screen)
level3 = Level(level_map3,screen)
hiddenlevel = Level(hidden_level_map,screen)

# Game states
START = "start"
MENU = "menu"
LEVEL_1 = "level1"
LEVEL_2 = "level2"
LEVEL_3 = "level3"
HIDDEN_LEVEL = "hidden_level"
PAUSED = "paused"
DEATH_RESTART = "death_restart"



# Let the Games Begin!!!! =======================================================================



# Initial game state
current_state = START        



# MAIN GAME LOOP ================================================================================     



while True:
    for event in pygame.event.get():
        #
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Keyboard Presses for Scrolling Backgrounds During Levels
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                BGscroll_left = True
            if event.key == pygame.K_d:
                BGscroll_right = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                BGscroll_left = False
            if event.key == pygame.K_d:
                BGscroll_right = False



    # Start state ===============================================================================


    
    if current_state == START:
        pygame.display.set_caption("𝒫říběhy mé malé vydry - Start")

        # Menu background image
        screen.blit(StartBG, (0,-200))     # or     animated background?  make beautiful!!! 

        # "Press space to start" (to be animated to be flashing)
        screen.blit(StartIm, (800,0))


        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            current_state = MENU


    # Menu state =================================================================================================================================================================
            

    elif current_state == MENU: 


       #                   SET UP 


        pygame.display.set_caption("Game for Sash <3 - Menu")

        # Get the position of the mouse
        Menu_Mouse_Pos = pygame.mouse.get_pos()

        # Define the buttons based on the button class
        Level_1_Button = Button(image=pygame.image.load("images/buttons/Level1Button.png"), pos=(300,200),
                                text_input=".", font=level_fonts, base_colour="#d7fcd4", hovering_colour="White")
        Level_2_Button = Button(image=pygame.image.load("images/buttons/Level2Button.png"), pos=(300,300),
                                text_input="LEVEL 2", font=level_fonts, base_colour="#d7fcd4", hovering_colour="White")
        Level_3_Button = Button(image=pygame.image.load("images/buttons/Level3Button.png"), pos=(300,400),
                                text_input="LEVEL 3", font=level_fonts, base_colour="#d7fcd4", hovering_colour="White")
        Quit_Button =  Button(image=pygame.image.load("images/buttons/QuitButton.png"), pos=(300,500),
                                text_input="QUIT", font=level_fonts, base_colour="#d7fcd4", hovering_colour="White")
        #Settings_Button = 


        #                   WHATS ON SCREEN


        # Menu background image (line 29)w
        screen.blit(MenuBG, (0,-200))

        # Buttons 
        for button in [Level_1_Button, Level_2_Button, Level_3_Button, Quit_Button]:
                button.changeColour(Menu_Mouse_Pos)
                button.update(screen)

        # Menu text image
        screen.blit(MenuIm, (500,50))


                            # https://www.youtube.com/watch?v=GMBqjxcKogA  @ 3:07 for getting the buttons instead of the keys!!
        #draw_text("Press 1 for Level 1", pygame.font.Font(None, 24), BLACK, WIDTH // 2, HEIGHT // 2)
        #draw_text("Press 2 for Level 2", pygame.font.Font(None, 24), BLACK, WIDTH // 2, HEIGHT // 2 + 50)
        #draw_text("Press 3 for Level 3", pygame.font.Font(None, 24), BLACK, WIDTH // 2, HEIGHT // 2 + 100)
        pygame.display.flip()


        #                   INPUTS 


        keys = pygame.key.get_pressed()
        #if keys[pygame.K_1]:
            #current_state = LEVEL_1
        #elif keys[pygame.K_2]:
            #current_state = LEVEL_2
        #elif keys[pygame.K_3]:
            #current_state = LEVEL_3
        if keys[pygame.K_h]:
            current_state = HIDDEN_LEVEL
        #elif keys[pygame.K_ESCAPE]:
            #current_state = PAUSED  

        if event.type == pygame.MOUSEBUTTONDOWN:   
            if Level_1_Button.checkForInput(Menu_Mouse_Pos):
                current_state = LEVEL_1
            if Level_2_Button.checkForInput(Menu_Mouse_Pos):
                current_state = LEVEL_2
            if Level_3_Button.checkForInput(Menu_Mouse_Pos):
                current_state = LEVEL_3    
            if Quit_Button.checkForInput(Menu_Mouse_Pos):
                current_state = START


    # Level 1 state =================================================================================================================================================================
            

    elif current_state == LEVEL_1:


        #                   SET UP 


        # Caption
        pygame.display.set_caption("Game for Sash <3 - Level 1")

        #Get the mouse position in this screen
        Lvl1_Mouse_Pos = pygame.mouse.get_pos()

        # Define the buttons based on the button class
        Pause_Button = Button(image=pygame.image.load("images/buttons/Level2Button.png"), pos=(100,50),
                                text_input="PAUSE", font=level_fonts, base_colour="#d7fcd4", hovering_colour="White")        

        # Scrolling Background Setup
        WSCurrentValueL1 = level1.get_world_shift_state()
        
        if  WSCurrentValueL1 == 8:
            BGscroll -= 5
        if WSCurrentValueL1 == -8:
            BGscroll += 5
        if WSCurrentValueL1 == 0:
            BGscroll += 0

        l1_BG_Sp1 = (- BGscroll * 0.2) - 250
        l1_BG_Sp2 = (- BGscroll * 0.6) - 250
        l1_BG_Sp3 = (- BGscroll * 1) - 250
        l1_BG_Sp4 = (- BGscroll * 1.6) - 250
        l1_BG_Sp5 = (- BGscroll * 2) - 250
        l1_BG_Sp6 = (- BGscroll * 2.5) - 500


       #                   WHATS SHOWN ON SCREEN


        # Images/animations behind the character 
        screen.blit(BGimage, ( l1_BG_Sp1,0))              
        
#        draw_bg()

        # Sash and the tiles
        level1.run()  
        
        # Images/animations in front of the character
        screen.blit(BGimage2, ( l1_BG_Sp6,0))            
        
        # Buttons 
        for button in [Pause_Button]:
                button.changeColour(Lvl1_Mouse_Pos)
                button.update(screen)

        pygame.display.flip()      
        


       #                   INPUTS


        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            current_state = PAUSED

        if event.type == pygame.MOUSEBUTTONDOWN:   
            if Pause_Button.checkForInput(Lvl1_Mouse_Pos):
                current_state = PAUSED


    # Level 2 state =================================================================================================================================================================
            

    elif current_state == LEVEL_2:      


        #                   SET UP 

       
        pygame.display.set_caption("Game for Sash <3 - Level 2")
        Lvl2_Mouse_Pos = pygame.mouse.get_pos()
        Pause_Button = Button(image=pygame.image.load("images/buttons/Level2Button.png"), pos=(1100,50),
                                text_input="PAUSE", font=level_fonts, base_colour="#d7fcd4", hovering_colour="White") 


       #                   WHATS SHOWN ON SCREEN


        screen.fill('black')
        
                # Scrolling Background Setup
        WSCurrentValueL2 = level2.get_world_shift_state()
        
        if  WSCurrentValueL2 == 8:
            BGscroll -= 5
        if WSCurrentValueL2 == -8:
            BGscroll += 5
        if WSCurrentValueL2 == 0:
            BGscroll += 0

        l2_BG_Sp1 = (- BGscroll * 0.2) - 250
        l2_BG_Sp2 = (- BGscroll * 0.6) - 250
        l2_BG_Sp3 = (- BGscroll * 1) - 250
        l2_BG_Sp4 = (- BGscroll * 1.6) - 250
        l2_BG_Sp5 = (- BGscroll * 2) - 250
        l2_BG_Sp6 = (- BGscroll * 2.5) - 500


       #                   WHATS SHOWN ON SCREEN


        # Images/animations behind the character 
        screen.blit(BGimage2, ( l2_BG_Sp4,0))              
        
#        draw_bg()

        # Sash and the tiles

        level2.run()
        for button in [Pause_Button]:
                button.changeColour(Lvl2_Mouse_Pos)
                button.update(screen)          
        pygame.display.flip()      


       #                   INPUTS


        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            current_state = PAUSED        
        if event.type == pygame.MOUSEBUTTONDOWN:   
            if Pause_Button.checkForInput(Lvl2_Mouse_Pos):
                current_state = PAUSED

    # Level 3 state =================================================================================================================================================================
            

    elif current_state == LEVEL_3:
        pygame.display.set_caption("Game for Sash <3 - Level 3")

        screen.fill('black')
        level3.run()  
        pygame.display.flip()  

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            current_state = PAUSED        


    # Hidden state =================================================================================================================================================================
            

    elif current_state == HIDDEN_LEVEL:
        pygame.display.set_caption("Game for Sash <3 - Hidden Level")

        screen.fill('black')
        hiddenlevel.run()  
        pygame.display.flip() 

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            current_state = PAUSED        


    #  Paused state =================================================================================================================================================================
            

    elif current_state == PAUSED:


        #                   SET UP 

 
        pygame.display.set_caption("Game for Sash <3 - Paused")
        Paused_Mouse_Pos = pygame.mouse.get_pos()
        QuitInPause_Button = Button(image=pygame.image.load("images/buttons/Level1Button.png"), pos=(550,300),
                                text_input="QUIT", font=level_fonts, base_colour="#d7fcd4", hovering_colour="White")
        MenuInPause_Button = Button(image=pygame.image.load("images/buttons/Level1Button.png"), pos=(550,400),
                                text_input="MENU", font=level_fonts, base_colour="#d7fcd4", hovering_colour="White") 
        

       #                   WHATS SHOWN ON SCREEN


        screen.fill('black')
        for button in [QuitInPause_Button, MenuInPause_Button]:
                button.changeColour(Paused_Mouse_Pos)
                button.update(screen)    


       #                   INPUTS
        

        if event.type == pygame.MOUSEBUTTONDOWN:   
            if QuitInPause_Button.checkForInput(Paused_Mouse_Pos):
                current_state = START
            if MenuInPause_Button.checkForInput(Paused_Mouse_Pos):
                current_state = MENU



    pygame.display.update()
    clock.tick(60)      
        

# helpful
# https://www.youtube.com/watch?v=AY9MnQ4x3zk @ 1:48:22 for game state and 1:56:19 for score
#https://www.youtube.com/watch?v=2iyx8_elcYg @ 7:44