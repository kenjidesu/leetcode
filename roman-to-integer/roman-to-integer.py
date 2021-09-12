class Solution(object):
    def romanToInt(self, s):
        # assign the value of each symbol
        translate = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        # replace the value that is smallest to the right
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        
        # adds each value of the symbols
        num = 0
        for i in s:
            num += translate[i]
            
        return num