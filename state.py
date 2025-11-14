import pygame

class State:
    def __init__(self):
        self.reactor_sanity =  20
        self.score = 0
        self.tick = 0
        self.max_reactor_sanity = 20

    def draw(self, screen):
        bar_width = int(250 * self.reactor_sanity / self.max_reactor_sanity)
        pygame.draw.rect(screen, (255, 0, 0), (50, 500, 250, 20))
        pygame.draw.rect(screen, (0, 255, 0), (50, 500, bar_width, 20))
        font = pygame.font.SysFont("Calibri", 24)
        text = font.render(f"Reactor Sanity: {self.reactor_sanity} / {self.max_reactor_sanity}", True, (0, 0, 0))
        screen.blit(text, (55, 500))

state = State()

