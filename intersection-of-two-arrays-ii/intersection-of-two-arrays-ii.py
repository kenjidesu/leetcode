from collections import Counter
class Solution(object):
    def intersect(self, nums1, nums2):
        inter = set(nums1) & set(nums2)
        x1 = Counter(nums1)
        x2 = Counter(nums2)
        arr = []
        for i in inter:
            mn = min(x1[i], x2[i])
            c = [i] * mn
            arr += c
            
        return arr
        