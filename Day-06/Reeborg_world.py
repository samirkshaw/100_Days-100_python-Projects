def turn_right():
    turn_left()
    turn_left()
    turn_left()
while front_is_clear():
    move()
while not_at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif not right_is_clear():
        turn_left()
        if not front_is_clear():
            turn_left()
    if front_is_clear():
        while not right_is_clear() and front_is_clear():
            move()
