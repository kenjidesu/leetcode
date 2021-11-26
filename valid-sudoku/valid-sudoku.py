class Solution(object):
    def isValidSudoku(self, board):        
        for i in range(9):
            st1, st2 = set(), set()
            for j in range(9):
                # Checks Columns
                if board[i][j].isnumeric():
                    if board[i][j] in st1:
                        return False
                    st1.add(board[i][j])
                # Checks Columns
                if board[j][i].isnumeric():
                    if board[j][i] in st2:
                        return False
                    st2.add(board[j][i])
                    
        # Checks 3 x 3 grid 
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                st3 = set()
                for k in range(3):
                    for l in range(3):
                        if board[i+k][j+l].isnumeric():
                            if board[i+k][j+l] in st3:
                                return False
                            st3.add(board[i+k][j+l])
                            
        return True