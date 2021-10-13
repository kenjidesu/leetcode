from collections import Counter
class Solution(object):
    def intersect(self, nums1, nums2):
        # similarities of nums1 and nums2
        inter = set(nums1) & set(nums2)
        # returns a dict of how many ith value does it have inside the array
        x1 = Counter(nums1)
        x2 = Counter(nums2)
        
        arr = []
        # loops through the set of similarities
        for i in inter:
            # gets the minimum counts of x1 and x2
            mn = min(x1[i], x2[i])
            # we multiply on how many ith does it have in the arrays
            # since we got the similarities in set() which removes duplicates
            c = [i] * mn
            # we just append the array
            arr += c
            
        return arr
        