class Solution(object):
    def climbStairs(self, n):
        # default elements for fibonacci
        f = [1, 1]
        
        # Gets the Fibonacci sequence
        for i in range(2, n+1):
            f.append(f[i-1] + f[i-2])
        
        # returns last index of fibonacci
        return f[n]