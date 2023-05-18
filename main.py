import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button



def run_game():
    #initialize gama and create a screen object.
    pygame.init()

    settings=Settings()

    screen = pygame.display.set_mode((settings.screen_width,settings.screen_height))

    # make a ship
    ship = Ship(screen,settings)

    pygame.display.set_caption("Alien Invasion")

    #make a group of all shots firred
    bullet = Group()

    #make alien
    alien = Alien(settings,screen)

    #make group of aliens
    alien= Group()

    #create fleets of aliens
    gf.create_fleet(settings,screen,alien,ship)

    #create Stats object
    game_stats= GameStats(settings)

    #create button
    button = Button(settings,screen,"Play")

    #start the game loop
    while True:
        gf.check_events(settings,screen,ship,bullet,alien,game_stats)
        if (game_stats.game_active):
            ship.update()
            gf.update_bullet(alien,bullet,settings,screen,ship)
            gf.update_alien(settings,alien,ship,screen,game_stats,bullet)
        gf.update_screen(settings,screen,ship,bullet,alien,game_stats,button)

run_game()



