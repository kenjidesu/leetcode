class Solution(object):
    def longestCommonPrefix(self, strs):
        # gets the shortest word in strs
        shrtest = min(strs, key=len)
        
        # enumerate() = (index, indexValue)
        for i, c in enumerate(shrtest):
            # checks if strs is != to the indexValue of shrtest
            for j in strs:
                # returns the longest prefix if j is != indexValue
                if j[i] != c:
                    return shrtest[:i]
        return shrtest