from numpy import median

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        # Merge Two Sorted Arrays
        twoArr = nums1 + nums2
        
        return median(twoArr)