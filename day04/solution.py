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

def part2(grid: list[list[str]]) -> int:
    """Perform rounds of moving rolls until no more can be moved.

    In each round collect all '@' cells that have fewer than 4 '@' neighbors,
    then mark them as moved (set to '.'). Repeat rounds until
    a round moves zero cells. Return the total number of moved rolls.
    """
    total_moved = 0
    round_no = 0
    while True:
        round_no += 1
        to_move: list[tuple[int, int]] = []

        # Scan grid and collect moves for this round
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if get_cell(grid, row, col) != '@':
                    continue
                neighbors = list(get_neighbors(grid, row, col))
                paper_neighbors = []
                for neighbor in neighbors:
                    if neighbor == '@':
                        paper_neighbors.append(neighbor)
                if len(paper_neighbors) < 4:
                    to_move.append((row, col))

        # Apply moves
        moved_this_round = 0
        for r, c in to_move:
            grid[r][c] = '.'
            moved_this_round += 1

        if moved_this_round == 0:
            break

        total_moved += moved_this_round

    return total_moved


if __name__ == "__main__":
    grid = read_grid()

    print(f"Total movable rolls: {part1(grid)}")
    print(f"Total movable rolls: {part2(grid)}")
