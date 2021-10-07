# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        low = 1
        high = n
        res = n
        while low <= high:
            mid = low + (high - low) // 2
            
            if isBadVersion(mid):
                res = mid
                high = mid - 1
            else:
                low = mid + 1
            
        return res
        