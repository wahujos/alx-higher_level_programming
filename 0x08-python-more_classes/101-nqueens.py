#!/usr/bin/python3
def solve_n_queens(n):
    if n < 4:
        print("N must be at least 4")
        exit(1)

    board = [-1] * n
    solutions = []

    def is_safe(row, col):
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    def solve(row):
        if row == n:
            solutions.append([[i, col] for i, col in enumerate(board)])
            return
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                solve(row + 1)

    solve(0)

    for solution in solutions:
        for i, col in solution:
            print([i, col], end=" ")
        print()


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    solve_n_queens(n)
