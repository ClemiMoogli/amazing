from maze.maze import Maze
from .color import Color


def print_maze(maze: Maze, show_path: bool,
               shortest_path: list[tuple[int, int]],
               game_cell: tuple[int, int], color: str) -> None:
    """Using a grid of int to print a maze in the terminal
    using ASCII character

    keyword arguments:
    - maze -- the maze instance
    - show_path -- a bool arg to specify if we want to see the shortest
    path on the maze
    - shortest_path -- the sortest path list of coordinates
    - game_cell -- the coordinates of the player
    - color -- the maze color
    """
    is_visible_42 = maze.show_42
    h = maze.height
    w = maze.width
    grid = maze.maze
    top = []
    victory = False
    player_x, player_y = game_cell
    for x in range(w):
        cell = grid.get((x, 0))
        top.append("+")
        if cell and not cell.is_wall_open(0):
            top.append("---")
        else:
            top.append("   ")
    top.append("+")
    print(color + "".join(top) + Color.RESET.value)

    for y in range(h):
        mid = []
        for x in range(w):
            is_player = False
            cell = grid.get((x, y))
            if cell and not cell.is_wall_open(3):
                mid.append("|")
            else:
                mid.append(" ")
            if (player_x, player_y) == maze.exit:
                victory = True
            elif (player_x, player_y) != maze.entry and (x, y) == (player_x,
                                                                   player_y):
                is_player = True
                mid.append(" $")
            if (x, y) == maze.entry and (player_x, player_y) == maze.entry:
                mid.append(" $ ")
            elif (x, y) == maze.entry:
                mid.append(" \033[93m# " + color)
            elif (x, y) == maze.exit:
                mid.append(" \033[95m# " + color)
            elif (x, y) in shortest_path and show_path is True:
                mid.append(" \033[0m@ " + color)
            elif is_player:
                mid.append(" ")
            elif is_visible_42 and (x, y) in maze.res_xy:
                mid.append("\033[42;2m   \033[0m" + color)
            else:
                mid.append("   ")
        last = grid.get((w-1, y))
        if last and not last.is_wall_open(1):
            mid.append("|")
        else:
            mid.append(" ")
        print(color + "".join(mid) + Color.RESET.value)

        bot = []
        for x in range(w):
            cell = grid.get((x, y))
            bot.append("+")
            if cell and not cell.is_wall_open(2):
                bot.append("---")
            else:
                bot.append("   ")
        bot.append("+")
        print(color + "".join(bot) + Color.RESET.value)
    if victory is True:
        print("\n=========================")
        print("Congratulation, you won!")
        print("=========================")
