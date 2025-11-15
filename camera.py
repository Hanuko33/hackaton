class Camera:
    def __init__(self):
        self.x = 0
        self.y = 0

    def update(self,
               SCREEN_WIDTH,
               SCREEN_HEIGHT,
               WORLD_WIDTH,
               WORLD_HEIGHT,
               x,
               y
               ):
        self.x = x - SCREEN_WIDTH / 2
        self.x = self.x if self.x > 0 else 0
        self.x = self.x if self.x < WORLD_WIDTH - \
            SCREEN_WIDTH else WORLD_WIDTH - SCREEN_WIDTH
        if SCREEN_WIDTH > WORLD_WIDTH:
            self.x = self.x if self.x > 0 and self.x < WORLD_WIDTH - \
                SCREEN_WIDTH else (WORLD_WIDTH - SCREEN_WIDTH) / 2
        self.y = y - SCREEN_HEIGHT / 2
        self.y = self.y if self.y > 0 else 0
        self.y = self.y if self.y < WORLD_HEIGHT - \
            SCREEN_HEIGHT else WORLD_HEIGHT - SCREEN_HEIGHT
        if SCREEN_HEIGHT > SCREEN_HEIGHT:
            self.y = self.y if self.y > 0 and self.y < WORLD_HEIGHT - \
                SCREEN_HEIGHT else (WORLD_HEIGHT - SCREEN_HEIGHT) / 2
