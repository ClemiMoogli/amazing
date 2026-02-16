from maze.maze import Maze
from .color import Color
def print_maze(maze: Maze, show_path: bool,
                     shortest_path: list[tuple[int, int]], color:str) -> None:
    """Using a grid of int to print a maze in the terminal
    using ASCII character

    keyword arguments:
    - maze -- the maze instance
    - show_path -- a bool arg to specify if we want to see the shortest path on the maze
    - shortest_path -- the sortest path list of coordinates
    - color -- the maze color
    """

    h = maze.height
    w = maze.width
    grid = maze.maze
    top = [] 
    for x in range(w):
        cell = grid.get((x, 0))
        top.append("+")
        if not cell.is_wall_open(0):
            top.append("---")
        else:
            top.append("   ")
    top.append("+")
    print(color + "".join(top) + Color.RESET.value)

    for y in range(h):
        mid = []
        for x in range(w):
            cell = grid.get((x, y))
            if not cell.is_wall_open(3):
                mid.append("|")
            else:
                mid.append(" ")
            if (x, y) == maze.entry:
                mid.append(" \033[91m# " + color)
            elif (x, y) == maze.exit:
                mid.append(" \033[32m# " + color)
            elif (x, y) in shortest_path and show_path is True:
                mid.append(" @ ")
            else:
                mid.append("   ")
        last = grid.get((w-1, y))
        if not last.is_wall_open(1):
            mid.append("|")
        else:
            mid.append(" ")
        print(color + "".join(mid) + Color.RESET.value)

        bot = []
        for x in range(w):
            cell = grid.get((x, y))
            bot.append("+")
            if not cell.is_wall_open(2):
                bot.append("---")
            else:
                bot.append("   ")
        bot.append("+")
        print(color + "".join(bot) + Color.RESET.value)


