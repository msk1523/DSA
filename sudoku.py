# Sudoku Solver
# Write a program to solve a Sudoku puzzle by filling the empty cells.

# A sudoku solution must satisfy all of the following rules:

# Each of the digits 1-9 must occur exactly once in each row.

# Each of the digits 1-9 must occur exactly once in each column.

# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

# The '.' character indicates empty cells.

# Constraints:

# board.length == 9

# board[i].length == 9

# board[i][j] is a digit between 1 and 9 , inclusive or '.'.

# It is guaranteed that the input board has only one solution.

# Example: 

# board = [

# ["5", "3", ".", ".", "7", ".", ".", ".", "."],

# ["6", ".", ".", "1", "9", "5", ".", ".", "."],

# [".", "9", "8", ".", ".", ".", ".", "6", "."],

# ["8", ".", ".", ".", "6", ".", ".", ".", "3"],

# ["4", ".", ".", "8", ".", "3", ".", ".", "1"],

# ["7", ".", ".", ".", "2", ".", ".", ".", "6"],

# [".", "6", ".", ".", ".", ".", "2", "8", "."],

# [".", ".", ".", "4", "1", "9", ".", ".", "5"],

# [".", ".", ".", ".", "8", ".", ".", "7", "9"]

# ]

# Output : 


# [

# ["5", "3", "4", "6", "7", "8", "9", "1", "2"],

# ["6", "7", "2", "1", "9", "5", "3", "4", "8"],

# ["1", "9", "8", "3", "4", "2", "5", "6", "7"],

# ["8", "5", "9", "7", "6", "1", "4", "2", "3"],

# ["4", "2", "6", "8", "5", "3", "7", "9", "1"],

# ["7", "1", "3", "9", "2", "4", "8", "5", "6"],

# ["9", "6", "1", "5", "3", "7", "2", "8", "4"],

# ["2", "8", "7", "4", "1", "9", "6", "3", "5"],

# ["3", "4", "5", "2", "8", "6", "1", "7", "9"]

# ]

def solveSudoku(board):
    #The function modifies the board in place to present the solution. Hence there is no need to return the board 

    def isValid(board, row, col, num):
        # Check if a number 'num' can be placed at board[row][col].
        for x in range(9):
            # Check row and column: The number must not already exist in the same row and column.
            if board[x][col] == num or board[row][x] == num:
                return False

            # Calculate the start row and column index for the 3x3 sub-box.
            r = 3 * (row // 3) + x // 3
            c = 3 * (col // 3) + x % 3

            # Check 3x3 sub-box: The number must not already exist in the same 3x3 sub-box.
            if board[r][c] == num:
                return False

        # If the number 'num' is not found in the same row, column, and 3x3 sub-box, it is valid.
        return True

    def helper(board):
        # Iterate through each cell in the board.
        for row in range(9):
            for col in range(9):
                # If the cell is empty ('.').
                if board[row][col] == '.':
                    # Try placing each number from 1 to 9 in the empty cell.
                    for num in '123456789':
                        # Check if the number is valid in the current position.
                        if isValid(board, row, col, num):
                            # Place the number in the cell.
                            board[row][col] = num

                            # Recursively attempt to solve the rest of the board with this number placed.
                            if helper(board):
                                return True

                            # If placing the number does not lead to a solution, reset the cell and try the next number.
                            board[row][col] = '.'

                    # If no number from 1 to 9 can be placed in this cell, backtrack.
                    return False

        # If the entire board is filled without conflicts, the puzzle is solved.
        return True

    # Start the solving process.
    helper(board)

    
print(solveSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."],["6", ".", ".", "1", "9", "5", ".", ".", "."],[".", "9", "8", ".", ".", ".", ".", "6", "."],["8", ".", ".", ".", "6", ".", ".", ".", "3"],["4", ".", ".", "8", ".", "3", ".", ".", "1"],["7", ".", ".", ".", "2", ".", ".", ".", "6"],[".", "6", ".", ".", ".", ".", "2", "8", "."],[".", ".", ".", "4", "1", "9", ".", ".", "5"],[".", ".", ".", ".", "8", ".", ".", "7", "9"]]))    
