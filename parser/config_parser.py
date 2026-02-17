def read_config_file(file_path: str = "config.txt") -> dict[str, str]:
    """Function to read the configuration file.

    Keywords arguments:
    file_path -- the file path of the file to read (default "config.txt")

    return value:
    A dictionary containing all the config arguments.
    """
    dict_config = {}
    with open(file_path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" not in line:
                raise ValueError("Invalid config, uncommented line without '='")
            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip()
            if not key:
                raise ValueError("Empty key in the config file.")
            dict_config[key] = value
    return dict_config


def parsing_conversion(dict_config:dict[str, str]) -> dict:
    """A function to cast every config arguments in the configuration dictionary."""
    casted_dict = {}
    for key, value in dict_config.items():
        match key:
            case "WIDTH" | "HEIGHT":
                casted_dict[key] = int(value)
            case "ENTRY" | "EXIT":
                args = [arg.strip() for arg in value.split(",")]
                if len(args) != 2:
                    raise ValueError(f"Invalid configuration: {key} must be in format x,y")
                casted_dict[key] = (int(args[0]),int(args[1]))
            case "OUTPUT_FILE":
                casted_dict[key] = value
            case "PERFECT":
                if value.lower() == "true":
                    casted_dict[key] = True
                elif value.lower() == "false":
                    casted_dict[key] = False
                else:
                    raise ValueError("Invalid PERFECT configuration (must be True or False).")
            case _:
                pass
    return casted_dict


def parsing_verification(casted_dict:dict):
    """A function to check if every config arguments is valid."""
    required = {"WIDTH", "HEIGHT", "ENTRY", "EXIT", "OUTPUT_FILE", "PERFECT"}
    missing = required - casted_dict.keys()
    if missing:
        raise ValueError(f"Invalid configuration: missing {missing} configuration.")
    
    # check width and height
    w, h = casted_dict["WIDTH"], casted_dict["HEIGHT"]
    if w < 0 or h < 0:
        raise ValueError("WIDTH and HEIGHT must be > 0")

    #check entry and exit
    en_x, en_y = casted_dict["ENTRY"]
    ex_x, ex_y = casted_dict["EXIT"]
    if (en_x, en_y) == (ex_x, ex_y):
        raise ValueError("Entry and Exit must be different")
    if not (0 <= en_x < w and 0 <= en_y < h):
        raise ValueError("ENTRY coordinates is invalid")
    if not (0 <= ex_x < w and 0 <= ex_y < h):
        raise ValueError("EXIT coordinates is invalid")
    
    #check OUTPUT_FILE
    if not casted_dict["OUTPUT_FILE"].endswith(".txt"):
        raise ValueError("OUTPUT_FILE must end with .txt")
    return casted_dict

def parse_config(file_path:str) -> dict:
    dict = read_config_file(file_path)
    dict = parsing_conversion(dict)
    dict = parsing_verification(dict)
    return dict
