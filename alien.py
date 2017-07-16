#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
alien.py
Defines the Alien class, part of the nightmare invasion package. It is the
enemy class that is used to populate the space that the ship shoots at.
"""

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet"""
    def __init__(self, game_settings, screen, stats):
        """Initialize the alien and its starting position"""
        super().__init__()
        self.screen = screen
        self.game_settings = game_settings
        
        #Load the alien image and set its rect attributes
        alien_path = 'images/' + game_settings.alien_filenames[stats.element_index]
        self.image = pygame.image.load(alien_path)
        self.rect = self.image.get_rect()
        
        #start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.game_settings.alien_ystart  #self.rect.height
        
        #Store the alien's exact position
        self.x = float(self.rect.x)
        
    def update(self):
        """Move the alien horizontally either right or left"""
        self.x += self.game_settings.alien_speed * self.game_settings.fleet_direction
        self.rect.x = self.x
        
    def check_edges(self):
        """Return true if alien has hit an edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        
    def blitme(self):
        """Draw the alien at its current location"""
        self.screen.blit(self.image, self.rect)
        
