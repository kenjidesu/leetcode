class Solution(object):
    def addDigits(self, num):
        # holds num
        n = num
        while True:
            # add digits
            t = 0
            for i in range(len(str(n))):
                t += int(str(n)[i])
            
            # checks if t is only 1 digit
            if  len(str(t)) == 1:
                return t
            
            # updates n
            n = t
            
        