from enum import Enum


class Shape(Enum):
    CIRCLE = 1
    SQUARE = 2


class Square:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height



