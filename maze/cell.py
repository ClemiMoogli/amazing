
class Cell:
    def __init__(self, x: int, y: int, width:int):
        """The Cell class represente one cell in the maze.

        Keywords arguments:
        -x -- The x position
        -y -- The y position
        -identity --
        -wall -- The wall Open/Close
        """
        self.x = x
        self.y = y
        self.identity = y * width + x
        self.wall = [1, 1, 1, 1]

    def is_wall_open(self, wall_nb:int) -> bool:
        """check if the given wall number is already opened, if open return True
        1 = Close
        0 = Open
        """
        if self.wall[wall_nb] == 1:
            return False
        return True

    def open_wall(self, wall_nb: int) -> None:
        """change the wall value to 0 to open it"""
        self.wall[wall_nb] = 0

    def show_cell_hexa(self) -> str:
        """return the cell as an hexa value"""
        hexa_tab = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B",
                    "C", "D", "E", "F"]
        a = b = c = d = 0
        if self.wall[0] == 1:
            a = 1
        if self.wall[1] == 1:
            b = 2
        if self.wall[2] == 1:
            c = 4
        if self.wall[3] == 1:
            d = 8
        total = a + b + c + d
        return hexa_tab[total]
