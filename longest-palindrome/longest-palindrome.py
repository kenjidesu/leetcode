class Solution(object):
    def longestPalindrome(self, s):
        # initialize set
        ss = set()
        # loop through s
        for i in s:
            # add in set if i not in set
            if i not in ss:
                ss.add(i)
            # remove if in set
            else:
                ss.remove(i)
        
        # if set is not empty, return length of s minus the length of set + 1
        if len(ss) != 0:
            return len(s) - len(ss) + 1
        # return the length of s
        else:
            return len(s)