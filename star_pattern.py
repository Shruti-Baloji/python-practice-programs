N = 5  # Number of rows in the pattern

for i in range(1, N + 1):
    # Print leading spaces for alignment
    print(" " * (N - i), end="")
    # Print asterisks in each row
    print("*" * (2 * i - 1))