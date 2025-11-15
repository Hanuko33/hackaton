import pygame
from random import choice, randint
possibilities = [
    ("Barium", "Krypton", 200),
    ("Barium", "Krypton", 170),
    ("Tellurium", "Zirconium", 197)
]

textures = {
    "Barium": pygame.transform.scale(
        pygame.image.load("./textures/Barium.png"), (24, 24)),
    "Krypton": pygame.transform.scale(
        pygame.image.load("./textures/Krypton.png"), (24, 24)),
    "Tellurium": pygame.transform.scale(
        pygame.image.load("./textures/Tellurium.png"), (24, 24)),
    "Zirconium": pygame.transform.scale(
        pygame.image.load("./textures/Zirconium.png"), (24, 24))
}


class Particle:
    def __init__(self, name, font, x, y):
        self.live = 100
        self.x = x
        self.y = y
        if type(name) is type(""):
            self.texture = textures[name]
            self.vx = randint(-2, 2)
            self.vy = randint(-2, 2)
        if type(name) is type(1):
            self.texture = font.render(
                str(name) + "MeV", True, (255, 255, 255))
            self.vy = -1
            self.vx = 0

    def update(self, delta):
        self.x += self.vx * delta
        self.y += self.vy * delta
        self.live -= 1

    def draw(self, screen: "pygame.Surface"):
        screen.blit(self.texture, (self.x, self.y))


class ParticleManager:
    def __init__(self):
        self.particles: list["Particle"] = []

    def update(self, delta):
        for p in self.particles:
            p.update(delta)
            if p.live < 0:
                self.particles.remove(p)
                break

    def draw(self, screen: "pygame.Surface"):
        for p in self.particles:
            p.draw(screen)

    def add_random_pair(self, x, y, font):
        pair = choice(possibilities)
        self.particles.append(Particle(pair[0], font, x, y))
        self.particles.append(Particle(pair[1], font, x, y))
        self.particles.append(Particle(pair[2], font, x, y))
        return pair[2]


particle_manager = ParticleManager()
