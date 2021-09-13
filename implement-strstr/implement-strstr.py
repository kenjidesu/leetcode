class Solution(object):
    def strStr(self, haystack, needle):
        # checks if needle in haystack
        if needle in haystack:
            # gets the index of the needle in the haystack
            ind = haystack.index(needle)
            # return the index
            return ind
        else:
            # return -1 if not in haystack
            return -1