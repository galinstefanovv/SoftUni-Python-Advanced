def fill_the_box(height, length, width, *args):
    volume = height * length * width
    cubes_left = 0
    is_finish = False

    for x in args:
        if x == 'Finish':
            is_finish = True
        elif is_finish:
            cubes_left += x
        elif x > volume:
            x -= volume
            cubes_left += x
            volume = 0
        else:
            volume -= x

    if volume > 0:
        return f"There is free space in the box. You could put {volume} more cubes."
    else:
        return f"No more free space! You have {cubes_left} more cubes."


print(fill_the_box(10, 10, 10, 1000, "Finish", 2, 15, 30))
# No more free space! You have 47 more cubes.