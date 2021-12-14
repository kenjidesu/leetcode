class Solution(object):
    def maxSubArray(self, nums):
        mx = tmp = nums[0]
        for i in range(1, len(nums)):
            tmp = max(nums[i], nums[i] + tmp)
            
            if tmp > mx: mx = tmp
            
        return mx
        