

import pygame

# Standard gamepad buttons:
# (tested with 'esperanza' standard ps2-like-gamepad)
# index | PS-button-name
# 0 - Triangle
# 1 - Circle
# 2 - Cross
# 3 - Square
# 4 - L1
# 5 - R1
# 6 - L2
# 7 - R2
# 8 - Select
# 9 - Start
# 10 - L3
# 11 - R3


def get_action_from_keyboard():
    keys = pygame.key.get_pressed()
    result_actions = []
    # direction
    up_down = 0  # -1 ~ up, 0 ~ neutral, 1 ~ down
    if keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
        up_down = -1
    if keys[pygame.K_DOWN] and not keys[pygame.K_UP]:
        up_down = 1
    left_right = 0  # -1 ~ left, 0 ~ neutral, 1 ~ right
    if keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
        left_right = -1
    if keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
        left_right = 1
    if up_down == -1:  # up
        if left_right == -1:  # left
            result_actions.append("UP_LEFT")
        elif left_right == 0:  # neutral
            result_actions.append("UP")
        elif left_right == 1:  # right
            result_actions.append("UP_RIGHT")
    elif up_down == 0: # neutral
        if left_right == -1:  # left
            result_actions.append("LEFT")
        elif left_right == 1:  # right
            result_actions.append("RIGHT")
    elif up_down == 1:  # down
        if left_right == -1:  # left
            result_actions.append("DOWN_LEFT")
        elif left_right == 0:  # neutral
            result_actions.append("DOWN")
        elif left_right == 1:  # right
            result_actions.append("DOWN_RIGHT")
    # shot
    if keys[pygame.K_SPACE]:
        result_actions.append("SHOT")
    # return
    return result_actions


def get_action_from_gamepad(gamepad):
    result_actions = []
    #gamepad = pygame.joystick.Joystick(0)
    # direction
    # get axes
    up_down = round(gamepad.get_axis(1))
    left_right = round(gamepad.get_axis(0))
    #up_down = gamepad.get_axis(0)
    #left_right = gamepad.get_axis(1)
    if up_down == -1:  # up
        if left_right == -1:  # left
            result_actions.append("UP_LEFT")
        elif left_right == 0:  # neutral
            result_actions.append("UP")
        elif left_right == 1:  # right
            result_actions.append("UP_RIGHT")
    elif up_down == 0:  # neutral
        if left_right == -1:  # left
            result_actions.append("LEFT")
        elif left_right == 1:  # right
            result_actions.append("RIGHT")
    elif up_down == 1:  # down
        if left_right == -1:  # left
            result_actions.append("DOWN_LEFT")
        elif left_right == 0:  # neutral
            result_actions.append("DOWN")
        elif left_right == 1:  # right
            result_actions.append("DOWN_RIGHT")
    # shot
    if gamepad.get_button(2) == 1:
        result_actions.append("SHOT")
    # return
    return result_actions

