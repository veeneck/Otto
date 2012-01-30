import sys
import pygame
from lib.base import Base
import lib.core

class MainMenu(Base):

    menu_group = pygame.sprite.LayeredUpdates()

    def __init__(self):
        Base.__init__(self)

    def draw_background(self, screen):

        self.load_resources()

        while 1:
            for event in pygame.event.get():
                self.handle_core_events(event)

            self.menu_group.draw(screen) # draw everything in the group
            pygame.display.flip()
            
    def load_resources(self):

        resources = {
            'bg' : {'layer' : 0, 'topleft' : [0, 0], 'image' : 'otto_interface_bg.jpg'},
            'logo' : {'layer' : 1, 'topleft' : [200, 125], 'image' : 'otto_logo.png'},
            'play_icon' : {'layer' : 1, 'topleft' : [615, 414], 'image' : 'otto_interface_x.png'},
            'option_icon' : {'layer' : 1, 'topleft' : [615, 464], 'image' : 'otto_interface_x.png'},
            'quit_icon' : {'layer' : 1, 'topleft' : [615, 514], 'image' : 'otto_interface_x.png'}       
        }

        for assets in resources:
            asset = resources[assets]
            spr = pygame.sprite.Sprite()
            spr.image = pygame.image.load('resources/' + asset['image'])
            spr.rect = spr.image.get_rect()
            spr.rect.topleft = asset['topleft']
            spr._layer = asset['layer']
            self.menu_group.add(spr)