""" Advent of Code 2016 day 7 """

INPUT_FILE = "7.input"


def has_abba(ip):
    for i in range(len(ip) - 3):
        if ip[i] == ip[i + 3] and ip[i + 1] == ip[i + 2] and ip[i] != ip[i + 1]:
            return True
    return False


def is_aba(ip):
    if len(ip) < 3:
        return False
    return ip[0] == ip[2] and ip[0] != ip[1] and ip[1] != "-"


def get_bab(ip):
    return ip[1] + ip[0] + ip[1]


def supports_tls(ip, hypernet):
    if not has_abba(ip):
        return False
    if has_abba(hypernet):
        return False
    return True


def separate_hypernet(ip):
    parts = ip.replace("[", "-").replace("]", "-").split("-")
    return "-".join(parts[::2]), "-".join(parts[1::2])


def supports_ssl(ip, hypernet):
    for i in range(len(ip) - 2):
        if is_aba(ip[i : i + 3]):
            bab = get_bab(ip[i : i + 2])
            if hypernet.find(bab) >= 0:
                return True
    return False


if __name__ == "__main__":

    with open(INPUT_FILE) as f:
        data = f.read().strip().split("\n")

    tls_support_count = 0
    ssl_support_count = 0
    for ip1 in data:
        ip, hypernet = separate_hypernet(ip1)

        if supports_tls(ip, hypernet):
            tls_support_count += 1
        if supports_ssl(ip, hypernet):
            ssl_support_count += 1

    print("Part 1:\t", tls_support_count)

    print("Part 2:\t", ssl_support_count)
