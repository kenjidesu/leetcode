class Solution(object):
    def isAnagram(self, s, t):
        # return false if length are not the same
        if len(s) != len(t):
            return False
        
        # either set() of t or s
        v = set(s)
        # loop through the set
        for i in v:
            # count how many letters on s an t
            # if not equal, invalid anagram
            if s.count(i) != t.count(i):
                return False
        
        # valid anagram
        return True
        