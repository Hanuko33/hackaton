import pygame

class State:
    def __init__(self):
        self.reactor_sanity =  20
        self.score = 0
        self.tick = 0
        self.max_reactor_sanity = 20
        self.lost_tick = -1

    def draw(self, screen):
        bar_width = int(250 * self.reactor_sanity / self.max_reactor_sanity)
        pygame.draw.rect(screen, (255, 0, 0), (50, 500, 250, 20))
        pygame.draw.rect(screen, (0, 255, 0), (50, 500, bar_width, 20))
        font = pygame.font.SysFont("Calibri", 24)
        text = font.render(f"Reactor Sanity: {self.reactor_sanity} / {self.max_reactor_sanity}", True, (0, 0, 0))
        screen.blit(text, (55, 500))
        score_font = pygame.font.SysFont("2048", 24)
        points = score_font.render(f"SCORE: {state.score}", True, (255, 255, 255))
        screen.blit(points, (55, 55))

state = State()
