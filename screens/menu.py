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
import lib.services.sound_manager

class MainMenu(Base):

    menu_group = pygame.sprite.LayeredUpdates()
    font_group = lib.services.font_manager.FontManager()
    sound_group = lib.services.sound_manager.SoundManager()
    resources = {}

    def __init__(self):
        Base.__init__(self)

    """ ---------------------------
            MAIN LOOP
    --------------------------- """

    def draw_background(self, screen):

        self.load_resources()
        self.load_fonts()
        self.load_sounds()

        while 1:

            clicked = False

            for event in pygame.event.get():
                self.handle_core_events(event)
                if event.type is pygame.MOUSEBUTTONDOWN:
                    clicked = True

            ret = self.check_menu_hover(clicked)
            if(ret):
                if ret is lib.core.GameState.PLAYING:
                    pygame.mixer.music.set_volume(1.0)
                else:
                    return ret

            self.menu_group.draw(screen)
            self.font_group.draw(screen)

            pygame.display.flip()

    """ ---------------------------
            MOUSE EVENTS
    --------------------------- """

    def check_menu_hover(self, clicked):

        coords = pygame.mouse.get_pos()
        for key in self.font_group.messages:
            message = self.font_group.messages[key]
            icon = self.resources[message['key'] + '_icon']

            if message['rect'] is not None and message['rect'].collidepoint(coords):

                message['color'] = (199, 196, 70)

                if icon['image'] is not 'otto_interface_circle.png':
                    icon['image'] = 'otto_interface_circle.png'
                    icon['sprite'] = self.load_sprite(icon, icon['sprite'])
                    self.sound_group.play_sound(message['key'])

                if clicked:
                    return message['state']

            else:
                message['color'] = (77, 77, 77)
                if icon['image'] is not 'otto_interface_x.png':
                    icon['image'] = 'otto_interface_x.png'
                    icon['sprite'] = self.load_sprite(icon, icon['sprite'])  
        
        return False      
    
    """ ---------------------------
            LOAD ASSETS
    --------------------------- """ 
            
    def load_resources(self):

        self.resources = {
            'bg'            : {'layer' : 0, 'topleft' : [0, 0],     'image' : 'otto_interface_bg.jpg', 'sprite': None},
            'logo'          : {'layer' : 1, 'topleft' : [200, 125], 'image' : 'otto_logo.png', 'sprite': None},
            'play_icon'     : {'layer' : 1, 'topleft' : [615, 414], 'image' : 'otto_interface_x.png', 'sprite': None},
            'option_icon'   : {'layer' : 1, 'topleft' : [615, 464], 'image' : 'otto_interface_x.png', 'sprite': None},
            'quit_icon'     : {'layer' : 1, 'topleft' : [615, 514], 'image' : 'otto_interface_x.png', 'sprite': None}        
        }

        for assets in self.resources:
            asset = self.resources[assets]
            spr = pygame.sprite.Sprite()
            spr = self.load_sprite(asset, spr)
            self.menu_group.add(spr)

    def load_sprite(self, asset, spr):
        spr.image = pygame.image.load('resources/' + asset['image'])
        spr.rect = spr.image.get_rect()
        spr.rect.topleft = asset['topleft']
        spr._layer = asset['layer']
        asset['sprite'] = spr
        return spr

    def load_fonts(self):

        messages = [
            {'layer' : 2, 'font' : 'resources/dinconra.ttf', 'size' : 35, 'color' : (77, 77, 77), 'topleft' : [650, 405], 'text' : 'play', 'key' : 'play', 'state' : lib.core.GameState.PLAYING},
            {'layer' : 2, 'font' : 'resources/dinconra.ttf', 'size' : 35, 'color' : (77, 77, 77), 'topleft' : [650, 455], 'text' : 'options', 'key' : 'option', 'state' : lib.core.GameState.OPTIONS},
            {'layer' : 2, 'font' : 'resources/dinconra.ttf', 'size' : 35, 'color' : (77, 77, 77), 'topleft' : [650, 505], 'text' : 'quit', 'key' : 'quit', 'state' : lib.core.GameState.EXITING}
        ]

        self.font_group.add_messages(messages)

    def load_sounds(self):
        self.sound_group.add_sound('play', 'resources/sound/Otto_interface_snd_01.ogg')
        self.sound_group.add_sound('option', 'resources/sound/Otto_interface_snd_02.ogg')
        self.sound_group.add_sound('quit', 'resources/sound/Otto_interface_snd_03.ogg')

        self.sound_group.add_music('resources/sound/otto_basetrack.ogg')
        pygame.mixer.music.set_volume(0.2)
        self.sound_group.play_music()

