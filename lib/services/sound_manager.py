import pygame
 
class SoundManager:

    sounds = {}

    def __init__(self):
        pass

    def add_sound(self, key, file):
        sound = pygame.mixer.Sound(file)
        self.sounds[key] = sound

    def play(self, key):
        self.sounds[key].play()