class Solution(object):
    def intersection(self, nums1, nums2):
        # gets the intersection of nums1 and nums2
        return list(set(nums1) & set(nums2))