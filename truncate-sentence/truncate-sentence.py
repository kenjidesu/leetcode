class Solution(object):
    def truncateSentence(self, s, k):
        ars = s.split()
        return "".join(ars[i] + " " if i != k-1 else ars[i] for i in range(k))
        