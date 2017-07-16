#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
button.py
Defines Button class for nightmare invasion package
It's basically a text button with a font, font color,
font size, and background color that is blitted to the
screen. Not used by hud, but just by initial 
splash button

To do:
    Have it take font color and bg color as inputs.
"""

import pygame.font

class Button():
    """Button for games"""
    def __init__(self, game_settings, screen, message, rect, font_size = 48, 
                 text_color = (255, 255, 255), button_color = (0, 0, 0), justify = 'center',
                 underline = False):
        """Initialize button attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        #Set properties of button
        self.button_color = button_color
        self.text_color = text_color
        self.font = pygame.font.SysFont(None, font_size)
        self.underline = underline
        self.justify = justify
        #Built button's rect object, and center
        self.rect = rect 
        #self.rect.centerx = self.screen_rect.centerx
        #The button message needs to be prepped only once
        self.prep_msg(message)
        
    def prep_msg(self, message):
        """Turn message into a rendered image and center text on button"""
        if self.underline:
            self.font.set_underline(True)
        self.msg_image = self.font.render(message, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        if self.justify == 'left':
            self.msg_image_rect.left = self.rect.left + 10
        elif self.justify == 'right':
            self.msg_image_rect.right = self.rect.right - 10

        
    def draw_button(self):
        """Draw button to screen: fill self.rect with color, then blit message text"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

