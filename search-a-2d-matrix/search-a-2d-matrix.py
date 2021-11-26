class Solution(object):
    def searchMatrix(self, matrix, target):
        for i in range(len(matrix)):
            # only checks if the first element of matrix[i] is <= target
            # since the matrix are sorted
            if target in matrix[i] and matrix[i][0] <= target:
                return True
        
        return False
    