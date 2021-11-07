class Solution(object):
    def getSumAbsoluteDifferences(self, nums):
        smb = 0
        smt = sum(nums)
        res = []
        for i in range(len(nums)):
            smt -= nums[i]
            res.append(smt - (len(nums)-1 - i) * nums[i] + i * nums[i] - smb)
            smb += nums[i]
        
        return res