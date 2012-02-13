import pygame
 
class SoundManager:

    sounds = {}

    def __init__(self):
        pass

    def add_sound(self, key, file):
        sound = pygame.mixer.Sound(file)
        self.sounds[key] = sound

    def play_sound(self, key):
        self.sounds[key].play()

    def add_music(self, file):
        pygame.mixer.music.load(file)

    def play_music(self):
        pygame.mixer.music.play()
