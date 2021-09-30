from math import log, ceil

class Solution(object):
    def isPowerOfTwo(self, n):
        if n < 1:
            return False
        tl = math.log(n, 2)
        g = float("{:.14f}".format(tl))
        return math.ceil(g) == g