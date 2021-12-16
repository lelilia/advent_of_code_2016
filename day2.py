""" Adent of Code 2016 day 2 """

INPUT_FILE = "2.input"

with open(INPUT_FILE) as f:
    data = f.read().strip().split("\n")

pos = 5
code = ""
for line in data:
    for char in line:
        if char == "U":
            pos = pos - 3 if pos > 3 else pos
        elif char == "D":
            pos = pos + 3 if pos < 7 else pos
        elif char == "L":
            pos = pos - 1 if pos % 3 != 1 else pos
        else:
            pos = pos + 1 if pos % 3 != 0 else pos
    code += str(pos)
print("Part 1:\t", code)

key_pad = [
    [None, None, 1, None, None],
    [None, 2, 3, 4, None],
    [5, 6, 7, 8, 9],
    [None, "A", "B", "C", None],
    [None, None, "D", None, None],
]
x = 2
y = 0
code = ""
for line in data:
    for char in line:
        if char == "U":
            x = x - 1 if x - 1 >= 0 and key_pad[x - 1][y] != None else x
        elif char == "D":
            x = x + 1 if x + 1 < 5 and key_pad[x + 1][y] != None else x
        elif char == "L":
            y = y - 1 if y - 1 >= 0 and key_pad[x][y - 1] != None else y
        else:
            y = y + 1 if y + 1 < 5 and key_pad[x][y + 1] != None else y

    code += str(key_pad[x][y])
print("Part 2:\t", code)
