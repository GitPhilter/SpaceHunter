import pygame

import physics.shapes
import physics.states
from movements.sine_wave_movement import SineWaveMovement


class SmallShip1:

    def __init__(self, x_pos, initial_y, x_step, amplitude):
        # general
        self.x = x_pos
        self.y = initial_y
        self.image = pygame.image.load("images/small_ship_1.png")
        self.dying_sequence_counter = 0
        self.state = physics.states.State.LIVING
        # shape
        self.shape = physics.shapes.Shape.SQUARE
        rect = self.image.get_rect()
        self.squares = []
        self.squares.append((0, 0, rect.width, rect.height))
        # class specific
        self.movement = SineWaveMovement(x_step, amplitude, initial_y)
        self.collision_damage = 1
        self.health = 1

    def get_new_position(self):
        if self.state == physics.states.State.DYING:
            self.set_dying_sequence()
        return self.movement.get_new_position(self.x, self.y)

    def set_dying_sequence(self):
        slice = 16 / 4
        if self.dying_sequence_counter <= slice:
            self.image = pygame.image.load("images/small_ship_1_explosion_1.png")
        elif self.dying_sequence_counter <= 2 * slice:
            self.image = pygame.image.load("images/small_ship_1_explosion_2.png")
        elif self.dying_sequence_counter <= 3 * slice:
            self.image = pygame.image.load("images/small_ship_1_explosion_3.png")
        elif self.dying_sequence_counter <= 4 * slice:
            self.image = pygame.image.load("images/small_ship_1_explosion_4.png")
        else:
            self.state = physics.states.State.DEAD
        self.dying_sequence_counter += 1

