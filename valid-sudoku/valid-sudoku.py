class Solution(object):
    def isValidSudoku(self, board):
        # Checks row and column
        for i in range(9):
            col, row = set(), set()
            for j in range(9):
                if board[i][j].isalnum():
                    if board[i][j] in col:
                        return False
                    col.add(board[i][j])
                    
                if board[j][i].isalnum():
                    if board[j][i] in row:
                        return False
                    row.add(board[j][i])
        
        # Checks 3x3 grid
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                grid = set()
                for k in range(3):
                    for l in range(3):
                        if board[i+k][j+l].isalnum():
                            if board[i+k][j+l] in grid:
                                return False
                            grid.add(board[i+k][j+l])
                            
        return True
        