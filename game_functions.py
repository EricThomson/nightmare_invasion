#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
game_functions.py
All of the functions used in nightmare invasion, a space invaders clone 
adapted from Python Crash Course by Eric Matthes.
"""
import sys
from time import sleep 
from random import randint
import pygame
import pygame.mixer

from bullet import Bullet
from alien import Alien
from button import Button
    
"""
USER-INTERACTIONS: USER EVENT RELATED FUNCTIONS
Functions for checking and getting events from user, either keyboard or mouse.
"""
def check_events(game_settings, screen, stats, scoreboard, buttons, ship, aliens, bullets):
    """respond to keypresses and mouse events from user."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_clicked(game_settings, screen, stats, scoreboard, buttons, ship, 
                              aliens, bullets,  mouse_x, mouse_y)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, game_settings, screen, stats, ship, bullets, scoreboard, aliens)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_keydown_events(event, game_settings, screen, stats, ship, bullets, scoreboard, aliens):
    """Respond to keypresses for moving, shooting, quitting"""
    if event.key == pygame.K_RIGHT:
        #move to the right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        #Move to the left
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        #Fire bullet
        fire_bullet(game_settings, screen, stats, ship, bullets)
    elif event.key == pygame.K_RETURN and not stats.game_active:
        start_new_game(game_settings, screen, stats, scoreboard, ship, aliens, bullets)
    elif event.key == pygame.K_p and stats.user_started_game:  #toggle game active state unless game hasn't begun
        stats.game_active = not stats.game_active
        
    elif event.key == pygame.K_q:
        #quit with key q
        pygame.quit()
        sys.exit()
     
