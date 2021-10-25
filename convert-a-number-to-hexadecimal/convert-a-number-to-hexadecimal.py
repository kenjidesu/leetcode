class Solution(object):
    def toHex(self, num):
        # hex of 0 is 0
        if num == 0: return '0'
        # these are hex symbols or values
        hexx = "0123456789abcdef"
        # Two's compliment
        if num < 0: num += 2 ** 32
        # return string
        stret = ""
        # loop until num == 0
        while num > 0:
            # gets the remainder of num // 16
            dig = num % 16
            # updates num
            num = (num - dig) // 16
            # appends the symbols based on the remainder
            stret += hexx[dig]
        
        # return reverse string
        return stret[::-1]
        
        