class Solution(object):
    def missingNumber(self, nums):
        # get rid of duplicate number using set()
        distnum = set(nums)
        for i in range(len(nums)+1):
            # checks if i in distnum
            if i not in distnum:
                # if not return i
                return i
        