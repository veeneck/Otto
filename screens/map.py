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

class PlayLevel(Base):

    level_group = pygame.sprite.LayeredUpdates()
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

            for event in pygame.event.get():
                self.handle_core_events(event)

            screen.fill(self.COLOR_BLACK)
            pygame.display.flip()    
    
    """ ---------------------------
            LOAD ASSETS
    --------------------------- """ 
            
    def load_resources(self):
        pass

    def load_fonts(self):
        pass

    def load_sounds(self):
        self.sound_group.add_music('resources/sound/otto_basetrack.ogg')
        pygame.mixer.music.set_volume(1.0)
        self.sound_group.play_music()

