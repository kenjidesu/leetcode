class Solution(object):
    def findRelativeRanks(self, score):
        pl = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        n = 1
        arr = len(score) * [None]
        for i in reversed(sorted(score)):
            ind = score.index(i)
            if n <= 3:
                arr[ind] = pl[n-1]
            else:
                arr[ind] = str(n)
                
            n += 1
            
        return arr