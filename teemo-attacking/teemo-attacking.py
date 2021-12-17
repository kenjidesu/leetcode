class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        if duration == 0: return 0
        
        time = 0
        for i in range(1, len(timeSeries)):
            mn = min(timeSeries[i] - timeSeries[i-1], duration)
            time += mn
            
        return time + duration