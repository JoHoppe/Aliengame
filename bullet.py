import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class defining the bullet"""

    def __init__ (self, settings, screen, ship):
        """create a bullet at ships pos"""
        super().__init__()
        self.screen = screen

        #Create a bullet rect at (0,0) and then correct the position(why not at correct pos from the start)
        self.rect = pygame.Rect(0,0,settings.bullet_width,settings.bullet_height)
        self.rect.centerx=ship.rect.centerx
        self.rect.top= ship.rect.top

        #store the bullets pos in decimal
        self.y = float(self.rect.y)

        self.color = settings.bullet_color
        self.bullet_speed = settings.bullet_speed_factor

    def update(self,bullet):
        """move the bullet"""
        #Update the decimal pos of the bullet
        self.y -= self.bullet_speed
        # Update the rect pos
        self.rect.y = self.y

        # if bullet out of bound ,yeet it. we loop over a copy but remove from the original
        for s_bullet in bullet.copy():
            if s_bullet.y <= 0:
                bullet.remove(s_bullet)
            # print(len(bullet))


    def draw_self(self):
        """draw the bullet on screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)







