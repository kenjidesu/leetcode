class Solution(object):
    def isHappy(self, n):
        x = n
        # generate set() to get avoid duplicates
        res = set()
        while True:
            s = 0
            for i in range(len(str(x))):
                # we get the exp2 of each digit of x and sum up
                s += int(str(x)[i]) ** 2
            
            # if the result is alreayd in set(), its not a happy number
            if s in res:
                return False
            # happy number
            elif s == 1:
                return True
            # we track the result of s
            else:
                res.add(s)
            
            # update the value
            x = s
            
        