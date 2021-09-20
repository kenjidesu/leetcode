class Solution(object):
    def titleToNumber(self, columnTitle):
        # exponential
        multip = 1
        # value of columnTitle
        colnum = 0
        
        for i in reversed(columnTitle):
            # n^j, and add each value of char 
            colnum += multip * (ord(i) - 64)
            # multip is the j or the exponent to get the next letter
            multip *= 26
            
        return colnum
            
        