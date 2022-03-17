import physics.shapes


class Shot:

    def __init__(self, x, y, speed, image):
        self.x = x
        self.y = y
        self.image = image
        rect = self.image.get_rect()
        self.radius = rect.height / 2
        self.shape = physics.shapes.Shape.CIRCLE
        self.speed = speed
        self.collision_damage = 1

