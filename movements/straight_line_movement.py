

class StraightLineMovement:

    def __init__(self, x_step, y_step):
        self.x_step = x_step
        self.y_step = y_step

    def get_new_position(self, current_x, current_y):
        return current_x + self.x_step, current_y + self.y_step


