class Solution(object):
    def reverse(self, x):
        isNeg = False
        # checks if x is neg
        if x < 0:
            isNeg = True
            # converts x to positive
            x = x * -1
        
        # reverse num mathematically
        rev_num = 0
        while x > 0:
            # gets the last digit
            sgl_dig = x % 10
            # appends to rev_num
            rev_num = (rev_num * 10) + sgl_dig
            # removes the last digit of x
            x = x // 10
            
        # converts rev_num to neg if x is neg
        if isNeg:
            rev_num = rev_num * -1
        
        # returns rev_num if value is inside the signed 32-bit int range
        # else returns 0
        return rev_num if rev_num >= -2**31 and rev_num <= 2**31-1 else 0
