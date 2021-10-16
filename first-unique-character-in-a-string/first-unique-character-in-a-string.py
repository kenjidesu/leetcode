class Solution(object):
    def firstUniqChar(self, s):
        # set ind to the highest value
        ind = float('inf')
        # removes duplicates of s
        m = set(s)
        for i in m:
            # counts how i's in s
            if s.count(i) == 1:
                # if 1, get the index and compare to ind if its less than
                # since we need to find the first non-repeating char
                if s.index(i) < ind:
                    # updates ind
                    ind = s.index(i)
        
        # return -1 if ind didn't change, that means we don't have a non-
        # repeating char, otherwise return ind
        return -1 if ind == float('inf') else ind