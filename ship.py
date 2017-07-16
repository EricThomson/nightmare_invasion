#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ship.py
Defines the Ship() class as part of nightmare_invastion package. This class
defines the protagonist's vehicle that shoots at enemies.
"""
import pygame
import pygame.mixer
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, game_settings, screen, stats):
        """initialize the ship and set its starting position"""
        super().__init__()
        self.screen = screen     
        self.game_settings = game_settings
        self.stats = stats
        #Movement flags
        self.moving_right = False
        self.moving_left = False
        
        #load ship image and get its rect
        ship_path = 'images/' + game_settings.ship_filenames[stats.element_index]
        #print("Ship path: " + ship_path)
        self.image = pygame.image.load(ship_path)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #start each new ship at the bottom center
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
  
    def center_ship(self):
        """center the ship on the screen"""
        self.center = self.screen_rect.centerx
        
    def change_image(self):
        """Change the image based on the element_index"""
        #print("change_image stats.element_index: " + str(self.stats.element_index))
        ship_path = 'images/' + self.game_settings.ship_filenames[self.stats.element_index]
        self.image = pygame.image.load(ship_path)    
         
    def update(self):
        """Update position based on movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.game_settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.center -= self.game_settings.ship_speed
        #update center
        self.rect.centerx = self.center
            
    def blitme(self):
        """transfer (blit) the ship image to the current location"""
        self.screen.blit(self.image, self.rect)
