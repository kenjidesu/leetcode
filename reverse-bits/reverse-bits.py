class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # we add 2**32 to make n a 32 bits unsigned integer
        unsint = n + 2 ** 32
        # reverse bits and remove the prefix of python
        bint = bin(unsint)[:2:-1]
        # return the int value base 2
        return int(bint, 2)