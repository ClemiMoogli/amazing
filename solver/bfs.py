from maze.maze import Maze


def find_neighbors(maze: Maze, loc: tuple[int, int]) -> list:
    """
    A function to find the opened cells next to a current cell.

    keyword arguments:
    - maze -- the maze instance
    - loc -- the current cell

    return value:
    a list of opened cell next to the current cell
    """
    neighbors = []
    x, y = loc
    grid = maze.maze
    current_cell = grid.get(loc)
    if current_cell.is_wall_open(0):
        neighbors.append((x, y - 1))
    if current_cell.is_wall_open(1):
        neighbors.append((x + 1, y))
    if current_cell.is_wall_open(2):
        neighbors.append((x, y + 1))
    if current_cell.is_wall_open(3):
        neighbors.append((x - 1, y))
    return neighbors


def find_path(parent: dict, entry_loc: tuple[int, int],
              exit_loc: tuple[int, int]) -> list[tuple[int,int]]:
    """
    A function to structure the path between entry and exit.

    keyword arguments:
    - parent -- a dictionary of previous cell: current cell during the solution path.
    - entry_loc -- the maze entry
    - exit_loc -- the maze output

    return value:
    A list of coordinates.
    """
    path = []
    current_loc = exit_loc
    while current_loc != entry_loc:
        path.append(current_loc)
        current_loc = parent[current_loc]
    path.append(entry_loc)
    path.reverse()
    return path


def bfs_solver(maze: Maze, entry_loc: tuple[int, int], exit_loc:
               tuple[int, int]) -> list[tuple[int, int]]:
    """
    A function using breadth first search algortythm to find the shortest_path between entry and exit.

    keyword arguments:
    - maze -- the maze instance
    - entry_loc -- the maze entry
    - exit_loc -- the maze exit

    return value:
    A list of coordinates.
    """
    queue = [entry_loc]
    visited = {entry_loc}
    parent = {}
    while queue:
        current_loc = queue.pop(0)
        if current_loc == exit_loc:
            break
        neighbors = find_neighbors(maze, current_loc)
        for cell in neighbors:
            if cell not in visited:
                visited.add(cell)
                queue.append(cell)
                parent[cell] = current_loc
    way = find_path(parent, entry_loc, exit_loc)
    return way


def convert_path_to_NSWE(shortest_path: list[tuple[int, int]]) -> str:
    """
    A function that take a shortest path in coordinates format and convert it to NSWE format.
    """
    path = ""
    for i in range(0, len(shortest_path) - 1):
        curr_x, curr_y = shortest_path[i]
        if (curr_x + 1, curr_y) == shortest_path[i+1]:
            path += "E"
        if (curr_x - 1, curr_y) == shortest_path[i+1]:
            path += "W"
        if (curr_x, curr_y + 1) == shortest_path[i+1]:
            path += "S"
        if (curr_x, curr_y - 1) == shortest_path[i+1]:
            path += "N"
    return path
