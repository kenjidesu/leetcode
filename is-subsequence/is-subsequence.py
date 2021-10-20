class Solution(object):
    def isSubsequence(self, s, t):
        # checks if s exists, if not return True
        if not s: return True
        
        # s pointer
        spointer = 0
        # loop through t
        for i in t:
            # tracks the pointer
            if spointer < len(s):
                # we add 1 to spointer to get the next char of s
                if s[spointer] == i:
                    spointer += 1
            
            # return if spointer == len(s), that means we already
            # visited all the subsequence and no need to continue the loop
            if spointer == len(s): return True
        
        # spointer will be equal to len(s) if s is a subsequence of t
        return spointer == len(s)
        