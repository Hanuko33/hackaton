#!/bin/python3
import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN, RESIZABLE
from neutron_uranium_glue import neutron_uranium_manager

from player import Player
from camera import Camera
from state import state
from explosion import explosion_manager
from sfx import sfx
from music import music

pygame.init()
pygame.mixer.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
WORLD_WIDTH = 1500
WORLD_HEIGHT = 900

screen: "pygame.Surface" = pygame.display.set_mode(
    (SCREEN_WIDTH, SCREEN_HEIGHT), RESIZABLE)
world_surface = pygame.Surface((SCREEN_WIDTH + WORLD_WIDTH,
                                SCREEN_HEIGHT + WORLD_HEIGHT))
pygame.display.set_caption("URANEX HALF-LIFE")
clock = pygame.time.Clock()

# font = pygame.font.Font("file_name.ttf", 32)
font = pygame.font.SysFont("Calibri", 32)
background = pygame.image.load("./textures/Background.png")
background = pygame.transform.scale(
    background, (WORLD_WIDTH, WORLD_HEIGHT))

running = True


def handle_events():
    global running
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()


player = Player()
camera = Camera()
sfx.load()
while running:
    music.update()
    (SCREEN_WIDTH, SCREEN_HEIGHT) = screen.get_size()
    camera.update(SCREEN_WIDTH, SCREEN_HEIGHT,
                  WORLD_WIDTH, WORLD_HEIGHT, player)
    pygame.display.update()
    clock.tick(FPS)
    state.tick += 1
    world_surface.blit(background, (0, 0))
    handle_events()
    keys = pygame.key.get_pressed()
    player.key(keys)
    player.update(WORLD_WIDTH,
                  WORLD_HEIGHT)
    player.draw(world_surface)
    neutron_uranium_manager.draw(world_surface)
    neutron_uranium_manager.update(
        state, WORLD_WIDTH, WORLD_HEIGHT, player)
    explosion_manager.clear_explosions()
    explosion_manager.draw(world_surface)
    screen.blit(world_surface, (-camera.x, -camera.y))
    state.draw(screen, font, SCREEN_HEIGHT)
pygame.mixer.quit()
pygame.quit()
