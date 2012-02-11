"""
Screen to display the Main Menu.
    :module: Otto.screens.menu
    :synopsis: Contains its own game loop, and returns lib.core.GameState status
        based on user selection.
"""

import sys
import pygame
from lib.base import Base
import lib.core
import lib.services.font_manager

class MainMenu(Base):

    menu_group = pygame.sprite.LayeredUpdates()
    font_group = lib.services.font_manager.FontManager()

    def __init__(self):
        """ Init parent class """
        Base.__init__(self)

    def draw_background(self, screen):
        """
        Main game loop for the main menu screen.
        """

        self.load_resources()
        self.load_fonts()

        while 1:
            for event in pygame.event.get():
                self.handle_core_events(event)

            # animation & events
            self.check_menu_hover()

            # drawing
            self.menu_group.draw(screen)
            self.font_group.draw(screen)
            pygame.display.flip()

    def check_menu_hover(self):
        coords = pygame.mouse.get_pos()
        for key in self.font_group.messages:
            message = self.font_group.messages[key]
            if message['rect'] is not None and message['rect'].collidepoint(coords):
                message['color'] = (199, 196, 70)
            else:
                message['color'] = (77, 77, 77)
            
    def load_resources(self):
        """
        Bring in the stuffs.
        """

        resources = {
            'bg'            : {'layer' : 0, 'topleft' : [0, 0],     'image' : 'otto_interface_bg.jpg'},
            'logo'          : {'layer' : 1, 'topleft' : [200, 125], 'image' : 'otto_logo.png'},
            'play_icon'     : {'layer' : 1, 'topleft' : [615, 414], 'image' : 'otto_interface_x.png'},
            'option_icon'   : {'layer' : 1, 'topleft' : [615, 464], 'image' : 'otto_interface_x.png'},
            'quit_icon'     : {'layer' : 1, 'topleft' : [615, 514], 'image' : 'otto_interface_x.png'}       
        }

        for assets in resources:
            asset = resources[assets]
            spr = pygame.sprite.Sprite()
            spr.image = pygame.image.load('resources/' + asset['image'])
            spr.rect = spr.image.get_rect()
            spr.rect.topleft = asset['topleft']
            spr._layer = asset['layer']
            self.menu_group.add(spr)

    def load_fonts(self):

        messages = [
            {'layer' : 2, 'font' : 'resources/dinconra.ttf', 'size' : 35,
                'color' : (77, 77, 77), 'topleft' : [650, 405], 'text' : 'play', 'key' : 'play'},
            {'layer' : 2, 'font' : 'resources/dinconra.ttf', 'size' : 35, 
                'color' : (77, 77, 77), 'topleft' : [650, 455], 'text' : 'options', 'key' : 'options'},
            {'layer' : 2, 'font' : 'resources/dinconra.ttf', 'size' : 35, 
                'color' : (77, 77, 77), 'topleft' : [650, 505], 'text' : 'quit', 'key' : 'quit'}
        ]

        self.font_group.add_messages(messages)
