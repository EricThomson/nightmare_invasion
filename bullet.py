#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
bullet.py
Defines the Bullet class
Part of nightmare invasion package
"""

import pygame
import pygame.mixer
from pygame.sprite import Sprite

class Bullet(Sprite):
    """"Class to handle bullets fired from the ship"""
    
    def __init__(self, game_settings, screen, stats, ship):
        """Create a bullet object at the ship's current position"""
        super().__init__()
        self.screen = screen
        #Load sound file
        soundPath = 'sounds/' + game_settings.bullet_sound_file
        self.bulletSound = pygame.mixer.Sound(soundPath)
        #Create bullet rect at (0,0) and then set correct position
        self.rect = pygame.Rect(0, 0, game_settings.bullet_width,  game_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        #Store position as float
        self.y = float(self.rect.y)
        
        #Bullet parameters
        self.color = game_settings.bullet_colors[stats.element_index]
        self.speed = game_settings.bullet_speed
        
    def update(self):
        """Set the y position of the bullet acc'd to the speed factor"""
        self.y -= self.speed
        self.rect.y = self.y
        
    def draw_bullet(self):
        """Draw bullet to screen. No blit needed:
           https://stackoverflow.com/a/17456583/1886357"""
        pygame.draw.rect(self.screen, self.color, self.rect)