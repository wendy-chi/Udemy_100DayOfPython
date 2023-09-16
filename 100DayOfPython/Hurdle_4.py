def turn_right():
    turn_left()
    turn_left()
    turn_left()


def leap():
    while wall_on_right() == 0:
        turn_right()
        move()
        turn_right()
        move()


while not at_goal():
    if front_is_clear() == 1 and wall_on_right() == 1:
        move()
    elif front_is_clear() == 0 and wall_on_right() == 1:
        turn_left()
    else:
        leap()