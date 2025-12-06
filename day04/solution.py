def read_grid(path: str = "day04/input.txt") -> list[list[str]]:
    """Reads grid from file and returns as list of list of strings."""
    grid: list[list[str]] = []
    try:
        with open(path, 'r') as f:
            for line in f:
                clean = line.rstrip('\n')
                if clean == '':
                    continue
                grid.append(list(clean))
    except FileNotFoundError:
        print(f"ERROR: The file '{path}' was not found. Please create it and add data.")
    return grid


def get_cell(grid: list[list[str]], row: int, col: int) -> str:
    """Returns value of cell using 0-based indices."""
    return grid[row][col]


def get_neighbors(grid: list[list[str]], row: int, col: int):
    """Returns list of neighbor cell values (8-neighborhood)."""
    neighbors = [(-1, -1), (-1, 0), (-1, 1),
                (0, -1),            (0, 1),
                (1, -1),    (1, 0), (1, 1)]

    for row_offset, col_offset in neighbors:
        neighbor_row, neighbor_col = row + row_offset, col + col_offset
        if 0 <= neighbor_row < len(grid) and 0 <= neighbor_col < len(grid[0]):
            yield grid[neighbor_row][neighbor_col]


def part1(grid: list[list[str]]) -> int:
    """Returns the number of movable paper rolls ('@') in the grid."""
    movable_rolls = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            # Iterate over each cell (if it is a paper roll) and find its neighbors
            if get_cell(grid, row, col) == '@':
                neighbors = list(get_neighbors(grid, row, col))
                paper_neighbors = []
                for neighbor in neighbors:
                    if neighbor == '@':
                        paper_neighbors.append(neighbor)
                if len(paper_neighbors) < 4:
                    movable_rolls += 1
                    print(f"Cell ({row},{col}) has {len(paper_neighbors)} '@' neighbors.")
            else:
                continue
    return movable_rolls


if __name__ == "__main__":
    grid = read_grid()

    print(f"Total movable rolls: {part1(grid)}")
