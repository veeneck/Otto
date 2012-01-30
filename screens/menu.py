import sys
import pygame
from lib.base import Base
import lib.core

class MainMenu(Base):

    menu_group = pygame.sprite.Group()

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

        # Logo image
        logo = pygame.sprite.Sprite()
        logo.image = pygame.image.load("resources/otto_logo.png")
        logo.rect = logo.image.get_rect()
        logo.rect.topleft = [200, 125]

        # Background image
        bg = pygame.sprite.Sprite()
        bg.image = pygame.image.load("resources/otto_interface_bg.jpg")
        bg.rect = bg.image.get_rect()
        bg.rect.topleft = [0, 0]

        self.menu_group.add(bg, logo)