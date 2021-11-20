class Solution(object):
    def findComplement(self, num):
        n = bin(num)[2:]
        nc = ["1" if i == "0" else "0" for i in n]
        c = "".join(i for i in nc)
        return int(c, 2)
        