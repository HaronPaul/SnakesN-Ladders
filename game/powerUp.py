import pygame
import pygame.sprite as sprite
from game.constants import SQUARE_SIZE

powerUpFileNames = ['plus1.png', 'plus2.png', 'plus3.png', 'minus1.png', 'minus2.png', 'minus3.png']

class PowerUp(sprite.Sprite):
    def __init__(self, pic_path, number, row, col, pos_X, pos_Y):
        super().__init__()
        self.image = pygame.image.load(pic_path)
        self.rect = self.image.get_rect()
        self.row = row
        self.col = col
        self.pos = (pos_X, pos_Y)
        self.number = number
        self.rect = self.image.get_rect()
        self.consumed = False
        self.rect.center = ((pos_X+SQUARE_SIZE / 2),(pos_Y + SQUARE_SIZE / 2)) # Location is at the center of the tile

    def update(self):
        if self.consumed == True:
            self.kill()