import math

import pygame

import physics.states
from controls import player_input
from physics.collision_detection import is_collision
from ship.shot import *



width = 1200
total_height = 700
game_screen_height = 600
menu_height = 100
background_x = 0
delay_time = int(1000 / 60)
shots_per_second = 6
shot_lock_time = 1000 / shots_per_second
shot_locked = False
current_shot_time = 0
background = pygame.image.load("images/background.png")
shot_image = pygame.image.load("images/ship_bullet.png")
menu_border_image = pygame.image.load("images/menu_bar_blue.png")
shots = []
villains = []
slices = []


def start(ship, level, window):
    print("flight.start()")
    run(ship, level, window)


def collision_detection(ship):
    # shots
    for s in shots:
        for v in villains:
            if v.state != physics.states.State.DYING and v.state != physics.states.State.DEAD and is_collision(s, v):
                v.health -= s.collision_damage
                if v.health <= 0:
                    v.state = physics.states.State.DYING
                if s in shots:  # make sure the shot has not been removed by another villain collision before
                    shots.remove(s)
    # ship
    for v in villains:
        if v.state != physics.states.State.DYING and v.state != physics.states.State.DEAD and is_collision(ship, v):
            v.health -= ship.collision_damage
            if v.health <= 0:
                v.state = physics.states.State.DYING
            deal_damage_to_ship(ship, v.collision_damage)

def deal_damage_to_ship(ship, damage):
    ship.health -= damage
    if ship.health <= 0:
        ship.state = physics.states.State.DYING

def update_villains():
    for v in villains:
        # remove dead villains
        if v.state == physics.states.State.DEAD:
            villains.remove(v)
        # remove villains out of sight
        bounds_margin = 600
        if v.x < -bounds_margin or v.x > width + bounds_margin or v.y < -bounds_margin or v.y > game_screen_height + bounds_margin:
            villains.remove(v)
        else:
            new_x, new_y = v.get_new_position()
            v.x = new_x
            v.y = new_y


def update_shots():
    # check if shots have left the screen
    for s in shots:
        s.x += s.speed
        if s.x >= width:
            shots.remove(s)
    # update shot lock
    global shot_locked, current_shot_time
    if shot_locked:
        current_shot_time += delay_time
        if current_shot_time >= shot_lock_time:
            shot_locked = False
            current_shot_time = 0


def upgrade_background():
    background_speed = .2
    global background_x
    background_x -= background_speed
    if background_x <= -3600:
        background_x = 0


def init_level_slices(level):
    for i in range(0, 13):
        load_level_slice(level.get_next_slice())


def load_level_slice(new_slice):
    slices.append(new_slice)
    if new_slice is None or new_slice == "EOL":
        return
    for v in new_slice.villains:
        # print("adding new villain! v.x:", v.x)
        v.x += width
        villains.append(v)


def draw_game(ship, win):
    # fill background
    win.blit(background, (background_x, 0))
    win.blit(background, (background_x + 3600, 0))
    # draw objects
    win.blit(ship.image, (ship.x, ship.y))
    for s in shots:
        win.blit(shot_image, (s.x, s.y))
    vc = 1
    for v in villains:
        # print("villain no", vc, " -> x:", v.x, ", y:", v.y)
        vc += 1
        win.blit(v.image, (v.x, v.y))



def draw_game_stats(ship, win):
    # fill in all black
    pygame.draw.rect(win, (0, 0, 0), pygame.Rect(0, 600, 1200, 100))
    # border
    win.blit(menu_border_image, (0, 600))
    # health
    length_of_max_health = 100
    health = ship.health
    max_health = ship.max_health
    length_of_health = length_of_max_health * (health / max_health)
    health_color = (255, 0, 0)
    health_frame_color = (100, 255, 0)
    pygame.draw.rect(win, health_frame_color, pygame.Rect(19, 619, length_of_max_health + 2, 22))
    pygame.draw.rect(win, health_color, pygame.Rect(20, 620, length_of_health, 20))



def draw_health_string(ship, win):
    font = pygame.font.Font("freesansbold.ttf", 16)
    label = font.render("10 / 10", True, (255, 100, 0))
    labelRect = label.get_rect()
    labelRect.center = (50, 620)
    win.blit(label, labelRect)

def run(ship, level, win):
    global shot_locked
    # gamepad
    if pygame.joystick.get_count() != 0:
        gamepad = pygame.joystick.Joystick(0)
        # init level beginning
        init_level_slices(level)
    else:
        gamepad = None
        pixels_travelled_counter = 0
    running = True
    while running:
        pygame.event.pump()
        pygame.time.delay(delay_time)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # get actions
        #actions = player_input.get_action_from_keyboard()
        if gamepad:
            actions = player_input.get_action_from_gamepad(gamepad)
            # apply movement
            apply_movement(actions, ship)
            # shot
            if "SHOT" in actions and not shot_locked:
                shots.append(Shot(ship.x, ship.y, 8, shot_image))
                shot_locked = True
        # "move" slices
        pixels_travelled_counter += 1
        if pixels_travelled_counter >= 100:
            pixels_travelled_counter = 0
            load_level_slice(level.get_next_slice())
            if slices[0] == "EOL":
                print("main.py: EOL reached. Level has ended.")
                running = False
            else:
                del (slices[0])

        update_shots()
        update_villains()
        collision_detection(ship)
        upgrade_background()
        draw_game(ship, win)
        draw_game_stats(ship, win)
        # update actual display
        pygame.display.update()


def apply_movement(actions, ship):
    diagonal_factor = 1 / math.sqrt(2)
    # left
    if "LEFT" in actions:
        ship.x -= ship.speed
        if ship.x < 0:
            ship.x = 0
    # up_left
    elif "UP_LEFT" in actions:
        ship.y -= ship.speed * diagonal_factor
        if ship.y < 0:
            ship.y = 0
        ship.x -= ship.speed * diagonal_factor
        if ship.x < 0:
            ship.x = 0
    # up
    elif "UP" in actions:
        ship.y -= ship.speed
        if ship.y < 0:
            ship.y = 0
    # up_right
    elif "UP_RIGHT" in actions:
        ship.y -= ship.speed * diagonal_factor
        if ship.y < 0:
            ship.y = 0
        ship.x += ship.speed * diagonal_factor
        rect = ship.image.get_rect()
        if ship.x > width - rect.width:
            ship.x = width - rect.width
    # right
    elif "RIGHT" in actions:
        ship.x += ship.speed
        rect = ship.image.get_rect()
        if ship.x > width - rect.width:
            ship.x = width - rect.width
    # down_right
    elif "DOWN_RIGHT" in actions:
        ship.y += ship.speed * diagonal_factor
        rect = ship.image.get_rect()
        if ship.y > game_screen_height - rect.height:
            ship.y = game_screen_height - rect.height
        ship.x += ship.speed * diagonal_factor
        rect = ship.image.get_rect()
        if ship.x > width - rect.width:
            ship.x = width - rect.width
    # down
    elif "DOWN" in actions:
        ship.y += ship.speed
        rect = ship.image.get_rect()
        if ship.y > game_screen_height - rect.height:
            ship.y = game_screen_height - rect.height
    # down_left
    elif "DOWN_LEFT" in actions:
        ship.y += ship.speed * diagonal_factor
        rect = ship.image.get_rect()
        if ship.y > game_screen_height - rect.height:
            ship.y = game_screen_height - rect.height
        ship.x -= ship.speed * diagonal_factor
        if ship.x < 0:
            ship.x = 0