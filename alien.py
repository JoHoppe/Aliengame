import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class about the alien space ships"""

    def __init__(self,settings,screen):
        """init and set start pos"""
        super(Alien,self).__init__()
        self.screeen = screen
        self.settings = settings

        #load the image sprite set its rect attribute
        self.image = pygame.image.load("images/spaceship-clipart-pixel-6.jpg")
        self.rect = self.image.get_rect()


        #put the image in the top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store the x pos as float
        self.x = float(self.rect.x)

        self.speed = settings.alien_speed


    def blitme(self):
        """draw the ship at current pos"""
        self.screeen.blit(self.image,self.rect)

    def check_edges(self):
        """return true if at the edge of screen"""
        screen_rect = self.screeen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True


    def update(self):
        """moves the alien to the right"""
        self.x += (self.speed*self.settings.alien_direction)
        self.rect.x = self.x

