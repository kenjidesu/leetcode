class Solution(object):
    def matrixReshape(self, mat, r, c):
        orgr = len(mat)
        colc = len(mat[0])
        
        if orgr * colc != r * c:
            return mat
        
        outarr = [[0 for _ in range(c)] for _ in range(r)]
        cc = 0
        for i in range(orgr):
            for j in range(colc):
                outarr[cc // c][cc % c] = mat[i][j]
                cc += 1
                
        return outarr
        