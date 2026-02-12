NORTH = 1  # bit 0
EAST = 2  # bit 1
SOUTH = 4  # bit 2
WEST = 8  # bit 3


def load_hex_grid(path: str) -> list[list[int]]:
    """Function to take an hex matrix and convert it to an array of array
    of int, representing the maze"""
    grid: list[list[int]] = []
    with open(path, "r") as f:
        for raw in f:
            line = raw.strip()
            if not line:
                break
            grid.append([int(ch, 16) for ch in line])
    return grid


def print_maze_ascii(grid: list[list[int]], entry_loc: tuple[int, int],
                     exit_loc: tuple[int, int], show_path: bool,
                     shortest_path: list[tuple[int, int]]) -> None:
    """Using a grid of int to print a maze in the terminal
    using ASCII character"""
    h = len(grid)
    w = len(grid[0]) if h else 0
    if h == 0 or w == 0:
        print("(empty maze)")
        return

    top = []
    for x in range(w):
        cell = grid[0][x]
        top.append("+")
        top.append("---" if (cell & NORTH) else "   ")
    top.append("+")
    print("".join(top))

    for y in range(h):
        mid = []
        for x in range(w):
            cell = grid[y][x]
            mid.append("|" if (cell & WEST) else " ")
            if (x, y) == entry_loc:
                mid.append(" # ")
            elif (x, y) == exit_loc:
                mid.append(" # ")
            elif (x, y) in shortest_path and show_path is True:
                mid.append(" @ ")
            else:
                mid.append("   ")
        last = grid[y][w - 1]
        mid.append("|" if (last & EAST) else " ")
        print("".join(mid))

        bot = []
        for x in range(w):
            cell = grid[y][x]
            bot.append("+")
            bot.append("---" if (cell & SOUTH) else "   ")
        bot.append("+")
        print("".join(bot))


def print_maze(output_file: str, entry_loc: tuple[int, int],
               exit_loc: tuple[int, int], show_path: bool,
               shortest_path: list[tuple[int, int]]) -> None:
    """The full function that take an hex matrix and print
    the maze in the stdout."""
    grid = load_hex_grid(output_file)
    print_maze_ascii(grid, entry_loc, exit_loc, show_path, shortest_path)
