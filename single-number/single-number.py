class Solution(object):
    def singleNumber(self, nums):
        # Transistive closure, a + b = b + a
        a = 0
        for num in nums:
            # Returns 1 if one of the bits is 1 and the other is 0
            a ^= num
            
        return a
        