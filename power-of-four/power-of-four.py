from math import log, ceil
class Solution(object):
    def isPowerOfFour(self, n):
        if n <= 0: return False
        nlog = log(n, 4)
        
        return ceil(nlog) == nlog
        