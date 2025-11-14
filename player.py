import pygame

speed = 0.2
player_width = 10
player_height = 10
player_image = pygame.image.load("./textures/Player.png")
player_image = pygame.transform.scale(player_image, (64, 64))


class Player:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.vx = 0
        self.vy = 0
        self.points = 0

    def draw(self, screen):
        screen.blit(player_image, (self.x - 32, self.y - 32))

    def to_position(self):
        return (self.x, self.y)

    def key(self, keys):
        if (keys[pygame.K_LEFT]):
            self.vx -= speed
        elif self.vx < 0:
            self.vx += speed * 2
            if self.vx < 1 and self.vx > -1:
                self.vx = 0
        if self.vx < -10:
            self.vx = -10

        if (keys[pygame.K_DOWN]):
            self.vy += speed
        elif self.vy > 0:
            self.vy -= speed * 2
            if self.vy < 1 and self.vy > -1:
                self.vy = 0
        if self.vy > 10:
            self.vy = 10

        if (keys[pygame.K_UP]):
            self.vy -= speed
        elif self.vy < 0:
            self.vy += speed * 2
            if self.vy < 1 and self.vy > -1:
                self.vy = 0
        if self.vy < -10:
            self.vy = -10

        if (keys[pygame.K_RIGHT]):
            self.vx += speed
        elif self.vx > 0:
            self.vx -= speed * 2
            if self.vx < 1 and self.vx > -1:
                self.vx = 0
        if self.vx > 10:
            self.vx = 10

    def update(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.x += self.vx
        self.y += self.vy
        if self.x >= SCREEN_WIDTH - player_width:
            self.vx = (-self.vx) / 3
            self.x = SCREEN_WIDTH - player_width - 1
        if self.y >= SCREEN_HEIGHT - player_height:
            self.vy = (-self.vy) / 3
            self.y = SCREEN_HEIGHT - player_height - 1
        if self.x < 0:
            self.x = 1
            self.vx = (-self.vx) / 3
        if self.y < 0:
            self.y = 1
            self.vy = (-self.vy) / 3
