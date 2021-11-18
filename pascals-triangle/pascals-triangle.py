class Solution(object):
    def generate(self, numRows):
        # Instantly creates arrays of 1 base on numRows
        pascal = [[1]*(i+1) for i in range(numRows)]
        
        # Starts at 2 because the first 2 arrays are supposed to be 1's only
        for i in range(2, numRows):
            for j in range(1, i):
                # adds the last array and set it to the mid of pascal
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
                
        return pascal