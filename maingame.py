import pygame
import os
from game.constants import WIDTH, HEIGHT, VIOLET
from game.field import Field
from game.player import Player
from game.functions import renderExtras, renderDiceNumber, renderPlayerInventory, renderWaitingText
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

def winner(player):
    pygame.display.set_caption("Winner")
    while True:
        SCREEN.blit(BG, (0, 0))
        WINNER_MOUSE_POS = pygame.mouse.get_pos()
            
        if player == 0:
            text="Player 1"
            
        if player == 1:
            text="Player 2"
             
        if player == 2:
            text="Player 3"
            
        if player == 3:
            text="Player 4"            
        
        text1="WINS!"
        WINNER_TEXT = get_font(90).render(text, True, "red")
        WINNER_OB = WINNER_TEXT.get_rect(center=(400, 250))
        SCREEN.blit(WINNER_TEXT, WINNER_OB)
        WINNER_TEXT = get_font(110).render(text1, True, "red")
        WINNER_OB = WINNER_TEXT.get_rect(center=(400, 400))
        SCREEN.blit(WINNER_TEXT, WINNER_OB)
                
        WINNER_BACK = Button(image=pygame.image.load("assets/Quit Ob.png"), pos=(400,570), 
                            text_input="MENU", font=get_font2(35), base_color="white", hovering_color="black")

        WINNER_BACK.changeColor(WINNER_MOUSE_POS)
        WINNER_BACK.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if WINNER_BACK.checkForInput(WINNER_MOUSE_POS):
                    game_title()

        pygame.display.update()

