class Solution(object):
    def decode(self, encoded, first):
        output = [first]
        for i in encoded:
            output.append(output[-1] ^ i)
            
        return output
        