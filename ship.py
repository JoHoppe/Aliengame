import pygame


class Ship():
    def __init__(self,screen,settings):


        """Initizialze the ship at the starting pos."""
        self.screen=screen

        """init Settings"""
        self.settings=settings

        #Load the ship image and get rect
        self.image=pygame.image.load("Images/rocket-g3081ca617_1280.png")
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        #Start each new shipt at teh bottom center of the screen
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom

        #store a decimal value for ship position
        self.center= float(self.rect.centerx)

        #movement flag
        self.moving_right= False
        self.moving_left= False

    def update(self):
        """update the ships position depending on mov_flag status"""
        # we edit the ships pos value instead of the position in order to have decimal values
        if self.moving_right and (self.rect.right+self.settings.ship_speed_factor) < self.screen_rect.right:
         self.center +=self.settings.ship_speed_factor
        if self.moving_left and self.rect.left-self.settings.ship_speed_factor > self.screen_rect.left:
         self.center -=self.settings.ship_speed_factor

        self.rect.centerx= self.center

    def blitme(self):
        """Draw the ship at the current location"""
        self.screen.blit(self.image,self.rect)

    def ship_center(self):
        self.center= self.screen_rect.centerx

