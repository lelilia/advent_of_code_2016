"""
Advent of Code 2016
--- Day 8: Two-Factor Authentication ---
"""

import numpy as np

WIDTH = 50
HEIGHT = 6


class Screen:
    def __init__(self, filename):
        self.screen = np.zeros((HEIGHT, WIDTH))
        self.input = self.get_input(filename)
        self.parse_input()

    def __repr__(self):
        result = ""
        for row in range(HEIGHT):
            for col in range(WIDTH):
                if self.screen[row, col] == 1:
                    result += "#"
                else:
                    result += " "
            result += "\n"
        return result

    def get_input(self, filename):
        with open(filename, "r") as f:
            return f.readlines()

    def rect(self, a, b):
        self.screen[:b, :a] = 1

    def rotate_row(self, a, b):
        temp = self.screen[a, :]
        new = np.append(temp[-b:], temp[:-b])
        self.screen[a, :] = new

    def rotate_col(self, a, b):
        temp_col = self.screen[:, a]
        new_col = np.append(temp_col[-b:], temp_col[:-b])
        self.screen[:, a] = new_col

    def parse_input(self):
        for line in self.input:

            line = line.strip()
            command, *rest = line.split(" ")

            if command == "rect":
                a, b = rest[0].split("x")
                self.rect(int(a), int(b))

            if command == "rotate":
                a = int(rest[1].split("=")[-1])
                b = int(rest[3])
                if rest[0] == "column":
                    self.rotate_col(a, b)
                else:
                    self.rotate_row(a, b)

    def result_part_1(self):
        print("Part 1:", np.sum(self.screen))

    def result_part_2(self):
        print("Part 2:")
        print(self)


s = Screen("8.input")

s.result_part_1()
s.result_part_2()
