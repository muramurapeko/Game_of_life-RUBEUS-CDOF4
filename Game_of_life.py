import os
import time

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def initialize_grid(width, height):
    grid = []
    for _ in range(height):
        row = [0] * width
        grid.append(row)
    return grid

def print_grid(grid):
    for row in grid:
        print(''.join(['#' if cell else ' ' for cell in row]))

def update_grid(grid):
    new_grid = initialize_grid(len(grid[0]), len(grid))
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            live_neighbors = count_live_neighbors(grid, i, j)
            if grid[i][j]:
                new_grid[i][j] = 1 if 2 <= live_neighbors <= 3 else 0
            else:
                new_grid[i][j] = 1 if live_neighbors == 3 else 0
    return new_grid

def count_live_neighbors(grid, row, col):
    count = 0
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if (0 <= i < len(grid)) and (0 <= j < len(grid[i])):
                if (i != row or j != col) and grid[i][j]:
                    count += 1
    return count

def main():
    # Set the width and height of the grid
    width = 40
    height = 20

    # Initialize the grid
    grid = initialize_grid(width, height)

    # Set some initial live cells
    grid[5][5] = 1
    grid[5][6] = 1
    grid[6][5] = 1
    grid[6][7] = 1
    grid[7][6] = 1

    # Run the game loop
    while True:
        clear_screen()
        print_grid(grid)
        grid = update_grid(grid)
        time.sleep(0.5)

if __name__ == '__main__':
    main()