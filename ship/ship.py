import physics.shapes


class Ship:

    def __init__(self, x, y, speed, health, image):
        self.x = x
        self.y = y
        self.image = image
        self.speed = speed
        self.collision_damage = 1
        self.health = health
        self.max_health = health
        self.shape = physics.shapes.Shape.SQUARE
        self.state = physics.states.State.LIVING
        self.squares = []
        #self.squares.append((0, 0, 40, 20))
        self.squares.append((5, 5, 35, 10))
        self.squares.append((10, 0, 13, 20))

