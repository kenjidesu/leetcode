class Solution(object):
    def majorityElement(self, nums):
        n = len(nums) // 2
        # set(nums) to loop through non-duplicated nums
        for i in set(nums):
            cc = nums.count(i)
            # checks if cc if the element that appears
            # more than n / 2
            if cc >= n+1:
                return i
        