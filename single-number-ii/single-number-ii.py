from collections import Counter

class Solution(object):
    def singleNumber(self, nums):
        x = Counter(nums)
        return x.most_common()[-1][0]