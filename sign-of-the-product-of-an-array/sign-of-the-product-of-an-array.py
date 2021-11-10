class Solution(object):
    def arraySign(self, nums):
        if len(nums) == 0: return 0
        
        product = nums[0]
        for i in range(1, len(nums)):
            product *= nums[i]
            
        if product > 0:
            return 1
        elif product < 0:
            return -1
        else:
            return 0
        