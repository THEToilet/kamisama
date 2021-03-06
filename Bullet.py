import Vector2 as vec2

class Bullet:
    def __init__(self):
        self.pos = vec2.Vec2(0, 0)
        self.vec = 0
        self.size = 2
        self.speed = 6
        self.color = 7
        self.direction = 0

    def update(self, x, y, dx, size, color):
        self.pos.x = x
        self.pos.y = y
        self.vec = dx
        self.size = size
        self.color = color
