"""
split(), inputs a string value and outputs a list of words contained within 
the string by separating or splitting the words on all the whitespaces by default.
len(), used to calculate the length

[-1] access the last index of the list of words of s, we can also use [len(spl)], but
for simplicity we're gonna use [-1]
"""
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
