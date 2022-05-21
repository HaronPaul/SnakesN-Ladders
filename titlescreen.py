import pygame, sys
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((800, 700))
pygame.display.set_caption("Snakes N Ladders")

BG = pygame.image.load("assets/Background.png")

def get_font(size):
    return pygame.font.Font("assets/KB3BusRoute123.ttf", size)
def get_font2(size):
    return pygame.font.Font("assets/Kumadinya.ttf", size)

def computer():
    pygame.display.set_caption("Play with Computer")
    while True:
        SCREEN.blit(BG, (0, 0))
        
        COMPUTER_MOUSE_POS = pygame.mouse.get_pos()
    
        COMPUTER_BACK = Button(image=pygame.image.load("assets/Quit Ob.png"), pos=(610,583), 
                            text_input="BACK", font=get_font2(35), base_color="white", hovering_color="black")

        COMPUTER_BACK.changeColor(COMPUTER_MOUSE_POS)
        COMPUTER_BACK.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if COMPUTER_BACK.checkForInput(COMPUTER_MOUSE_POS):
                    play()
                
        pygame.display.update()
        
def twoplayers():
    pygame.display.set_caption("2 Players")
    while True:
        SCREEN.blit(BG, (0, 0))
        
        TWOPLAYERS_MOUSE_POS = pygame.mouse.get_pos()
    
        TWOPLAYERS_BACK = Button(image=pygame.image.load("assets/Quit Ob.png"), pos=(610,583), 
                            text_input="BACK", font=get_font2(35), base_color="white", hovering_color="black")

        TWOPLAYERS_BACK.changeColor(TWOPLAYERS_MOUSE_POS)
        TWOPLAYERS_BACK.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if TWOPLAYERS_BACK.checkForInput(TWOPLAYERS_MOUSE_POS):
                    multiplayer()
                
        pygame.display.update()

def threeplayers():
    pygame.display.set_caption("3 Players")
    while True:
        SCREEN.blit(BG, (0, 0))
        
        THREEPLAYERS_MOUSE_POS = pygame.mouse.get_pos()
    
        THREEPLAYERS_BACK = Button(image=pygame.image.load("assets/Quit Ob.png"), pos=(610,583), 
                            text_input="BACK", font=get_font2(35), base_color="white", hovering_color="black")

        THREEPLAYERS_BACK.changeColor(THREEPLAYERS_MOUSE_POS)
        THREEPLAYERS_BACK.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if THREEPLAYERS_BACK.checkForInput(THREEPLAYERS_MOUSE_POS):
                    multiplayer()
                
        pygame.display.update()
        
def fourplayers():
    pygame.display.set_caption("4 Players")
    while True:
        SCREEN.blit(BG, (0, 0))
        
        FOURPLAYERS_MOUSE_POS = pygame.mouse.get_pos()
    
        FOURPLAYERS_BACK = Button(image=pygame.image.load("assets/Quit Ob.png"), pos=(610,583), 
                            text_input="BACK", font=get_font2(35), base_color="white", hovering_color="black")

        FOURPLAYERS_BACK.changeColor(FOURPLAYERS_MOUSE_POS)
        FOURPLAYERS_BACK.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if FOURPLAYERS_BACK.checkForInput(FOURPLAYERS_MOUSE_POS):
                    multiplayer()
                
        pygame.display.update()

def multiplayer():
    pygame.display.set_caption("Multiplayer")
    while True:
        SCREEN.blit(BG, (0, 0))
        
        MULTIPLAYER_MOUSE_POS = pygame.mouse.get_pos()
        
        TWOPLAYERS_BUTTON = Button(image=None, pos=(400, 250), 
                    text_input="2 Players", font=get_font(50), base_color="green", hovering_color="blue")
        TWOPLAYERS_BUTTON.changeColor(MULTIPLAYER_MOUSE_POS)
        TWOPLAYERS_BUTTON.update(SCREEN)
        
        THREEPLAYERS_BUTTON = Button(image=None, pos=(400, 350), 
                    text_input="3 Players", font=get_font(50), base_color="green", hovering_color="blue")
        THREEPLAYERS_BUTTON.changeColor(MULTIPLAYER_MOUSE_POS)
        THREEPLAYERS_BUTTON.update(SCREEN)
        
        FOURPLAYERS_BUTTON = Button(image=None, pos=(400, 450), 
                    text_input="4 Players", font=get_font(50), base_color="green", hovering_color="blue")
        FOURPLAYERS_BUTTON.changeColor(MULTIPLAYER_MOUSE_POS)
        FOURPLAYERS_BUTTON.update(SCREEN)
    
        MULTIPLAYER_BACK = Button(image=pygame.image.load("assets/Quit Ob.png"), pos=(610,583), 
                            text_input="BACK", font=get_font2(35), base_color="white", hovering_color="black")

        MULTIPLAYER_BACK.changeColor(MULTIPLAYER_MOUSE_POS)
        MULTIPLAYER_BACK.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if TWOPLAYERS_BUTTON.checkForInput(MULTIPLAYER_MOUSE_POS):
                    twoplayers()
                if THREEPLAYERS_BUTTON.checkForInput(MULTIPLAYER_MOUSE_POS):
                    threeplayers()
                if FOURPLAYERS_BUTTON.checkForInput(MULTIPLAYER_MOUSE_POS):
                    fourplayers()
                if MULTIPLAYER_BACK.checkForInput(MULTIPLAYER_MOUSE_POS):
                    play()
                
        pygame.display.update()