def check_keyup_events(event, ship):
    """Respond to key releases for moving ship"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_play_clicked(game_settings, screen, stats, scoreboard, buttons, ship, aliens, bullets, 
                      mouse_x, mouse_y):
    """Start a new game when the player clicks opening splash screen."""
    splash_height = buttons[-1].rect.bottom - buttons[0].rect.top
    splash_rect = pygame.Rect(buttons[0].rect.left, 
                              buttons[0].rect.top, 
                              buttons[0].rect.width,
                              splash_height)  #left, top, width, height
    splash_clicked = splash_rect.collidepoint(mouse_x, mouse_y)
    #button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    #Only activate via click if game is presently inactive
    if splash_clicked and not stats.game_active:
        start_new_game(game_settings, screen, stats, scoreboard, ship, aliens, bullets)


"""
DRAWING: CREATING AND DRAWING STUFF TO SCREEN
"""
def update_screen(game_settings, screen, stats, scoreboard, ship, aliens, bullets, buttons):
    """
    Update images on the screen and flip to the new screen.
    This is the core drawing function that draws each iteration
    through the main program loop.
    """
    #Draw screen with background color
    screen.fill(game_settings.background_colors[stats.element_index]) ###
    #Draw bullets behind ships and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()  #don't use bullets.draw(screen) because we aren't using images
    ship.blitme()
    aliens.draw(screen)
    #Draw scoreboard
    scoreboard.show_score()
    #Draw the play button if the game is inactive (after others so it shows up)
    if not stats.game_active and not stats.user_started_game:
        for button in buttons:
            button.draw_button()
    #Flip to new screen
    pygame.display.flip()
    
def update_aliens(game_settings, screen, stats, scoreboard, ship, aliens, bullets):
    """Check for interactions with screen edges, bullets, and ship, and move accordingly"""
    check_fleet_edges(game_settings, aliens)
    #Look for aliens hitting bottom of screen
    check_fleet_bottom(game_settings, screen, stats, scoreboard, ship, aliens, bullets)
    #look for alein-ship collisions
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(game_settings, screen, stats, scoreboard, ship, aliens, bullets)
    aliens.update()  #built-in for sprites.group: calls update for each instance in group
        
def update_bullets(game_settings, screen, stats, scoreboard, ship, aliens, bullets):
    """Get rid of bullets that have moved off screen, check for collisions, and
    update position of bullets."""
    #Get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(game_settings, screen, stats, scoreboard, ship, aliens, bullets)
    bullets.update() #update position
    
def fire_bullet(game_settings, screen, stats, ship, bullets):
    """Fire a bullet if limit of number of bullets not reached yet, and play bullet sound"""
    #Create a new bullet and add it to the bullets group
    if len(bullets) < game_settings.bullets_allowed:
        new_bullet = Bullet(game_settings, screen, stats, ship)
        bullets.add(new_bullet)
        #Play shooting sound
        if stats.game_active: #without this will play sound during button screen
            new_bullet.bulletSound.play(0)
        
def create_fleet(game_settings, screen, stats, ship, aliens):
    """create a full fleet of aliens"""
    alien = Alien(game_settings, screen, stats)  #this is just to get width
    number_columns = get_number_columns(game_settings, alien.rect.width)
    number_rows = get_number_rows(game_settings, ship.rect.height, alien.rect.height)
    #print("Number of rows: " + str(number_rows))
    #Create first row of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_columns):
            #create an alien and place it in the row
            create_alien(game_settings, screen, stats, aliens, alien_number, row_number)
    #print("Alien speed: " + str(game_settings.alien_speed)) #for debugging
    
def create_alien(game_settings, screen, stats, aliens, alien_number, row_number):
    """Create an alien and place it in a row."""
    alien = Alien(game_settings, screen, stats)
    alien_width = alien.rect.width
    alien.x = alien_width*0.25 + 2*alien_width*alien_number
    alien.rect.x= alien.x
    alien.rect.y = game_settings.alien_ystart + 1.3*alien.rect.height*row_number
    aliens.add(alien)
   

def start_new_game(game_settings, screen, stats, scoreboard, ship, aliens, bullets):
    """Initialize stuff for starting new game when user initiates game"""
    #Hide mouse cursor (will reappear when game ends in ship_hit)
    pygame.mouse.set_visible(False)
    #Reset game settings
    game_settings.initialize_dynamic_settings()
    #Reset game stats
    stats.reset_stats()
    stats.game_active = True
    #Create new ship (otherwise ship will remain where it was)
    ship.change_image()
    #Reset scoreboard images
    scoreboard.prep_scoreboard_all()
    #Empty list of aliens and bullets
    aliens.empty()
    bullets.empty()
    #Creatre a new alien fleet and center ship
    create_fleet(game_settings, screen, stats, ship, aliens)
    ship.center_ship()
    stats.user_started_game = True

"""
DYNAMICS: FUNCTIONS FOR LOOKING FOR, RESPONDING TO INTERACTIONS BETWEEN ELEMENTS OF SCREEN
"""

def check_bullet_alien_collisions(game_settings, screen, stats, scoreboard, ship, aliens, bullets):
    """
    Checks for collisions between bullets and enemies, and handles the
    consequences of any collisions.
    """
    #Check for collision, and remove any that have collided 
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    #Increment score and check to see if high score has been passed
    if collisions:
        for aliens in collisions.values():
            stats.score += game_settings.alien_points*len(aliens)
            scoreboard.prep_score()
        check_high_score(stats, scoreboard)
    #If you killed 'em all, play celebration and reset things
    if len(aliens) == 0:
        #Play appropriate sound for levelling up
        if stats.level <= 10:
            play_level_sound(game_settings, stats)
        #Adjust speed of aliens
        alien_speed_adjust(game_settings, stats)
        stats.level += 1
        element_index_update(stats)
        bullets.empty()
        ship.change_image()
        create_fleet(game_settings, screen, stats, ship, aliens)
        scoreboard.prep_level()

def alien_speed_adjust(game_settings, stats):
    """Adjust speed of aliens when needed"""
    if stats.level <= 10:
        game_settings.increase_speed()
    if stats.level >= 15 and game_settings.alien_speed <= 2.3:
        game_settings.increase_speed()
    if stats.level >= 25 and game_settings.alien_speed <= 2.8:
        game_settings.increase_speed()
    #print(game_settings.alien_speed)  #for debugging


def check_fleet_bottom(game_settings, screen, stats, scoreboard, ship, aliens, bullets):
    """Check if any enemies have reached the bottom of the screen. """
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #Treat this the same as if the ship got hit
            ship_hit(game_settings, screen, stats, scoreboard, ship, aliens, bullets)
            break #break out of for loop so it doesn't keep checking aliens
        
def check_fleet_edges(game_settings, aliens):
    """Respond appropriately if any aliens have reached an edge"""
    for alien in aliens.sprites():
        #check_edges returns True if they are at an edge
        if alien.check_edges():
            lower_fleet(game_settings, aliens)
            break #break out of for loop so each alien doesn't send it down
        
def lower_fleet(game_settings, aliens):
    """Drop the entire fleet and change its direction of movement."""
    for alien in aliens.sprites():
        alien.rect.y += game_settings.alien_drop_distance
    game_settings.fleet_direction *= -1

def ship_hit(game_settings, screen, stats, scoreboard, ship, aliens, bullets):
    """Respond to ship being hit by alien"""
    #set up and play death sound
    death_sound_filename = game_settings.death_wavfiles[stats.life_num-1]
    play_sound(death_sound_filename)
    #Deal with cases with ships remaining, versus game over
    if stats.ships_left > 0:
        #Update stats and scoreboard
        stats.ships_left -= 1
        scoreboard.prep_ships()
        #Empty the list of aliens and bullets, create new fleet
        aliens.empty()
        bullets.empty()
        create_fleet(game_settings, screen, stats, ship, aliens)
        #Pause let user regroup
        sleep(0.75)
    else:
        stats.game_active = False
        stats.user_started_game = False
        pygame.mouse.set_visible(True)
    #which life are you on?
    stats.life_num += 1
        
def play_level_sound(game_settings, stats):
    """Play celebration sound for levelling up"""
    level_sound_filename = game_settings.level_wavfiles[stats.element_index]
    if stats.level == 10:
        numSoundRepeats = 1
    else:
        numSoundRepeats = 0
    play_sound(level_sound_filename, numSoundRepeats)
        
def play_sound(fileName, numRepeats = 0):
    """Play the wave fileName"""
    pygame.mixer.stop()
    filepath = 'sounds/' + fileName
    try:
        sound = pygame.mixer.Sound(filepath)
        sound.play(numRepeats)
    except pygame.error as message:
        print('Error in game_functions.play_sound: ' + str(message))

    
"""
STATS: BASIC CALCULATIONS AND RECORDKEEPING STUFF
"""
def get_number_columns(game_settings, alien_width):
    """determine how many enemies fit in a row"""
    usable_screen_width = game_settings.screen_width - alien_width
    number_columns = int(usable_screen_width / (2 * alien_width))  
    return number_columns

def get_number_rows(game_settings, ship_height, alien_height):
    """Determine number of alien rows that will fit on screen."""
    usable_screen_height = game_settings.screen_height - 2*alien_height - 2*ship_height
    number_rows = int(usable_screen_height / alien_height)
    return number_rows

def element_index_update(stats):
    """Update current index used to synch up elements at each level."""
    #set bg color depending on level
    currentLevel = stats.level
    if currentLevel <= 10:
        stats.element_index = currentLevel - 1
    else:
        stats.element_index = randint(0,9)
        
def check_high_score(stats, scoreboard):
    """Check to see if there's a new high score"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        scoreboard.prep_high_score()


