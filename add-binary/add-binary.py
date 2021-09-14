"""
bin(), converts and returns the binary equivalent string of a given integer
int(), converts string to integer

What's the 2 in int()?
The second parameter of int() is the base of the first parameter. We put 2 since we need to get the binary of the converted
integer from string.

Why [2:]?
bin() returns 0b which is the Python prefix for the representation  of binary numbers. I used [2:] because we only need to
return the binary numbers not with the python prefix.
"""
class Solution(object):
    def addBinary(self, a, b):
        # return sum of the binary string
        return bin(int(a, 2) + int(b, 2))[2:]
