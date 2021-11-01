class Solution(object):
    def repeatedSubstringPattern(self, s):
        if len(s) == 0: return False
        
        ss = (s + s)[1:-1]
        return s in ss
        