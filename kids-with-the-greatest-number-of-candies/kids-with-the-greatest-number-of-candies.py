class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        # Greatest Number of candies
        mx = max(candies)
        arr = []
        for i in candies:
            x = i + extraCandies
            # Append bool, if x is greatest among the kids
            arr.append(x >= mx)
        
        return arr
        