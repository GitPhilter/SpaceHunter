import pygame

from game import flight
from ship.ship import *
from villains.meteor import *
from level.level_slice import *

width = 1200
height = 700


if __name__ == "__main__":
    print("SpaceHunter.main()")
    # init and error check
    (numpass, numfail) = pygame.init()
    print("number of modules booted successfully: ", numpass)
    print("number of modules not booted: ", numfail)
    # set window
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("I am a window")
    (x, y) = win.get_size()
    print("window created, with width", x, "and height", y)
    # variables
    ship_image = pygame.image.load("images/ship.png")
    ship = Ship(10, 150, 2, 10, ship_image)
    level = get_stub_level()
    flight.start(ship, level, win)

    pygame.quit()


