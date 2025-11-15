import pygame


class SFX:
    def __init__(self):
        self.explosion = None

    def load(self):
        self.explosion = pygame.mixer.Sound(
            "./sounds/synthetic_explosion_1.flac")
        self.alarm = pygame.mixer.Sound("./sounds/alarm.flac")

    def play_explosion(self):
        if self.explosion:
            self.explosion.play()

    def play_alarm(self, times):
        self.explosion.stop()
        if self.alarm:
            self.alarm.play(times)


sfx = SFX()
