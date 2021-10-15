# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        # Guessing the Number using Binary Search
        low = 1
        high = n
        res = n
        while low <= high:
            mid = low + (high - low) // 2
            s = guess(mid)
            if s == -1:
                res = mid
                high = mid -1
            elif s == 1:
                low = mid + 1
            elif s == 0:
                return mid
            
        return res
            