class Solution(object):
    def removeDuplicates(self, nums):
        # returns 0 if nums is empty
        if not nums:
            return 0
        
        # tracks the distinct numbers
        i = 0
        for j in range(1, len(nums)):
            # if != then we need to update the num to remove duplicates
            if nums[j] != nums[i]:
                i += 1
                # updates the nums to remove the duplicates
                nums[i] = nums[j]
        
        # +1 because the i started at 0
        return i + 1