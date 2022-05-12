import pygame
import pygame.sprite as sprite
from game.constants import SQUARE_SIZE

class Player(sprite.Sprite):
    def __init__(self, image, playerNum, pos_X, pos_Y):
        super().__init__()
        self.image = image
        self.playerNum = playerNum
        self.rect = self.image.get_rect()
        self.rect.center = ((pos_X+SQUARE_SIZE / 2),(pos_Y + SQUARE_SIZE / 2) )
