def turn_right():
    turn_left()
    turn_left()
    turn_left()


def leap():
    # move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while not at_goal():
    if front_is_clear() == 1:
        move()
    else:
        leap()
