class Solution(object):
    def restoreString(self, s, indices):
        stt = len(s) * [None]
        for i in range(len(s)):
            stt[indices[i]] = s[i]
            
        return "".join(i for i in stt)
        