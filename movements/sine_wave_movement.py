import math


class SineWaveMovement:

    def __init__(self, x_step, amplitude, initial_y):
        self.x_step = x_step
        self.amplitude = amplitude
        self.initial_y = initial_y
        self.current_phase = 0

    def get_new_position(self, current_x, current_y):
        self.current_phase += 1
        if self.current_phase >= 360:
            self.current_phase = 0
        new_x = current_x + self.x_step
        new_y = self.initial_y + math.sin(math.radians(self.current_phase)) * self.amplitude
        print("SineWaveMovement.get_new_position-> new_x:", new_x, "new_y:", new_y)
        return new_x, new_y