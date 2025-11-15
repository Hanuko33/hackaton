import pygame
bar_texture = pygame.transform.scale(
    pygame.image.load("./textures/HP_bar.png"),
    (350, 45)
)

empty_bar_texture = pygame.transform.scale(
    pygame.image.load("./textures/Empty_HP_bar.png"),
    (350, 45)
)


class State:
    def __init__(self):
        self.reactor_sanity = 20
        self.score = 0
        self.tick = 0
        self.max_reactor_sanity = 20
        self.lost_tick = -1
        self.hold = 0
        self.rhold = 0

    def draw(self, screen, font, SCREEN_HEIGHT):
        bar_width = int(350 * self.reactor_sanity / self.max_reactor_sanity)

        screen.blit(empty_bar_texture, (55, SCREEN_HEIGHT - 100))
        chopped = pygame.transform.chop(
            bar_texture, (
                bar_width - self.reactor_sanity / self.max_reactor_sanity,
                0,
                350 - bar_width,
                0
            )
        )
        screen.blit(chopped, (55, SCREEN_HEIGHT - 100))
        text = font.render(f"Reactor Sanity: {
            self.reactor_sanity} / {self.max_reactor_sanity}",
            True, (255, 255, 255))
        screen.blit(text, (60, SCREEN_HEIGHT - 150))


state = State()
