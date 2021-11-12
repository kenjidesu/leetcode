class Solution(object):
    def buildArray(self, nums):
        arr = []
        # if nums is empty, return empty
        if len(nums) == 0: return arr
        
        # loop through nums and append nums[i]
        for i in nums:
            arr.append(nums[i])
        
        return arr
        