class Solution(object):
    def removeElement(self, nums, val):
        if not nums:
            return 0
        
        # helps track the nums[i] != val
        k = 0
        for i in range(len(nums)):
            # if ith != val, remove the update the k
            if nums[i] != val:
                # updates num of the kth place
                nums[k] = nums[i]
                # adds 1, to update the next nums[i]
                k += 1
                
        # returns length of nums[i] != val
        return k
        