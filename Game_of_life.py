#!/usr/bin/env python3
import time
import os
import random
import sys

def clear_console():
    os.system("cls")

def create_initial_grid(rows, cols):
    grid = []
    for row in range(rows):
        grid_rows = []
        for col in range(cols):
            # Generate a random number and based on that decide whether to add a live or dead cell to the grid
            if random.randint(0, 7) == 0:
                grid_rows += [1]
            else:
                grid_rows += [0]
        grid += [grid_rows]
    return grid

def print_grid(rows, cols, grid, generation):
    clear_console()
    output_str = ""
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 0:
                output_str += "  "
            else:
                output_str += "■ "
        output_str += "\n\r"
    print(output_str, end="")


def create_next_grid(rows, cols, grid, next_grid):

    for row in range(rows):
        for col in range(cols):
            # Get the number of live cells adjacent to the cell at grid[row][col]
            live_neighbors = get_live_neighbors(row, col, rows, cols, grid)

            # If the number of surrounding live cells is < 2 or > 3 then we make the cell at grid[row][col] a dead cell
            if live_neighbors < 2 or live_neighbors > 3:
                next_grid[row][col] = 0
            # If the number of surrounding live cells is 3 and the cell at grid[row][col] was previously dead then make
            # the cell into a live cell
            elif live_neighbors == 3 and grid[row][col] == 0:
                next_grid[row][col] = 1
            # If the number of surrounding live cells is 3 and the cell at grid[row][col] is alive keep it alive
            else:
                next_grid[row][col] = grid[row][col]


def get_live_neighbors(row, col, rows, cols, grid):
    life_sum = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            # Make sure to count the center cell located at grid[row][col]
            if not (i == 0 and j == 0):
                # Using the modulo operator (%) the grid wraps around
                life_sum += grid[((row + i) % rows)][((col + j) % cols)]
    return life_sum

def run_game():
    # INITIALISATION
    clear_console()
    rows=25
    cols=50
    generations = 5000
    current_generation = create_initial_grid(rows, cols)
    next_generation = create_initial_grid(rows, cols)
    
    # RUN
    gen = 1
    for gen in range(1, generations + 1):
        print_grid(rows, cols, current_generation, gen)
        create_next_grid(rows, cols, current_generation, next_generation)
        time.sleep(1 / 5.0)
        current_generation, next_generation = next_generation, current_generation

    print_grid(rows, cols, current_generation, gen)
    return input("Game finished !")

# START
run_game()
   
