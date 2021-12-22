class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        output = []
        for i in nums:
            counter = 0
            for j in nums:
                if j != i and j < i:
                    counter += 1
                    
            output.append(counter)
        
        return output