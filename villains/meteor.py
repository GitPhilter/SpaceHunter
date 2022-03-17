import pygame

import physics.shapes
import physics.states
from movements.straight_line_movement import *


class Meteor:

    def __init__(self, x_pos, y_pos, x_step, y_step):
        # general
        self.x = x_pos
        self.y = y_pos
        self.image = pygame.image.load("images/meteor.png")
        self.dying_sequence_counter = 0
        self.state = physics.states.State.LIVING
        # shape
        self.shape = physics.shapes.Shape.CIRCLE
        rect = self.image.get_rect()
        self.radius = rect.height / 2
        # class specific
        self.movement = StraightLineMovement(x_step, y_step)
        self.collision_damage = 1
        self.health = 1

    def get_new_position(self):
        if self.state == physics.states.State.DYING:
            self.set_dying_sequence()
        return self.movement.get_new_position(self.x, self.y)

    def set_dying_sequence(self):
        slice = 16 / 4
        if self.dying_sequence_counter <= slice:
            self.image = pygame.image.load("images/standard_explosion_1.png")
        elif self.dying_sequence_counter <= 2 * slice:
            self.image = pygame.image.load("images/standard_explosion_2.png")
        elif self.dying_sequence_counter <= 3 * slice:
            self.image = pygame.image.load("images/standard_explosion_3.png")
        elif self.dying_sequence_counter <= 4 * slice:
            self.image = pygame.image.load("images/standard_explosion_4.png")
        else:
            self.state = physics.states.State.DEAD
        self.dying_sequence_counter += 1




