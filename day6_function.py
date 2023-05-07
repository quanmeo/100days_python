def turn_right():
    for _ in range(3):
        turn_left()

turn_right_in_a_row = 0

while not at_goal():

    if right_is_clear():
        if turn_right_in_a_row >= 3:
            move()
            turn_right_in_a_row = 0
            continue

        turn_right()
        turn_right_in_a_row += 1
        move()

    elif front_is_clear():
        move()

    else:
        turn_left()
