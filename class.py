#dictio : {(x, y): {"identity": i, "walls_value": hexa}}
#calcul des murs: 1 1 1 1 = 15 (si 1 = 2^n ou n position)
#donc si 1 1 1 1 -> 2^3 + 2^2 + 2^1 + 2^0
#                -> 8 + 4 + 2 + 1
# algo de fusion aleatoire des chemins: une valeur est associé a chaque cellule,
# tout les murs sont fermes de base, ouverture d'un mur aleatoire a chaque fois,
# les cellules qui se touches prennent la meme identity si pas deja le cas
# sinon n'ouvre pas, jusqu'a se que toutes les cellules aient toutes la meme identity
# class cell ? a = 1, b = 1, c = 1, d = 1

from parser import read_config_file
import random


class Cell:
    def __init__(self, x: int, y: int, width:int):
        self.x = x
        self.y = y
        self.identity = y * width + x
        self.wall = [1, 1, 1, 1]

    def is_wall_open(self, wall_nb:int) -> bool:
        """check if the given wall number is already opened, if open return True"""
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


class Maze:
    """
    The maze class.
    """
    def __init__(self, width: int, height: int):
        """
        Initialize the maze as a dictionnary. The key is tuple (x, y) with x as the width
        and y as the height. The value is another dictio with identity (cell number), used 
        for the algo, and the hexa value of the walls.
        """
        self.width = width
        self.height = height
        self.maze = {(x, y): Cell(x, y, width)
                     for y in range(height)
                     for x in range(width)}

    def print_maze(self) -> None:
        """
        Print the maze with the correct format.
        
        :param maze: the maze dict
        :param width: width of the maze
        :param height: height of the maze
        """

        for y in range(self.height):
            for x in range(self.width):
                cell = self.maze.get((x, y))
                if cell:
                    print(cell.show_cell_hexa(), end="")
            print()

    def create_perfect_maze(self) -> None:
        """
        First create a list of possible walls. This list is composed of tuple:
        first a global tuple, in this tuple there is a tuple with x y
        coordinate for the actual wall, a tuple with east (if x+1) cell coord,
        or south cell coord (if y+1), then at the end of the tuple is the direction:
        1 for east, 2 for south.
        This list of walls is shuffled, then the program check if the actual global tuple
        is valid (check if the identity of the two cell are the same or not).
        If the identity are not the same, call open_wall from the Cell class to open the
        first wall with the corresponding direction, then open the inverse wall of the cell
        in this direction
        At the end check all the cells identity to change the value if needed
        """
        walls_list = []
        
        for y in range(self.height):
            for x in range(self.width):
                if x + 1 < self.width:
                    walls_list.append(((x, y), (x + 1, y), 1))
                if y + 1 < self.height:
                    walls_list.append(((x, y), (x, y + 1), 2))
        
        random.shuffle(walls_list)
        
        for (x_a, y_a), (x_b, y_b), direction in walls_list:
            cell_a = self.maze[(x_a, y_a)]
            cell_b = self.maze[(x_b, y_b)]
            if cell_a.identity != cell_b.identity:
                cell_a.open_wall(direction)
                second_wall = (direction + 2) % 4
                cell_b.open_wall(second_wall)
                old_identity = cell_b.identity
                new_identity = cell_a.identity
                for cell in self.maze.values():
                    if cell.identity == old_identity:
                        cell.identity = new_identity


def main():
    maze = Maze(10, 10)
    maze.create_perfect_maze()
    maze.print_maze()

main()
