from parser.config_parser import read_config_file
from maze.maze import Maze
from render.color import choose_colors
from render.render import print_maze
from solver.bfs import bfs_solver, convert_path_to_NSWE
from typing import Dict
from simple_term_menu import TerminalMenu


def is_valid_config(config: Dict) -> bool:
    """Function to check if the configuration file is in a valid format.

    Keywords arguments:
    config -- the maze configuration dictionnary.
    """
    if (config["ENTRY"] == config["EXIT"]
        or len(config["ENTRY"]) != 3
        or len(config["EXIT"]) != 3
        or int(config["ENTRY"][0]) < 0 or int(config["ENTRY"][2]) < 0
        or int(config["EXIT"][0]) < 0 or int(config["EXIT"][2]) < 0
        or int(config["HEIGHT"]) < 0 or int(config["WIDTH"]) < 0
        or int(config["ENTRY"][0]) > int(config["WIDTH"]) 
        or int(config["ENTRY"][2]) > int(config["HEIGHT"])
        or int(config["EXIT"][0]) > int(config["WIDTH"]) 
        or int(config["EXIT"][2]) > int(config["HEIGHT"])
        or (config["PERFECT"] != "True" and config["PERFECT"] != "False")):
        return False
    return True


def main(config_file: str = "config.txt"):
    color = choose_colors.WHITE
    options = ["Regenerate maze",
               "Show quickest valid path",
               "Change wall color",
               "Exit"]
    terminal_menu = TerminalMenu(options)

    color_options = ["Red", "Green", "Blue", "Purple", "Yellow", "White"]
    options_menu = TerminalMenu(color_options)

    config = read_config_file(config_file)
    if not is_valid_config(config):
        print("Invalid configuration, please check")
        return
    if config is None:
        print("Configuration is missing! update the config.txt file.")
        return
    print(config)

    perfect = config.get('PERFECT')
    entry_loc = config.get('ENTRY')
    entry_loc = tuple(map(int, entry_loc.split(',')))
    exit_loc = config.get('EXIT')
    exit_loc = tuple(map(int, exit_loc.split(',')))
    maze = Maze(int(config.get('WIDTH')), int(config.get('HEIGHT')),
                entry_loc, exit_loc)
    
    print("entry: ", entry_loc)
    print("exit: ", exit_loc)
    if perfect == 'True':
        print("perfect")
        maze.create_perfect_maze()
    else:
        print("imperfect")
        maze.create_imperfect_maze()
    #maze.print_maze()
    maze.generate_maze_output()
    shortest_path = bfs_solver(maze, entry_loc, exit_loc)
    print_maze("output_maze.txt", entry_loc, exit_loc, False, shortest_path, color)
    print("Legend:\n\033[91m#\033[0m: Entry\n\033[32m#\033[0m: Exit")
    print(f"Output path: {convert_path_to_NSWE(shortest_path)}")

    while 1:
        menu_entry_index = terminal_menu.show()
        if options[menu_entry_index] == "Regenerate maze":
            maze.generate_maze_output()
            shortest_path = bfs_solver(maze, entry_loc, exit_loc)
            print_maze("output_maze.txt", entry_loc, exit_loc, False, shortest_path, color)
            print("Legend:\n\033[91m#\033[0m: Entry\n\033[32m#\033[0m: Exit")
            print(f"Output path: {convert_path_to_NSWE(shortest_path)}")
        if options[menu_entry_index] == "Show quickest valid path":
            print_maze("output_maze.txt", entry_loc, exit_loc, True, shortest_path, color)
            print("Legend:\n\033[91m#\033[0m: Entry\n\033[32m#\033[0m: Exit\n@: path")
            print(f"Output path: {convert_path_to_NSWE(shortest_path)}")
        if options[menu_entry_index] == "Change wall color":
            color_entry = options_menu.show()
            if color_options[color_entry] == "Red":
                color = choose_colors.RED
            if color_options[color_entry] == "Green":
                color = choose_colors.GREEN
            if color_options[color_entry] == "Blue":
                color = choose_colors.BLUE
            if color_options[color_entry] == "Purple":
                color = choose_colors.PURPLE
            if color_options[color_entry] == "Yellow":
                color = choose_colors.YELLOW
            if color_options[color_entry] == "White":
                color = choose_colors.WHITE
        if options[menu_entry_index] == "Exit":
            break

    #print(shortest_path)

main()
