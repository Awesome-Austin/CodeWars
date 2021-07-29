
import queue

from pprint import pprint
UP, DOWN, LEFT, RIGHT = (0, -1), (0, 1), (-1, 0), (1, 0)


def maze_solver(maze):
    def _start_end_positions(maze):
        start, end = '', ''
        for x, row in enumerate(maze):
            for y, cel in enumerate(row):
                if cel == 'O':
                    start = (x, y)
                elif cel == 'X':
                    end = (x, y)

                if type(start) is tuple and type(end) is tuple:
                    return start, end

    def _move_point(point, direction):
        return point[0] + direction[0], point[1] + direction[1]

    def _valid_point(point):
        # if point[0] < 0:
        #     return False
        # elif point[0] > len(maze):
        #     return False
        # elif point[1] < 0:
        #     return False
        # elif point[1] > len(maze[0]):
        #     return False
        if maze[point[0]][point[1]] == "#":
            return False
        else:
            return True

    maze = [[c for c in l] for l in maze.strip().split('\n')]
    start, end = _start_end_positions(maze)
    paths = queue.Queue()
    paths.put([start])
    while True:
        path = paths.get()
        # print(path)

        for direction in [UP, DOWN, LEFT, RIGHT]:
            point = _move_point(path[-1], direction)
            if not _valid_point(point):
                continue
            if point == end:
                return path[1:]
            paths.put(path + [point])


def print_maze(maze, path=tuple()):
    if len(path) > 0:
        maze = [[c for c in l] for l in maze.strip().split('\n')]
        for point in path:
            maze[point[0]][point[1]] = "+"

        maze = '\n'.join([''.join(l) for l in maze])

    print(maze)


def maze_generator(width, height, border=True):
    maze = [[' ' for c in range(width)] for r in range(height)]
    if border:
        maze[0] = ['#' for c in range(width)]
        maze[-1] = ['#' for c in range(width)]
        for row in maze:
            row[0] = '#'
            row[-1
] = '#'


    return '\n'.join([''.join(r) for r in maze])


if __name__ == '__main__':
    mazes = [
        "#####O#\n"
        "#   # #\n"
        "# # # #\n"
        "# #   #\n"
        "# ### #\n"
        "#   # #\n"
        "#X#####",

        "#####O###\n"
        "#       #\n"
        "# ## ## #\n"
        "# #   # #\n"
        "# # # # #\n"
        "# # # # #\n"
        "# # # ###\n"
        "#       #\n"
        "#X#######",

        "#####O###\n"
        "#  X    #\n"
        "# ## ## #\n"
        "# #   # #\n"
        "# # # # #\n"
        "# # # # #\n"
        "# # # ###\n"
        "#       #\n"
        "#########",
    ]

    # for maze in mazes:
    #     sol = maze_solver(maze)
    #     # print_maze(maze)
    #     # print(sol)
    #     print_maze(maze, sol)
    #     print()

    print(maze_generator(10, 5))

