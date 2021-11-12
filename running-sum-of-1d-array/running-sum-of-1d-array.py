class Solution(object):
    def runningSum(self, nums):
        # return empty array if there's nothing to sum
        if len(nums) == 0: return []
        
        for i in range(1, len(nums)):
            nums[i] = nums[i-1] + nums[i]
        return nums