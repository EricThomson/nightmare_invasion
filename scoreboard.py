#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scoreboard.py
Scoareboard for nightmare invasion package that generates hud elements for 
display, such as score, lives, high score, etc..
"""

import pygame.font

class Scoreboard():
    """Generate HUD foruser reporting score, level, high score, and lives remaining"""
    def __init__(self, screen, stats):
        """Initialize HUD"""
        self.screen = screen 
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.scoreboard_top = 5
        self.scoreboard_left = 5
        
        #Font settings
        self.text_color = (255, 255, 255)
        self.background_color = (255, 20, 147)
        self.font = pygame.font.SysFont(None, 35)
        
        #Set initial values for all elements of hud
        self.prep_scoreboard_all()
        
    def prep_score(self):
        """Turn the score into a rendered image"""
        rounded_score = round(self.stats.score, -1)
        score_str = "Score: {:,}".format(rounded_score)
        #print("Prepping score: " + score_str)
        self.score_image = self.font.render(score_str, True, self.text_color, self.background_color)
        #Display score at top right
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = self.scoreboard_top
        
    def prep_high_score(self):
        """Turn high score into rendered image"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "High Score: {:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, 
                                                 self.text_color, self.background_color)
        #Center at top of screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
        
    def prep_level(self):
        """Turn level into rendered image"""
        level_str = "Level: " + str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, 
                                            self.background_color)
        #Positoin a few pixels below score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 3
        
    def prep_ships(self):
        """Turn lives left into rendered text image."""
        lives_remaining_str = "Lives: " + str(self.stats.ships_left)
        self.lives_image = self.font.render(lives_remaining_str, True, self.text_color,
                                            self.background_color)
        #Position at top left
        self.lives_rect = self.lives_image.get_rect()
        self.lives_rect.left = self.scoreboard_left
        self.lives_rect.top =  self.scoreboard_top
        
    def prep_scoreboard_all(self):
        """Initialize images for each element of scoreboard"""
        self.prep_score()
        self.prep_high_score()
        self.prep_ships()
        self.prep_level()
   
    def show_score(self):
        """Draw score to screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.lives_image, self.lives_rect)

