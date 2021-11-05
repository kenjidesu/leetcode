class Solution(object):
    def shiftingLetters(self, s, shifts):
        # shifter
        sf = 0
        # s.toarray()
        s = [i for i in s]
        
        # reverse loop
        for i in range(len(s)-1, -1, -1):
            # add shifts by the next one and limit it to 26
            sf += shifts[i] % 26
            # limit char to 26 and update s[i]
            s[i] = (chr((ord(s[i]) - ord('a') + sf) % 26 + ord('a')))
        
        return "".join(x for x in s)