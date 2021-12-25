class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        n = len(grid)
        mx_r = n * [0]
        mx_c = n * [0]
        result = 0
        
        for i in range(n):
            for j in range(n):
                mx_r[i] = max(mx_r[i], grid[i][j])
                mx_c[j] = max(mx_c[j], grid[i][j])
                
                
        for i in range(n):
            for j in range(n):
                result += min(mx_r[i], mx_c[j]) - grid[i][j]
                
        return result
        