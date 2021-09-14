class Solution(object):
    def maxSubArray(self, nums):
        # sets ng,ng = nums[0]
        ng = nc = nums[0]
        for i in range(1, len(nums)):
            # gets the max of i, i + nc
            nc = max(nums[i], nums[i] + nc)
            # updates ng if nc > ng, ng will be our max sub
            if nc > ng:
                ng = nc
                
        return ng