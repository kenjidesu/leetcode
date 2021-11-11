from collections import Counter

class Solution(object):
    def sumOfUnique(self, nums):
        # checks if nums exist
        if len(nums) == 0: return 0
        
        # counts the quantity of set(nums)
        x = Counter(nums)
        n = 0
        # loop through counts
        for i in x.most_common():
            # [1] is the quantity of each num
            if i[1] == 1:
                # [0] is the number
                n += i[0]
                
        return n
        