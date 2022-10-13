from random import choice as rand_choice

NUMBERS = '0123456789'


def interpret(code):
    def _push_to_stack(*args):
        nonlocal stack
        for a in args:
            stack.append(a)

    def _push_to_output(_):
        nonlocal output
        output += str(_)

    def _up():
        nonlocal x_mod, y_mod
        x_mod, y_mod = 0, -1

    def _down():
        nonlocal x_mod, y_mod
        x_mod, y_mod = 0, 1

    def _left():
        nonlocal x_mod, y_mod
        x_mod, y_mod = -1, 0

    def _right():
        nonlocal x_mod, y_mod
        x_mod, y_mod = 1, 0

    def _progress():
        nonlocal x, y, x_mod, y_mod
        y = (y + y_mod) % len(mtrx)
        x = (x + x_mod) % len(mtrx[y])

    # noinspection PyShadowingNames
    def _current():
        nonlocal x, y
        try:
            v = mtrx[y][x]
        except IndexError as e:
            print(x, y)
            raise e
        return v

    def _add():
        a = stack.pop()
        b = stack.pop()
        _push_to_stack(b + a)

    def _sub():
        a = stack.pop()
        b = stack.pop()
        _push_to_stack(b - a)

    def _product():
        a = stack.pop()
        b = stack.pop()
        _push_to_stack(b * a)

    def _divide():
        a = stack.pop()
        b = stack.pop()
        try:
            _push_to_stack(b // a)
        except ZeroDivisionError:
            _push_to_stack(0)

    def _modulo():
        a = stack.pop()
        b = stack.pop()
        try:
            _push_to_stack(b % a)
        except ZeroDivisionError:
            _push_to_stack(0)

    def _logical_not():
        a = stack.pop()
        _push_to_stack(int(a == 0))

    def _greater_than():
        a = stack.pop()
        b = stack.pop()
        _push_to_stack(int(b > a))

    def _random_direction():
        rand_choice([_left, _right, _up, _down])()

    def _left_or_right():
        a = stack.pop()
        [_left, _right][a == 0]()

    def _up_or_down():
        a = stack.pop()
        [_up, _down][a == 0]()

    def _dup_top_of_stack():
        try:
            _push_to_stack(stack[-1])
        except IndexError:
            _push_to_stack(0)

    def _swap_top_of_stack():
        # nonlocal stack
        a = stack.pop()
        try:
            b = stack.pop()
        except IndexError:
            b = 0
        _push_to_stack(a, b)

    def _discard():
        stack.pop()

    def _output_integer():
        a = stack.pop()
        _push_to_output(a)
        pass

    def _ascii_character():
        # a = chr(int(_next_x(1)))
        a = stack.pop()
        a = chr(a)
        _push_to_output(a)
        pass

    def _skip():
        _progress()

    # noinspection PyShadowingNames
    def _put():
        y = stack.pop()
        x = stack.pop()
        v = stack.pop()
        mtrx[y][x] = chr(v)

    # noinspection PyShadowingNames
    def _get():
        y = stack.pop()
        x = stack.pop()
        v = mtrx[y][x]
        _push_to_stack(ord(v))

    def _toggle_string_mode():
        nonlocal in_string_mode
        in_string_mode = not in_string_mode

    def _toggle_end():
        nonlocal end_of_program
        end_of_program = True

    funcs = {
                '-': _sub,
                '+': _add,
                '*': _product,
                '/': _divide,
                '%': _modulo,
                '!': _logical_not,
                '`': _greater_than,
                '>': _right,
                '<': _left,
                '^': _up,
                'v': _down,
                '?': _random_direction,
                '_': _left_or_right,
                '|': _up_or_down,
                '"': _toggle_string_mode,
                ':': _dup_top_of_stack,
                '\\': _swap_top_of_stack,
                '$': _discard,
                '.': _output_integer,
                ',': _ascii_character,
                '#': _skip,
                'p': _put,
                'g': _get,
                '@': _toggle_end,
                # ' ': pass
    }

    x, y, x_mod, y_mod = 0, 0, 0, 0
    in_string_mode = False
    end_of_program = False

    stack = []
    output = ''

    mtrx = [[c for c in _] for _ in code.splitlines()]
    _right()

    while not end_of_program:
        v = _current()
        if in_string_mode and v != '"':
            _push_to_stack(ord(v))

        elif v in NUMBERS:
            _push_to_stack(int(v))

        else:
            try:
                funcs[v]()
            except KeyError:
                pass

        _progress()


    return output
