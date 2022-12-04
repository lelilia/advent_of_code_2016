"""
Advent of Code 2016
--- Day 9: Explosives in Cyberspace ---
"""


def get_input(filename):
    with open(filename, "r") as f:
        return f.read()


def solve(code):
    solution_1 = solution_2 = 0
    code_length = len(code)
    i = 0
    while i < code_length:
        if code[i] == "(":
            command = ""
            i += 1
            while True:
                if code[i] == ")":
                    i += 1
                    break
                command += code[i]
                i += 1
            length, times = [int(x) for x in command.split("x")]
            solution_1 += length * times
            solution_2 += times * solve(code[i : i + length])[1]
            i += length
        else:
            solution_1 += 1
            solution_2 += 1
            i += 1
    return solution_1, solution_2


input = get_input("9.input")
part_1, part_2 = solve(input)
print("Part 1:", part_1)
print("Part 2:", part_2)


if __name__ == "__main__":
    assert solve("ADVENT")[0] == 6, f"is {part_1('ADVENT')}"
    assert solve("A(1x5)BC")[0] == 7
    assert solve("(3x3)XYZ")[0] == 9
    assert solve("A(2x2)BCD(2x2)EFG")[0] == 11
    assert solve("(6x1)(1x3)A")[0] == 6
    assert solve("X(8x2)(3x3)ABCY")[0] == 18
    assert (
        solve(
            "(6x6)AFPLBX(2x3)ZE(53x13)(4x7)ZGQO(2x4)NJ(1x8)M(24x11)(18x7)HMLOASMJNGZHMCEVEX(11x2)(6x6)TRDPQX"
        )[0]
        == 753
    )
    assert solve("(2x700)AB")[0] == 1400

    assert solve("(3x3)XYZ")[1] == 9
    assert solve("X(8x2)(3x3)ABCY")[1] == 20
    assert solve("(27x12)(20x12)(13x14)(7x10)(1x12)A")[1] == 241920
