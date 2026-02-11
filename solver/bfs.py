from maze.maze import Maze

def find_neighbors(maze:Maze, loc:tuple(int,int)) -> list:
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

def find_path(parent:dict, entry_loc:tuple(int,int), exit_loc:tuple(int,int)) -> tuple:
    path = []
    current_loc = exit_loc
    while current_loc != entry_loc:
        path.append(current_loc)
        current_loc = parent[current_loc]
    path.append(entry_loc)
    path.reverse()
    return path

def bfs_solver(maze:Maze, entry_loc:tuple(int,int), exit_loc:tuple(int,int)):
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
