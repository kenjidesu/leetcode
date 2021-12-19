class Solution(object):
    def firstUniqChar(self, s):
        for i in s:
            x = s.count(i)
            if x == 1:
                return s.index(i)
        
        return -1
        