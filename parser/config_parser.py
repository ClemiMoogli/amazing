def read_config_file(file_path: str = "config.txt") -> dict:
    """Function to read the configuration file.

    Keywords arguments:
    file_path -- the file path of the file to read (default "config.txt")

    return value:
    A dictionary containing all the config arguments.
    """
    dict_config = {}
    with open(file_path) as f:
        for line in f:
            striped_line = line.strip()
            if (len(striped_line) > 0) and (striped_line[0] != "#"):
                split_line = striped_line.split(sep="=", maxsplit=1)
                dict_config[split_line[0]] = split_line[1]
    return dict_config


def is_valid_config(config: dict) -> bool:
    """Function to check if the configuration file is in a valid format.

    Keywords arguments:
    config -- the maze configuration dictionnary.
    """
    try:
        int(config["ENTRY"][0])
        int(config["ENTRY"][2])
        int(config["EXIT"][0])
        int(config["EXIT"][2])
        int(config["HEIGHT"])
        int(config["WIDTH"])
    except Exception:
        return False

    if (config["ENTRY"] == config["EXIT"]
       or len(config["ENTRY"]) != 3
       or len(config["EXIT"]) != 3
       or config["EXIT"][1] != ","
       or config["ENTRY"][1] != ","
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
