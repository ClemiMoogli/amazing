
def read_config_file(file_path: str = "config.txt") -> dict:
    """Function to read the configuration file.

    Keywords arguments:
    file_path -- the file path of the file to read (default "config.txt")
    """
    dict_config = {}
    with open(file_path) as f:
        for line in f:
            l = line.strip()
            if (len(l) > 0) and (l[0] != "#"):
                split_line = l.split(sep="=", maxsplit=1)
                dict_config[split_line[0]] = split_line[1]
    return dict_config


