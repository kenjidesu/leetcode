class Solution(object):
    def countPoints(self, rings):
        c = 0
        i = 0
        while i <= 9:
            if "B" + str(i) in rings and "R" + str(i) in rings and "G" + str(i) in rings:
                c += 1
            i += 1
        return c
        