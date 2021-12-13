class Solution(object):
    def maxArea(self, height):
        mx = 0
        l, r = 0, len(height)-1
        while l != r:
            # get the area
            area = (r - l) * min(height[l], height[r])
            mx = max(mx, area)
            # shift the lowest val in l, r
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
            
        return mx
                