from math import log, ceil
# log(), compute the logarithm
# ceil(), returns a ceiling value of n

class Solution(object):
    def isPowerOfTwo(self, n):
        # to avoid value error
        if n < 1:
            return False
        # gets the log of n base 2
        tl = math.log(n, 2)
        # format it to 14 decimal places
        g = float("{:.14f}".format(tl))
        # if decimals are not 0 it adds 1
        # if all 0 it stays the same value therefore its equal to g
        return math.ceil(g) == g