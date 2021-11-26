class Solution(object):
    def searchMatrix(self, matrix, target):
        for i in range(len(matrix)):
            if target in matrix[i] and matrix[i][0] <= target:
                return True
        
        return False
    