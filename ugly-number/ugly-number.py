class Solution(object):
    def isUgly(self, n):
        # checks if positive
        if n < 1: return False
        
        # Gets the lowest value of n using the given prime factors
        while n % 2 == 0: n /= 2
        while n % 3 == 0: n /= 3
        while n % 5 == 0: n /= 5
        
        # If 1, that means it is divisible by this prime factors
        return n == 1
        
