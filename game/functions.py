
import pygame
import os

def renderExtras(WIN):
    # Render a roll button on the bottom right of the screen
    roll_button = pygame.image.load(os.path.join(os.path.dirname(__file__), '..', 'assets', 'roll_button.png'))
    WIN.blit(roll_button, (450, 800))

    # Render current player text
    current_player_text = pygame.image.load(os.path.join(os.path.dirname(__file__), '..', 'assets', 'current_player_text.png'))
    WIN.blit(current_player_text, (0, 800))

    # Render Power-ups textt
    power_ups_text = pygame.image.load(os.path.join(os.path.dirname(__file__), '..', 'assets', 'power_ups_text.png'))
    WIN.blit(power_ups_text, (200, 800))



