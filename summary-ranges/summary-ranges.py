class Solution(object):
    def summaryRanges(self, nums):
        nums.append(-1) # dummy element
        f = 0   # first pointer
        l = 0   # last pointer
        j = 0   # prev pointer
        arr = []
        for i in range(1, len(nums)):
            # updates l if the difference of prev and i is 1
            if nums[j] + 1 == nums[i]:
                l = i
            # if the difference is not 1, append f,l and update to i
            elif l > f:
                s = str(nums[f]) + "->" + str(nums[l])
                arr.append(s)
                f = i
                l = i
            # solo value, update f to i
            else:
                arr.append(str(nums[f]))
                f = i
            
            # add j
            j += 1
            
        return arr
            
        