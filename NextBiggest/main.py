from itertools import permutations


def next_bigger(n):
    l = [c for c in str(n)]
    if len(set(l)) == 1:
        return -1

    _l = l.copy()
    _l.sort(reverse=True)
    if l == _l:
        return -1

    for i in range(-2, -(len(l)+1), -1):
        l1, l2 = l[:i], l[i:]
        try:
            p = min([''.join(c) for c in permutations(l2) if int(''.join(c)) > int(''.join(l2))])
            return int(''.join(l1) + p)
        except ValueError:
            pass
    else:
        return -1

# def next_bigger(n):
#
#     l = [c for c in str(n)]
#     if len(set(l)) == 1:
#         return -1
#
#     _l = l.copy()
#     _l.sort(reverse=True)
#     if l == _l:
#         return -1
#
#     if len(l) == 2:
#         return int(''.join(_l))
#
#     # [0, 1, 2, 3, ..., -4, -3, -2, -1]
#
#     # [0, 1, 2, 3, ..., -4, -3, -1, -2]
#
#     # [0, 1, 2, 3, ..., -4, -2, -3, -1]
#     # [0, 1, 2, 3, ..., -4, -2, -1, -3]
#
#     for i in range(-2, -(len(l)), -1):
#         l1, l2 = l[:i], next_bigger(int(''.join(l[i:])))
#         if l2 != -1:
#             new_n = int(''.join(l1 + [l2]))
#         else:
#             new_n = -1
#
#         if new_n > n:
#             return new_n
#     else:
#         return -1


if __name__ == "__main__":
    print(next_bigger(2017))
    print(next_bigger(17))

