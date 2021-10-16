class Solution(object):
    def firstUniqChar(self, s):
        ind = float('inf')
        m = set(s)
        for i in m:
            if s.count(i) == 1:
                if s.index(i) < ind:
                    ind = s.index(i)
        
        return -1 if ind == float('inf') else ind