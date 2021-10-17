class Solution(object):
    def findTheDifference(self, s, t):
        # calculate the ord val of each strings
        nums = sum([ord(i) for i in s])
        numt = sum([ord(i) for i in t])
        
        # get the absolute difference of both strings
        return chr(abs(nums-numt))
        
