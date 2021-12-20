class Solution(object):
    def minOperations(self, boxes):
        ones = [i for i in range(len(boxes)) if boxes[i] == '1']
        output = []
        for i in range(len(boxes)):
            x = 0
            for j in ones:
                x += abs(i - j)
            output.append(x)
                
        return output