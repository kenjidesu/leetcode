class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        w = "".join(i for i in word1)
        w1 = "".join(i for i in word2)
        return w == w1
        