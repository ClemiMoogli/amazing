from parser.config_parser import read_config_file
from maze.maze import Maze
from typing import Dict


def is_valid_config(config:Dict) -> bool:
    """Function to check if the configuration file is in a valid format.

    Keywords arguments:
    config -- the maze configuration dictionnary.
    """
    return True

def main():
    config = read_config_file()
    if not is_valid_config(config):
        print("Invalid configuration, please check")
        return
    if config is None:
        print("Configuration is missing! update the config.txt file.")
        return
    print(config)
    maze = Maze(int(config.get('WIDTH')), int(config.get('HEIGHT')))
    maze.create_perfect_maze()
    maze.print_maze()
    maze.generate_maze_output()

main()
