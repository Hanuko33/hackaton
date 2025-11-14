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


music = Music()
