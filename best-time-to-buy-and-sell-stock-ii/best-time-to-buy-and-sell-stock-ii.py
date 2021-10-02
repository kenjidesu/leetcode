class Solution(object):
    def maxProfit(self, prices):
        # set the profit to 0
        pr = 0
        for i in range(1, len(prices)):
            # get the profit if i-1 < i
            if prices[i-1] < prices[i]:
                mx = prices[i] - prices[i-1]
                # add profit
                pr += mx
                
        return pr