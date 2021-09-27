class Solution(object):
    def summaryRanges(self, nums):
        nums.append(-1)
        f = 0
        l = 0
        j = 0
        arr = []
        for i in range(1, len(nums)):
            if nums[j] + 1 == nums[i]:
                l = i
            elif l > f:
                s = str(nums[f]) + "->" + str(nums[l])
                arr.append(s)
                f = i
                l = i
            else:
                arr.append(str(nums[f]))
                f = i
                
            j += 1
            
        return arr
            
        