def gameScreen(WIN, NUM_PLAYERS, vsCPU):
    pygame.display.set_caption('Snakes N\' Ladders')
    
    FPS = 60    # Frame rate for the game
    clock = pygame.time.Clock()
    
    field = Field()

    # Call the draw_squares function of the field instance  
    playerList = []

    # Instantiate the players 
    playerCPU = False
    for i in range(NUM_PLAYERS):
        picPath = os.path.join(os.path.dirname(__file__), 'assets', f'player{i+1}.png')
        playerImage = pygame.image.load(picPath)

        if vsCPU and i>0:
            playerCPU = True
        # 3rd and 4th parameters are x and y position
        newPlayer = Player(playerImage, i+1, 0, 630, field, playerCPU) # Initialize player's position at number 1 tile
        playerList.append(newPlayer)

    powerUpGroup = pygame.sprite.Group()
    powerUpHotkeys = [pygame.K_1, pygame.K_2, pygame.K_3]
    for p in field.powerUps:
       powerUpGroup.add(p)

    currentPlayer = 1 # Initialize player 1 at start of the game
    run = True
    while run:
        # Reset rendering every loop 
        # Render other asssets (buttons, player text, etc)
        renderExtras(WIN, currentPlayer)
        field.draw_squares(WIN)
        
        #Render the power-ups 
        powerUpGroup.draw(WIN)

        # Render the players
        for p in playerList:
            p.draw(WIN)

        GAMESCREEN_BACK = Button(image=pygame.image.load("assets/Gamequit Ob.png"), pos=(750,660), text_input="QUIT", font=get_font2(35), base_color="black", hovering_color="red")
        GAMESCREEN_MOUSE_POS = pygame.mouse.get_pos()
        GAMESCREEN_BACK.changeColor(GAMESCREEN_MOUSE_POS)
        
        if playerList[currentPlayer - 1].isCPU and  playerList[currentPlayer - 1].isMoving == False and playerList[currentPlayer - 1].rolled == False:
            playerList[currentPlayer - 1].rollDice()
            diceNumber = playerList[currentPlayer - 1].rolledNumber
        
        # Loop through all the events happening. May be a mouse click/key press
        for event in pygame.event.get():
            # When user clicks the close button of the window equate run to False and hasPlayed to True
            
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if GAMESCREEN_BACK.checkForInput(GAMESCREEN_MOUSE_POS):
                    play()
            
            if not playerList[currentPlayer - 1].isCPU:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        # This condition will prevent other players from moving when the currebt player is moving
                        if playerList[currentPlayer - 1].isMoving == False and playerList[currentPlayer - 1].rolled == False:
                            playerList[currentPlayer - 1].rollDice()
                            diceNumber = playerList[currentPlayer - 1].rolledNumber

                    if event.key == pygame.K_ESCAPE:
                        if playerList[currentPlayer - 1].rolled and playerList[currentPlayer - 1].isWaiting and playerList[currentPlayer - 1].aligned and len(playerList[currentPlayer - 1].inventory) > 0:
                            playerList[currentPlayer - 1].isWaiting = False

                    # If player presses 1, 2 or 3, use the corresponding power-up
                    if event.key in powerUpHotkeys:
                        if playerList[currentPlayer - 1].rolled and playerList[currentPlayer - 1].isWaiting and playerList[currentPlayer - 1].aligned and len(playerList[currentPlayer - 1].inventory) > 0:
                            playerList[currentPlayer - 1].calculateJumpTile(event.key)
                            playerList[currentPlayer - 1].isWaiting = False
            
        GAMESCREEN_BACK.update(SCREEN)

        # Update the dice number text on screen
        if playerList[currentPlayer - 1].isMoving:
            renderDiceNumber(WIN, diceNumber)
        
        # Render the player's inventory if it is not empty
        if len(playerList[currentPlayer - 1].inventory) > 0:
            renderPlayerInventory(WIN, playerList[currentPlayer - 1])
        
        if len(playerList[currentPlayer - 1].inventory) > 0 and playerList[currentPlayer - 1].aligned and playerList[currentPlayer - 1].isWaiting:
            renderWaitingText(WIN)
        
        playerList[currentPlayer - 1].update()
        print(playerList[currentPlayer - 1].rect.x)
        if(playerList[currentPlayer - 1].rolled == True and playerList[currentPlayer - 1].isMoving == False):
            if playerList[currentPlayer - 1].win:
                print(f'Player {currentPlayer} has won!!')
                winner(currentPlayer - 1)
            playerList[currentPlayer - 1].checkTile()
            playerList[currentPlayer - 1].rolled = False
            playerList[currentPlayer - 1].aligned = False
            if len(playerList[currentPlayer - 1].inventory) > 0: playerList[currentPlayer - 1].isWaiting = True
            if currentPlayer == NUM_PLAYERS: currentPlayer = 1
            else: currentPlayer += 1

        pygame.display.update()        
        powerUpGroup.update()
        clock.tick(FPS)
    pygame.quit()

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
                    gameScreen(SCREEN, 2, False)
                if THREEPLAYERS_BUTTON.checkForInput(MULTIPLAYER_MOUSE_POS):
                    gameScreen(SCREEN, 3, False)
                if FOURPLAYERS_BUTTON.checkForInput(MULTIPLAYER_MOUSE_POS):
                    gameScreen(SCREEN, 4, False)
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
                    gameScreen(SCREEN, 2, True)
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
        text2='2. Take it in turns to press the SPACEBAR and roll the dice.'
        text3='3. You will move forward the number of tiles shown on the dice.'
        text4='4. If you land at the bottom of a ladder, you will move up to the top of the ladder.'
        text5='5. If you land on the head of a snake, you will slide down to the tail of the snake.'
        text6='6. If you land on a power-up tile, you can use it for your future turn.'
        text7='Note: If a player has a power-up in the inventory, wait until it has finished moving.'
        text8='After moving, you can press ESC to skip using a power up or press 1, 2, or 3 to use'
        text9='the power-up in the inventory.'
        text10='7. The first player to get to the FINAL position is the winner.'
        
        RULES_TEXT = get_font(45).render(text, True, "green")
        RULES_OB = RULES_TEXT.get_rect(center=(400, 120))
        SCREEN.blit(RULES_TEXT, RULES_OB)
        RULES_TEXT1 = get_font2(20).render(text1, True, "white")
        RULES_OB = RULES_TEXT1.get_rect(center=(247, 180))
        SCREEN.blit(RULES_TEXT1, RULES_OB)
        RULES_TEXT2 = get_font2(20).render(text2, True, "white")
        RULES_OB = RULES_TEXT2.get_rect(center=(279, 220))
        SCREEN.blit(RULES_TEXT2, RULES_OB)
        RULES_TEXT3 = get_font2(20).render(text3, True, "white")
        RULES_OB = RULES_TEXT3.get_rect(center=(290, 260))
        SCREEN.blit(RULES_TEXT3, RULES_OB)
        RULES_TEXT4 = get_font2(20).render(text4, True, "white")
        RULES_OB = RULES_TEXT4.get_rect(center=(362, 300))
        SCREEN.blit(RULES_TEXT4, RULES_OB)
        RULES_TEXT5 = get_font2(20).render(text5, True, "white")
        RULES_OB = RULES_TEXT5.get_rect(center=(355, 340))
        SCREEN.blit(RULES_TEXT5, RULES_OB)
        RULES_TEXT6= get_font2(20).render(text6, True, "white")
        RULES_OB = RULES_TEXT6.get_rect(center=(312, 380))
        SCREEN.blit(RULES_TEXT6, RULES_OB)
        RULES_TEXT7= get_font2(20).render(text7, True, "yellow")
        RULES_OB = RULES_TEXT7.get_rect(center=(390, 420))
        SCREEN.blit(RULES_TEXT7, RULES_OB)
        RULES_TEXT8= get_font2(20).render(text8, True, "yellow")
        RULES_OB = RULES_TEXT8.get_rect(center=(420, 460))
        SCREEN.blit(RULES_TEXT8, RULES_OB)
        RULES_TEXT9 = get_font2(20).render(text9, True, "yellow")
        RULES_OB = RULES_TEXT9.get_rect(center=(217, 500))
        SCREEN.blit(RULES_TEXT9, RULES_OB)
        RULES_TEXT10 = get_font2(20).render(text10, True, "white")
        RULES_OB = RULES_TEXT10.get_rect(center=(283, 540))
        SCREEN.blit(RULES_TEXT10, RULES_OB)


        RULES_BACK = Button(image=pygame.image.load("assets/Quit Ob.png"), pos=(625,583), 
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