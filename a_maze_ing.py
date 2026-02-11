from parser.config_parser import read_config_file
from maze.maze import Maze
from maze.render import print_maze
from solver.bfs import bfs_solver
from typing import Dict


def is_valid_config(config: Dict) -> bool:
    """Function to check if the configuration file is in a valid format.

    Keywords arguments:
    config -- the maze configuration dictionnary.
    """
    return True


def main(config_file:str="config.txt"):
    config = read_config_file(config_file)
    if not is_valid_config(config):
        print("Invalid configuration, please check")
        return
    if config is None:
        print("Configuration is missing! update the config.txt file.")
        return
    print(config)
    maze = Maze(int(config.get('WIDTH')), int(config.get('HEIGHT')))
    perfect = config.get('PERFECT')
    entry_loc = config.get('ENTRY')
    entry_loc = tuple(map(int, entry_loc.split(',')))
    exit_loc = config.get('EXIT')
    exit_loc = tuple(map(int, exit_loc.split(',')))

    print("entry: ", entry_loc)
    print("exit: ", exit_loc)
    if perfect == 'True':
        print("perfect")
        maze.create_perfect_maze()
    else:
        print("imperfect")
        maze.create_imperfect_maze(entry_loc, exit_loc)
    maze.print_maze()
    maze.generate_maze_output()
    print_maze("output_maze.txt", entry_loc, exit_loc)
    print(bfs_solver(maze, entry_loc, exit_loc))

main()
