class Solution(object):
    def checkIfPangram(self, sentence):
        total = [ord(i) for i in set(sentence)]
        return sum(total) >= 2847
        