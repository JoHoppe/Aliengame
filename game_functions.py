import pygame
import sys
from bullet import Bullet
from alien import Alien
from time import sleep

def get_max_aliens_row(settings,alien_width):
    """get max aliens that fit in a row"""
    availble_space = settings.screen_width - (2 * alien_width)
    max_row_aliens = int(availble_space / (2 * alien_width))
    return max_row_aliens

def get_max_rows(settings,ship_hight,alien_height):
    """returns max number of alien rows"""
    max_space_y= (settings.screen_height-(3*alien_height)-ship_hight)
    max_rows = int(max_space_y/(2*alien_height))
    return max_rows


def create_alien(settings,screen,alien,alien_number,row_number):
    """create alien and and place it at pos"""
    single_alien = Alien(settings,screen)
    single_alien_width = single_alien.rect.width
    single_alien.x = single_alien_width + 2 * single_alien_width * alien_number
    single_alien.rect.x = single_alien.x
    single_alien.rect.y = single_alien.rect.height + 2*single_alien.rect.height*row_number
    alien.add(single_alien)

def create_fleet(settings,screen,alien,ship):
    """creates fleets of aliens"""
    single_alien=Alien(settings,screen)
    max_row_aliens = get_max_aliens_row(settings,single_alien.rect.width)
    max_rows=get_max_rows(settings,ship.rect.height,single_alien.rect.height)


    #create the fleet of aliens
    for row_number in range(max_rows):
        for alien_number in range(max_row_aliens):
            #create alien and place it in row
            create_alien(settings,screen,alien,alien_number,row_number)


def fire_bullet(settings,screen,ship,bullet):
    new_bullet = Bullet(settings, screen, ship)
    bullet.add(new_bullet)


# when pressing the buttom, set mov flag, when stop pressing buttom set mov flag false
def check_key_down_event(event,settings,screen,ship,bullet,alien,game_stats):

    if event.key == pygame.K_RIGHT:
        #move the ship to the right when press right arrow
        ship.moving_right= True

    if event.key == pygame.K_LEFT:
        ship.moving_left= True

    elif event.key == pygame.K_SPACE:
        #when spacebar is pressed call create bullet and add to group
        fire_bullet(settings,screen,ship,bullet)
    elif event.key == pygame.K_q:
        sys.exit()
    if event.type == 768 and not game_stats.game_active:
        set_game_active(settings,screen,ship,bullet,alien,game_stats)
        settings.initzialize_dynamic_settings()
def check_key_up_event(event, ship, bullet):
    if event.key == pygame.K_RIGHT:
        ship.moving_right= False

    if event.key == pygame.K_LEFT:
        ship.moving_left= False
    elif event.key == pygame.K_SPACE:
        bullet.shoot_flag=False
def check_events(settings,screen,ship,bullet,alien,game_stats):

    """repsong the keypresses"""
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_key_down_event(event,settings,screen,ship,bullet,alien,game_stats)
        elif event.type == pygame.KEYUP:
            check_key_up_event(event, ship, bullet)

def set_game_active(settings,screen,ship,bullet,alien,game_stats):
    game_stats.game_active=True
    game_stats.reset_stats()
    alien.empty()
    bullet.empty()

    create_fleet(settings,screen,alien,ship)
    ship.ship_center()



def update_alien(settings,alien,ship,screen,game_stats,bullet):
    """call the update alien, moves alien"""
    check_alien_collision(settings,alien,ship,screen,game_stats,bullet)
    check_alien_bottom(settings,alien,ship,screen,game_stats,bullet)
    check_fleet_edges(settings,alien)
    alien.update()

def ship_hit(settings,game_stats,screen,ship,alien,bullet):
    """reacts to ship getting hit"""
    game_stats.ship_lives-=1
    print("ship hit")
    print(game_stats.ship_lives)
    if(game_stats.ship_lives>0):
        """reset aliens and bullets"""
        alien.empty()
        bullet.empty()

        """create new fleet"""
        create_fleet(settings,screen,alien,ship)
        ship.ship_center()

        """pauses the game """
        sleep(0.5)

    else:
        game_stats.game_active=False
        print("Game Over")


def check_alien_collision(settings,alien,ship,screen,game_stats,bullet):
    """detecs alien and ship collision and calls ship hit reaction"""
    if pygame.sprite.spritecollideany(ship,alien):
        ship_hit(settings,game_stats,screen,ship,alien,bullet)

def check_alien_bottom(settings,alien,ship,screen,game_stats,bullet):
    """check if alien have reached bottom"""
    screen_rect = screen.get_rect()
    for s_alien in alien.sprites():
        if s_alien.rect.bottom >= screen_rect.bottom:
            ship_hit(settings,game_stats,screen,ship,alien,bullet)
            break

def check_fleet_edges(settings,alien):
    for s_alien in alien.sprites():
        if s_alien.check_edges():
            change_fleet_direction(settings,alien)
            break

def change_fleet_direction(settings,alien):
    """drops the fleet and changes direction"""
    for s_alien in alien.sprites():
        s_alien.rect.y += settings.fleet_drop_factor
    settings.alien_direction*=-1

def update_bullet(alien,bullet,settings,screen,ship):
    bullet.update(bullet)
    check_collision(alien,bullet)

    if len(alien)==0:
        'removes all bullets and creates new fleet'
        bullet.empty()
        create_fleet(settings,screen,alien,ship)
        settings.increase_speed()

def check_collision(alien,bullet):
    '''loops thoruh alien and bullet, checks collion and if so deletes both'''
    collision = pygame.sprite.groupcollide(bullet, alien, True, True)

def update_screen(settings,screen,ship,bullet,alien,game_stats,button):

    #Update screen and flip to the next screen
    # redraw everyloop the bg color
    screen.fill(settings.bg_color)

    # draw the ship
    ship.blitme()

    #draw all bullets
    for bullet in bullet.sprites():
        bullet.draw_self()

    alien.draw(screen)

    if not(game_stats.game_active):
        button.draw_button()

    # make the most recent screen visible
    pygame.display.flip()

