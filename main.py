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
from levels import levels
from particle import particle_manager

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
game_over_image = pygame.image.load("textures/GAME_OVER.png")
background = pygame.transform.scale(pygame.image.load(
    "./textures/Background.png"), (WORLD_WIDTH, WORLD_HEIGHT))

# font = pygame.font.Font("file_name.ttf", 32)
font = pygame.font.SysFont("Calibri", 32)

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
highscore = 0

while running:
    (SCREEN_WIDTH, SCREEN_HEIGHT) = screen.get_size()
    music.update()
    levels.update(font, state, screen, SCREEN_WIDTH,
                  SCREEN_HEIGHT, WORLD_WIDTH, WORLD_HEIGHT)
    camera.update(SCREEN_WIDTH, SCREEN_HEIGHT,
                  WORLD_WIDTH, WORLD_HEIGHT, player)
    pygame.display.update()
    delta = clock.tick(FPS) / 15
    state.tick += 1
    handle_events()
    if state.reactor_sanity <= 0:
        if state.lost_tick == -1:
            for i in range(0, WORLD_WIDTH, 100):
                for j in range(0, WORLD_HEIGHT, 100):
                    explosion_manager.add(i, j)
            state.lost_tick = state.tick
            music.play_lost()
            try:
                f = open("highscore", "r")
                highscore = int(f.read())
                f.close()
            except FileNotFoundError:
                pass

            if highscore < state.score:
                highscore = state.score
                f = open("highscore", "w")
                f.write(str(state.score))
                f.close()
        if state.lost_tick + 10 < state.tick:
            scaled = pygame.transform.scale(
                game_over_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
            screen.blit(scaled, (0, 0))
        txt = font.render(
            f"You got {state.score} score.", True, (255, 255, 255))
        screen.blit(txt, (SCREEN_WIDTH / 2 - txt.get_width() /
                    2, SCREEN_HEIGHT - txt.get_height() * 2 - 10))
        txt = font.render(
            f"Highscore: {highscore}.", True, (255, 255, 255))
        screen.blit(txt, (SCREEN_WIDTH / 2 - txt.get_width() /
                    2, SCREEN_HEIGHT - txt.get_height() - 5))
    else:
        world_surface.blit(background, (0, 0))
        keys = pygame.key.get_pressed()
        player.key(keys, delta)
        player.update(WORLD_WIDTH,
                      WORLD_HEIGHT, delta)
        player.draw(world_surface)
        neutron_uranium_manager.draw(world_surface)
        neutron_uranium_manager.update(
            state, WORLD_WIDTH, WORLD_HEIGHT, player, font, delta)
        particle_manager.update(delta)
        particle_manager.draw(world_surface)
        explosion_manager.clear_explosions()
        explosion_manager.draw(world_surface)
        state.draw(screen, font, SCREEN_HEIGHT)
        screen.blit(world_surface, (-camera.x, -camera.y))
        state.draw(screen, font, SCREEN_HEIGHT)

pygame.mixer.quit()
pygame.quit()
