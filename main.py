#!/bin/python3
import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN

from player import Player

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

screen: "pygame.Surface" = pygame.display.set_mode(
    (SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Życie małego uranka")
clock = pygame.time.Clock()

# font = pygame.font.Font("file_name.ttf", 32)
font = pygame.font.SysFont("Calibri", 32)

t = 0
running = True


def handle_events():
    global running
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            print(x, y)

player = Player()
while running:
    pygame.display.update()
    clock.tick(FPS)
    t = t + 1
    screen.fill((0, 0, 0))
    handle_events()
    keys = pygame.key.get_pressed()
    player.key(keys)
    player.update(SCREEN_WIDTH, SCREEN_HEIGHT)
    player.draw(screen)

pygame.quit()
