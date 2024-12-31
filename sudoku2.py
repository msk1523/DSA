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

def solveSudoku(self, board: list[list[str]]) -> None:
    boxes = [{} for _ in range(9)]
    rows = [{} for _ in range(9)]
    cols = [{} for _ in range(9)]
    
    def getBox(row,col):
        new_c = col //3
        new_r = (row//3)*3
        return new_c + new_r
    
    for i in range(9):
        for j in range(9):
            if board[i][j] != '.':
                value = board[i][j]
                x = getBox(i,j)
                boxes[x][value]=True
                rows[i][value]=True
                cols[j][value]=True
                
    def isValid(box,row,col,num):
        if (num in box) or (num in row) or (num in col):
            return False
        return True    

    def solveBacktrack(board,boxes,rows,cols,r,c):
        if r==9 :
            return True 
        if board[r][c]=='.':
            box = getBox(r,c)
            for num in range(1,10):
                numVal = str(num)
                boxId = getBox(r,c)
                box = boxes[boxId]
                row = rows[r]
                col=cols[c]
                if (isValid(box,row,col,numVal)):
                    board[r][c]= numVal
                    box[numVal]=True
                    row[numVal]=True
                    col[numVal]=True
                    if c==8:
                        if(solveBacktrack(board,boxes,rows,cols,r+1,0)):return True
                    else:
                        if(solveBacktrack(board,boxes,rows,cols,r,c+1)):return True    
                    #backtrack
                    del box[numVal]
                    del row[numVal]
                    del col[numVal]
                    board[r][c]='.'
            return False
        else:
            if c==8:
                if(solveBacktrack(board,boxes,rows,cols,r+1,0)):return True
            else:
                if(solveBacktrack(board,boxes,rows,cols,r,c+1)):return True

    solveBacktrack(board,boxes,rows,cols,0,0) 
    
print(solveSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."],["6", ".", ".", "1", "9", "5", ".", ".", "."],[".", "9", "8", ".", ".", ".", ".", "6", "."],["8", ".", ".", ".", "6", ".", ".", ".", "3"],["4", ".", ".", "8", ".", "3", ".", ".", "1"],["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."],[".", ".", ".", "4", "1", "9", ".", ".", "5"],[".", ".", ".", ".", "8", ".", ".", "7", "9"]]))