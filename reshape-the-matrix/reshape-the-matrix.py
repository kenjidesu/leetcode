class Solution(object):
    def matrixReshape(self, mat, r, c):
        vals = []
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                vals.append(mat[i][j])
        
        if c * r != len(vals): return mat
        
        arr = []
        cc = 0
        for i in range(r):
            tmp = []
            for j in range(c):
                tmp.append(vals[cc])
                cc += 1
            arr.append(tmp)
        return arr