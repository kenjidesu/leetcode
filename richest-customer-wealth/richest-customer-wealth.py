class Solution(object):
    def maximumWealth(self, accounts):
        # 0, if there's no accounts
        if len(accounts) == 0: return 0
        
        # declare the lowest possible value
        mx = float('-inf')
        for i in accounts:
            # update mx with the maximum wealth 
            mx = (max(sum(i), mx))
        
        return mx
        