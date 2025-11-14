import pygame
import random

neutron_width = 10
neutron_height = 10

class Neutron:
    #image = pygame.image.load()
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.x = SCREEN_WIDTH / 2
        self.y = SCREEN_HEIGHT - 100
        self.attached_to_player = False
        self.dist_x = 0
        self.dist_y = 0

    def draw(self, screen):
        #screen.blit(Neutron.image, (self.x, self.y))
        pygame.draw.rect(screen, (0, 0, 255), (self.x, self.y, neutron_width, neutron_height))

    def update(self):
        self.x += random.randint(0, 1)
        self.y += random.randint(0, 1)


class NeutronManager:
    #image = pygame.image.load()
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(0, SCREEN_HEIGHT)
        self.neutrons = []

    def draw(self, screen):
        for neutron in self.neutrons:
            neutron.draw(screen)

    def update(self, player):
        for neutron in self.neutrons:
            if neutron.attached_to_player:
                neutron.x = player.x + neutron.dist_x
                neutron.y = player.y + neutron.dist_y
            else:
                neutron.update()