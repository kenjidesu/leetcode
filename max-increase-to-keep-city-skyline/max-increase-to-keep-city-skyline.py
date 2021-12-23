class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        transpose = []
        for i in range(len(grid)):
            temp = []
            for j in range(len(grid[i])):
                temp.append(grid[j][i])
            transpose.append(temp)    
            
        output = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                mn = min(max(grid[i]), max(transpose[j]))
                output += abs(grid[i][j] - mn)
                
        return output
        