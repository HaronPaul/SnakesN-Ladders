# To install pygame, simply use the command 'pip install pygame'
import pygame
import os
from game.constants import WIDTH, HEIGHT, VIOLET
from game.field import Field
from game.player import Player
from game.functions import renderExtras, renderDiceNumber, renderPlayerInventory, consumePowerUp

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
    playerList = []

    # Instantiate the players 
    for i in range(NUM_PLAYERS):
        picPath = os.path.join(os.path.dirname(__file__), 'assets', f'player{i+1}.png')
        playerImage = pygame.image.load(picPath)

        # 3rd and 4th parameters are x and y position
        newPlayer = Player(playerImage, i+1, 0, 630, field) # Initialize player's position at number 1 tile
        playerList.append(newPlayer)

    powerUpGroup = pygame.sprite.Group()
    powerUpHotkeys = [pygame.K_1, pygame.K_2, pygame.K_3]
    for p in field.powerUps:
       powerUpGroup.add(p)
    playedPowerUp = False

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
                
        # Loop through all the events happening
        # May be a mouse click/key press
        for event in pygame.event.get():
            # When user clicks the close button of the window
            # equate run to False and hasPlayed to True
            if event.type == pygame.QUIT:
                run = False

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

        # Update the dice number text on screen
        if playerList[currentPlayer - 1].isMoving:
            renderDiceNumber(WIN, diceNumber)
        
        # Render the player's inventory if it is not empty
        if len(playerList[currentPlayer - 1].inventory) > 0:
            renderPlayerInventory(WIN, playerList[currentPlayer - 1])
        
        playerList[currentPlayer - 1].update()

        if(playerList[currentPlayer - 1].rolled == True and playerList[currentPlayer - 1].isMoving == False):
            print(f'Player {currentPlayer} is done')
            playerList[currentPlayer - 1].checkTile()
            playerList[currentPlayer - 1].rolled = False
            playerList[currentPlayer - 1].aligned = False
            if len(playerList[currentPlayer - 1].inventory) > 0: playerList[currentPlayer - 1].isWaiting = True
            if currentPlayer == 4: currentPlayer = 1
            else: currentPlayer += 1
        
        powerUpGroup.update()
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()

if __name__ == '__main__':
    main()

