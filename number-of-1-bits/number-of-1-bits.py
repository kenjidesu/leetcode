class Solution(object):
    def hammingWeight(self, n):
        # convert n to 32 bit unsigned int by adding 2**32
        unsint = n + 2 ** 32
        # counts the 1 of bin(unsint)
        # -1 because the python prefix for binary is 0b1, whichs is another 1
        return bin(unsint).count('1')-1
        