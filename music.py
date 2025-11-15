from random import choice
import pygame


class Music:
    def __init__(self):
        self.filenames = ["elevator_to_reactor.mp3",
                          "nuclear_cave.mp3", "Ruined City Theme.flac"]

    def update(self):
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load("./sounds/music/" + choice(self.filenames))
            pygame.mixer.music.play()

    def play_lost(self):
        pygame.mixer.music.load("./sounds/music/Sadness.ogg")
        pygame.mixer.music.play(-1)

    def play_intro(self):
        pygame.mixer.music.load("./sounds/music/MiddelWeie.flac")
        pygame.mixer.music.play(-1)

    def stop(self):
        pygame.mixer.music.stop()


music = Music()
