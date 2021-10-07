# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        low = 1     # leftmost value
        high = n    # rightmost value
        res = n     # this will hold the fbv once the loop ends
        while low <= high:
            # gets the mid
            mid = low + (high - low) // 2
            
            # If mid is > fbv
            if isBadVersion(mid):
                # updates res and the rightmost val
                res = mid
                high = mid - 1
            # if mid is < fbv
            else:
                # updates the leftmost val
                low = mid + 1
        
        return res
        