def play():
    pygame.display.set_caption("Play")
    while True:
        SCREEN.blit(BG, (0, 0))
        
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        
        MULTIPLAYER_BUTTON = Button(image=None, pos=(400, 300), 
                    text_input="Multiplayer", font=get_font(50), base_color="orange", hovering_color="red")
        MULTIPLAYER_BUTTON.changeColor(PLAY_MOUSE_POS)
        MULTIPLAYER_BUTTON.update(SCREEN)
        
        COMPUTER_BUTTON = Button(image=None, pos=(400, 400), 
                    text_input="Play with Computer", font=get_font(50), base_color="orange", hovering_color="red")
        COMPUTER_BUTTON.changeColor(PLAY_MOUSE_POS)
        COMPUTER_BUTTON.update(SCREEN)
    
        PLAY_BACK = Button(image=pygame.image.load("assets/Quit Ob.png"), pos=(610,583), 
                            text_input="BACK", font=get_font2(35), base_color="white", hovering_color="black")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MULTIPLAYER_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    multiplayer()
                if COMPUTER_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    computer()
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    game_title()
                
        pygame.display.update()
    
def rules():
    pygame.display.set_caption("Rules")
    while True:
        SCREEN.blit(BG, (0, 0))
        
        RULES_MOUSE_POS = pygame.mouse.get_pos()

        text= "Rules"
        text1='1. Initally, all the players are at the starting position.'
        text2='2. Take it in turns to roll the dice.'
        text3='3. Move forward the number of tiles shown on the dice.'
        text4='4. If you land at the bottom of a ladder, you can move up to the top of the ladder.'
        text5='5. If you land on the head of a snake, you must slide down to the tail of the snake.'
        text6='6. If you land on a power-up tile, you can use it for your next turn.'
        text7='7. The first player to get to the FINAL position is the winner.'
        text8='8. Hit enter to roll the dice.'
        
        RULES_TEXT = get_font(45).render(text, True, "green")
        RULES_OB = RULES_TEXT.get_rect(center=(400, 120))
        SCREEN.blit(RULES_TEXT, RULES_OB)
        RULES_TEXT1 = get_font2(20).render(text1, True, "white")
        RULES_OB = RULES_TEXT1.get_rect(center=(283, 200))
        SCREEN.blit(RULES_TEXT1, RULES_OB)
        RULES_TEXT2 = get_font2(20).render(text2, True, "white")
        RULES_OB = RULES_TEXT2.get_rect(center=(219, 250))
        SCREEN.blit(RULES_TEXT2, RULES_OB)
        RULES_TEXT3 = get_font2(20).render(text3, True, "white")
        RULES_OB = RULES_TEXT3.get_rect(center=(302, 300))
        SCREEN.blit(RULES_TEXT3, RULES_OB)
        RULES_TEXT4 = get_font2(20).render(text4, True, "white")
        RULES_OB = RULES_TEXT4.get_rect(center=(400, 350))
        SCREEN.blit(RULES_TEXT4, RULES_OB)
        RULES_TEXT5 = get_font2(20).render(text5, True, "white")
        RULES_OB = RULES_TEXT5.get_rect(center=(398, 400))
        SCREEN.blit(RULES_TEXT5, RULES_OB)
        RULES_TEXT6= get_font2(20).render(text6, True, "white")
        RULES_OB = RULES_TEXT6.get_rect(center=(344, 450))
        SCREEN.blit(RULES_TEXT6, RULES_OB)
        RULES_TEXT7= get_font2(20).render(text7, True, "white")
        RULES_OB = RULES_TEXT7.get_rect(center=(325, 500))
        SCREEN.blit(RULES_TEXT7, RULES_OB)
        RULES_TEXT8= get_font2(20).render(text8, True, "white")
        RULES_OB = RULES_TEXT8.get_rect(center=(198, 550))
        SCREEN.blit(RULES_TEXT8, RULES_OB)

        RULES_BACK = Button(image=pygame.image.load("assets/Quit Ob.png"), pos=(610,583), 
                            text_input="BACK", font=get_font2(35), base_color="white", hovering_color="black")

        RULES_BACK.changeColor(RULES_MOUSE_POS)
        RULES_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RULES_BACK.checkForInput(RULES_MOUSE_POS):
                    game_title()

        pygame.display.update()

def game_title():
    while True:
        SCREEN.blit(BG, (0, 0))

        GT_MOUSE_POS = pygame.mouse.get_pos()

        GT1_TEXT = get_font(63).render("SNAKES N' LADDERS", True, "green")
        GT1_RECT = GT1_TEXT.get_rect(center=(400, 170))
        GT2_TEXT = get_font(50).render("Powered Up", True, "blue")
        GT2_RECT = GT2_TEXT.get_rect(center=(400, 240))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Ob.png"), pos=(400, 350), 
                            text_input="PLAY", font=get_font2(35), base_color="white", hovering_color="black")
        RULES_BUTTON = Button(image=pygame.image.load("assets/Rules Ob.png"), pos=(400, 460), 
                            text_input="RULES", font=get_font2(35), base_color="white", hovering_color="black")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Ob.png"), pos=(400,570), 
                            text_input="QUIT", font=get_font2(35), base_color="white", hovering_color="black")

        SCREEN.blit(GT1_TEXT, GT1_RECT)
        SCREEN.blit(GT2_TEXT, GT2_RECT)

        for button in [PLAY_BUTTON, RULES_BUTTON, QUIT_BUTTON]:
            button.changeColor(GT_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(GT_MOUSE_POS):
                    play()
                if RULES_BUTTON.checkForInput(GT_MOUSE_POS):
                    rules()
                if QUIT_BUTTON.checkForInput(GT_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

game_title()