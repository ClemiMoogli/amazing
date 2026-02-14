# dictio : {(x, y): {"identity": i, "walls_value": hexa}}
# calcul des murs: 1 1 1 1 = 15 (si 1 = 2^n ou n position)
# donc si 1 1 1 1 -> 2^3 + 2^2 + 2^1 + 2^0
#                -> 8 + 4 + 2 + 1
# algo de fusion aleatoire des chemins: une valeur est associé a
# chaque cellule,
# tout les murs sont fermes de base, ouverture d'un mur aleatoire a
# chaque fois,
# les cellules qui se touches prennent la meme identity si pas deja le cas
# sinon n'ouvre pas, jusqu'a se que toutes les cellules aient toutes la
# meme identity
# class cell ? a = 1, b = 1, c = 1, d = 1

from .cell import Cell
import random
from math import floor


class Maze:
    """
    The maze class.
    """
    def __init__(self, width: int, height: int, entry: tuple, exit: tuple):
        """
        Initialize the maze as a dictionnary. The key is tuple (x, y) with x
        as the width
        and y as the height. The value is another dictio with identity
        (cell number), used
        for the algo, and the hexa value of the walls.
        """
        try:
            self.show_42 = True
            if width <= 0:
                raise ValueError("width must be > 0")
            self.width = width
            if height <= 0:
                raise ValueError("height must be > 0")
            self.height = height
            if self.width > 7 and self.height > 6:
                self.ft_x = floor((self.width - 6) / 2)
                self.ft_y = floor((self.height - 5) / 2)
                self.res_xy = [(self.ft_x, self.ft_y),
                               (self.ft_x + 4, self.ft_y),
                               (self.ft_x + 5, self.ft_y),
                               (self.ft_x, self.ft_y + 1),
                               (self.ft_x + 5, self.ft_y + 1),
                               (self.ft_x, self.ft_y + 2),
                               (self.ft_x + 1, self.ft_y + 2),
                               (self.ft_x + 2, self.ft_y + 2),
                               (self.ft_x + 4, self.ft_y + 2),
                               (self.ft_x + 5, self.ft_y + 2),
                               (self.ft_x, self.ft_y),
                               (self.ft_x + 2, self.ft_y + 3),
                               (self.ft_x + 4, self.ft_y + 3),
                               (self.ft_x + 2, self.ft_y + 4),
                               (self.ft_x + 4, self.ft_y + 4),
                               (self.ft_x + 5, self.ft_y + 4)]
                if entry in self.res_xy or exit in self.res_xy:
                    self.ft_x = 0
                    self.fr_y = 0
                    self.res_xy = [(self.ft_x, self.ft_y - 2),
                                   (self.ft_x + 4, self.ft_y - 2),
                                   (self.ft_x + 5, self.ft_y - 2),
                                   (self.ft_x, self.ft_y - 1),
                                   (self.ft_x + 5, self.ft_y - 1),
                                   (self.ft_x, self.ft_y),
                                   (self.ft_x + 1, self.ft_y),
                                   (self.ft_x + 2, self.ft_y),
                                   (self.ft_x + 4, self.ft_y),
                                   (self.ft_x + 5, self.ft_y),
                                   (self.ft_x + 2, self.ft_y + 1),
                                   (self.ft_x + 4, self.ft_y + 1),
                                   (self.ft_x + 2, self.ft_y + 2),
                                   (self.ft_x + 4, self.ft_y + 2),
                                   (self.ft_x + 5, self.ft_y + 2)]
                if entry in self.res_xy or exit in self.res_xy:
                    self.ft_x = width - 7
                    self.ft_y = height - 3
                    self.res_xy = [(self.ft_x, self.ft_y - 2),
                                   (self.ft_x + 4, self.ft_y - 2),
                                   (self.ft_x + 5, self.ft_y - 2),
                                   (self.ft_x, self.ft_y - 1),
                                   (self.ft_x + 5, self.ft_y - 1),
                                   (self.ft_x, self.ft_y),
                                   (self.ft_x + 1, self.ft_y),
                                   (self.ft_x + 2, self.ft_y),
                                   (self.ft_x + 4, self.ft_y),
                                   (self.ft_x + 5, self.ft_y),
                                   (self.ft_x + 2, self.ft_y + 1),
                                   (self.ft_x + 4, self.ft_y + 1),
                                   (self.ft_x + 2, self.ft_y + 2),
                                   (self.ft_x + 4, self.ft_y + 2),
                                   (self.ft_x + 5, self.ft_y + 2)]
                if entry in self.res_xy or exit in self.res_xy:
                    self.ft_x = width - 4
                    self.ft_y = height + 2
                    self.res_xy = [(self.ft_x, self.ft_y - 2),
                                   (self.ft_x + 4, self.ft_y - 2),
                                   (self.ft_x + 5, self.ft_y - 2),
                                   (self.ft_x, self.ft_y - 1),
                                   (self.ft_x + 5, self.ft_y - 1),
                                   (self.ft_x, self.ft_y),
                                   (self.ft_x + 1, self.ft_y),
                                   (self.ft_x + 2, self.ft_y),
                                   (self.ft_x + 4, self.ft_y),
                                   (self.ft_x + 5, self.ft_y),
                                   (self.ft_x + 2, self.ft_y + 1),
                                   (self.ft_x + 4, self.ft_y + 1),
                                   (self.ft_x + 2, self.ft_y + 2),
                                   (self.ft_x + 4, self.ft_y + 2),
                                   (self.ft_x + 5, self.ft_y + 2)]
                if entry in self.res_xy or exit in self.res_xy:
                    self.ft_x = width - 1
                    self.ft_y = height + 2
                    self.res_xy = [(self.ft_x, self.ft_y - 2),
                                   (self.ft_x + 4, self.ft_y - 2),
                                   (self.ft_x + 5, self.ft_y - 2),
                                   (self.ft_x, self.ft_y - 1),
                                   (self.ft_x + 5, self.ft_y - 1),
                                   (self.ft_x, self.ft_y),
                                   (self.ft_x + 1, self.ft_y),
                                   (self.ft_x + 2, self.ft_y),
                                   (self.ft_x + 4, self.ft_y),
                                   (self.ft_x + 5, self.ft_y),
                                   (self.ft_x + 2, self.ft_y + 1),
                                   (self.ft_x + 4, self.ft_y + 1),
                                   (self.ft_x + 2, self.ft_y + 2),
                                   (self.ft_x + 4, self.ft_y + 2),
                                   (self.ft_x + 5, self.ft_y + 2)]
                if entry in self.res_xy or exit in self.res_xy:
                    self.show_42 = False
                    print("Error: cannot print 42 with the current"
                          "entry and exit point")
            else:
                self.show_42 = False
            if entry == exit:
                raise ValueError("entry and exit must be different")
            for nb in entry:
                if isinstance(nb, int) is False:
                    raise ValueError("entry coordinate must be numbers")
                if nb < 0:
                    raise ValueError("entry coordinate must be equal or"
                                     " superior to 0")
            if len(entry) > 2 or len(entry) < 2:
                raise ValueError("entry coordinate must be of format x,y")
            if entry[0] > self.width or entry[1] > self.height:
                raise ValueError("Entry point must be in the maze")
            self.entry = entry
            for nb in exit:
                if isinstance(nb, int) is False:
                    raise ValueError("exit coordinate must be numbers")
                if nb < 0:
                    raise ValueError("exit coordinate must be equal"
                                     "or superior to 0")
            if len(exit) > 2 or len(exit) < 2:
                raise ValueError("exit coordinate must be of format x,y")
            if exit[0] > self.width or exit[1] > self.height:
                raise ValueError("Exit point must be in the maze")
            self.exit = exit
        except ValueError as e:
            print(f"Error creating maze class: {e}")
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

    def generate_maze_output(self, output_file="output_maze.txt") -> None:
        """Generate the Hex format of the maze and save it in the
        output file."""
        with open(output_file, "w") as f:
            for y in range(self.height):
                for x in range(self.width):
                    cell = self.maze.get((x, y))
                    if cell:

                        f.write(f"{cell.show_cell_hexa()}")
                f.write("\n")

    def create_perfect_maze(self) -> None:
        """
        First create a list of possible walls. This list is composed of tuple:
        first a global tuple, in this tuple there is a tuple with x y
        coordinate for the actual wall, a tuple with east (if x+1) cell coord,
        or south cell coord (if y+1), then at the end of the tuple is the
        direction:
        1 for east, 2 for south.
        This list of walls is shuffled, then the program check if the actual
        global tuple is valid (check if the identity of the
        two cell are the same or not).
        If the identity are not the same, call open_wall from the Cell
        class to open the first wall with the corresponding direction,
        then open the inverse wall of the cell in this direction
        At the end check all the cells identity to change the value if needed
        """
        walls_list = []

        for y in range(self.height):
            for x in range(self.width):
                if x + 1 < self.width:
                    walls_list.append(((x, y), (x + 1, y), 1))
                if y + 1 < self.height:
                    walls_list.append(((x, y), (x, y + 1), 2))

        random.seed()
        random.shuffle(walls_list)
        if self.show_42 is True:
            for (x_a, y_a), (x_b, y_b), direction in walls_list:
                cell_a = self.maze[(x_a, y_a)]
                cell_b = self.maze[(x_b, y_b)]
                if (
                    cell_a.identity != cell_b.identity
                   and (cell_a.x, cell_a.y) not in self.res_xy
                   and (cell_b.x, cell_b.y) not in self.res_xy
                   ):
                    cell_a.open_wall(direction)
                    second_wall = (direction + 2) % 4
                    cell_b.open_wall(second_wall)
                    old_identity = cell_b.identity
                    new_identity = cell_a.identity
                    for cell in self.maze.values():
                        if cell.identity == old_identity:
                            cell.identity = new_identity

        else:
            print("Error: maze must be of 8x7 size to be able to print the 42")
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

    def create_imperfect_maze(self) -> None:
        """
        Create an imperfect maze with the same logic as the perfect.
        Here we open walls until the identity of entry and exit are the same,
        then we open wall until all the walls have the same identity

        :param self: the maze
        :param entry: entry point
        :type entry: tuple
        :param exit: exit point
        :type exit: tuple
        """
        # creer la liste des murs, definir entry cell et exit cell
        # faire du open jusqu'a se que identity de open == identity de exit?
        walls_list = []

        for y in range(self.height):
            for x in range(self.width):
                if x + 1 < self.width:
                    walls_list.append(((x, y), (x + 1, y), 1))
                if y + 1 < self.height:
                    walls_list.append(((x, y), (x, y + 1), 2))

        random.seed()
        random.shuffle(walls_list)
        entry_cell = self.maze[self.entry]
        exit_cell = self.maze[self.exit]

        if self.show_42 is True:
            for (x_a, y_a), (x_b, y_b), direction in walls_list:
                if entry_cell.identity != exit_cell.identity:
                    cell_a = self.maze[(x_a, y_a)]
                    cell_b = self.maze[(x_b, y_b)]
                    if (
                        (cell_a.x, cell_a.y) not in self.res_xy
                        and (cell_b.x, cell_b.y) not in self.res_xy
                       ):
                        cell_a.open_wall(direction)
                        second_wall = (direction + 2) % 4
                        cell_b.open_wall(second_wall)
                        old_identity = cell_b.identity
                        new_identity = cell_a.identity
                        for cell in self.maze.values():
                            if cell.identity == old_identity:
                                cell.identity = new_identity

            for (x_a, y_a), (x_b, y_b), direction in walls_list:
                cell_a = self.maze[(x_a, y_a)]
                cell_b = self.maze[(x_b, y_b)]
                if (
                    cell_a.identity != cell_b.identity
                    and (cell_a.x, cell_a.y) not in self.res_xy
                    and (cell_b.x, cell_b.y) not in self.res_xy
                   ):
                    cell_a.open_wall(direction)
                    second_wall = (direction + 2) % 4
                    cell_b.open_wall(second_wall)
                    old_identity = cell_b.identity
                    new_identity = cell_a.identity
                    for cell in self.maze.values():
                        if cell.identity == old_identity:
                            cell.identity = new_identity

        else:
            print("Error: maze must be of 8x7 size to be able to print the 42")
            for (x_a, y_a), (x_b, y_b), direction in walls_list:
                if entry_cell.identity != exit_cell.identity:
                    cell_a = self.maze[(x_a, y_a)]
                    cell_b = self.maze[(x_b, y_b)]
                    cell_a.open_wall(direction)
                    second_wall = (direction + 2) % 4
                    cell_b.open_wall(second_wall)
                    old_identity = cell_b.identity
                    new_identity = cell_a.identity
                    for cell in self.maze.values():
                        if cell.identity == old_identity:
                            cell.identity = new_identity

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


# def main():
#    maze = Maze(10, 10)
#    maze.create_perfect_maze()
#    maze.print_maze()
#    maze.generate_maze_output()
#   print(convert_hex_to_binary("1A"))
# main()
