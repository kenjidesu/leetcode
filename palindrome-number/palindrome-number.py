class Solution(object):
    def isPalindrome(self, x):
        # store the org num
        org_num = x
        # returns False if x < 0
        if x < 0:
            return False
        
        # performs the reverse mathematically
        rev_num = 0
        while x > 0:
            # gets the last digit
            sig_dig = x % 10
            # append to rev_num
            rev_num = (rev_num * 10) + sig_dig
            # pop the last digit of x
            x = x // 10
        
        # checks if palindrome
        return org_num == rev_num