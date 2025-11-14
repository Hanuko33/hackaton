import pygame


class SFX:
    def __init__(self):
        self.explosion = None

    def load(self):
        self.explosion = pygame.mixer.Sound(
            "./sounds/synthetic_explosion_1.flac")

    def play_explosion(self):
        if self.explosion:
            self.explosion.play()


sfx = SFX()
