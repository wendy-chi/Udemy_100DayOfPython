
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def leap():
    # move()
    turn_left()
    move()
    turn_right()

direction = 0
level = 0
while not at_goal():
    if front_is_clear() == 1:

        move()
        # if facing upwords, after moving level+1 and turn right to face front
        if direction == 1:
            level = level + 1
            turn_right()
            direction = 0
        elif direction == 3:
            level = level - 1
            if level == 0:
                turn_left()
                direction = 0
        elif direction == 0:
            # after moving forward, if facing front and level > 0, turn down
            if level > 0:
                turn_right()
                direction = 3

    # front is not clear
    else:
        # front is not clear: if facing up, turn right to face front
        if direction == 1:
            turn_right()
            direction = 0
        # front is not clear: if facing right, true right to face up
        elif direction == 0:
            turn_left()
            direction = 1
        # if facing down && on floor, turn left to face right
        elif direction == 3:
            if level == 0:
                turn_left()
                direction = 0
