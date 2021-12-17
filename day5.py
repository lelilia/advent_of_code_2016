""" Advent of Code 2016 day 5 """

from hashlib import md5

input = "ffykfhsq"
password = ""
index = 0
for _ in range(8):
    while True:
        res = md5((input + str(index)).encode()).hexdigest()
        index += 1
        if res[:5] == "00000":
            password += res[5]
            break
print("Part 1:\t", password)

password = [None] * 8
index = 0
while password.count(None) != 0:
    while True:
        res = md5((input + str(index)).encode()).hexdigest()
        index += 1
        if res[:5] == "00000":
            pos = int(res[5], 16)
            val = res[6]
            if pos < 8:
                if password[pos] == None:
                    password[pos] = val
                    break
print("Part 2:\t", "".join(password))
