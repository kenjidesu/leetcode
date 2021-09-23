class Solution(object):
    def containsDuplicate(self, nums):
        # if there's a duplicate, set() will get rid of it
        # and length of that will get affected
        return len(nums) != len(set(nums))