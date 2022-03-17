from villains.meteor import Meteor
import random

from villains.small_ship_1 import SmallShip1


class Level:

    def __init__(self, slices):
        self.slices = slices

    def get_next_slice(self):
        if len(self.slices) == 0:
            return None
        next_slice = self.slices[0]
        del(self.slices[0])
        return next_slice


class Slice:

    def __init__(self, x_pos, villains):
        self.villains = villains
        self.x = x_pos
        #for v in self.villains:
            #v.x = self.x + v.x

def get_stub_level():
    slices = []
    # add beginning_slices
    for i in range(0, 12):
        slices.append(Slice(i * 100, []))
    # actual level
    for i in range(0, 24):
        x_pos = random.randrange(0, 100)
        y_pos = random.randrange(1, 600)
        x_speed = random.randrange(-6, -1)
        villain_1 = Meteor(x_pos, y_pos, x_speed, 0)
        x_pos = random.randrange(0, 100)
        y_pos = random.randrange(1, 600)
        x_speed = random.randrange(-6, -1)
        villain_2 = Meteor(x_pos, y_pos, x_speed, 0)
        x_pos = random.randrange(0, 100)
        y_pos = random.randrange(1, 600)
        x_speed = random.randrange(-6, -1)
        villain_3 = Meteor(x_pos, y_pos, x_speed, 0)
        # little_ship_1
        x_pos = random.randrange(0, 100)
        amplitude = random.randrange(0, 50)
        initial_y = random.randrange(1, 600)
        x_speed = random.randrange(-6, -1)
        villain_4 = SmallShip1(x_pos, initial_y, x_speed, amplitude)
        #
        villains = [villain_1, villain_2, villain_3, villain_4]
        slices.append(Slice(i * 100 + 1600, villains))
    # add end_slices
    offset = len(slices)
    #for i in range(0, 4):
        #slices.append(Slice(offset * 100 + i * 100, []))
    # add End-Of-Level
    slices.append("EOL")
    return Level(slices)

