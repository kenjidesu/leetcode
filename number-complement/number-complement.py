class Solution(object):
    def findComplement(self, num):
        # Binary of num, [2:] to get rid of '0b'
        n = bin(num)[2:]
        # Flip all 0's to 1's and 1's to 0's
        nc = ["1" if i == "0" else "0" for i in n]
        # Join them together for conversion
        c = "".join(i for i in nc)
        # return the int base 2
        return int(c, 2)
        