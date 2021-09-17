class Solution(object):
    def getRow(self, rowIndex):
        # creates 1's with the size of rowIndex
        arr = [1] * (rowIndex + 1)
        i = rowIndex
        j = 1
        
        for x in range(1, i):
            # formula for getting the sum of two numbers
            arr[x] = arr[x-1] * i//j
            i -= 1
            j += 1
            
        return arr