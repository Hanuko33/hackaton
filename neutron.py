import pygame

neutron_image = pygame.image.load("./textures/Neutron.png")
neutron_image = pygame.transform.scale(neutron_image, (16, 16))


class Neutron:
    def __init__(self, x, y):
        self.x = x
        self.vx = 0
        self.y = y
        self.vy = 0

    def draw(self, screen):
        screen.blit(neutron_image, (self.x - 8, self.y - 8))

    def update(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.x += self.vx
        self.y += self.vy
        image_width = 16
        if self.x >= SCREEN_WIDTH - image_width:
            self.vx = (-self.vx) / image_width
            self.x = SCREEN_WIDTH - image_width - 1
        if self.y >= SCREEN_HEIGHT - image_width:
            self.vy = (-self.vy) / image_width
            self.y = SCREEN_HEIGHT - image_width - 1
        if self.x < 0:
            self.x = 1
            self.vx = (-self.vx) / image_width
        if self.y < 0:
            self.y = 1
            self.vy = (-self.vy) / image_width

    def distance_to_squared(self, x, y):
        return (self.x - x) ** 2 + (self.y - y) ** 2

    def is_colliding(self, u):
        return self.distance_to_squared(u.x, u.y) < 40 ** 2

    def find_closest_position(self, positions):
        if not len(positions):
            return None
        closest = positions[0]
        closest_dist = self.distance_to_squared(
            positions[0][0], positions[0][1])
        for p in positions:
            dist = self.distance_to_squared(p[0], p[1])
            if closest_dist > dist:
                closest = p
                closest_dist = dist
        return closest

    def update_velocity(self, positions):
        closest = self.find_closest_position(positions)
        if not closest:
            return
        (other_x, other_y) = closest
        dx = other_x - self.x
        dy = other_y - self.y

        distance = (dx ** 2 + dy ** 2) ** 0.5

        if distance > 0 and distance < 100:
            # Normalize the vector
            dx /= distance
            dy /= distance

            self.vx += dx / 2
            self.vy += dy / 2


class NeutronManager:
    def __init__(self):
        self.neutrons: list["Neutron"] = []

    def add(self, x, y):
        self.neutrons.append(Neutron(x, y))

    def draw(self, screen):
        for n in self.neutrons:
            n.draw(screen)

    def update(self, uranium_positions, SCREEN_WIDTH, SCREEN_HEIGHT):
        for n in self.neutrons:
            n.update_velocity(uranium_positions)
            n.update(SCREEN_WIDTH, SCREEN_HEIGHT)
