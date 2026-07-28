# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def calculate_sum(numbers):
    """Return the sum of all values in 'numbers' without using sum()."""
    total = 0
    for value in numbers:
        total += value
    return total


def calculate_average(numbers):
    """Return the average of all values in 'numbers'."""
    return calculate_sum(numbers) / len(numbers)


def find_maximum(numbers):
    """Return the largest value in 'numbers' without using max()."""
    largest = numbers[0]
    for value in numbers:
        if value > largest:
            largest = value
    return largest


def find_minimum(numbers):
    """Return the smallest value in 'numbers' without using min()."""
    smallest = numbers[0]
    for value in numbers:
        if value < smallest:
            smallest = value
    return smallest


def main():
    count = int(input("How many numbers? "))

    if count <= 0:
        print("Error: The count must be a positive integer.")
        return

    numbers = []
    for i in range(1, count + 1):
        value = float(input(f"Enter number {i}: "))
        numbers.append(value)

    print("\nResults:")
    print(f"Sum:     {calculate_sum(numbers):g}")
    print(f"Average: {calculate_average(numbers):g}")
    print(f"Maximum: {find_maximum(numbers):g}")
    print(f"Minimum: {find_minimum(numbers):g}")


if __name__ == "__main__":
    main()