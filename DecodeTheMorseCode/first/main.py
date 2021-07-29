from DecodeTheMorseCode.definitions import MORSE_CODE


def decode_morse(morse_code):
    return ' '.join([''.join([MORSE_CODE.get(l, '~') for l in w.split(' ')]) for w in morse_code.strip().split('   ')]).upper()


if __name__ == '__main__':
    # s = '.... . -.--   .--- ..- -.. .'
    s = '...---...'
    s = '      ...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.-  '
    dm = decode_morse(s)
    print(dm)
    print(MC)