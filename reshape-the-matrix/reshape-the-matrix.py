class Solution(object):
    def matrixReshape(self, mat, r, c):
        # Gets all the value in mat
        nums = []
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                nums.append(mat[i][j])
        
        # return original matrix if reshape operation is not possible
        if r * c != len(nums): return mat
        
        # Reshape matrix
        arr = []
        q = 0   # Track on what value to put in matrix
        for i in range(r):
            temp = []
            for j in range(c):
                temp.append(nums[q])
                q += 1
            # append the column row to the row array
            arr.append(temp)
            
        return arr