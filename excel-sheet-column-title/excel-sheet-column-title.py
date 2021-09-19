class Solution(object):
    def convertToTitle(self, columnNumber):
        # creates list of all letters
        alp = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        output = ""
        while columnNumber > 0:
            # it gets the letter on alp and appends it to output
            # based on the (columnNumber-1) % 26
            output += alp[(columnNumber-1) % 26]
            # formula for getting the next letter
            columnNumber = (columnNumber - 1) // 26
        
        # reverse the output
        return output[::-1]
        