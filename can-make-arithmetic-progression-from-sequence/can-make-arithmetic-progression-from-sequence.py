class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        if len(arr) == 0: 
            return False
        elif len(arr) <= 2:
            return True
        
        arr.sort()
        diff = arr[0] - arr[1]
        for i in range(2, len(arr)):
            if arr[i-1] - arr[i] != diff:
                return False
        
        return True
        