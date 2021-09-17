class Solution(object):
    def maxProfit(self, prices):
        # float('inf'), is just to get the minimum possible number
        mx, mn = 0, float('inf')
        for i in prices:
            # gets the minimum to buy stock
            mn = min(mn, i)
            # pr, gets the profit and updates mx if its greater than its current max
            pr = i - mn
            mx = max(mx, pr)
            
        return mx