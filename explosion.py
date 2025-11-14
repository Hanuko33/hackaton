#!/bin/python3
from sfx import sfx
import pygame
from os import listdir
explosion_dir = "./textures/explosions/"
explosion_images: list[pygame.Surface] = [
    pygame.image.load(explosion_dir + "/" + name)
    for name in sorted(listdir(explosion_dir))]
explosion_images = [
    pygame.transform.scale(pygame.image.load(
        explosion_dir + "/" + name), (64, 64))
    for name in sorted(listdir(explosion_dir))
]


class Explosion:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.iter = 0
        self.dead = False

    def draw(self, screen: "pygame.Surface"):
        if self.dead:
            return
        screen.blit(explosion_images[int(self.iter)],
                    (self.x - 32, self.y - 32))
        self.iter += 0.75
        if round(self.iter) == len(explosion_images):
            self.dead = True


class ExplosionManager:
    def __init__(self):
        self.explosions: list[Explosion] = []

    def add(self, x, y):
        self.explosions.append(Explosion(x, y))
        sfx.play_explosion()

    def clear_explosions(self):
        for e in self.explosions:
            if e.dead:
                self.explosions.remove(e)
                break

    def draw(self, screen: "pygame.Surface"):
        for e in self.explosions:
            e.draw(screen)


explosion_manager = ExplosionManager()
