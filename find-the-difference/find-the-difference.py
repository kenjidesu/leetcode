class Solution(object):
    def findTheDifference(self, s, t):
        nums = sum([ord(i) for i in s])
        numt = sum([ord(i) for i in t])
        return chr(abs(nums-numt))
        