"""
Advent of Code 2016
--- Day 12: Leonardo's Monorail ---
"""


class Computer:
    def __init__(self, part=1, filename="12.input"):
        self.registers = dict(zip("abcd", [0, 0, 0, 0]))
        self.read_input(filename)
        if part == 2:
            self.registers["c"] = 1

    def read_input(self, filename):
        with open(filename, "r") as f:
            self.code = f.readlines()

    def run_code(self):
        i = 0
        code_length = len(self.code)
        while i < code_length:
            command, *rest = self.code[i].strip().split(" ")
            if command == "cpy":
                to_copy, register = rest
                if to_copy.isalpha():
                    self.registers[register] = self.registers[to_copy]
                else:
                    self.registers[register] = int(to_copy)

            elif command == "inc":
                register = rest[0]
                self.registers[register] += 1

            elif command == "dec":
                register = rest[0]
                self.registers[register] -= 1

            elif command == "jnz":
                check, jump = rest

                if check == "0":
                    i += 1
                    continue
                if check.isalpha():
                    if self.registers[check] == 0:
                        i += 1
                        continue
                i += int(jump)
                continue
            i += 1


c_1 = Computer()
c_1.run_code()
print("Part 1:", c_1.registers["a"])

c_2 = Computer(2)
c_2.run_code()
print("Part 2:", c_2.registers["a"])
