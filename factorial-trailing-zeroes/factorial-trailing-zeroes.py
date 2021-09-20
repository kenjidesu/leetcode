class Solution(object):
    def trailingZeroes(self, n):
        zeros = 0
        while n > 0:
            # number that can be divided by 5 will have 1 more zero
            # can be divided by 5*5 will have 2 more zero... and so on
            n = n // 5
            zeros += n
            
        return zeros
        
        