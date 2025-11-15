import pygame
from random import randint
from explosion import explosion_manager

uranium_image = pygame.image.load("./textures/Uranium.png")
uranium_image = pygame.transform.scale(uranium_image, (64, 64))


class Uranium:
    def __init__(self, x, y, satisfaction):
        self.x = x
        self.y = y
        self.satisfied = satisfaction
        self.max_satisfaction = satisfaction

    def draw(self, screen):
        modified = uranium_image.copy().convert_alpha()
        color = [(1000 - self.satisfied) / 6, self.satisfied / 6, 255]
        for i in range(0, 3):
            color[i] = max(color[i], 0)
            color[i] = min(color[i], 255)
        modified.fill(color,
                      special_flags=pygame.BLEND_RGBA_MIN)
        screen.blit(modified, (self.x - 32, self.y - 32))

    def update(self, delta):
        divide_by = self.satisfied / 500
        divide_by = divide_by if divide_by > 0.25 else 0.25
        self.x += randint(-1, 1) / divide_by * delta
        self.y += randint(-1, 1) / divide_by * delta
        self.satisfied -= 1


class UraniumManager:
    def __init__(self):
        self.uranium: "Uranium" = []

    def add(self, x, y, t):
        self.uranium.append(Uranium(x, y, 1000 - t / 10))

    def draw(self, screen: "pygame.Surface"):
        for u in self.uranium:
            u.draw(screen)

    def to_positions(self):
        retval = []
        for u in self.uranium:
            retval.append((u.x, u.y))
        return retval

    def update(self, state, delta):
        for u in self.uranium:
            u.update(delta)
            if (u.satisfied < 0):
                self.uranium.remove(u)
                state.score -= 200
                state.reactor_sanity -= 1
                for x in range(-32, 32, 16):
                    for y in range(-32, 32, 16):
                        explosion_manager.add(u.x + x, u.y + y)
                break
