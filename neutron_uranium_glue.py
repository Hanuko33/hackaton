from neutron import NeutronManager
from uranium import UraniumManager
import pygame
from random import randint
from explosion import explosion_manager


class NeutronUraniumManager:
    def __init__(self):
        self.neutron_manager = NeutronManager()
        self.uranium_manager = UraniumManager()
        self.lt_neutron = -1000
        self.lt_uranium = -1000

    def draw(self, screen: "pygame.Surface"):
        self.uranium_manager.draw(screen)
        self.neutron_manager.draw(screen)  # NOTE: Draw neutrons ABOVE uranium

    def collisions(self, state):
        for u in self.uranium_manager.uranium:
            for n in self.neutron_manager.neutrons:
                if (n.is_colliding(u)):
                    state.score += 1
                    explosion_manager.add(n.x, n.y)
                    self.uranium_manager.uranium.remove(u)
                    rn = randint(0, 100)

                    if rn < 25:  # 25% for a one to appear
                        self.add_neutron(u.x, u.y)
                    elif rn < 75:  # 50% for one to disappear (get lost)
                        self.neutron_manager.neutrons.remove(n)
                    # 25% for nothing to happen
                    break

    def update(self, state, SCREEN_WIDTH, SCREEN_HEIGHT, player):
        self.collisions(state)
        positions = self.uranium_manager.to_positions()
        positions.append(player.to_position())
        self.neutron_manager.update(
            positions,
            SCREEN_WIDTH,
            SCREEN_HEIGHT,
        )
        self.uranium_manager.update(state)

        uranium_delay = 60 - state.tick / 75
        uranium_delay = uranium_delay if uranium_delay > 10 else 10

        if (self.lt_uranium + uranium_delay < state.tick):
            self.lt_uranium = state.tick
            self.add_uranium(randint(0, SCREEN_WIDTH), randint(
                0, SCREEN_HEIGHT), state.tick)
        if (self.lt_neutron + 160 < state.tick):
            self.lt_neutron = state.tick
            self.add_neutron(randint(0, SCREEN_WIDTH,), randint(
                0, SCREEN_HEIGHT))

    def add_neutron(self, x, y):
        self.neutron_manager.add(x, y)

    def add_uranium(self, x, y, t):
        self.uranium_manager.add(x, y, t)


neutron_uranium_manager = NeutronUraniumManager()
