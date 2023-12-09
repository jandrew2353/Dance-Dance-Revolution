import pygame, sys

class Arrow():
    def __init__(self, image, x_pos, y_pos):
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos

    def update(self, screen):
	    if self.image is not None:
		    screen.blit(self.image)