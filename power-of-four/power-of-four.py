from math import log, ceil
class Solution(object):
    def isPowerOfFour(self, n):
        # Negative numbers are undefined in log()
        if n <= 0: return False
        # gets the log of n base 4
        nlog = log(n, 4)
        
        # ceil(), to make sure there's no decimal
        # if there's decimal, ceil() rounds a number up to the next largest integer
        # and that will make the ceil(nlog) != nlog
        return ceil(nlog) == nlog
        
