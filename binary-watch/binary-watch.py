class Solution(object):
    def readBinaryWatch(self, turnedOn):
        arr = []    # return array
        # loop through hours
        for i in range(12):
            # loop through minutes
            for j in range(60):
                # bitcount of i,j == turnedOn, append
                if bin(i).count('1') + bin(j).count('1') == turnedOn:
                    # minute < 10, add a leading zero
                    if j < 10:
                        arr.append("%d:0%d" % (i, j))
                    else:
                        arr.append("%d:%d" % (i, j))
                        
        return arr
        