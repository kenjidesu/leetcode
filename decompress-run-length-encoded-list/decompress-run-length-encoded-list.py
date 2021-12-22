class Solution(object):
    def decompressRLElist(self, nums):
        output = []
        for i in range(0, len(nums), 2):
            [freq, val] = [nums[i], nums[i+1]]
            output += freq * [val]
            
        return output
        