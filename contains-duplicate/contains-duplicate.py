class Solution(object):
    def containsDuplicate(self, nums):
        m = []
        
        for i in nums:
            if i not in m:
                m.append(i)
            elif i in m:
                return True
            
        return False