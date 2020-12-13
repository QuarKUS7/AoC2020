def solve():
    i = 1
    while True:
        # LCM 13 19 29 37 997
        t = 264235907 * i
        if not ((t-10) % 41 == 0):
            i += 1
            continue
        if not ((t+8) % 23 == 0):
            i += 1
            continue
        if not ((t+19) % 19 == 0):
            i += 1
            continue
        if not ((t+29) % 29 == 0):
            i += 1
            continue
        if not ((t+31) % 619 == 0):
            i += 1
            continue
        if not ((t+37) % 37 == 0):
            i += 1
            continue
        if not ((t+48) % 17 == 0):
            i += 1
            continue
        return t - 13


if __name__ == '__main__':

    print(solve())
