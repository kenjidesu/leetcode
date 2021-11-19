class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        # False, if arr is empty
        if len(arr) == 0: 
            return False
        # can't compare the difference to others if arr <= 2
        elif len(arr) <= 2:
            return True
      
        arr.sort()
        # Get the difference
        diff = arr[0] - arr[1]
        for i in range(2, len(arr)):
            # if the difference is different, return false
            if arr[i-1] - arr[i] != diff:
                return False
        
        return True
        