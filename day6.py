""" Advent of Code 2016 day 6 """

import numpy as np
from statistics import mode

INPUT_FILE = "6.input"

data = np.loadtxt(INPUT_FILE, dtype=str)
data = np.array([list(row) for row in data])

mode = least = ""

for i in range(len(data[0])):
    array = list(data[:, i])
    sorted_list = sorted(set(array), key=lambda x: array.count(x))
    mode += sorted_list[-1]
    least += sorted_list[0]

print("Part 1:\t", mode)
print("Part 2:\t", least)
