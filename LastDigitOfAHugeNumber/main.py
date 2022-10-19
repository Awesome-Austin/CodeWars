CYCLES = {
    0: 1,
    1: 1,
    2: 4,
    3: 4,
    4: 2,
    5: 1,
    6: 1,
    7: 4,
    8: 4,
    9: 2}


def last_digit(lst):
    def _power(lst):
        if len(lst) == 1:
            return lst[0]
        elif sum(lst) == 0:
            if len(lst) % 2 == 0:
                return 1
            else:
                return 0

        base, power_components = lst[0], lst[1:]
        power = _power(power_components)
        if power > 2:
            power = power - 2
            power = power % 4
            power = power + 2
        expo = pow(base, power)
        return expo

    n = _power(lst)
    return n % 10


def _last_digit(lst):
    def _power(lst):
        if len(lst) == 0:
            return 1
        elif len(lst) == 1:
            return lst[0]
        elif sum(lst) == 0:
            if len(lst) % 2 == 0:
                return 1
            else:
                return 0

        a, p = lst[0], lst[1:]

        c = CYCLES[a % 10]
        # if c == 1:
        #     return a
        p = _power(p)
        # p = p % a
        if c == 1:
            return a % 10
            # return a ** p
        #     return (a % 10) ** p
        if p != 0:
            p = p - 1
            p = p % c
            p = p + 1
        return a ** p

    ans = _power(lst)
    return ans % 10


if __name__ == "__main__":
    test, ans = ([4, 3, 6], 4)
    # test, ans = ([4, 216], 4)
    a = last_digit(test)
    print(a)
