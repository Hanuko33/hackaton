#!/bin/python3
import pygame
from pygame.locals import (QUIT, MOUSEBUTTONDOWN, MOUSEBUTTONUP,
                           RESIZABLE, VIDEORESIZE, FULLSCREEN, KEYDOWN)
from neutron_uranium_glue import neutron_uranium_manager

from player import Player
from camera import Camera
from state import state
from explosion import explosion_manager
from sfx import sfx
from music import music
from levels import levels
from particle import particle_manager
from intro import intro

pygame.init()
pygame.mixer.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 120
WORLD_WIDTH = 1500
WORLD_HEIGHT = 900

screen: "pygame.Surface" = pygame.display.set_mode(
    (0, 0), RESIZABLE | FULLSCREEN)
world_surface = pygame.Surface((SCREEN_WIDTH + WORLD_WIDTH,
                                SCREEN_HEIGHT + WORLD_HEIGHT))
pygame.display.set_caption("URANEX HALF-LIFE")
clock = pygame.time.Clock()
game_over_image = pygame.image.load("textures/GAME_OVER.png")
background = pygame.transform.scale(pygame.image.load(
    "./textures/Background.png"), (WORLD_WIDTH, WORLD_HEIGHT))
background_scaled = pygame.transform.scale(
    background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# font = pygame.font.Font("file_name.ttf", 32)
font = pygame.font.SysFont("Calibri", 32)

running = True
fullscreen = True
automatic = False
debug = False


def draw_debug():
    i = 0
    for t in [
        f"debug: {debug}",
        f"automatic: {automatic}",
        f"x: {player.x}",
        f"y: {player.y}",
        f"vx: {player.vx}",
        f"vy: {player.vy}",
        f"reached: {player.reached}",
        f"fullscreen: {fullscreen}",
        f"lvl: {levels.level}",
        f"score: {state.score}"
    ]:
        txt = font.render(t, True, (255, 255, 255))
        screen.blit(txt, (0, i * txt.get_height()))
        i += 1


def handle_key(key):
    global automatic
    global debug
    global fullscreen
    global screen
    match key:
        case pygame.K_F1:
            automatic ^= 1
        case pygame.K_F2:
            debug ^= 1
        case pygame.K_F11:
            fullscreen ^= 1
            if fullscreen:
                screen = pygame.display.set_mode(
                    (0, 0), pygame.FULLSCREEN | pygame.RESIZABLE)
            else:
                screen = pygame.display.set_mode(
                    (SCREEN_WIDTH - 50, SCREEN_HEIGHT - 50),
                    pygame.RESIZABLE)


def handle_events():
    global background_scaled
    global running
    global SCREEN_WIDTH
    global SCREEN_HEIGHT
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                state.hold = 1
            if event.button == 3:
                state.rhold = 1
            x, y = pygame.mouse.get_pos()

        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                state.hold = 0
            if event.button == 3:
                state.rhold = 0

        if event.type == KEYDOWN:
            handle_key(event.key)

        if event.type == VIDEORESIZE:
            (SCREEN_WIDTH, SCREEN_HEIGHT) = screen.get_size()
            background_scaled = pygame.transform.scale(
                background, (SCREEN_WIDTH, SCREEN_HEIGHT))


player = Player()

camera = Camera()
sfx.load()
highscore = 0

intro(screen, font)
(SCREEN_WIDTH, SCREEN_HEIGHT) = screen.get_size()
background_scaled = pygame.transform.scale(
    background, (SCREEN_WIDTH, SCREEN_HEIGHT))

while running:
    (SCREEN_WIDTH, SCREEN_HEIGHT) = screen.get_size()
    music.update()
    levels.update(font, state, screen, SCREEN_WIDTH,
                  SCREEN_HEIGHT, WORLD_WIDTH, WORLD_HEIGHT)
    if state.rhold:
        mx, my = pygame.mouse.get_pos()
        camera.update(SCREEN_WIDTH, SCREEN_HEIGHT,
                      WORLD_WIDTH, WORLD_HEIGHT, mx, my)
    else:
        camera.update(SCREEN_WIDTH, SCREEN_HEIGHT,
                      WORLD_WIDTH, WORLD_HEIGHT, player.x, player.y)
    pygame.display.update()
    delta = clock.tick(FPS) / 15
    state.tick += 1
    handle_events()
    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        state.reset()
        player.reset()
        explosion_manager.reset()
        music.stop()
        levels.reset()
        particle_manager.reset()
        neutron_uranium_manager.reset()
        continue
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
        txt = font.render(
            "Press escape to play again.", True, (255, 255, 255))
        screen.blit(txt, (SCREEN_WIDTH / 2 - txt.get_width() /
                    2, 5))
        if state.lost_tick + 300 < state.tick:
            running = False
    else:
        world_surface = pygame.transform.chop(
            world_surface, (WORLD_WIDTH, WORLD_HEIGHT, 1000, 1000))
        world_surface.blit(background, (0, 0))
        screen.blit(background_scaled, (0, 0))
        if automatic:
            player.automatic(
                neutron_uranium_manager.uranium_manager.to_positions(), delta)
        else:
            keys = pygame.key.get_pressed()
            player.key(keys, delta, state)
        if state.hold:
            x, y = pygame.mouse.get_pos()
            player.mouse(x + camera.x, y + camera.y, delta)
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
        if debug:
            draw_debug()

pygame.mixer.quit()
pygame.quit()
