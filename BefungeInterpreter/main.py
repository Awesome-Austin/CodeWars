from random import choice as rand_choice


def interpret(code):
    def change_directions(a):
        nonlocal dx, dy
        dx, dy = a

    def _progress():
        nonlocal x, y, dx, dy
        y = (y + dy) % len(mtrx)
        x = (x + dx) % len(mtrx[y])

    def put(y, x, v):
        mtrx[y][x] = chr(v)

    left, right, up, down = (-1, 0), (1, 0), (0, -1), (0, 1)
    push = lambda a: stack.append(a)
    push_output = lambda a: output.append(str(a))

    funcs = {
        '-': lambda: push(-stack.pop() + stack.pop()),
        '+': lambda: push(stack.pop() + stack.pop()),
        '*': lambda: push(stack.pop() * stack.pop()),
        '/': lambda: push(0 if stack[-1] == 0 else stack.pop(-2) // stack.pop()),
        '%': lambda: push(0 if stack[-1] == 0 else stack.pop(-2) % stack.pop()),
        '!': lambda: push(int(stack.pop() == 0)),
        '`': lambda: push(int(stack.pop() < stack.pop())),
        '>': lambda: change_directions(right),
        '<': lambda: change_directions(left),
        '^': lambda: change_directions(up),
        'v': lambda: change_directions(down),
        '?': lambda: change_directions(rand_choice([left, right, up, down])),
        '_': lambda: change_directions([left, right][stack.pop() == 0]),
        '|': lambda: change_directions([up, down][stack.pop() == 0]),
        ':': lambda: push(0 if len(stack) == 0 else stack[-1]),
        '\\': lambda: push(0 if len(stack) < 2 else stack.pop(-2)),
        '$': lambda: stack.pop(),
        '.': lambda: push_output(stack.pop()),
        ',': lambda: push_output(chr(stack.pop())),
        '#': lambda: _progress(),
        # '#': lambda: progress(x, y),
        'p': lambda: put(stack.pop(), stack.pop(), stack.pop()),
        'g': lambda: push(ord(mtrx[stack.pop()][stack.pop()])),
        ' ': lambda: None,
    }

    x, y, dx, dy = 0, 0, 0, 0
    change_directions(right)

    string_mode = False
    stack, output = list(), list()

    mtrx = [[c for c in _] for _ in code.splitlines()]
    while True:
        v = mtrx[y][x]

        if v == '"':
            string_mode = not string_mode

        elif string_mode:
            push(ord(v))

        elif v.isdigit():
            push(int(v))

        elif v == '@':
            break

        else:
            funcs[v]()

        _progress()

    return ''.join(output)
