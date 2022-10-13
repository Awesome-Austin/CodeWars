from pprint import pprint

LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,? *'


def _encrypt_one101(c, n):
    for i in range(n):
        ind = LETTERS.find(c)
        c = LETTERS[((ind + 1) * 2 - 1) % len(LETTERS)]
    return c


def _encrypt_one102(c, n):
    for i in range(n):
        ind = LETTERS.find(c)
        ind += 1
        ind *= 2
        ind -= 1
        ind = ind % len(LETTERS)
        c = LETTERS[ind]
    return c


def encode(s):
    return "".join(_encrypt_one102(c, i+1) if c in LETTERS else c for i, c in enumerate(s))


def decode(s):
    def _encode():
        v = encode(s)
    l = [_encode() for i in range(65)]

    for x in range(65):
        s = encode(s)
    return s


# def decode(s):
#     def _decrypt_one102(c, n):
#         for i in range(n):
#             ind = LETTERS.find(c) + 1
#             c = LETTERS[((ind + (len(LETTERS) * (ind % 2)))//2) - 1]
#         return c
#     return "".join(_decrypt_one102(c, i+1) if c in LETTERS else c for i, c in enumerate(s))


if __name__ == "__main__":
    a = "Hello World!"
    b, i = encode(a), 0
    decode(b)
    # while a != b:
    #     b = encode(b)
    #     i += 1
    #
    # print(i)
