#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
nightmare_invasion.py
Main part of Nightmare Invasion package, which is adapted from Alien Invasion
in Python Crash Course by Eric Matthes.
"""
import pygame
import pygame.mixer
from pygame.sprite import Group

from settings import Settings  
from ship import Ship
from game_stats import GameStats 
from scoreboard import Scoreboard
import game_functions

# set up mixer to pretend you know what you are doing  
pygame.mixer.pre_init(44100, -16, 2, 2048)

def run_game():
    #initialize game and create a screen object
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Nightmare Invasion")  
    #Create a game stats and scoreboard instance
    stats = GameStats(game_settings)
    scoreboard = Scoreboard(screen, stats)
    #Make a ship
    ship = Ship(game_settings, screen, stats)
    #Make an alien group
    aliens = Group()
    game_functions.create_fleet(game_settings, screen, stats, ship, aliens)
    #Make a group to store bullets in
    bullets = Group()
    #Splash screen of buttons
    buttons = game_functions.create_buttons(game_settings, screen)
    #Start main game loop
    while True:
        game_functions.check_events(game_settings, screen, stats, scoreboard, 
                                    buttons, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            game_functions.update_bullets(game_settings, screen, stats, scoreboard, 
                                          ship, aliens, bullets)
            game_functions.update_aliens(game_settings, screen, stats, scoreboard, 
                                         ship, aliens, bullets)
        game_functions.update_screen(game_settings, screen, stats, scoreboard, ship, 
                                     aliens, bullets, buttons) 

if __name__ == '__main__':
    run_game()
