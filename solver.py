from pysat.solvers import Glucose3
import pandas as pd
import numpy as np

def read_table_from_csv(file_path):
    """
    Reads a sudoku puzzle from a csv file.
    file_path: path to the csv file
    Return: 2D matrix of integers (1-9) or null (0) for empty cells
    """
    table = pd.read_csv(file_path, header=None).to_numpy()
    return table


def fill_table(table, max_sol_num=1):
    """
    Solves a sudoku puzzle using SAT solver.
    table: 2D matrix of integers (1-9) or null (0) for empty cells
    Return: 2D matrix of integers (1-9) representing the solved sudoku puzzle.
    """

    solver = Glucose3()

    # Add clauses
    # r=row(0~8), c=column(0~8), v=value(1~9), number=r*81 + c*9 + v
    # block_r=block_row(0~2), block_c=block_column(0~2)

    # Value
    # value indicated in the table
    for r in range(9):
        for c in range(9):
            v = int(table[r][c])
            if v != 0:
                solver.add_clause([r * 81 + c * 9 + v])
            
    # Cell
    # Each cell has a value
    for r in range(9):
        for c in range(9):
            solver.add_clause([(r * 81 + c * 9 + v) for v in range(1, 10)])
    # Each cell has only one value
    for r in range(9):
        for c in range(9):
            for v1 in range(1, 9):
                for v2 in range(v1 + 1, 10):
                    solver.add_clause([-(r * 81 + c * 9 + v1), -(r * 81 + c * 9 + v2)])

    # Row
    # Each row does not have duplicate values
    for r in range(9):
        for v in range(1, 10):
            for c1 in range(8):
                for c2 in range(c1 + 1, 9):
                    solver.add_clause([-(r * 81 + c1 * 9 + v), -(r * 81 + c2 * 9 + v)])

    # Column
    # Each column does not have duplicate values
    for c in range(9):
        for v in range(1, 10):
            for r1 in range(8):
                for r2 in range(r1 + 1, 9):
                    solver.add_clause([-(r1 * 81 + c * 9 + v), -(r2 * 81 + c * 9 + v)])

    # Block
    # Each block does not have duplicate values
    for block_r in range(3):
        for block_c in range(3):
            for v in range(1, 10):
                for r1 in range(3*block_r, 3*(block_r + 1)):
                    for r2 in range(3*block_r, 3*(block_r + 1)):
                        for c1 in range(3*block_c, 3*(block_c + 1)):
                            for c2 in range(3*block_c, 3*(block_c + 1)):
                                if r1 < r2 or c1 < c2:
                                    solver.add_clause([-(r1 * 81 + c1 * 9 + v), -(r2 * 81 + c2 * 9 + v)])

    # Solve
    solutions = []
    # Find all solutions
    while solver.solve():
        model = solver.get_model()
        # Convert model to 2D matrix
        sol = []
        sol_table = np.zeros((9, 9), dtype=int)
        # Fill the solution table
        for n in model:
            if n > 0:
                r = (n - 1) // 81
                c = ((n - 1) % 81) // 9
                v = (n - 1) % 9 + 1
                # record the solution table
                sol_table[r][c] = v
                # record the solution list
                sol.append(n)
                
        solutions.append(sol_table)
        if len(solutions) >= max_sol_num:
            break
        solver.add_clause([-i for i in sol])

    return solutions


def show_solution(solutions):
    """
    Show the sudoku solution
    solutions: list of 2D matrix of integers
    """
    for i, solution in enumerate(solutions):
        print(f"Solution {i + 1}:")
        show_table(solution)
        print()


def show_table(table):
    """
    Show the sudoku table
    table: 2D matrix of integers
    """
    print("-------------------------------")
    for r in range(9):
        print("| ", end='')
        for c in range(9):
            print(table[r][c], end='  ' if c % 3 != 2 else ' | ')
        print()
        if r % 3 == 2 and r != 8:
            print("----------+---------+---------")
    print("-------------------------------")

# Get a table from a csv file
path = input("Enter the path to the csv file: ")
table = read_table_from_csv(path)
max_sol_num = int(input("Enter the max number of solutions to find: "))
solutions = fill_table(table, max_sol_num)
show_solution(solutions)
