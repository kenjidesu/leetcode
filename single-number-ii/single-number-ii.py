class Solution(object):
    def singleNumber(self, nums):
        if len(nums) == 0: return
        
        for i in set(nums):
            if nums.count(i) == 1:
                return i
        
        return