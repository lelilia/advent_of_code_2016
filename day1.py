""" Advent of Code 2016 day 1 """

INPUT_FILE = "1.input"


def read_input(input_file):
    with open(input_file) as f:
        return f.read().strip().split(", ")


def change_orientation(orientation, turn):
    if turn == "R":
        return (orientation + 1) % 4
    else:
        return (orientation - 1) % 4


def walk_n_steps(pos, orientation, distance):
    i = j = 0
    if orientation == 0:
        i = distance
    elif orientation == 2:
        i = -distance
    elif orientation == 1:
        j = distance
    else:
        j = -distance
    return (pos[0] + i, pos[1] + j)


def get_manhattan_distance(pos):
    return abs(pos[0]) + abs(pos[1])


def part_2(input_data):
    orientation = 0
    pos = (0, 0)
    seen = {}
    seen[(0, 0)] = True

    for command in input_data:
        turn = command[0]
        distance = int(command[1:])

        orientation = change_orientation(orientation, turn)
        x, y = pos
        if orientation == 0:
            for x_i in range(x + 1, x + distance + 1):
                if (x_i, y) in seen:
                    return (x_i, y)
                else:
                    seen[(x_i, y)] = True
            x += distance
        elif orientation == 2:
            for x_i in range(x - distance, x):
                if (x_i, y) in seen:
                    return (x_i, y)
                else:
                    seen[(x_i, y)] = True
            x -= distance
        elif orientation == 1:
            for y_i in range(y + 1, y + distance + 1):
                if (x, y_i) in seen:
                    return (x, y_i)
                else:
                    seen[(x, y_i)] = True
            y += distance
        else:
            for y_i in range(y - distance, y):
                if (x, y_i) in seen:
                    return (x, y_i)
                else:
                    seen[(x, y_i)] = True
            y -= distance
        pos = (x, y)


if __name__ == "__main__":
    input_data = read_input(INPUT_FILE)

    orientation = 0
    pos = (0, 0)

    for command in input_data:
        turn = command[0]
        distance = int(command[1:])

        orientation = change_orientation(orientation, turn)
        pos = walk_n_steps(pos, orientation, distance)

    print("Part 1:\t", get_manhattan_distance(pos))

    first_pos = part_2(input_data)
    print("Part 2:\t", get_manhattan_distance(first_pos))
