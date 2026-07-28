# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================


def read_matrix(rows, cols, label=""):
    """Read a rows x cols matrix from the user, one row per line."""
    print(f"\nEnter matrix {label} ({rows} x {cols}):")
    matrix = []
    for i in range(rows):
        while True:
            entries = input(f"Enter row {i + 1}: ").split()
            if len(entries) != cols:
                print(f"Error: expected {cols} values, got {len(entries)}. Try again.")
                continue
            matrix.append([float(value) for value in entries])
            break
    return matrix


def display_matrix(matrix, title="Matrix"):
    """Print a matrix in a neat, aligned grid."""
    print(f"\n{title}:")
    for row in matrix:
        formatted_row = "  ".join(f"{value:g}" for value in row)
        print(formatted_row)


def transpose_matrix(matrix):
    """Return the transpose of 'matrix' using nested loops."""
    rows = len(matrix)
    cols = len(matrix[0])

    result = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]

    return result


def add_matrices(a, b):
    """Return the element-wise sum of two same-sized matrices."""
    rows = len(a)
    cols = len(a[0])

    result = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            result[i][j] = a[i][j] + b[i][j]

    return result


def multiply_matrices(a, b):
    """Return the matrix product A x B using nested loops."""
    rows_a = len(a)
    cols_a = len(a[0])
    cols_b = len(b[0])

    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += a[i][k] * b[k][j]
            result[i][j] = total

    return result


def get_positive_int(prompt):
    """Read a positive integer from the user, re-prompting on invalid input."""
    while True:
        value = int(input(prompt))
        if value > 0:
            return value
        print("Error: value must be a positive integer.")


def part_a_transpose():
    rows = get_positive_int("Enter number of rows: ")
    cols = get_positive_int("Enter number of columns: ")

    matrix = read_matrix(rows, cols)
    result = transpose_matrix(matrix)

    display_matrix(matrix, "Original Matrix")
    display_matrix(result, "Transposed Matrix")


def part_b_add():
    rows = get_positive_int("Enter number of rows: ")
    cols = get_positive_int("Enter number of columns: ")

    matrix_a = read_matrix(rows, cols, "A")
    matrix_b = read_matrix(rows, cols, "B")
    result = add_matrices(matrix_a, matrix_b)

    display_matrix(matrix_a, "Matrix A")
    display_matrix(matrix_b, "Matrix B")
    display_matrix(result, "A + B")


def part_c_multiply():
    rows_a = get_positive_int("Enter number of rows for Matrix A: ")
    cols_a = get_positive_int("Enter number of columns for Matrix A: ")
    rows_b = cols_a
    print(f"(Matrix B must have {rows_b} rows to match Matrix A's columns.)")
    cols_b = get_positive_int("Enter number of columns for Matrix B: ")

    matrix_a = read_matrix(rows_a, cols_a, "A")
    matrix_b = read_matrix(rows_b, cols_b, "B")
    result = multiply_matrices(matrix_a, matrix_b)

    display_matrix(matrix_a, "Matrix A")
    display_matrix(matrix_b, "Matrix B")
    display_matrix(result, "A x B")


def main():
    while True:
        print("\nMatrix Operations Menu")
        print("A. Transpose a Matrix")
        print("B. Add Two Matrices")
        print("C. Multiply Two Matrices")
        print("Q. Quit")

        choice = input("Choose an option: ").strip().upper()

        if choice == "A":
            part_a_transpose()
        elif choice == "B":
            part_b_add()
        elif choice == "C":
            part_c_multiply()
        elif choice == "Q":
            break
        else:
            print("Invalid option. Please choose A, B, C, or Q.")


if __name__ == "__main__":
    main()