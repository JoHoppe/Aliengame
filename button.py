import pygame.font


class Button():
    def __init__(self,settings,screen,msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        #set dimension of the button
        self.widht,self.height = 200,50
        self.button_color = (244,255,244)
        self.text_color = (0,0,0)
        self.font = pygame.font.SysFont(None,48)


        #Build the button and put it center of screen
        self.rect = pygame.Rect(0,0,self.widht,self.height)
        self.rect.center = self.screen_rect.center

        #call render msg
        self.render_msg(msg)

    def render_msg(self,msg):
        """turn the msg into rendered image and put it center of button"""
        self.msg_image = self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center= self.rect.center

    def draw_button(self):
        """draws the button"""
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)
