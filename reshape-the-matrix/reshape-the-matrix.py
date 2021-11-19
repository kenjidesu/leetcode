class Solution(object):
    def matrixReshape(self, mat, r, c):
        # ===============================
        nums = []
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                nums.append(mat[i][j])
        # ===============================
        if r * c != len(nums): return mat
        # ===============================
        arr = []
        q = 0
        for i in range(r):
            temp = []
            for j in range(c):
                temp.append(nums[q])
                q += 1
            arr.append(temp)
            
        return arr
        