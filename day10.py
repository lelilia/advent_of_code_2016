"""
Advent of Code 2016
--- Day 10: Balance Bots ---
"""



def get_input(filename):
    with open(filename, "r") as f:
        return f.readlines()

class Bot:
    def __init__(self, name):
        self.name = name
        self.items = []
        self.is_full = False
        self.output = None
        self.command_low = None
        self.command_high = None

    def __repr__(self):
        return "bot " + str(self.name) + str(self.items)

    def get_value(self, value):
        self.items.append(value)
        if len(self.items) == 2:
            self.is_full = True

    def handover(self):
        return min(self.items), max(self.items)

    def store_command(self, command):
        self.comand = command


if __name__ == "__main__":
    input = get_input("10.input")
    number_of_bots = 280
    # input = get_input("test10.input")
    # number_of_bots = 3

    bots = {}
    for i in range(number_of_bots):
        bots[i] = Bot(i)

    full_bots = []

    for line in input:
        line = line.strip()
        actor, *rest = line.split(" ")
        print(actor)
        if actor == "value":
            print(rest)
            value, _, _, target, index = rest
            if target == "bot":
                bot = bots[int(index)]
                bot.get_value(int(value))
                if bot.is_full:
                    full_bots.append(bot)
        else:
            index, _, _, _, target_1, index_1, _, _, _, target_2, index_2 = rest

            bot = bots[int(index)]
            bot.command_low = [target_1, int(index_1)]
            bot.command_high = [target_2, int(index_2)]

    while full_bots:
        curr_bot = full_bots.pop()
        if curr_bot.is_full:
            print("do something", curr_bot)
            value_low, value_high = curr_bot.handover()
            target_low, index_low = curr_bot.command_low
            if target_low == "bot":
                bots[index_low].get_value(value_low)
                if bots[index_low].is_full:
                    full_bots.append(bots[index_low])
            else:
                bots[index_low].output = value_low
            target_high, index_high = curr_bot.command_high
            if target_high == "bot":
                bots[index_high].get_value(value_high)
                if bots[index_high].is_full:
                    full_bots.append(bots[index_high])
            else:
                bots[index_high].output = value_high





    for bot in bots.values():
        if bot.items == [61, 17] or bot.items == [17, 61]:
            print("Part 1:", bot.name)
            break

    print("Part 2:", bots[0].output * bots[1].output * bots[2].output)
