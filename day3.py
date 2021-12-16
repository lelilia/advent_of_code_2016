""" Advent of Code 2016 day 3 """

INPUT_FILE = "3.input"

with open(INPUT_FILE) as f:
    data = f.read().strip().split("\n")

possible_triangles = 0
for triangle in data:
    a, b, c = triangle.split()
    a, b, c = int(a), int(b), int(c)
    if a + b > c and b + c > a and c + a > b:
        possible_triangles += 1
print("Part 1:\t", possible_triangles)

possible_triangles_2 = 0
for i in range(0, len(data), 3):
    a1, b1, c1 = data[i].split()
    a2, b2, c2 = data[i + 1].split()
    a3, b3, c3 = data[i + 2].split()

    a1, a2, a3 = int(a1), int(a2), int(a3)
    b1, b2, b3 = int(b1), int(b2), int(b3)
    c1, c2, c3 = int(c1), int(c2), int(c3)

    if a1 + a2 > a3 and a1 + a3 > a2 and a2 + a3 > a1:
        possible_triangles_2 += 1

    if b1 + b2 > b3 and b1 + b3 > b2 and b2 + b3 > b1:
        possible_triangles_2 += 1
    if c1 + c2 > c3 and c1 + c3 > c2 and c2 + c3 > c1:
        possible_triangles_2 += 1
print("Part 2:\t", possible_triangles_2)
