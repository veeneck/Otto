import sys
import pygame

class Base:

    COLOR_BLACK = 0, 0, 0

    def __init__(self):
        return

    def handle_core_events(self, event):
        self.handle_quit_event(event)

    def handle_quit_event(self, event):
        if event.type == pygame.QUIT: 
            sys.exit()