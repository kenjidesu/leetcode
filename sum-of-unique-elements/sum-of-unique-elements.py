from collections import Counter

class Solution(object):
    def sumOfUnique(self, nums):
        if len(nums) == 0: return 0
        
        x = Counter(nums)
        n = 0
        for i in x.most_common():
            if i[1] == 1:
                n += i[0]
                
        return n
        