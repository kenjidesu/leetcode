class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        v = set(s)
        for i in v:
            if s.count(i) != t.count(i):
                return False
            
        return True
        