class Solution(object):
    def findRotation(self, mat, target):
        # return right away if mat == target, no need to rotate
        if mat == target: return True
        
        # stops when we rotated mat back to its original place
        s = self.rotate(mat)
        while s != mat:
            # return true if s == target
            if s == target:
                return True
            # otherwise, rotate it again
            else:
                s = self.rotate(s)
        
        # If it stops then it can't be obtained by rotation
        return False
    
        
    def rotate(self, mat):
        arr = []
        for i in range(len(mat)):
            temp = []
            for j in range(len(mat[i])-1, -1, -1):
                temp.append(mat[j][i])
            arr.append(temp)
            
        return arr
        