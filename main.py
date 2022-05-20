# To install pygame, simply use the command 'pip install pygame'
import pygame
import os
from game.constants import WIDTH, HEIGHT, VIOLET
from game.field import Field
from game.player import Player
from game.functions import renderExtras

pygame.init()

# Set the window size
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snakes N\' Ladders')

# Frame rate for the game
FPS = 60

clock = pygame.time.Clock()
def main():
    NUM_PLAYERS = 4 # This is the number of players
    field = Field()

    # Call the draw_squares function of the field instance  
    # field.draw_squares(WIN)
    playerList = []

    # Render other asssets (buttons, player text, etc)
    # renderExtras(WIN)
    
    # Instantiate the players 
    for i in range(NUM_PLAYERS):
        picPath = os.path.join(os.path.dirname(__file__), 'assets', f'player{i+1}.png')
        playerImage = pygame.image.load(picPath)
        newPlayer = Player(playerImage, i+1, 0, 720) # Initialize player's position at number 1 tile
        playerList.append(newPlayer)

    run = True

    currentPlayer = 1 # Initialize player 1 at start of the game
    while run:

        # Reset rendering every loop 
        renderExtras(WIN)
        field.draw_squares(WIN)
        for p in playerList:
            p.draw(WIN)
                
        # Loop through all the events happening
        # May be a mouse click/key press
        for event in pygame.event.get():
            # When user clicks the close button of the window
            # equate run to False and hasPlayed to True
            if event.type == pygame.QUIT:
                run = False

            # If clicked position is the 'Roll Dice Button'
            # then randomize a number
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if (mouse_pos[0] >= 450 and  mouse_pos[0] <= 800) and (mouse_pos[1] >= 800 and mouse_pos[1] <= 900):

                    # This condition will prevent other players from clicking when a player is currently moving
                    if(playerList[currentPlayer - 1].isMoving == False and playerList[currentPlayer - 1].rolled == False):
                        print('Clicked the roll button')
                        playerList[currentPlayer - 1].rollDice()
                    # playerList[currentPlayer - 1].isMoving = True
                    # playerList[currentPlayer - 1].moveRight = True
        playerList[currentPlayer - 1].update()
        
        if(playerList[currentPlayer - 1].rolled == True and playerList[currentPlayer - 1].isMoving == False):
            print('Player turn is done')
            playerList[currentPlayer - 1].rolled = False
            if currentPlayer == 4: currentPlayer = 1
            else: currentPlayer += 1

        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()

if __name__ == '__main__':
    main()

