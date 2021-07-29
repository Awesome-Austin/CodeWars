from DecodeTheMorseCode import decode_morse


def decode_bits(bits):
    bits = bits.strip('0')
    rate = min([len(b) for b in bits.replace('01', '0|1').replace('10', '1|0').split('|') if len(b) > 0])

    return bits \
        .replace('0' * rate * 7, ' ' * 3) \
        .replace('0' * rate * 3, ' ') \
        .replace('1' * rate * 3, '-') \
        .replace('1' * rate, '.') \
        .replace('0' * rate, '')


if __name__ == '__main__':
    tests = [
        '00110011001100110000001100000011111100110011111100111111000000000000001100111111001111110011111100000011001100111111000000111111001100110000001100',
        '1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011',
        '1',
        '101',
        '10001'
    ]

    for test in tests:
        db = decode_bits(test)
        dm = decode_morse(db)
        print(db, '|', dm)

