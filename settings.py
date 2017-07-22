#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
settings.py
Defines the Setttings() class as part of nightmare invasion package.
This class stores all the main parameters used.
"""

class Settings():
    """A class to store all the parameters used in for Nightmare Invasion."""
    def __init__(self):
        """Initialize the game's settings"""
        #Screen settings                        
        self.screen_width = 1200
        self.screen_height = 800
        self.background_colors = [(200, 200, 0), (200, 200, 200), (120, 255, 120), (0, 0, 0), 
                                  (255, 60, 150), (130, 200, 255), (65, 186, 32), (193, 184, 255),
                                  (255, 255, 255), (255, 27, 0)]
                                  

        #Sound settings
        self.death_wavfiles = ['awwSad.wav', 'youBlewIt.wav',  'gameover.wav']
        self.level_wavfiles = ['onePersonCheer.wav', 'jollyLaugh.wav',  'inconceivable.wav',
                               'wimpyCheer.wav', 'yell4yeeha.wav', 'yababy.wav',
                               'taDaa.wav',   'enthusiasticCheer.wav', 'charge.wav',
                               'celebration.wav']
        
        #Ship settings#
        self.ship_filenames = ['celestiaYellow.bmp', 'spikeGray.bmp', 'daringDoGreen.bmp',
                              'djpon3Black.bmp', 'applejackFuscia.bmp', 'rarityBlue.bmp', 
                              'pinkiePieGreen.bmp', 'fluttershyBlue2.bmp', 'rainbowDashWhite.bmp', 
                              'twilightRed.bmp']     #
        self.num_spare_ships_initial = 2  #number of spare ships
        
        #Alien settings
        self.alien_filenames =  ['nightmareMoonYellow.bmp', 'changelingGray2.bmp', 'ahuizotlGreen.bmp',
                                'dazzlingsBlack.bmp', 'batFuscia.bmp', 'diamondDogBlue2.bmp', 
                                'discordGreen.bmp', 'garbleBlue.bmp', 'chrysalisWhite2.bmp', 
                                'starlightRed.bmp']  #nightmareMoonYellow.bmp
        
        self.alien_ystart = 50  #starting y position (0 is top)
        self.alien_drop_distance = 25

        #Bullet settings
        self.bullet_sound_file = 'bullet.wav'
        self.bullet_width = 5
        self.bullet_height = 10
        self.bullet_colors = [(0, 0, 255), (0, 0, 0), (0, 0, 0), 
                              (240, 240, 240), (255, 255, 0), (0, 0, 0),
                              (0, 0, 0), (0, 0, 0), (0, 0, 0),
                              (255, 255, 0)]
        self.bullets_allowed = 3
        
        #Button settings
        self.buttons_x = int(self.screen_width/3)
        self.buttons_ystart = int(self.screen_height/4)
        self.buttons_width = int(self.screen_width/2)
        self.buttons_height = 50
        
        #Set scale factors
        self.speedup_scale = 1.06 #1.06  #aliens, bullets, and ship speed
        self.score_scale = 1.25  #How much score goes up for hit each level
        #initialize values for attributes that will change each level
        self.initialize_dynamic_settings() 
        
    def initialize_dynamic_settings(self):
        """Initialize settings that change throughought the game"""
        self.ship_speed = 1.1
        self.bullet_speed = 3
        self.alien_speed = 1
        #Scoring
        self.alien_points = 50
        #fleet direction
        self.fleet_direction = 1
        
    def increase_speed(self):
        """Increase speed settings"""
        #To make it harder, ship speed will stop increasing relative to aliens
        if self.ship_speed <= 2.5:
            self.ship_speed *= self.speedup_scale
            self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        #alien points increases, but hits ceiling at 1000
        self.alien_points = min(int(self.alien_points * self.score_scale), 1000)
            
        #Debug
        #print("Alien speed factor: " + str(self.alien_speed))
        #print("Alien points: " + str(self.alien_points))