"""
CREAING BASIC STATIC ELEMENTS
Things like buttons. Probably should be class for these.
""" 
def create_buttons(game_settings, screen):
    """Create list of all buttons for splash screen"""    
    play_rect, click_rect, move_rect, quit_rect, pause_rect = \
        prepare_button_rects(game_settings)
    title_button = Button(game_settings, screen, "Nightmare Invasion", play_rect, 
                          text_color = (0, 0, 0), button_color = (255, 20, 147), 
                          justify = 'center', underline = True) 
    play_button = Button(game_settings, screen, "Click here or press Enter to play", 
                          click_rect, font_size = 40, text_color = (255, 255, 255), 
                          button_color = (255, 20, 147), justify = 'left')  
    move_button = Button(game_settings, screen, "Use L/R arrows to move, space to shoot", 
                         move_rect, font_size = 40, text_color = (255, 255, 255), 
                         button_color = (255, 20, 147), justify = 'left') 
    quit_button = Button(game_settings, screen, "Press q to quit", 
                         quit_rect, font_size = 40, text_color = (255, 255, 255), 
                         button_color = (255, 20, 147), justify = 'left') 
    pause_button = Button(game_settings, screen, "Press p to pause/unpause game", 
                          pause_rect, font_size = 40, text_color = (255, 255, 255), 
                          button_color = (255, 20, 147), justify = 'left') 
    buttons = [title_button, play_button, move_button, quit_button, pause_button]
    return buttons
    
    
def prepare_button_rects(game_settings):
    """Return rectangles for initial splash screen. This is brittle and app-specific.
    title--play--move--quit--pause"""
    play_rect = pygame.Rect(game_settings.buttons_x, 
                            game_settings.buttons_ystart,
                            game_settings.buttons_width, 
                            game_settings.buttons_height)  #will become title_rect
    click_rect = pygame.Rect(game_settings.buttons_x, 
                             game_settings.buttons_ystart + game_settings.buttons_height,
                             game_settings.buttons_width, 
                             game_settings.buttons_height)  #play
    move_rect = pygame.Rect(game_settings.buttons_x, 
                             game_settings.buttons_ystart + 2* game_settings.buttons_height,
                             game_settings.buttons_width, 
                             game_settings.buttons_height)  #move
    quit_rect = pygame.Rect(game_settings.buttons_x, 
                             game_settings.buttons_ystart + 3* game_settings.buttons_height,
                             game_settings.buttons_width, 
                             game_settings.buttons_height)  #move
    pause_rect = pygame.Rect(game_settings.buttons_x, 
                             game_settings.buttons_ystart + 4* game_settings.buttons_height,
                             game_settings.buttons_width, 
                             game_settings.buttons_height)  #move 
    
    return play_rect, click_rect, move_rect, quit_rect, pause_rect









    
        
        
        
        
        
#%% hi