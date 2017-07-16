#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
game_stats.py
Defines GameStats() class, part of nightmare invasion.
Tracks various game statistics that change with the game (unlike
Settings() which are parameters and do not depend on user input.
"""

class GameStats():
    """Track statistics for Nightmare Invasion"""
    def __init__(self, game_settings):
        """Initialize statistics."""
        self.game_settings = game_settings
        self.game_active = False  #game is started and drawing (can be paused)
        self.user_started_game = False  #for pause functionality (if game hasn't started, pause does nothing)
        self.high_score = 0  #is not reset with  a new game
        #Reset the values that are   reset with a new game
        self.reset_stats()

        
    def reset_stats(self):
        """Initialize stats that can change with a new game"""
        self.ships_left = self.game_settings.num_spare_ships_initial 
        self.life_num = 1 
        self.score = 0
        self.level = 1
        self.element_index = 0  #index used to pull images, colors for current level