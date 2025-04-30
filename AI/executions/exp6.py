def solveNQueens(board, col, N):
    # If all queens are placed, return True
    if col == N:
        printSolution(board, N)
        return True

    # Try placing this queen in all rows one by one
    res = False
    for i in range(N):
        if isSafe(board, i, col, N):
            board[i][col] = 1  # Place the queen

            # Recur to place the rest of the queens
            res = solveNQueens(board, col + 1, N) or res

            # If placing queen in board[i][col] doesn't lead to a solution, backtrack
            board[i][col] = 0

    return res


def isSafe(board, row, col, N):
    # Check this row on the left side
    for x in range(col):
        if board[row][x] == 1:
            return False

    # Check upper diagonal on the left side
    for x, y in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[x][y] == 1:
            return False

    # Check lower diagonal on the left side
    for x, y in zip(range(row, N, 1), range(col, -1, -1)):
        if board[x][y] == 1:
            return False

    return True


def printSolution(board, N):
    print("One of the solutions:")
    for i in range(N):
        for j in range(N):
            print('Q' if board[i][j] == 1 else '.', end=" ")
        print()
    print()


# Main execution block
if __name__ == "__main__":
    N = int(input("Enter the size of the chessboard (N): "))
    board = [[0 for x in range(N)] for y in range(N)]

    if not solveNQueens(board, 0, N):
        print("No solution found")
