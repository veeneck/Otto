import sys
import pygame
from lib.base import Base
import lib.core

class Game(Base):

    screen = False
    game_state = lib.core.GameState.MENU

    def __init__(self):
        Base.__init__(self)
        pygame.init()
        self.screen = pygame.display.set_mode([1024, 768])

    def main_loop(self):
        while 1:
            for event in pygame.event.get():
                self.handle_core_events(event)   
        
            if(self.game_state == lib.core.GameState.MENU):
                self.show_menu()

            elif(self.game_state == lib.core.GameState.EXITING):
                sys.exit()
                
            else:
                self.screen.fill(self.COLOR_BLACK)
                self.play_level()

    def show_menu(self):
        import screens.menu
        menu = screens.menu.MainMenu()
        self.game_state = menu.draw_background(self.screen)

    def play_level(self):
        import screens.map
        level = screens.map.PlayLevel()
        self.game_state = level.draw_background(self.screen)

# Game entry point!
g = Game()
g.main_loop()