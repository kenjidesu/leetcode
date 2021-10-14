class Solution(object):
    def isPerfectSquare(self, num):
        odd = 1
        while num > 0:
            num -= odd
            if num < 0:
                return False
            odd += 2
            
        return True
            
        
        