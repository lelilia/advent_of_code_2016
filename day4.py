""" Advent of Code 2016 day 4 """

INPUT_FILE = "4.input"


def get_checksum(code):
    return "".join(sorted(set(code), key=lambda x: (-code.count(x), x))[:5])


def is_real_room(room):
    code, checksum = "".join(room.split("-")[:-1]), room.split("-")[-1]
    id, checksum = checksum.replace("]", "").split("[")
    id = int(id)
    if get_checksum(code) == checksum:
        return id
    return 0


def decrypt(room):
    code, id = "".join(room.split("-")[:-1]), int(room.split("-")[-1].split("[")[0])
    move = id % 26
    decoded = ""
    for char in code:
        new_ord = ord(char) + move
        if ord("z") - new_ord < 0:
            new_ord = new_ord - ord("z") - 1 + ord("a")
        decoded += chr(new_ord)

    if "north" in decoded:
        return id


id_sum = 0

with open(INPUT_FILE) as f:
    data = f.read().strip().split("\n")

north_pole_id = None

for room in data:
    id = is_real_room(room)
    if id:
        north_pole_id = decrypt(room)
        if north_pole_id:
            break

    id_sum += is_real_room(room)

print(id_sum)
print(north_pole_id)
