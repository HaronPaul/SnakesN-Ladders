# To install pygame, simply use the command 'pip install pygame'
import pygame
import os
from game.constants import WIDTH, HEIGHT, VIOLET
from game.field import Field
from game.player import Player
from game.functions import rollDice

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
    field.draw_squares(WIN)
    
    playerGroup = pygame.sprite.Group()
    
    # Instantiate the players
    for i in range(NUM_PLAYERS):
        picPath = os.path.join(os.path.dirname(__file__), 'assets', f'player{i+1}.png')
        playerImage = pygame.image.load(picPath)
        newPlayer = Player(playerImage, i+1, 0, 720) # Initialize player's position at number 1 tile
        playerGroup.add(newPlayer)
    
    # Render the player sprites
    playerGroup.draw(WIN)

    # Render a button on the bottom right of the screen
    myFont = pygame.font.SysFont('Arial', 40)
    rollText = myFont.render('ROLL DICE', True, (255,255,255))
    pygame.draw.rect(WIN, VIOLET, [580, 815, 200,70])
    WIN.blit(rollText, (580,815))

    clock.tick(FPS)
    run = True

    while run:
        # Loop through all the events happening
        # May be a mouse click/key press
        for event in pygame.event.get():
            # When user clicks the close button of the window
            # equate run to False
            if event.type == pygame.QUIT:
                run = False
            
            # If clicked position is the 'Roll Dice Button'
            # then randomize a number
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if (mouse_pos[0] >= 580 and  mouse_pos[0] <= 780) and (mouse_pos[1] >= 815 and mouse_pos[1] <= 885):
                    rollDice()

        pygame.display.update()
    pygame.quit()

if __name__ == '__main__':
    main()

