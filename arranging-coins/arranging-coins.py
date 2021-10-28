class Solution(object):
    def arrangeCoins(self, n):
        """
        Instead of building a staircase of n in Ascending Order, we're gonna do it
        in Descending Order. Where i, decides how many columns does the row need, it can
        be also our row counter since the columns and row place are the same value, then
        add 1 to i for everytime we deduct n and i which build the staircase. We do this
        until n becomes 0 or less than 0.

        If n is 0 that means all the rows are complete so we can just return the i, else
        n less than 0 means the last row is incomplete so we need to return the last row
        which is the i - 1.
        """
        # row counter
        i = 0
        # loop n until 0
        while n > 0:
            i += 1
            # deduction of n, i to build a staircase
            n -= i
            
        # complete rows of staircase
        if n == 0:
            return i
        # staircase incomplete, return the prev row count
        else:
            return i - 1
        