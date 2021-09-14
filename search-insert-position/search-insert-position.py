class Solution(object):
    def searchInsert(self, nums, target):
        
        try:
            # finds the index of target if target in nums
            return nums.index(target)
        except ValueError:
            # returns the len(nums) which is the last index of nums
            if target > nums[-1]:
                return len(nums)
            
            # returns index where target can be inserted
            for i in range(len(nums)):
                if nums[i] >= target:
                    return i