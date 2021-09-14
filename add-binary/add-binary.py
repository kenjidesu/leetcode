class Solution(object):
    def addBinary(self, a, b):
        # return sum of the binary string
        return bin(int(a, 2) + int(b, 2))[2:]