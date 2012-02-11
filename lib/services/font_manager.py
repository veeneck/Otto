import pygame
 
class FontManager:

    fonts = {}
    messages = {}

    """
    message = {
        'font' : 'dinconra.ttf', 
        'size' : 35, 
        'color' : (77, 77, 77), 
        'topleft' : [650, 405], 
        'text' : 'play'
        'key' : 'play'
        'rect' : [assigned after each drawing]
    }
    """

    ANTI_ALIAS = 1

    def __init__(self):
        pass

    # Expects tuples to be passed in. i.e.: ('arial', 18)
    def add_font(self, font):
        typeface = font[0]
        size = font[1]
        self.fonts[font] = pygame.font.Font(typeface, size)

    def add_messages(self, messages):
        for message in messages:
            message['rect'] = None
            self.messages[message['key']] = message 
            self.add_font((message['font'], message['size']))

    def draw_single_message(self, surface, message):
        font = self.fonts[(message['font'], message['size'])]
        font_surface = font.render(message['text'], self.ANTI_ALIAS, message['color'])

        # set rect for later collision detection
        message['rect'] = font_surface.get_rect()
        message['rect'].x = message['topleft'][0]
        message['rect'].y = message['topleft'][1]

        surface.blit(font_surface, message['topleft'])

    def draw(self, surface):
        for key in self.messages:
            message = self.messages[key]
            self.draw_single_message(surface, message)