class Solution(object):
    def isSubsequence(self, s, t):
        if not s:
            return True
        spointer = 0
        for i in t:
            if spointer < len(s):
                if s[spointer] == i:
                    spointer += 1
                
        return spointer == len(s)
        