import pygame 

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0,0)
        self.radius = radius

    def draw(self, screen):
        pass

    def update(self, dt):
        pass

    def check_collision(self, circle):
        # circle shapes have positions which are vectors. Distance_to method returns the difference we're looking for.
        if self.radius + circle.radius < self.position.distance_to(circle.position):
            return False
        else:
            return True
