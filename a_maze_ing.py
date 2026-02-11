from parser.config_parser import read_config_file
from maze.maze import Maze
from maze.render import print_maze
from typing import Dict


def is_valid_config(config: Dict) -> bool:
    """Function to check if the configuration file is in a valid format.

    Keywords arguments:
    config -- the maze configuration dictionnary.
    """
    return True


def main(config_file: str = "config.txt"):
    config = read_config_file(config_file)
    if not is_valid_config(config):
        print("Invalid configuration, please check")
        return
    if config is None:
        print("Configuration is missing! update the config.txt file.")
        return
    print(config)
    perfect = config.get('PERFECT')
    entry = config.get('ENTRY')
    entry = tuple(map(int, entry.split(',')))
    exit = config.get('EXIT')
    exit = tuple(map(int, exit.split(',')))
    maze = Maze(int(config.get('WIDTH')), int(config.get('HEIGHT')),
                entry, exit)

    if perfect is True:
        maze.create_perfect_maze()
    else:
        maze.create_imperfect_maze()
    maze.print_maze()
    maze.generate_maze_output()
    print_maze()


main()
