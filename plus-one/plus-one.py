class Solution(object):
    def plusOne(self, digits):
        # holds the integer of the represented array
        num = 0
        for i in digits:
            # it mathematically converts digits to whole integer
            num = (num * 10) + i
        
        # returns array of num + 1
        return [j for j in str(num+1)]