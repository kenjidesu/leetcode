class Solution(object):
    def maximumGap(self, nums):
        # return 0 if less than 2 elemets
        if len(nums) < 2: return 0
        
        # sort nums
        nums.sort()
        # initialize the lowest possible number
        mx = float('-inf')
        for i in range(1, len(nums)):
            # subtract the successive elements to get the gap
            sub = nums[i] - nums[i-1]
            # update mx to the maximum gap
            mx = max(mx, sub)
            
        return mx
        