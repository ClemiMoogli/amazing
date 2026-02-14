from enum import Enum

class Color(Enum):
    WHITE="\033[97m"
    BLUE="\033[34m"
    RED="\033[31m"
    GREEN="\033[32m"
    YELLOW="\033[33m"
    PURPLE="\033[35m"
    RESET="\033[0m"


def check_return_color(color_str:str) -> str:
    """Check if the input color is in the Enum Color, else return a KeyError"""
    try:
        match color_str.upper():
            case "WHITE":
                return Color.WHITE.value
            case "BLUE":
                return Color.BLUE.value
            case "GREEN":
                return Color.GREEN.value
            case "RED":
                return Color.RED.value
            case "YELLOW":
                return Color.YELLOW.value
            case "PURPLE":
                return Color.PURPLE.value
            case "RESET":
                return Color.RESET.value
    except KeyError:
        "Invalid color"

