import math

from physics.shapes import *


def is_collision(entity_a, entity_b):
    if entity_a.shape == Shape.CIRCLE and entity_b.shape == Shape.CIRCLE:
        return circle_to_circle(entity_a, entity_b)
    if entity_a.shape == Shape.SQUARE and entity_b.shape == Shape.CIRCLE:
        return square_to_circle(entity_a, entity_b)
    if entity_a.shape == Shape.CIRCLE and entity_b.shape == Shape.SQUARE:
        return square_to_circle(entity_b, entity_a)
    return False


def circle_to_circle(entity_a, entity_b):
    x_dist = (entity_a.x + entity_a.radius) - (entity_b.x + entity_b.radius)
    y_dist = (entity_a.y + entity_a.radius) - (entity_b.y + entity_b.radius)
    dist = math.sqrt(x_dist*x_dist + y_dist*y_dist)
    if dist < entity_a.radius + entity_b.radius:
        return True
    return False


# a ~ square, b ~ circle
def square_to_circle(entity_a, entity_b):
    radius = entity_b.radius
    center = (entity_b.x + radius, entity_b.y + radius)
    for square in entity_a.squares:
        bigger_square = (entity_a.x - square[0] - radius, entity_a.y - square[1] - radius, square[2] + 2 * radius, square[3] + 2 * radius)
        if point_is_in_square(center[0], center[1], bigger_square):
            return True
    return False


def point_is_in_square(point_x, point_y, square):
    if square[0] < point_x < square[0] + square[2] and square[1] < point_y < square[1] + square[3]:
        return True
    return False

