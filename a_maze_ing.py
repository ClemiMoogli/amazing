from parser.config_parser import read_config_file
from maze.maze import Maze
from render.render import print_maze
from solver.bfs import bfs_solver, convert_path_to_NSWE
from typing import Dict
from simple_term_menu import TerminalMenu
import sys


def is_valid_config(config: Dict) -> bool:
    """Function to check if the configuration file is in a valid format.

    Keywords arguments:
    config -- the maze configuration dictionnary.
    """
    return True


def main(config_file: str = "config.txt"):
    options = ["Regenerate maze",
               "Show quickest valid path",
               "Change wall color to blue",
               "Quit"]
    terminal_menu = TerminalMenu(options)
    config = read_config_file(config_file)
    if not is_valid_config(config):
        print("Invalid configuration, please check")
        return
    if config is None:
        print("Configuration is missing! update the config.txt file.")
        return
    perfect = config.get('PERFECT')
    entry_loc = config.get('ENTRY')
    entry_loc = tuple(map(int, entry_loc.split(',')))
    exit_loc = config.get('EXIT')
    exit_loc = tuple(map(int, exit_loc.split(',')))
    output_file = config.get('OUTPUT_FILE')
    maze = Maze(int(config.get('WIDTH')), int(config.get('HEIGHT')),
                entry_loc, exit_loc)
    if perfect == 'True':
        maze.create_perfect_maze()
    else:
        maze.create_imperfect_maze()
    shortest_path = bfs_solver(maze, entry_loc, exit_loc)
    shortest_path_NSWE = convert_path_to_NSWE(shortest_path)
    maze.generate_maze_output(output_file, entry_loc, exit_loc, shortest_path_NSWE)
    print_maze(output_file, entry_loc, exit_loc, False, shortest_path, "purple")
    print("Legend:\n\033[91m#\033[0m: Entry\n\033[32m#\033[0m: Exit\n")
    while 1:
        menu_entry_index = terminal_menu.show()
        if options[menu_entry_index] == "Regenerate maze":
            maze.generate_maze_output(output_file, entry_loc, exit_loc, shortest_path_NSWE)
            shortest_path = bfs_solver(maze, entry_loc, exit_loc)
            print_maze(output_file, entry_loc, exit_loc, False, shortest_path, "white")
            print("Legend:\n\033[91m#\033[0m: Entry\n\033[32m#\033[0m: Exit\n")
        if options[menu_entry_index] == "Show quickest valid path":
            print_maze(output_file, entry_loc, exit_loc, True, shortest_path, "white")
            print("Legend:\n\033[91m#\033[0m: Entry\n\033[32m#\033[0m: Exit\n@: path\n")
        if options[menu_entry_index] == "Change wall color to blue":
            print_maze(output_file, entry_loc, exit_loc, True, shortest_path, "blue")
            print("Legend:\n\033[91m#\033[0m: Entry\n\033[32m#\033[0m: Exit\n@: path\n")
        if options[menu_entry_index] == "Quit":
            sys.exit()


main()
