from parser.config_parser import read_config_file, is_valid_config
from maze.maze import Maze
from render.render import print_maze
from solver.bfs import bfs_solver, convert_path_to_NSWE, find_neighbors
from typing import Dict
from render.color import Color
from simple_term_menu import TerminalMenu
from utils.utils import clear_console
from game.game import play_game
import sys


def main(config_file: str = "config.txt"):
    game_cell = (-10,-10)
    options = ["Regenerate maze",
               "Show/hide quickest valid path",
               "Change wall color",
               "Play the fabulous maze game!",
               "Quit"]
    terminal_menu = TerminalMenu(options)
    color_options = ["Red", "Green", "Blue", "Purple", "Yellow", "White"]
    options_menu = TerminalMenu(color_options)
    color = Color.WHITE.value
    print(color)

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
    print_maze(maze, False, shortest_path, game_cell, color)
    print("Legend:\n\033[93m#\033[0m: Entry\n\033[95m#\033[0m: Exit\n")
    show_path = False
    while 1:
        menu_entry_index = terminal_menu.show()
        if options[menu_entry_index] == "Regenerate maze":
            maze.generate_maze_output(output_file, entry_loc, exit_loc, shortest_path_NSWE)
            shortest_path = bfs_solver(maze, entry_loc, exit_loc)
            clear_console()
            print_maze(maze, show_path, shortest_path, game_cell, color)
            print("Legend:\n\033[93m#\033[0m: Entry\n\033[95m#\033[0m: Exit\n")
        if options[menu_entry_index] == "Show/hide quickest valid path":
            show_path = False if show_path == True else True
            clear_console()
            print_maze(maze, show_path, shortest_path, game_cell, color)
            print("Legend:\n\033[93m#\033[0m: Entry\n\033[95m#\033[0m: Exit\n@: path\n")
        if options[menu_entry_index] == "Change wall color":
            color_entry = options_menu.show()
            if color_options[color_entry] == "Red":
                color = Color.RED.value
            if color_options[color_entry] == "Green":
                color = Color.GREEN.value
            if color_options[color_entry] == "Blue":
                color = Color.BLUE.value
            if color_options[color_entry] == "Purple":
                color = Color.PURPLE.value
            if color_options[color_entry] == "Yellow":
                color = Color.YELLOW.value
            if color_options[color_entry] == "White":
                color = Color.WHITE.value
        if options[menu_entry_index] == "Play the fabulous maze game!":
            game_cell = entry_loc
            play_game(maze, shortest_path, game_cell, color)

        if options[menu_entry_index] == "Quit":
            sys.exit()

main()
