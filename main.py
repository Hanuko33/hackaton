#!/bin/python3
import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN
from neutron_uranium_glue import neutron_uranium_manager

from player import Player
from state import state
from explosion import explosion_manager

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

screen: "pygame.Surface" = pygame.display.set_mode(
    (SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("URANEX HALF-LIFE")
clock = pygame.time.Clock()

# font = pygame.font.Font("file_name.ttf", 32)
font = pygame.font.SysFont("Calibri", 32)
background = pygame.image.load("./textures/Background.png")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

running = True


def handle_events():
    global running
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()


player = Player()
while running:
    pygame.display.update()
    clock.tick(FPS)
    state.tick += 1
    screen.blit(background, (0, 0))
    handle_events()
    keys = pygame.key.get_pressed()
    player.key(keys)
    player.update(SCREEN_WIDTH, SCREEN_HEIGHT)
    player.draw(screen)
    neutron_uranium_manager.draw(screen)
    neutron_uranium_manager.update(state, SCREEN_WIDTH, SCREEN_HEIGHT, player)
    explosion_manager.clear_explosions()
    explosion_manager.draw(screen)
    state.draw(screen)
    
pygame.quit()
