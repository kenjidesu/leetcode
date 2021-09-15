class Solution(object):
    def mySqrt(self, x):
        # this represents an array [1,2,..,x]
        l = 1
        r = x
        
        # numbers < 2 are their own square roots
        if x < 2: return x
        
        # Binary Search of finding the sqrt
        while l < r:
            m = l + int((r - l) / 2)
            # if (x/2)^2 == x that's the sqrt
            if m * m == x:
                return m
            # if (x/2)^2 > x, m will be our rightmost
            elif m * m > x:
                r = m
            # if (x/2)^2 < x, m will be our leftmost
            elif m * m < x:
                l = m + 1
        
        # if l < r, means the l-1 is the sqrt
        return l - 1