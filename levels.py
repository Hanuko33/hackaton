from neutron_uranium_glue import neutron_uranium_manager
import pygame
from random import randint
from sfx import sfx


class Levels:
    def __init__(self):
        self.level = 1
        self.tick_changed = -1

    def reset(self):
        self.__init__()

    def next_level(self, state, WORLD_WIDTH, WORLD_HEIGHT):
        for _ in range(self.level * 10):
            neutron_uranium_manager.add_uranium(
                randint(0, WORLD_WIDTH), randint(0, WORLD_HEIGHT), state.tick)
        self.level += 1

    def draw_level_text(self, screen, font, SCREEN_WIDTH, SCREEN_HEIGHT):
        txt = font.render(
            "!HALF-LIFED URANEX STRIKE INCOMING!", True, (255, 0, 0))
        x = SCREEN_WIDTH // 2 - txt.get_width() // 2
        y = SCREEN_HEIGHT // 2 - 50
        x += randint(-5, 5)
        y += randint(-5, 5)
        screen.blit(txt, (x, y))

    def update(self,
               font,
               state,
               screen,
               SCREEN_WIDTH,
               SCREEN_HEIGHT,
               WORLD_WIDTH,
               WORLD_HEIGHT):
        if (len(neutron_uranium_manager.uranium_manager.uranium) == 0 and
                self.tick_changed == -1):
            self.tick_changed = state.tick + 1
        if state.tick - self.tick_changed == 2:
            sfx.play_alarm(min(self.level - 1, 2))
        if self.tick_changed > 0:
            if (state.tick // 20) % 2:
                screen.fill((255, 0, 0, 125),
                            special_flags=pygame.BLEND_RGBA_MIN)
            self.draw_level_text(screen, font, SCREEN_WIDTH, SCREEN_HEIGHT)
        if self.tick_changed + 300 < state.tick and self.tick_changed != -1:
            self.next_level(state, WORLD_WIDTH, WORLD_HEIGHT)
            self.tick_changed = -1


levels = Levels()
