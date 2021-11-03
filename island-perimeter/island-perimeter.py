class Solution(object):
    def islandPerimeter(self, grid):
        n = 0
        # loop row
        for i in range(len(grid)):
            # loop column
            for j in range(len(grid[i])):
                # execute only if grid[i][j] is an island
                if grid[i][j] == 1:
                    # One cell has 4 sides
                    n += 4
                    # -2 because 1 cell has 4 sides and if we
                    # combine 2 cells it'll only have 6 sides,
                    # we check i-1 and j-1 to see if there's a
                    # cell that has a 1 value (means its an island)
                    if i > 0 and grid[i-1][j] == 1:
                        n -= 2
                    if j > 0 and grid[i][j-1] == 1:
                        n -= 2
        
        return n