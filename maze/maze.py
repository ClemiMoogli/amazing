from .cell import Cell
import random
from math import floor


class Maze:
    """
    The maze class.
    """
    def __init__(self, width: int, height: int,
                 entry: tuple[int, int], exit: tuple[int, int]):
        """
        Initialize the maze as a dictionnary. The key is tuple (x, y) with x
        as the width
        and y as the height. The value is another dictio with identity
        (cell number), used
        for the algo, and the hexa value of the walls.
        """
        self.show_42 = True
        self.width = width
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
        self.entry = entry
        self.exit = exit
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

    def generate_maze_output(self, output_file: str,
                             entry_loc: tuple[int, int],
                             exit_loc: tuple[int, int],
                             shortest_path: str) -> None:
        """
        Generate the Hex format of the maze and save it in the
        output file.

        :param self: the maze
        :param output_file: the file where we print the result
        :type output_file: str
        :param entry_loc: entry coordinate (x, y)
        :type entry_loc: tuple[int, int]
        :param exit_loc: exit coordinate (x, y)
        :type exit_loc: tuple[int, int]
        :param shortest_path: shortest path from entry to exit
        :type shortest_path: list[tuple[int, int]]
        """
        with open(output_file, "w") as f:
            for y in range(self.height):
                for x in range(self.width):
                    cell = self.maze.get((x, y))
                    if cell:
                        f.write(f"{cell.show_cell_hexa()}")
                f.write("\n")
            f.write("\n")
            f.write(f"{entry_loc[0]},{entry_loc[1]}\n")
            f.write(f"{exit_loc[0]},{exit_loc[1]}\n")
            f.write(f"{shortest_path}\n")

    def create_perfect_maze(self) -> None:
        """
        Create a perfect maze using the random cell merging algorithm.
        First create a list of east and south walls for every cell possible,
        then shuffle it.
        Open walls until every cell have the same identity.
        If the maze width and height allow it, show a 42 composed of
        closed cells.

        :param self: the maze
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
        Create an imperfect maze using the random cell merging algorithm.
        Once every cell have the same identity, open 10% of the total
        walls to create an imperfect maze with circles.

        :param self: Description
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
        remaining_wall = []
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

            nb_to_open = len(walls_list) // 10
            random.shuffle(walls_list)

            for i in range(nb_to_open):
                (x_a, y_a), (x_b, y_b), direction = walls_list[i]
                cell_a = self.maze[(x_a, y_a)]
                cell_b = self.maze[(x_b, y_b)]
                if (
                    (cell_a.x, cell_a.y) not in self.res_xy
                    and (cell_b.x, cell_b.y) not in self.res_xy
                   ):
                    self.maze[(x_a, y_a)].open_wall(direction)
                    self.maze[(x_b, y_b)].open_wall((direction + 2) % 4)

        else:
            print("Error: maze must be of 8x7 size to be able to print the 42")
            for (x_a, y_a), (x_b, y_b), direction in walls_list:
                if entry_cell.identity != exit_cell.identity:
                    cell_a = self.maze[(x_a, y_a)]
                    cell_b = self.maze[(x_b, y_b)]

                if cell_a.identity != cell_b.identity:
                    cell_a.open_wall(direction)
                    cell_b.open_wall((direction + 2) % 4)
                    old_identity = cell_b.identity
                    new_identity = cell_a.identity
                    for cell in self.maze.values():
                        if cell.identity == old_identity:
                            cell.identity = new_identity

                else:
                    remaining_wall.append(((x_a, y_a), (x_b, y_b), direction))

            nb_to_open = len(remaining_wall) // 10
            random.shuffle(walls_list)

            for i in range(nb_to_open):
                (x_a, y_a), (x_b, y_b), direction = remaining_wall[i]
                self.maze[(x_a, y_a)].open_wall(direction)
                self.maze[(x_b, y_b)].open_wall((direction + 2) % 4)
