class Solution(object):
    def shuffle(self, nums, n):
        sthalf = nums[:n]
        ndhalf = nums[n:]
        rarr = []
        for i in range(n):
            rarr.append(sthalf[i])
            rarr.append(ndhalf[i])
        
        return rarr