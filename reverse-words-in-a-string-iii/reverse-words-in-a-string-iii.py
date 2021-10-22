class Solution(object):
    def reverseWords(self, s):
        # splits a string into a list
        spl = s.split()
        # return var
        rstr = ""
        # loop through list of words of s
        for i in spl:
            # reverse each word
            rev = i[::-1]
            # append to return var
            rstr += rev + ' '
        
        # cancel out the space at the end
        return rstr.rstrip()
        