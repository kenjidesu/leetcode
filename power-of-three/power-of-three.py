from math import log, ceil

class Solution(object):
    def isPowerOfThree(self, n):
        # Log of <= 0 nums are not defined in the real numbers.
        if n <= 0: return False
        
        # Gets the log of n
        lg = log(n, 3)
        
        # 3 exponent of the log result of n, to make sure they are equal
        return n == 3**ceil(lg)
        