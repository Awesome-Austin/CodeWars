import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
logging.disable(logging.DEBUG)


def brute_force_find(string):
    inf_string = list()
    # i, j = 0, 10000000000
    # while True:
    #     inf_string += [str(_) for _ in range(i, i + j)]
    #     if i % 10 ** 4 == 0:
    #         print(f'\t{i}')
    #     ans = ''.join(inf_string).find(string)
    #     if ans >= 0:
    #         return ans
    #     i = i + j
    numb = default_farthest_minimum_point(string)

    while True:
        inf_string.append(str(numb))
        ans = ''.join(inf_string).find(string)
        if ans >= 0:
            return ans
        numb -= 1

def in_sequence(num_list, empty_list_returns=False):
    if len(num_list) == 0:
        return empty_list_returns

    if num_list[0] == '0':
        return False

    num_list = [int(n) for n in num_list]
    if min(num_list) == 0:
        return False
    return num_list[1:] == [n + 1 for n in num_list[:-1]]


def default_farthest_minimum_point(num):
    num = int(num)
    i = len(str(num - 1))
    return (i * num) - int('1' * i)


def find_position(string):
    # if string[0] == '0':
    #     return find_position('1' + string) + 1

    ns = number_splits(string)
    for n in ns:
        if in_sequence(n):
            return default_farthest_minimum_point(n[0]) + ''.join(n).find(string)


def number_splits(string):
    if int(string) == 0:
        string = '1' + string
    for mini_string_len in range(1, len(string) + 1):
        for start in range(mini_string_len):
            numbers = [string[i:i+mini_string_len] for i in range(start, len(string), mini_string_len)]
            if start > 0:
                numbers = [string[:start]] + numbers
            yield tuple(numbers)
            yield from expand_number_list(numbers, mini_string_len)
    yield (string, )


def expand_number_list(number_list, length):
    def _valid_number_list(num_list):
        truth_functions = [
            lambda nl: len(nl) > 1,                                     # more than 1 item
            lambda nl: min([int(_) for _ in nl[1:]]) != 0,              # No zero value after index == 0
            lambda nl: sum([int(n[0] == '0') for n in nl[1:]]) == 0,    # No Leading zero after index == 0
            lambda nl: in_sequence(nl[1:-1], True),                     # all numbers in middle are sequential
        ]

        for func in truth_functions:
            if not func(num_list):
                return False
        return True

    def _align_two_elements(first, last):
        fst, lst = [_ for _ in first] + ['' for _ in range(len(last) - 1)], \
                   [_ for _ in last] + ['' for _ in range(len(first) - 1)]

        verify = [_ for _ in fst]
        while True:
            first_last = list(zip(fst, lst))
            if all([any([f == l, f == '', l == '']) for f, l in first_last]):

                f = ''.join([f if f != '' else l for f, l in first_last])
                l = ''.join([l for f, l in first_last])
                if f != l:
                    return f, l

            fst = [fst[-1]] + fst[:-1]
            if fst == verify:
                return first, last

    if not _valid_number_list(number_list):
        return None

    first, last = number_list[0], number_list[-1]

    if len(number_list) == 2:
        if all([int(first[0]) == 0, any([len(last) == 1, int(last[-1]) == 0])]):
            first = number_list[1] + first

        elif length > 1:
            first, last = _align_two_elements(first, last)
        length = max([length, len(first), len(last)]) + int(len(first) == len(last))


    if len(first) < length:
        n_mod = str(
            int(number_list[1][:length - len(first)])
            - int((number_list[1][-1] == '0') or
                  (len(number_list[1]) == 1)))
        first = n_mod + first

    if len(last) < length:
        mod_length = length-len(last)

        n_mod = number_list[-2]
        n_mod = n_mod[-mod_length:]
        n_mod = int(n_mod)
        n_mod = n_mod + 1
        n_mod = n_mod % (10 ** mod_length)
        n_mod = str(n_mod).zfill(mod_length)
        last = last + n_mod

    elif len(last) == length and length == 1:
        last = last + '0'

    yield tuple([first] + list(number_list[1:-1]) + [last])

if __name__ == '__main__':
    # n = ['4', '45', '4']
    # t = _expand_number_list(n, 2)
    # print(n)
    # print(t)

    test_cases = [
        # ("456", 3, "...3456..."),
        # ("454", 79, "...444546..."),
        # ("455", 98, "...545556..."),
        # ("910", 8, "...7891011..."),
        # ("9100", 188, "...9899100..."),
        # ("99100", 187, "...9899100..."),
        # ("00101", 190, "...9899100..."),
        # ("001", 190, "...9899100..."),
        # ("00", 190, "...9899100..."),
        # ("123456789", 0),
        # ("1234567891", 0),
        # ("123456798", 1000000071),
        # ("10", 9),
        # ("53635", 13034),
        # ("040", 1091),
        # ("11", 11),
        # ("99", 168),
        # ("667", 122),
        # ("0404", 15050),
        # ("949225100", 382689688),
        # ("58257860625", 24674951477),
        # ("3999589058124", 6957586376885),
        # ("555899959741198", 1686722738828503),
        # ("01", 10),
        ("091", 170),
        ("0910", 2927),
        ("0991", 2617),
        ("09910", 2617),
        ("09991", 35286),
    ]

    for test_string, *ans in test_cases:
        result = find_position(test_string)
        print(f'{test_string}: {result} {"==" if result == ans[0] else "!="} {ans[0]}')
        # if result != ans[0]:
        #     print(f'\t{brute_force_find(test_string)}\n')
        # break





        # s = find_position(test_string)
        # print('{test_string}{passed}'.format(
        #     test_string=test_string,
        #     passed=f': {s} != {ans[0]}' if s != ans[0] else ''
        # ))
        # print()
