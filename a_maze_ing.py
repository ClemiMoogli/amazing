from parser import read_config_file
from typing import Dict

def create_maze(config: Dict) -> None:
    """The maze creation function.

    Keywords arguments:
    config -- the maze configuration dictionnary
    """
    width = int(config.get("WIDTH"))
    height = int(config.get("HEIGHT"))
    maze_entry = config.get("ENTRY")
    maze_exit = config.get("EXIT")
    output_file = config.get("OUTPUT_FILE")
    bool_perfect = bool(config.get("PERFECT"))
    
    for i in range(height):
        if i == 0 or i == (height - 1):
            line = '*' * width
            print(line)
        else:
            line = 'x' + (" " * (width - 2) + 'x')
            print(line)

    
def is_valid_config(config:Dict) -> bool:
    """Function to check if the configuration file is in a valid format.

    Keywords arguments:
    config -- the maze configuration dictionnary.
    """
    try:
        int(config.get(WIDTH))
        
        return True
    Except Exceptions:
        return False

def main():
    config = read_config_file()
    if not is_valid_config(config):
        print("Invalid configuration, please check")
        return
    if config is None:
        print("Configuration is missing! update the config.txt file.")
        return
    print(config)
    create_maze(config)

main()
