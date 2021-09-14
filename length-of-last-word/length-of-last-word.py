class Solution(object):
    def lengthOfLastWord(self, s):
        # split the words, this becomes an array
        spl = s.split()
        if spl:
            # return the length of the last word
            # which is the last element in our array
            return len(spl[-1])
        
        # return 0 if spl is empty
        return 0