from maze.maze import Maze
from simple_term_menu import TerminalMenu
from render.render import print_maze
from maze.solver.bfs import find_neighbors
from utils.utils import clear_console


def play_game(maze: Maze, show_path: bool,
              shortest_path: list[tuple[int, int]],
              game_cell: tuple[int, int], color: str) -> None:
    """Function to play the maze game."""
    clear_console()
    print_maze(maze, False, shortest_path, game_cell, color)
    options_game = ["Up", "Down", "Left", "Right", "Quit"]
    game_menu = TerminalMenu(options_game)

    while 1:
        game_entry = game_menu.show()

        if options_game[game_entry] == "Up":
            x, y = game_cell
            new_loc = (x, y - 1)
            maze.maze.get((x, y))
            neighbors = find_neighbors(maze.maze, (x, y))
            if new_loc in neighbors:
                clear_console()
                print_maze(maze, False, shortest_path, new_loc, color)
                game_cell = new_loc
            else:
                print("\nImpossible move, try again!\n")

        if options_game[game_entry] == "Down":
            x, y = game_cell
            new_loc = (x, y + 1)
            maze.maze.get((x, y))
            neighbors = find_neighbors(maze.maze, (x, y))
            if new_loc in neighbors:
                clear_console()
                print_maze(maze, False, shortest_path, new_loc, color)
                game_cell = new_loc
            else:
                print("\nImpossible move, try again!\n")

        if options_game[game_entry] == "Left":
            x, y = game_cell
            new_loc = (x - 1, y)
            maze.maze.get((x, y))
            neighbors = find_neighbors(maze.maze, (x, y))
            if new_loc in neighbors:
                clear_console()
                print_maze(maze, False, shortest_path, new_loc, color)
                game_cell = new_loc
            else:
                print("\nImpossible move, try again!\n")

        if options_game[game_entry] == "Right":
            x, y = game_cell
            new_loc = (x + 1, y)
            maze.maze.get((x, y))
            neighbors = find_neighbors(maze.maze, (x, y))
            if new_loc in neighbors:
                clear_console()
                print_maze(maze, False, shortest_path, new_loc, color)
                game_cell = new_loc
            else:
                print("\nImpossible move, try again!\n")

        if options_game[game_entry] == "Quit":
            game_cell = (-10, -10)
            clear_console()
            print_maze(maze, show_path, shortest_path, game_cell, color)
            break
